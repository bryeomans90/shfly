import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import(
    roc_curve, roc_auc_score, precision_recall_curve, average_precision_score
)


def plot_training_history(history):
    plt.plot(history.epoch, history.history['loss'], label='Training Loss')
    plt.plot(history.epoch, history.history['val_loss'], label='Validation Loss')
    plt.legend()
    plt.xlabel('Epoch Number')
    plt.ylabel('Loss')
    plt.title('Training Loss Over Time')
    plt.show()


def evaluate_model_performance(y_pred, y_test):
    cats = [1,2,3,4,5,7]
    assert y_pred.shape[1] == len(cats)
    
    # ROC Curve
    all_aucs = []
    for i in range(len(cats)):
        y_test_1 = y_test[:,i]
        y_pred_1 = y_pred[:,i]
        
        auc_1 = round(roc_auc_score(y_test_1, y_pred_1),2)
        all_aucs.append(auc_1)
        
        fpr, tpr, _ = roc_curve(y_test_1, y_pred_1)
        plt.plot(fpr, tpr, label=f'Category:{cats[i]}, AUC:{auc_1}')
    mean_auc = round(np.mean(all_aucs),2)
    plt.plot((0,1),(0,1), label='Random', color='k')
    plt.title(f'ROC Curve\nMean AUC: {mean_auc}')
    plt.xlabel('False Positive Rate')
    plt.ylabel('Tue Positive Rate')
    plt.legend()
    plt.show()
    
    # Precision Recall Curve
    all_APs = []
    for i in range(len(cats)):
        y_test_1 = y_test[:,i]
        y_pred_1 = y_pred[:,i]
        
        AP_1 = round(average_precision_score(y_test_1, y_pred_1),2)
        all_APs.append(AP_1)
        
        precision, recall, _ = precision_recall_curve(y_test_1, y_pred_1)
        plt.plot(recall, precision, label=f'Category:{cats[i]}, AP:{AP_1}')
    mean_AP = round(np.mean(all_APs),2)
    plt.title(f'Precision Recall Curve\nMean Average Precision: {mean_AP}')
    plt.ylabel('Precision')
    plt.xlabel('Recall')
    plt.legend()
    plt.show()


