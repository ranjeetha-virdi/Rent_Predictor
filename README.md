![how_to_find_house_for_rent-iStock-149060607-1000x499](https://github.com/ranjeetha-virdi/house_rent_predictor/assets/81987445/b951f522-0d2b-45c5-b406-1733cd23ddae)









# Introduction


A house is not just a building. It is a home—a place that shelters, protects and nurtures its occupants. 
It supports their personal and professional development and offers a safe harbor. Affordable housing 
improves the quality of life of residents by leading to better health, adequate jobs, financial stability, 
security, and population diversity. The effects of affordable housing on residents are profound and capable 
of transforming communities. Affordable housing enables people to have more money in hand after paying rent, 
hence more purchasing power to pump money into the economy helping other small businesses like restaurants, 
supermarkets, bakeries etc. There by enabling over all economic development and quality of life.

Housing is a vital economic sector in the United States, contributing to 15% of the GDP. The majority of 
Americans (64%) own their own homes, but the remaining 36% who cannot afford to buy a home for themselves 
need to rent a home. Majority of them survive on paycheck-to-paycheck basis. Hence affordable housing is 
key to their survival and keep homelessness at bay.

There is a need to understand the statewide availability of housing for rent and how affordable they are 
at various levels including economic region, state and city level. There is also a need to analyze the most 
affordable cities to live in major states and also design a prediction system to predict the rent for apartments
in different major US states.


# Aim
Affordable housing is not a handout. It is a necessity. Finding ideal accommodation that fits our budget as well 
as the one that offers space for every member of the family. The rent of the house depends on the number of bedrooms, 
bathrooms and amenities available.  With use of appropriate machine learning algorithms people can find ideal home that 
best fits their needs and budget from all the available choices in the market. 
## To achieve this, we will do the following:

   I. Design a Machine Learning model to predict rent for desired homes at desired city or state
   
   
   II. Determine appropriate features required for predicting the rent for the homes
   
   
   The basic requirements to meet this aim we need to do the following steps: 
      
      1.	Data Collection
      
      2.	Data Cleaning
      
      3.	Exploratory Data Analysis
     
      4.	Feature Preprocessing
      
      5.	Feature Engineering to create new features like affordability and Economic Regions of US
      
      6.	Test Train Split
     
      7.	Modeling, test the data on different machine learning models 
      
      8.	Hyperparameter tuning
      
      9.	Model Evaluation and find the best model 

### Data Collection

For analysis of the housing rent market, in US we use the dataset available at UCI Machine Learning Repository at URL as stated below: 

https://archive.ics.uci.edu/dataset/555/apartment+for+rent+classified 

The dataset has data points for apartment, homes and retail properties available for rent across all the states in US. The dataset 
has 1,00,000 rows and 22 columns with each row representing each property available for rent with numerical features like bedrooms, 
bathrooms, square feet and rent and categorical features like category of the property whether home or apartment, amenities, pets 
allowed or not and has a fee or not.

### Data Cleaning 

To get an overview of the dataset at hand, like examining the spread of the numerical data like price, square feet, bedrooms and bathrooms
and examine the presence of null values, I have a helper function to summarize all these aspects of the data set we can easily have a 
summarized overview of the distribution of our data set. Also we can see that there are many columns like amenities, pets allowed and 
address with missing values. 
The cleaning process include dropping columns like address, latitude and longitude. 
Convert the price feature for some properties were specified in terms of weekly basis to monthly basis. Formatting amenities columns to properly 
encode ordinal values based on their importance. Example if an apartment is with acess to golf club and swimming pool then it will be evaluated to
have a higher rent as compared to an apartment only with a refrigerator and ac. Bring columns like category which specifies the type of property ie 
an apartment or a home is available at rent. Then create seperate dataframes for each state with maximum data points in our case it was Texas, California, 
Varginia, North Carolina, Colorado, Florida, Massachusetts and Maryland.

### Exploratory Data Analysis

To understand the distribution of the properties at various levels starting at Economic Region Level. The US is divided into eight economic regions by 
The Bureau of Economic Analysis for comparison of economic data and they are as below.


![BEA_regions](https://github.com/ranjeetha-virdi/house_rent_predictor/assets/81987445/ab1f135e-2990-47b7-a43b-97494943ac1a)

Here we have create a new feature called economic region by grouping various states to create these regions from the existing feature state.
From this feature we could vizualize that Southeast is the most affordable region and Far West is the most expensive region to rent a home.
The region with maximum space available for rent is New England respectively.


![affordability](https://github.com/ranjeetha-virdi/house_rent_predictor/assets/81987445/164bc279-d06e-4491-960b-23abbbb3ed6f)


![price](https://github.com/ranjeetha-virdi/house_rent_predictor/assets/81987445/f48f0039-42f5-46a2-95e0-12b04ade214a)


![square_feet](https://github.com/ranjeetha-virdi/house_rent_predictor/assets/81987445/b4f44839-8ad0-4887-81af-4fdb914fe769)


Similarly we have also analysed states for the above aspects of affordability and expensiveness to rent a flat. The most affordable and 
with most available space is North Carolina, most expensive state to rent a home being California followed by Massachusetts.


![AFFORDABILITY_num](https://github.com/ranjeetha-virdi/house_rent_predictor/assets/81987445/77896f87-ab2b-410a-8390-78a9c3b6d7aa)


![SQUARE_FEET_num](https://github.com/ranjeetha-virdi/house_rent_predictor/assets/81987445/5b6ab044-fe9d-4a5b-b362-690ad96c69e9)

![PRICE_num](https://github.com/ranjeetha-virdi/house_rent_predictor/assets/81987445/13ad2d47-84c9-4c4d-889d-907260b4ed98)

We have also tried to analyze these aspects at city level for each state for example in California, most expensive city was Los Altos and most affordable 
city was Ridgecrest.Similarly in Florida the most expensive city was Palm Beach Gardens and the most affordable city was Seminole. In Texas the most 
expensive city being Leander and most affordable being Troup. 

![CA](https://github.com/ranjeetha-virdi/house_rent_predictor/assets/81987445/6b620e88-2c2b-4ed7-ba7c-f3dc68337be0)


![FL](https://github.com/ranjeetha-virdi/house_rent_predictor/assets/81987445/6659d653-8ff6-4bd1-b98e-a6e20ec311f5)


![TX](https://github.com/ranjeetha-virdi/house_rent_predictor/assets/81987445/8c835043-3cc9-4a17-81ac-40f087c72ee0)

We have also analysed cities for their spaciousness in various states. For example least spacious city in California is Wilton and most spacious 
being Granada Hills. In Colorado the most spacious city being Erie and least spacious being Highlands Ranch.


![CA](https://github.com/ranjeetha-virdi/house_rent_predictor/assets/81987445/826e6fa4-66cb-4b9b-8cae-e8a71d98ef28)

![CO](https://github.com/ranjeetha-virdi/house_rent_predictor/assets/81987445/48ad9b01-7fc5-448d-a35f-357044832014)



We have also tried to look at the distribution of Numerical columns like price,square feet, Bedrooms and Bathrooms.

![CA](https://github.com/ranjeetha-virdi/house_rent_predictor/assets/81987445/305ce54d-a36a-4fbe-a8dc-4d95af3498be)

![FL](https://github.com/ranjeetha-virdi/house_rent_predictor/assets/81987445/b346c7b2-a01d-4e21-96c6-026267e0bfac)


### Feature preprocessing and engineering new features

Feature preprocessing to include removal of outliers of numerical columns. One hot encoding for the categorical column cityname. Ordinal encoding 
of amenities, category and pets allowed. Creating new features like affordability by using exiting features of square feet and price and economic region from existing 
column state.

### Test Train Split

We will create seperate models for top eight states based on datapoints available i.e Texas, California, Varginia, North Carolina, Colorado, Florida, Massachusetts, Maryland. 
We will create a dictionary with key as state and values as the DataFrame, then we will divide these values of dictionary into two subsets. The first subset is used to fit the model for each state and is referred to as the training dataset. The second subset, test dataset is not used to train the model; instead, the input element of the dataset is provided to the model, then predictions are made and compared to the expected values. 

### Modeling and Hyperparameter Tuning

   The dataset was then used to train different set of Machine Learning models:
     1. Decision Tree Regression
     2. Random Forest Regression
     3. Adaboost Regression
     4. Gradient Boost Regression
     5. XGBoost Regression
![all_models_mae](https://github.com/ranjeetha-virdi/house_rent_predictor/assets/81987445/07caa464-4535-463d-8d2a-e3c39cfdca56)


![all_models_r2](https://github.com/ranjeetha-virdi/house_rent_predictor/assets/81987445/bcf0dd2f-8ccd-480f-b2c0-dfdf3b7b85c5)

#### After evaluation the best performing model was XGBoost Regression which performed the best. The models were evaluted on the basis of two metrics
        1. R² score
        2. Mean Absolute Error

   The model was further tuned by adjusting the hyperparameters for xgboost regressor which includes learning rate, max depth and n_estimators.
   
![hyperparameter_tuning](https://github.com/ranjeetha-virdi/house_rent_predictor/assets/81987445/c8de8224-7c9d-47b7-b421-58b28d23a1a0)

### To Obtain Prediction: 
We will configure a flask server to get the input and then run the prediction on our pickled model file. The front end is built using HTML, CSS and JavaScript to communicate with the web server.

![app](https://github.com/ranjeetha-virdi/house_rent_predictor/assets/81987445/c8860861-8853-476c-bb60-d94d5f0c243a)


We can test the flask server configuration using postman app.

![postman](https://github.com/ranjeetha-virdi/house_rent_predictor/assets/81987445/d665c6f6-39ff-426e-89d3-35b9ec42a4a1)


## Deploying the ML Model to Production on Amazon EC2 Server.
The final step of this project is to deploy the website to production using an Amazon EC2 instance. There will be a nginx and flsk server running on this instance as well as our website.
We will be doing a reverse proxy set up, to route all our requests to our flask server running on same EC2 instance at port 5000 using the saved ML Model to serve the predictions requests.

### Steps to setup EC2 on AWS:
1. Create EC2 instance, also setup security group to accept HTTP and HTTPS traffic by adding rules to allow HTTP and HTTPS incoming traffic.
2. Now connect to the instance using a command like this,
   ssh -i "C:\Users\kulpr\.ssh\usa.pem" ubuntu@ec2-3-133-88-210.eu-central-1.compute.amazonaws.com
3. Steps to setting up NGINX on the EC2 instance:
   (a) Install nginx on EC2 instance using these commands:
      sudo apt-get update
      sudo apt-get install nginx
   (b) The above command will install nginx server as well as run it. To check the status of the server use:
      sudo service nginx status
   (c) commands to start,stop and restart the server:
      sudo service nginx start
      sudo service nginx stop
      sudo service nginx restart
4. Once we setup the nginx web server, when we run the url for our EC2 instance it will run the welcome to nginx webpage.
5. Now copy all our code to EC2 instance. We can do this either using git or copy files using winscp. We will use winscp. You can download winscp from here:
        https://winscp.net/eng/download.php
6. Once you connect to EC2 instance from winscp, we can now copy all code files into /home/ubuntu/ folder. The full path of your root folder is now: /home/ubuntu/us_rent_prediction
7. After copying code on EC2 server now we can point nginx to load our rent_prediction website by default. For below steps,
   i.   Create this file /etc/nginx/sites-available/usr.conf. The file content looks like this,
    ```
          server {
                listen 80;
                    server_name bhp;
                    root /home/ubuntu/us_rent_prediction/client;
                    index app.html;
                    location /api/ {
                         rewrite ^/api(.*) $1 break;
                         proxy_pass http://127.0.0.1:5000;
                    }
            }
   ```
   ii. Create symlink for this file in /etc/nginx/sites-enabled by running this command,
            sudo ln -v -s /etc/nginx/sites-available/usr.conf
   iii. Remove symlink for default file in /etc/nginx/sites-enabled directory,
            sudo unlink default
   iv. Restart nginx,
            sudo service nginx restart
9. Now install python packages and start flask server
   sudo apt-get install python3-pip
   sudo pip3 install -r /home/ubuntu/us_rent_prediction/server/requirements.txt
   python3 /home/ubuntu/us_rent_prediction/client/server.py
10. Running last command above will prompt that server is running on port 5000.
11. Now just load your cloud url in browser (for me it was http://ec2-3-133-88-210.eu-central-1.compute.amazonaws.com/) and this will be fully functional website running in production cloud environment.
