import numpy as np
import pandas as pd


def get_previous_online_sessions_by_week(
    online_sessions:pd.DataFrame, 
    order_history:pd.DataFrame, 
    max_weeks_before:int
):
    order_history_basic = order_history[
        ['ordno', 'custno', 'orderdate']
    ].sort_values('ordno').copy()
    
    merged_sessions = order_history_basic.merge(
        online_sessions, on='custno', how='left',
        suffixes=('_current', '_previous')
    )
    
    all_prev_sessions = merged_sessions[
        merged_sessions['orderdate']
        > merged_sessions['start_time']
    ].copy()
    
    all_prev_sessions['days_before'] = (
        all_prev_sessions['orderdate'] - all_prev_sessions['start_time']
    ).astype('timedelta64[s]')/3600/24
    
    all_prev_sessions_clean = all_prev_sessions[
        [
            'ordno', 'days_before',
            'E1:-1.0', 'E1:1.0', 'E1:2.0', 'E1:4.0', 'E1:5.0', 'E1:6.0', 
            'E1:7.0', 'E1:8.0', 'E1:9.0', 'E1:10.0', 'E1:11.0',
            'E2:1', 'E2:2', 'E2:3', 'E2:4', 'E2:5', 
            'E2:6', 'E2:7', 'E2:8', 'E2:9', 'E2:10',
            'Cat:1', 'Cat:2', 'Cat:3'
        ]
    ].copy()
    
    all_prev_sessions_clean['weeks_before'] =(
        all_prev_sessions_clean['days_before'].apply(get_weeks_before)
    )
    all_prev_sessions_by_week = all_prev_sessions_clean.groupby(
        ['ordno','weeks_before'], as_index=False
    ).sum()
    all_prev_sessions_by_week_filtered = all_prev_sessions_by_week[
        all_prev_sessions_by_week['weeks_before']>0
    ]
    
    ordno_df = order_history_basic[['ordno', 'orderdate']].copy()
    ordno_df['key'] = 1 
    weeks_before_df = pd.DataFrame(
        np.arange(1,54).reshape(-1,1), columns=['weeks_before']
    )
    weeks_before_df['key']=1 
    ordno_weeks_before_df = ordno_df.merge(weeks_before_df, on='key')
    del(ordno_weeks_before_df['key'])
    assert ordno_df.shape[0] == ordno_weeks_before_df.shape[0]/53
    
    # For each order total the number of orders for each of the previous 24 months
    previous_online_sessions_by_week = ordno_weeks_before_df.merge(
        all_prev_sessions_by_week_filtered, 
        left_on=['ordno', 'weeks_before'],
        right_on=['ordno', 'weeks_before'],
        how='left'
    )
    previous_online_sessions_by_week = previous_online_sessions_by_week.fillna(0)
    
    previous_online_sessions_by_week = previous_online_sessions_by_week[
        previous_online_sessions_by_week['weeks_before'] <= max_weeks_before
    ].sort_values(by=['ordno', 'weeks_before'])
    
    return previous_online_sessions_by_week


def get_online_sessions_df(raw_online_df):
    # Convert to Datetime
    raw_online_df['start_time'] = pd.to_datetime(raw_online_df['dt']).copy()
    del(raw_online_df['dt'])

    # Fill in Missing Values with Dummie Value
    raw_online_df['event1'] = raw_online_df['event1'].fillna(-1)

    # Give clear category name for when it's split out to all the columns
    raw_online_df['event1'] = raw_online_df[['event1']].apply(
        lambda row: rename_categories('E1',row[0]), axis=1)
    raw_online_df['event2'] = raw_online_df[['event2']].apply(
        lambda row: rename_categories('E2',row[0]), axis=1)
    raw_online_df['category'] = raw_online_df[['category']].apply(
        lambda row: rename_categories('Cat',row[0]), axis=1)

    # Convert into dummy variables
    e1_dummies = pd.get_dummies(raw_online_df['event1'])
    e2_dummies = pd.get_dummies(raw_online_df['event2'])
    cat_dummies = pd.get_dummies(raw_online_df['category'])

    event_vars = (
        list(e1_dummies.columns) 
        + list(e2_dummies.columns) 
        + list(cat_dummies.columns)
    )
    
    online_expanded = pd.concat(
        [raw_online_df, e1_dummies, e2_dummies, cat_dummies],  axis=1
    )
    
    # Create Dictionary for Aggregation
    agg_dict = {}
    for event_var in event_vars:
        agg_dict[event_var] = 'sum'
    agg_dict['start_time'] = 'min'
    
    online_sessions_df = online_expanded.groupby(
        ['custno', 'session'], as_index=False
    ).agg(agg_dict).copy()

    return online_sessions_df 


