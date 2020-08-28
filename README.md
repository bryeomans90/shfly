 ### Objective
The objective of this gitrepo is to build a model that predicts the product category (prodcat1) that a customer is likely to order. Additionally, I added in a purchase history and online engagement based customer segmentation.

### Overall Approach and Rationele 
- **Data Exploration** - My goal was to understand the customers as well as possible using various different charts. Additionally I wanted to understand what data quality issues existed so that I could create a function in dataset_creation.py that would automatically clean the data as needed. 
- **Customer Segmentation** - My goal was to group customers together based on their overall engagement with the site and purchase history. In order to give each event and product category equal weighting I used a hyperbolic tangent layer inside an autoencoder so that I both reduced dimensionality and bounded all variables between -1 and 1. 
- **Product Category Prediction** - My goal here was to try to predict what the next category a user would purchase based on their online engagement and purchase history. I used a multi-input neural network that had three inputs (session history, order history, and month of order) and 1 output (probability 1 or products would be purchased in each category.) I considered using a recommender system such as collaborative filtering, but felt that the limited number of outputs and the fact that users can be repeat buyers made me elect to make this a classification problem.
    - Performance Evaluation - To evaluate predictive performance I used the following two metrics that measure overall predictive power independent of any chosen probability cutoff. 
        - Mean AUC of ROC Curve - This metric tells me whether or not the model is performing better than random (0.5) on average for each of the 6 product classes.
        - Mean Average Precision - This metric shows the average average precision across all levels of recall for all classes. The closer it is to 1 the better the performance. (This metric is very sensitive to the baseline proportion between the classes)

### Recommendations for Future Upgrades
- Customer Segmentation
    - Meet with marketing team to understand the objective of their customer segmentation.
- Product Category Prediction
    - Start tracking customer behavior just before making a purchase. This doesn't appear to be fully tracked in the existing data.
    - Use Category recommender in marketing campaigns
    - Design experiment to
    - **Improve Sophistication:** 
    - **Improve Understanding:** 
        - Understand how we intend to deploy this model

### Description on Contents
- Data Exploration
    1. Overview - Here I explore the order and online data to better understand the data quality issues that need to be addressed and get a better understanding of how users interact with the site. Additionally, I create a few prototype directed graphs showing the relationship between products that are frequently purchased together. 
    2. Individual-Orders - Here I explore individual customers to get a better understanding of what the behavior of the most engaged users are like. 

- Customer Segmentation
    1. Dataset Creation - Here I clean and reshape the order and session data so that it can be used to segment customers.
    2. AutoEncoder Training - Here I use an autoencoder to reduce the dimensionality of the the features and scale them to values between -1 and 1.
    3. K-Means Clustering - Here I cluster the customers with K-means using their embeddings and visualize the clusters using TSNE. 
    
- Product Category Predition
    1. Create Raw Modeling File - 
    2. Create Final Modeling File - 
    3. Build Model
- Other Contents
    - dataset_creation.py - This contains frequently used functions in the dataset creation process. 
    - performance_evaluation.py - This contains functions that are used to evaluate model performance
    - test_dataset_creation.py - This contains a number of unit tests for frequently used functions for dataset creation.
    - Other Exploration
        - This contains a number of different explorations that didn't quite make it into the final cut. Explore at your own risk.