model_vars = [
    'P2:-1.0_0_30', 'P2:-7.0_0_30', 'P2:10.0_0_30', 'P2:100.0_0_30', 'P2:101.0_0_30',
    'P2:102.0_0_30', 'P2:103.0_0_30', 'P2:104.0_0_30', 'P2:105.0_0_30', 'P2:106.0_0_30',
    'P2:107.0_0_30', 'P2:108.0_0_30', 'P2:109.0_0_30', 'P2:11.0_0_30', 'P2:110.0_0_30',
    'P2:111.0_0_30', 'P2:112.0_0_30', 'P2:113.0_0_30', 'P2:114.0_0_30', 'P2:115.0_0_30',
    'P2:116.0_0_30', 'P2:117.0_0_30', 'P2:118.0_0_30', 'P2:119.0_0_30', 'P2:12.0_0_30',
    'P2:120.0_0_30', 'P2:121.0_0_30', 'P2:122.0_0_30', 'P2:123.0_0_30', 'P2:124.0_0_30',
    'P2:125.0_0_30', 'P2:126.0_0_30', 'P2:127.0_0_30', 'P2:128.0_0_30', 'P2:129.0_0_30',
    'P2:13.0_0_30', 'P2:130.0_0_30', 'P2:131.0_0_30', 'P2:132.0_0_30', 'P2:133.0_0_30',
    'P2:134.0_0_30', 'P2:135.0_0_30', 'P2:136.0_0_30', 'P2:137.0_0_30', 'P2:138.0_0_30',
    'P2:139.0_0_30', 'P2:14.0_0_30', 'P2:140.0_0_30', 'P2:141.0_0_30', 'P2:142.0_0_30',
    'P2:143.0_0_30', 'P2:144.0_0_30', 'P2:145.0_0_30', 'P2:146.0_0_30', 'P2:147.0_0_30',
    'P2:148.0_0_30', 'P2:149.0_0_30', 'P2:15.0_0_30', 'P2:150.0_0_30', 'P2:151.0_0_30',
    'P2:152.0_0_30', 'P2:153.0_0_30', 'P2:154.0_0_30', 'P2:155.0_0_30', 'P2:156.0_0_30',
    'P2:157.0_0_30', 'P2:158.0_0_30', 'P2:159.0_0_30', 'P2:16.0_0_30', 'P2:160.0_0_30',
    'P2:161.0_0_30', 'P2:162.0_0_30', 'P2:164.0_0_30', 'P2:165.0_0_30', 'P2:166.0_0_30',
    'P2:167.0_0_30', 'P2:168.0_0_30', 'P2:169.0_0_30', 'P2:17.0_0_30', 'P2:170.0_0_30',
    'P2:171.0_0_30', 'P2:172.0_0_30', 'P2:173.0_0_30', 'P2:174.0_0_30', 'P2:175.0_0_30',
    'P2:176.0_0_30', 'P2:177.0_0_30', 'P2:178.0_0_30', 'P2:179.0_0_30', 'P2:18.0_0_30',
    'P2:180.0_0_30', 'P2:181.0_0_30', 'P2:182.0_0_30', 'P2:183.0_0_30', 'P2:184.0_0_30',
    'P2:185.0_0_30', 'P2:186.0_0_30', 'P2:187.0_0_30', 'P2:188.0_0_30', 'P2:189.0_0_30',
    'P2:19.0_0_30', 'P2:190.0_0_30', 'P2:191.0_0_30', 'P2:192.0_0_30', 'P2:193.0_0_30',
    'P2:194.0_0_30', 'P2:195.0_0_30', 'P2:196.0_0_30', 'P2:197.0_0_30', 'P2:198.0_0_30',
    'P2:199.0_0_30', 'P2:2.0_0_30', 'P2:20.0_0_30', 'P2:200.0_0_30', 'P2:201.0_0_30',
    'P2:202.0_0_30', 'P2:203.0_0_30', 'P2:204.0_0_30', 'P2:205.0_0_30', 'P2:206.0_0_30',
    'P2:207.0_0_30', 'P2:208.0_0_30', 'P2:209.0_0_30', 'P2:21.0_0_30', 'P2:210.0_0_30',
    'P2:211.0_0_30', 'P2:212.0_0_30', 'P2:213.0_0_30', 'P2:214.0_0_30', 'P2:215.0_0_30',
    'P2:216.0_0_30', 'P2:217.0_0_30', 'P2:218.0_0_30', 'P2:219.0_0_30', 'P2:220.0_0_30',
    'P2:221.0_0_30', 'P2:222.0_0_30', 'P2:223.0_0_30', 'P2:224.0_0_30', 'P2:225.0_0_30',
    'P2:226.0_0_30', 'P2:227.0_0_30', 'P2:228.0_0_30', 'P2:229.0_0_30', 'P2:23.0_0_30',
    'P2:230.0_0_30', 'P2:231.0_0_30', 'P2:232.0_0_30', 'P2:233.0_0_30', 'P2:234.0_0_30',
    'P2:235.0_0_30', 'P2:236.0_0_30', 'P2:237.0_0_30', 'P2:238.0_0_30', 'P2:239.0_0_30',
    'P2:24.0_0_30', 'P2:240.0_0_30', 'P2:241.0_0_30', 'P2:243.0_0_30', 'P2:244.0_0_30',
    'P2:245.0_0_30', 'P2:246.0_0_30', 'P2:247.0_0_30', 'P2:248.0_0_30', 'P2:249.0_0_30',
    'P2:25.0_0_30', 'P2:250.0_0_30', 'P2:251.0_0_30', 'P2:252.0_0_30', 'P2:253.0_0_30',
    'P2:255.0_0_30', 'P2:256.0_0_30', 'P2:257.0_0_30', 'P2:258.0_0_30', 'P2:259.0_0_30',
    'P2:26.0_0_30', 'P2:260.0_0_30', 'P2:261.0_0_30', 'P2:262.0_0_30', 'P2:263.0_0_30',
    'P2:27.0_0_30', 'P2:28.0_0_30', 'P2:3.0_0_30', 'P2:30.0_0_30', 'P2:32.0_0_30',
    'P2:33.0_0_30', 'P2:34.0_0_30', 'P2:35.0_0_30', 'P2:38.0_0_30', 'P2:39.0_0_30',
    'P2:4.0_0_30', 'P2:40.0_0_30', 'P2:41.0_0_30', 'P2:42.0_0_30', 'P2:43.0_0_30',
    'P2:44.0_0_30', 'P2:45.0_0_30', 'P2:46.0_0_30', 'P2:47.0_0_30', 'P2:48.0_0_30',
    'P2:49.0_0_30', 'P2:5.0_0_30', 'P2:50.0_0_30', 'P2:51.0_0_30', 'P2:52.0_0_30',
    'P2:53.0_0_30', 'P2:54.0_0_30', 'P2:55.0_0_30', 'P2:56.0_0_30', 'P2:57.0_0_30',
    'P2:58.0_0_30', 'P2:59.0_0_30', 'P2:6.0_0_30', 'P2:60.0_0_30', 'P2:61.0_0_30',
    'P2:62.0_0_30', 'P2:63.0_0_30', 'P2:64.0_0_30', 'P2:65.0_0_30', 'P2:66.0_0_30',
    'P2:67.0_0_30', 'P2:69.0_0_30', 'P2:7.0_0_30', 'P2:70.0_0_30', 'P2:71.0_0_30',
    'P2:72.0_0_30', 'P2:73.0_0_30', 'P2:74.0_0_30', 'P2:75.0_0_30', 'P2:76.0_0_30',
    'P2:77.0_0_30', 'P2:78.0_0_30', 'P2:79.0_0_30', 'P2:8.0_0_30', 'P2:80.0_0_30',
    'P2:81.0_0_30', 'P2:82.0_0_30', 'P2:83.0_0_30', 'P2:85.0_0_30', 'P2:86.0_0_30',
    'P2:88.0_0_30', 'P2:89.0_0_30', 'P2:9.0_0_30', 'P2:90.0_0_30', 'P2:91.0_0_30',
    'P2:92.0_0_30', 'P2:93.0_0_30', 'P2:94.0_0_30', 'P2:95.0_0_30', 'P2:96.0_0_30',
    'P2:97.0_0_30', 'P2:98.0_0_30', 'P2:99.0_0_30', 'P2:-1.0_30_350', 'P2:-7.0_30_350',
    'P2:10.0_30_350', 'P2:100.0_30_350', 'P2:101.0_30_350', 'P2:102.0_30_350', 'P2:103.0_30_350',
    'P2:104.0_30_350', 'P2:105.0_30_350', 'P2:106.0_30_350', 'P2:107.0_30_350', 'P2:108.0_30_350',
    'P2:109.0_30_350', 'P2:11.0_30_350', 'P2:110.0_30_350', 'P2:111.0_30_350', 'P2:112.0_30_350',
    'P2:113.0_30_350', 'P2:114.0_30_350', 'P2:115.0_30_350', 'P2:116.0_30_350', 'P2:117.0_30_350',
    'P2:118.0_30_350', 'P2:119.0_30_350', 'P2:12.0_30_350', 'P2:120.0_30_350', 'P2:121.0_30_350',
    'P2:122.0_30_350', 'P2:123.0_30_350', 'P2:124.0_30_350', 'P2:125.0_30_350', 'P2:126.0_30_350',
    'P2:127.0_30_350', 'P2:128.0_30_350', 'P2:129.0_30_350', 'P2:13.0_30_350', 'P2:130.0_30_350',
    'P2:131.0_30_350', 'P2:132.0_30_350', 'P2:133.0_30_350', 'P2:134.0_30_350', 'P2:135.0_30_350',
    'P2:136.0_30_350', 'P2:137.0_30_350', 'P2:138.0_30_350', 'P2:139.0_30_350', 'P2:14.0_30_350',
    'P2:140.0_30_350', 'P2:141.0_30_350', 'P2:142.0_30_350', 'P2:143.0_30_350', 'P2:144.0_30_350',
    'P2:145.0_30_350', 'P2:146.0_30_350', 'P2:147.0_30_350', 'P2:148.0_30_350', 'P2:149.0_30_350',
    'P2:15.0_30_350', 'P2:150.0_30_350', 'P2:151.0_30_350', 'P2:152.0_30_350', 'P2:153.0_30_350',
    'P2:154.0_30_350', 'P2:155.0_30_350', 'P2:156.0_30_350', 'P2:157.0_30_350', 'P2:158.0_30_350',
    'P2:159.0_30_350', 'P2:16.0_30_350', 'P2:160.0_30_350', 'P2:161.0_30_350', 'P2:162.0_30_350',
    'P2:164.0_30_350', 'P2:165.0_30_350', 'P2:166.0_30_350', 'P2:167.0_30_350', 'P2:168.0_30_350',
    'P2:169.0_30_350', 'P2:17.0_30_350', 'P2:170.0_30_350', 'P2:171.0_30_350', 'P2:172.0_30_350',
    'P2:173.0_30_350', 'P2:174.0_30_350', 'P2:175.0_30_350', 'P2:176.0_30_350', 'P2:177.0_30_350',
    'P2:178.0_30_350', 'P2:179.0_30_350', 'P2:18.0_30_350', 'P2:180.0_30_350', 'P2:181.0_30_350',
    'P2:182.0_30_350', 'P2:183.0_30_350', 'P2:184.0_30_350', 'P2:185.0_30_350', 'P2:186.0_30_350',
    'P2:187.0_30_350', 'P2:188.0_30_350', 'P2:189.0_30_350', 'P2:19.0_30_350', 'P2:190.0_30_350',
    'P2:191.0_30_350', 'P2:192.0_30_350', 'P2:193.0_30_350', 'P2:194.0_30_350', 'P2:195.0_30_350',
    'P2:196.0_30_350', 'P2:197.0_30_350', 'P2:198.0_30_350', 'P2:199.0_30_350', 'P2:2.0_30_350',
    'P2:20.0_30_350', 'P2:200.0_30_350', 'P2:201.0_30_350', 'P2:202.0_30_350', 'P2:203.0_30_350',
    'P2:204.0_30_350', 'P2:205.0_30_350', 'P2:206.0_30_350', 'P2:207.0_30_350', 'P2:208.0_30_350',
    'P2:209.0_30_350', 'P2:21.0_30_350', 'P2:210.0_30_350', 'P2:211.0_30_350', 'P2:212.0_30_350',
    'P2:213.0_30_350', 'P2:214.0_30_350', 'P2:215.0_30_350', 'P2:216.0_30_350', 'P2:217.0_30_350',
    'P2:218.0_30_350', 'P2:219.0_30_350', 'P2:220.0_30_350', 'P2:221.0_30_350', 'P2:222.0_30_350',
    'P2:223.0_30_350', 'P2:224.0_30_350', 'P2:225.0_30_350', 'P2:226.0_30_350', 'P2:227.0_30_350',
    'P2:228.0_30_350', 'P2:229.0_30_350', 'P2:23.0_30_350', 'P2:230.0_30_350', 'P2:231.0_30_350',
    'P2:232.0_30_350', 'P2:233.0_30_350', 'P2:234.0_30_350', 'P2:235.0_30_350', 'P2:236.0_30_350',
    'P2:237.0_30_350', 'P2:238.0_30_350', 'P2:239.0_30_350', 'P2:24.0_30_350', 'P2:240.0_30_350',
    'P2:241.0_30_350', 'P2:243.0_30_350', 'P2:244.0_30_350', 'P2:245.0_30_350', 'P2:246.0_30_350',
    'P2:247.0_30_350', 'P2:248.0_30_350', 'P2:249.0_30_350', 'P2:25.0_30_350', 'P2:250.0_30_350',
    'P2:251.0_30_350', 'P2:252.0_30_350', 'P2:253.0_30_350', 'P2:255.0_30_350', 'P2:256.0_30_350',
    'P2:257.0_30_350', 'P2:258.0_30_350', 'P2:259.0_30_350', 'P2:26.0_30_350', 'P2:260.0_30_350',
    'P2:261.0_30_350', 'P2:262.0_30_350', 'P2:263.0_30_350', 'P2:27.0_30_350', 'P2:28.0_30_350',
    'P2:3.0_30_350', 'P2:30.0_30_350', 'P2:32.0_30_350', 'P2:33.0_30_350', 'P2:34.0_30_350',
    'P2:35.0_30_350', 'P2:38.0_30_350', 'P2:39.0_30_350', 'P2:4.0_30_350', 'P2:40.0_30_350',
    'P2:41.0_30_350', 'P2:42.0_30_350', 'P2:43.0_30_350', 'P2:44.0_30_350', 'P2:45.0_30_350',
    'P2:46.0_30_350', 'P2:47.0_30_350', 'P2:48.0_30_350', 'P2:49.0_30_350', 'P2:5.0_30_350',
    'P2:50.0_30_350', 'P2:51.0_30_350', 'P2:52.0_30_350', 'P2:53.0_30_350', 'P2:54.0_30_350',
    'P2:55.0_30_350', 'P2:56.0_30_350', 'P2:57.0_30_350', 'P2:58.0_30_350', 'P2:59.0_30_350',
    'P2:6.0_30_350', 'P2:60.0_30_350', 'P2:61.0_30_350', 'P2:62.0_30_350', 'P2:63.0_30_350',
    'P2:64.0_30_350', 'P2:65.0_30_350', 'P2:66.0_30_350', 'P2:67.0_30_350', 'P2:69.0_30_350',
    'P2:7.0_30_350', 'P2:70.0_30_350', 'P2:71.0_30_350', 'P2:72.0_30_350', 'P2:73.0_30_350',
    'P2:74.0_30_350', 'P2:75.0_30_350', 'P2:76.0_30_350', 'P2:77.0_30_350', 'P2:78.0_30_350',
    'P2:79.0_30_350', 'P2:8.0_30_350', 'P2:80.0_30_350', 'P2:81.0_30_350', 'P2:82.0_30_350',
    'P2:83.0_30_350', 'P2:85.0_30_350', 'P2:86.0_30_350', 'P2:88.0_30_350', 'P2:89.0_30_350',
    'P2:9.0_30_350', 'P2:90.0_30_350', 'P2:91.0_30_350', 'P2:92.0_30_350', 'P2:93.0_30_350',
    'P2:94.0_30_350', 'P2:95.0_30_350', 'P2:96.0_30_350', 'P2:97.0_30_350', 'P2:98.0_30_350',
    'P2:99.0_30_350', 'P2:-1.0_350_380', 'P2:-7.0_350_380', 'P2:10.0_350_380', 'P2:100.0_350_380',
    'P2:101.0_350_380', 'P2:102.0_350_380', 'P2:103.0_350_380', 'P2:104.0_350_380', 'P2:105.0_350_380',
    'P2:106.0_350_380', 'P2:107.0_350_380', 'P2:108.0_350_380', 'P2:109.0_350_380', 'P2:11.0_350_380',
    'P2:110.0_350_380', 'P2:111.0_350_380', 'P2:112.0_350_380', 'P2:113.0_350_380', 'P2:114.0_350_380',
    'P2:115.0_350_380', 'P2:116.0_350_380', 'P2:117.0_350_380', 'P2:118.0_350_380', 'P2:119.0_350_380',
    'P2:12.0_350_380', 'P2:120.0_350_380', 'P2:121.0_350_380', 'P2:122.0_350_380', 'P2:123.0_350_380',
    'P2:124.0_350_380', 'P2:125.0_350_380', 'P2:126.0_350_380', 'P2:127.0_350_380', 'P2:128.0_350_380',
    'P2:129.0_350_380', 'P2:13.0_350_380', 'P2:130.0_350_380', 'P2:131.0_350_380', 'P2:132.0_350_380',
    'P2:133.0_350_380', 'P2:134.0_350_380', 'P2:135.0_350_380', 'P2:136.0_350_380', 'P2:137.0_350_380',
    'P2:138.0_350_380', 'P2:139.0_350_380', 'P2:14.0_350_380', 'P2:140.0_350_380', 'P2:141.0_350_380',
    'P2:142.0_350_380', 'P2:143.0_350_380', 'P2:144.0_350_380', 'P2:145.0_350_380', 'P2:146.0_350_380',
    'P2:147.0_350_380', 'P2:148.0_350_380', 'P2:149.0_350_380', 'P2:15.0_350_380', 'P2:150.0_350_380',
    'P2:151.0_350_380', 'P2:152.0_350_380', 'P2:153.0_350_380', 'P2:154.0_350_380', 'P2:155.0_350_380',
    'P2:156.0_350_380', 'P2:157.0_350_380', 'P2:158.0_350_380', 'P2:159.0_350_380', 'P2:16.0_350_380',
    'P2:160.0_350_380', 'P2:161.0_350_380', 'P2:162.0_350_380', 'P2:164.0_350_380', 'P2:165.0_350_380',
    'P2:166.0_350_380', 'P2:167.0_350_380', 'P2:168.0_350_380', 'P2:169.0_350_380', 'P2:17.0_350_380',
    'P2:170.0_350_380', 'P2:171.0_350_380', 'P2:172.0_350_380', 'P2:173.0_350_380', 'P2:174.0_350_380',
    'P2:175.0_350_380', 'P2:176.0_350_380', 'P2:177.0_350_380', 'P2:178.0_350_380', 'P2:179.0_350_380',
    'P2:18.0_350_380', 'P2:180.0_350_380', 'P2:181.0_350_380', 'P2:182.0_350_380', 'P2:183.0_350_380',
    'P2:184.0_350_380', 'P2:185.0_350_380', 'P2:186.0_350_380', 'P2:187.0_350_380', 'P2:188.0_350_380',
    'P2:189.0_350_380', 'P2:19.0_350_380', 'P2:190.0_350_380', 'P2:191.0_350_380', 'P2:192.0_350_380',
    'P2:193.0_350_380', 'P2:194.0_350_380', 'P2:195.0_350_380', 'P2:196.0_350_380', 'P2:197.0_350_380',
    'P2:198.0_350_380', 'P2:199.0_350_380', 'P2:2.0_350_380', 'P2:20.0_350_380', 'P2:200.0_350_380',
    'P2:201.0_350_380', 'P2:202.0_350_380', 'P2:203.0_350_380', 'P2:204.0_350_380', 'P2:205.0_350_380',
    'P2:206.0_350_380', 'P2:207.0_350_380', 'P2:208.0_350_380', 'P2:209.0_350_380', 'P2:21.0_350_380',
    'P2:210.0_350_380', 'P2:211.0_350_380', 'P2:212.0_350_380', 'P2:213.0_350_380', 'P2:214.0_350_380',
    'P2:215.0_350_380', 'P2:216.0_350_380', 'P2:217.0_350_380', 'P2:218.0_350_380', 'P2:219.0_350_380',
    'P2:220.0_350_380', 'P2:221.0_350_380', 'P2:222.0_350_380', 'P2:223.0_350_380', 'P2:224.0_350_380',
    'P2:225.0_350_380', 'P2:226.0_350_380', 'P2:227.0_350_380', 'P2:228.0_350_380', 'P2:229.0_350_380',
    'P2:23.0_350_380', 'P2:230.0_350_380', 'P2:231.0_350_380', 'P2:232.0_350_380', 'P2:233.0_350_380',
    'P2:234.0_350_380', 'P2:235.0_350_380', 'P2:236.0_350_380', 'P2:237.0_350_380', 'P2:238.0_350_380',
    'P2:239.0_350_380', 'P2:24.0_350_380', 'P2:240.0_350_380', 'P2:241.0_350_380', 'P2:243.0_350_380',
    'P2:244.0_350_380', 'P2:245.0_350_380', 'P2:246.0_350_380', 'P2:247.0_350_380', 'P2:248.0_350_380',
    'P2:249.0_350_380', 'P2:25.0_350_380', 'P2:250.0_350_380', 'P2:251.0_350_380', 'P2:252.0_350_380',
    'P2:253.0_350_380', 'P2:255.0_350_380', 'P2:256.0_350_380', 'P2:257.0_350_380', 'P2:258.0_350_380',
    'P2:259.0_350_380', 'P2:26.0_350_380', 'P2:260.0_350_380', 'P2:261.0_350_380', 'P2:262.0_350_380',
    'P2:263.0_350_380', 'P2:27.0_350_380', 'P2:28.0_350_380', 'P2:3.0_350_380', 'P2:30.0_350_380',
    'P2:32.0_350_380', 'P2:33.0_350_380', 'P2:34.0_350_380', 'P2:35.0_350_380', 'P2:38.0_350_380',
    'P2:39.0_350_380', 'P2:4.0_350_380', 'P2:40.0_350_380', 'P2:41.0_350_380', 'P2:42.0_350_380',
    'P2:43.0_350_380', 'P2:44.0_350_380', 'P2:45.0_350_380', 'P2:46.0_350_380', 'P2:47.0_350_380',
    'P2:48.0_350_380', 'P2:49.0_350_380', 'P2:5.0_350_380', 'P2:50.0_350_380', 'P2:51.0_350_380',
    'P2:52.0_350_380', 'P2:53.0_350_380', 'P2:54.0_350_380', 'P2:55.0_350_380', 'P2:56.0_350_380',
    'P2:57.0_350_380', 'P2:58.0_350_380', 'P2:59.0_350_380', 'P2:6.0_350_380', 'P2:60.0_350_380',
    'P2:61.0_350_380', 'P2:62.0_350_380', 'P2:63.0_350_380', 'P2:64.0_350_380', 'P2:65.0_350_380',
    'P2:66.0_350_380', 'P2:67.0_350_380', 'P2:69.0_350_380', 'P2:7.0_350_380', 'P2:70.0_350_380',
    'P2:71.0_350_380', 'P2:72.0_350_380', 'P2:73.0_350_380', 'P2:74.0_350_380', 'P2:75.0_350_380',
    'P2:76.0_350_380', 'P2:77.0_350_380', 'P2:78.0_350_380', 'P2:79.0_350_380', 'P2:8.0_350_380',
    'P2:80.0_350_380', 'P2:81.0_350_380', 'P2:82.0_350_380', 'P2:83.0_350_380', 'P2:85.0_350_380',
    'P2:86.0_350_380', 'P2:88.0_350_380', 'P2:89.0_350_380', 'P2:9.0_350_380', 'P2:90.0_350_380',
    'P2:91.0_350_380', 'P2:92.0_350_380', 'P2:93.0_350_380', 'P2:94.0_350_380', 'P2:95.0_350_380',
    'P2:96.0_350_380', 'P2:97.0_350_380', 'P2:98.0_350_380', 'P2:99.0_350_380' 
]