def get_previous_orders_by_month(order_totals_df, max_previous_months):
    # merge each order with all previous orders for the same user
    order_totals_df_basic = order_totals_df[
        ['ordno', 'custno', 'orderdate']
    ].sort_values('ordno').copy()
    
    merged_orders = order_totals_df_basic.merge(
        order_totals_df, on='custno', how='left',
        suffixes=('_current', '_previous')
    )
    all_prev_orders = merged_orders[
        merged_orders['orderdate_current']
        > merged_orders['orderdate_previous']
    ].copy()
    
    # For each order calculate how many months before each previous order is
    all_prev_orders['days_before'] = (
        all_prev_orders['orderdate_current'] - all_prev_orders['orderdate_previous']
    ).astype('timedelta64[s]')/3600/24

    all_prev_orders_clean = all_prev_orders[[
        'ordno_current', 'days_before',
        'P2:-1.0', 'P2:-7.0', 'P2:10.0', 'P2:100.0',
        'P2:101.0', 'P2:102.0', 'P2:103.0', 'P2:104.0', 'P2:105.0',
        'P2:106.0', 'P2:107.0', 'P2:108.0', 'P2:109.0',
        'P2:11.0', 'P2:110.0', 'P2:111.0', 'P2:112.0', 'P2:113.0',
        'P2:114.0', 'P2:115.0', 'P2:116.0', 'P2:117.0',
        'P2:118.0', 'P2:119.0', 'P2:12.0', 'P2:120.0', 'P2:121.0',
        'P2:122.0', 'P2:123.0', 'P2:124.0', 'P2:125.0',
        'P2:126.0', 'P2:127.0', 'P2:128.0', 'P2:129.0', 'P2:13.0',
        'P2:130.0', 'P2:131.0', 'P2:132.0', 'P2:133.0',
        'P2:134.0', 'P2:135.0', 'P2:136.0', 'P2:137.0', 'P2:138.0',
        'P2:139.0', 'P2:14.0', 'P2:140.0', 'P2:141.0',
        'P2:142.0', 'P2:143.0', 'P2:144.0', 'P2:145.0', 'P2:146.0',
        'P2:147.0', 'P2:148.0', 'P2:149.0', 'P2:15.0',
        'P2:150.0', 'P2:151.0', 'P2:152.0', 'P2:153.0', 'P2:154.0',
        'P2:155.0', 'P2:156.0', 'P2:157.0', 'P2:158.0',
        'P2:159.0', 'P2:16.0', 'P2:160.0', 'P2:161.0', 'P2:162.0',
        'P2:164.0', 'P2:165.0', 'P2:166.0', 'P2:167.0',
        'P2:168.0', 'P2:169.0', 'P2:17.0', 'P2:170.0', 'P2:171.0',
        'P2:172.0', 'P2:173.0', 'P2:174.0', 'P2:175.0',
        'P2:176.0', 'P2:177.0', 'P2:178.0', 'P2:179.0', 'P2:18.0',
        'P2:180.0', 'P2:181.0', 'P2:182.0', 'P2:183.0',
        'P2:184.0', 'P2:185.0', 'P2:186.0', 'P2:187.0', 'P2:188.0',
        'P2:189.0', 'P2:19.0', 'P2:190.0', 'P2:191.0',
        'P2:192.0', 'P2:193.0', 'P2:194.0', 'P2:195.0', 'P2:196.0',
        'P2:197.0', 'P2:198.0', 'P2:199.0', 'P2:2.0',
        'P2:20.0', 'P2:200.0', 'P2:201.0', 'P2:202.0', 'P2:203.0',
        'P2:204.0', 'P2:205.0', 'P2:206.0', 'P2:207.0',
        'P2:208.0', 'P2:209.0', 'P2:21.0', 'P2:210.0', 'P2:211.0',
        'P2:212.0', 'P2:213.0', 'P2:214.0', 'P2:215.0',
        'P2:216.0', 'P2:217.0', 'P2:218.0', 'P2:219.0', 'P2:220.0',
        'P2:221.0', 'P2:222.0', 'P2:223.0', 'P2:224.0',
        'P2:225.0', 'P2:226.0', 'P2:227.0', 'P2:228.0', 'P2:229.0',
        'P2:23.0', 'P2:230.0', 'P2:231.0', 'P2:232.0',
        'P2:233.0', 'P2:234.0', 'P2:235.0', 'P2:236.0', 'P2:237.0',
        'P2:238.0', 'P2:239.0', 'P2:24.0', 'P2:240.0',
        'P2:241.0', 'P2:243.0', 'P2:244.0', 'P2:245.0', 'P2:246.0',
        'P2:247.0', 'P2:248.0', 'P2:249.0', 'P2:25.0',
        'P2:250.0', 'P2:251.0', 'P2:252.0', 'P2:253.0', 'P2:255.0',
        'P2:256.0', 'P2:257.0', 'P2:258.0', 'P2:259.0',
        'P2:26.0', 'P2:260.0', 'P2:261.0', 'P2:262.0', 'P2:263.0',
        'P2:27.0', 'P2:28.0', 'P2:3.0', 'P2:30.0',
        'P2:32.0', 'P2:33.0', 'P2:34.0', 'P2:35.0', 'P2:38.0',
        'P2:39.0', 'P2:4.0', 'P2:40.0', 'P2:41.0',
        'P2:42.0', 'P2:43.0', 'P2:44.0', 'P2:45.0', 'P2:46.0',
        'P2:47.0', 'P2:48.0', 'P2:49.0', 'P2:5.0',
        'P2:50.0', 'P2:51.0', 'P2:52.0', 'P2:53.0', 'P2:54.0',
        'P2:55.0', 'P2:56.0', 'P2:57.0', 'P2:58.0',
        'P2:59.0', 'P2:6.0', 'P2:60.0', 'P2:61.0', 'P2:62.0',
        'P2:63.0', 'P2:64.0', 'P2:65.0', 'P2:66.0',
        'P2:67.0', 'P2:69.0', 'P2:7.0', 'P2:70.0', 'P2:71.0',
        'P2:72.0', 'P2:73.0', 'P2:74.0', 'P2:75.0',
        'P2:76.0', 'P2:77.0', 'P2:78.0', 'P2:79.0', 'P2:8.0',
        'P2:80.0', 'P2:81.0', 'P2:82.0', 'P2:83.0',
        'P2:85.0', 'P2:86.0', 'P2:88.0', 'P2:89.0', 'P2:9.0',
        'P2:90.0', 'P2:91.0', 'P2:92.0', 'P2:93.0',
        'P2:94.0', 'P2:95.0', 'P2:96.0', 'P2:97.0', 'P2:98.0',
        'P2:99.0' 
    ]].copy()

    # Convert to number representing months before
    all_prev_orders_clean['months_before'] =(
        all_prev_orders_clean['days_before'].apply(get_months_before)
    )

    # Aggregate to Order and months_before level 
    all_prev_order_by_month = all_prev_orders_clean.groupby(
        ['ordno_current','months_before'], as_index=False
    ).sum()

    # Make Empty Dataset Unique at ordno and months_before level
    ordno_df = order_totals_df_basic[['ordno', 'orderdate']].copy()
    ordno_df['key'] = 1 
    months_before_df = pd.DataFrame(
        np.arange(1,24).reshape(-1,1), columns=['months_before']
    )
    months_before_df['key']=1 
    ordno_months_before_df = ordno_df.merge(months_before_df, on='key')
    del(ordno_months_before_df['key'])

    # For each order total the number of orders for each of the previous 24 months
    previous_orders_by_month = ordno_months_before_df.merge(
        all_prev_order_by_month, 
        left_on=['ordno', 'months_before'],
        right_on=['ordno_current', 'months_before'],
        how='left'
    )

    # Fill in null values with 0s
    previous_orders_by_month = previous_orders_by_month.fillna(0)
    
    previous_orders_by_month = previous_orders_by_month[
        previous_orders_by_month['months_before']<=max_previous_months
    ].sort_values(by=['ordno', 'months_before']).copy()

    return previous_orders_by_month 


