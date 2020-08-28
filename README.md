 ### Objective
There are 2 main objectives of this analysis. The first is to predict the product category (prodcat1) that a customer is likely to order. The second is to segment the customer population. 

### Overall Approach and Rationale 
 1. **Data Exploration** My goal was to find data quality issues and understand the data better.
    1. _Overview:_ In this section I created multiple visualizations of both the online.csv and order.csv datasets. In this section I checked for missing values, date ranges, averages over time, typical customer engagement patterns, and even a directed graph showing which products are purchased together. Visualizing data to gain an intuitive understanding of the data's relationships and data quality issues are critical. Many of the data quality issues were fixed using functions stored and dataset_creation.py. These functions were then unit tested so as to reduce the chances of bugs entering my code. Unit testing is often a step that is often over looked by other data scientists, but is really helpful in improving overall code quality.
    2. _Individual Customer Exploration:_ This section was a quick supplemental analysis where I manually inspected the engagement of the most engaged customers across both their order and online history.
 2. **Customer Segmentation** - My goal was to segment customers based on how they engaged with the site as well as their particular product preferences. Normally, I would have sat down with the marketer to understand their objectives better before segmenting, but this is just a generic way to segment customers.
    1. _Dataset Creation:_ In this section I read in and cleaned customer order and online data for 2016 and 2017 because that's when they both are populated. Then calculated the total counts of online engagement and order history for each of the customers. I then exported this dataset to a pickle file to be used in the next section.
    2. _Auto Encoder Training:_ Here I built an autoencoder that both reduces the dimensionality of the input data and compresses the range of embeddings between -1 and 1. Compressing the dimensionality and standardizing the inputs to be between a consistent range will make clustering with k-means easier and give equal weighting to each dimension. 
    3. _K-Means Clustering:_ Here I score the customers using the auto encoder and then test out various levels of k to segment customers with the K-Means algorithm. Then I selected 8 clusters to be the optimal number of clusters by investigating the within sum of squares with the "Elbow Method." Afterwards I visualize the effectiveness of the clustering with the TSNE algorithm. Lastly, I calculate the average engagement values for each of the different clusters to try to get an idea of what the clusters represent. 
    
 3. **Product Category Prediction** - My goal here was to try to predict the next category a user would purchase based on their online engagement and purchase history. I make the assumption that we'll know the month of their purchase at time of prediction. Like for example if it was related to a marketing campaign.
     1. _Create Raw Modeling File:_ In this section I created a raw version of the modeling file that was eventually used to predict the category of product a user would purchase next. It resulted in the following datasets:
        - final_previous_order_df - Which matches each order with all the previous orders counts made by that customer for the last 14 months. 
        - dependent_vars - This contained the raw dependent variable of prodcat1 purchases as well as the month of purchase.
        - previous_online_sessions_by_week - This table consists of all the previous online session event counts made by that customer for the last 53 weeks.
     2. _Create Final Modeling File:_ In this section I created an HDF5 file for both the training and test dataset. This dataset contained all the independent and dependent variables that will be trained in the neural network.
     3. _Model Building:_ I used a multi-input neural network that had three inputs (session history, order history, and month of order) and 1 output (probability 1 or products would be purchased in each category.)
        - _Performance Evaluation_ - I used Mean AUC of the ROC Curve and Mean Average Precision to evaluate predictive performance because they are independent of any chosen probability cutoff.
          - Mean AUC of ROC Curve - This metric tells me whether or not the model is performing better than random (0.5) on average for each of the 6 product classes.
          - Mean Average Precision - This metric shows the average average precision across all levels of recall for all classes. The closer it is to 1 the better the performance. (This metric is very sensitive to the baseline proportion between the classes)

### Appendix
  - dataset_creation.py - This contains frequently used functions in the dataset creation process. 
  - performance_evaluation.py - This contains functions that are used to evaluate model performance.
  - test_dataset_creation.py - This contains a number of unit tests for frequently used functions for dataset creation.