def get_order_total_at_order_level(raw_order_df):
    
    raw_order_df['orderdate'] = pd.to_datetime(raw_order_df['orderdate'])
    
    # Clean prodcat1 and prodcat2
    raw_order_df['prodcat2'] = raw_order_df[['prodcat1', 'prodcat2']].apply(
        lambda row: prod_cat2_nan_fill(row['prodcat1'], row['prodcat2']), axis=1
    )
    raw_order_df['prodcat1'] = raw_order_df[['prodcat1', 'prodcat2']].apply(
        lambda row: clean_96_overlap(row['prodcat1'], row['prodcat2']), axis=1
    )
    
    # 1 hot encode prodcat1 and prodcat2
    raw_order_df['prodcat1'] = raw_order_df[['prodcat1']].apply(
        lambda row: rename_categories('P1',row[0]), axis=1
    )
    raw_order_df['prodcat2'] = raw_order_df[['prodcat2']].apply(
        lambda row: rename_categories('P2',row[0]), axis=1
    )
    
    p1_dummies = pd.get_dummies(raw_order_df['prodcat1'])
    p2_dummies = pd.get_dummies(raw_order_df['prodcat2'])
    
    order_expanded = pd.concat([raw_order_df, p1_dummies, p2_dummies], axis=1)
    
    # Create Dictionary for Aggregation
    pcat_columns = list(p1_dummies.columns) + list(p2_dummies.columns)
    
    order_agg_dict = {}
    for pcat_column in pcat_columns:
        order_agg_dict[pcat_column] = 'sum'
    order_agg_dict['orderdate'] = 'min'
    
    # Aggregate Orders to the order_id level
    order_total_at_order_level = order_expanded.groupby(
        ['ordno', 'custno'], as_index=False
    ).agg(order_agg_dict)
    
    order_total_at_order_level['ordermonth'] = order_total_at_order_level['orderdate'].dt.month
    
    assert (
        order_total_at_order_level.shape[0] == 
        len(order_total_at_order_level['ordno'].unique())
    )
    
    return order_total_at_order_level


def clean_96_overlap(prd_cat1, prd_cat2):
    if prd_cat2 == 96:
        prd_cat1 = 7
    return prd_cat1


def prod_cat2_nan_fill(prd_cat1, prd_cat2):
    if np.isnan(prd_cat2):
        return -1*prd_cat1
    else:
        return prd_cat2


def rename_categories(prefix, current_name):
    return f'{prefix}:{current_name}'

    
def get_months_before(days):
    i = 0
    for max_days in range(30,30*24,30):
        i+=1
        if days<max_days:
            return i
    return -1


def get_weeks_before(days):
    i = 0
    for max_days in range(7,7*24,7):
        i+=1
        if days<max_days:
            return i
    return -1