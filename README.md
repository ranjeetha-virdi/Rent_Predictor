

![MotleyFool-TMOT-deeef720-rental-home](https://github.com/ranjeetha-virdi/Rent_Predictor/assets/81987445/0256bc40-da14-49de-90b1-084bf81a86e6)







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


![PRICE](https://github.com/ranjeetha-virdi/Rent_Predictor/assets/81987445/23c94df3-e2e4-4637-9722-16710b1d6da7)

![SQUARE_FEET](https://github.com/ranjeetha-virdi/Rent_Predictor/assets/81987445/40804fa2-7e85-4eaf-abab-21e240feb22b)

Here we have create a new feature called economic region by grouping various states to create these regions from the existing feature state.
From this feature we could vizualize that Southeast is the most affordable region and Far West is the most expensive region to rent a home.
The region with maximum space available for rent is New England respectively.

![AFFORDABILITY_num](https://github.com/ranjeetha-virdi/Rent_Predictor/assets/81987445/d5d39c55-5a3f-4bfc-b9a4-724a93668fe0)


![PRICE_num](https://github.com/ranjeetha-virdi/Rent_Predictor/assets/81987445/b30d60a4-1fb1-4dd9-94c2-b6afb5779be5)


![SQUARE_FEET_num](https://github.com/ranjeetha-virdi/Rent_Predictor/assets/81987445/7d4f1480-7748-4be9-907b-eab48b77699e)



Similarly we have also analysed states for the above aspects of affordability and expensiveness to rent a flat. The most affordable and 
with most available space is North Carolina, most expensive state to rent a home being California followed by Massachusetts.

![AFFORDABILITY](https://github.com/ranjeetha-virdi/Rent_Predictor/assets/81987445/970a2fd0-7ec1-400a-b74a-40dd5139b236)


![PRICE_num](https://github.com/ranjeetha-virdi/Rent_Predictor/assets/81987445/e28b5354-79e8-42f0-90cd-6ac213177e01)



![SQUARE_FEET_num](https://github.com/ranjeetha-virdi/Rent_Predictor/assets/81987445/dbabc4a5-a727-4ffb-b959-e8541183867d)



We have also tried to analyze these aspects at city level for each state for example in California, most expensive city was Los Altos and most affordable 
city was Ridgecrest.Similarly in Florida the most expensive city was Palm Beach Gardens and the most affordable city was Seminole. In Texas the most 
expensive city being Leander and most affordable being Troup. 
![CA](https://github.com/ranjeetha-virdi/Rent_Predictor/assets/81987445/65ab156b-99e4-4470-bd30-2995cd2c1c94)


![FL](https://github.com/ranjeetha-virdi/Rent_Predictor/assets/81987445/434e53a9-68f8-456e-a834-2fa462ec46d8)



![TX](https://github.com/ranjeetha-virdi/Rent_Predictor/assets/81987445/9ae08348-7c04-47c0-a68d-fd7b0c86398a)

We have also analysed cities for their spaciousness in various states. For example least spacious city in California is Wilton and most spacious 
being Granada Hills. In Colorado the most spacious city being Erie and least spacious being Highlands Ranch.

![CA](https://github.com/ranjeetha-virdi/Rent_Predictor/assets/81987445/80dfe826-d912-4840-b12b-f9d53d4a4502)



![CO](https://github.com/ranjeetha-virdi/Rent_Predictor/assets/81987445/a9119cf2-ac5f-40ef-8314-2d633e15553d)




We have also tried to look at the distribution of Numerical columns like price,square feet, Bedrooms and Bathrooms.

![CA](https://github.com/ranjeetha-virdi/Rent_Predictor/assets/81987445/517a1109-fdc4-48e1-950e-279ba87c8e69)


![FL](https://github.com/ranjeetha-virdi/Rent_Predictor/assets/81987445/ca349160-3dd1-4540-91af-0275669bb9ed)


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
![all_models_mae](https://github.com/ranjeetha-virdi/Rent_Predictor/assets/81987445/eefd5592-6301-4887-94ff-f687df42766d)

![all_models_r2](https://github.com/ranjeetha-virdi/Rent_Predictor/assets/81987445/7bb03266-b06f-4e18-bd5c-70710648ee22)

#### After evaluation the best performing model was XGBoost Regression which performed the best. The models were evaluted on the basis of two metrics
        1. R² score
        2. Mean Absolute Error

   The model was further tuned by adjusting the hyperparameters for xgboost regressor which includes learning rate, max depth and n_estimators.
   
![hyperparameter_tuning](https://github.com/ranjeetha-virdi/Rent_Predictor/assets/81987445/d91399b6-7824-4154-8c03-00f52c5a844e)


### To Obtain Prediction: 
We will configure a flask server to get the input and then run the prediction on our pickled model file. The front end is built using HTML, CSS and JavaScript to communicate with the web server.

![app](https://github.com/ranjeetha-virdi/Rent_Predictor/assets/81987445/12bcbf05-9085-4c02-9489-7552d1a03a0e)



We can test the flask server configuration using postman app.

![postman](https://github.com/ranjeetha-virdi/Rent_Predictor/assets/81987445/2285d2b9-0311-439f-8dd5-dbb8fbec87f6)



## Deploying the ML Model to Production on Amazon EC2 Server.
The final step of this project is to deploy the website to production using an Amazon EC2 instance. There will be a nginx and flsk server running on this instance as well as our website.
We will be doing a reverse proxy set up, to route all our requests to our flask server running on same EC2 instance at port 5000 using the saved ML Model to serve the predictions requests.

### Steps to setup EC2 on AWS:
1. Create EC2 instance, also setup security group to accept HTTP and HTTPS traffic by adding rules to allow HTTP and HTTPS incoming traffic.
2. Now connect to the instance using a command like this,
    ````
   ssh -i "C:\Users\kulpr\.ssh\usa.pem" ubuntu@ec2-3-133-88-210.eu-central-1.compute.amazonaws.com
     ````
4. Steps to setting up NGINX on the EC2 instance:
   (a) Install nginx on EC2 instance using these commands:
    ````
      sudo apt-get update
      sudo apt-get install nginx
     ````
   (b) The above command will install nginx server as well as run it. To check the status of the server use:
    ````
      sudo service nginx status
     ````
   (c) commands to start,stop and restart the server:
    ````
      sudo service nginx start
      sudo service nginx stop
      sudo service nginx restart
     ````
6. Once we setup the nginx web server, when we run the url for our EC2 instance it will run the welcome to nginx webpage.
7. Now copy all our code to EC2 instance. We can do this either using git or copy files using winscp. We will use winscp. You can download winscp from here:
 ````
   https://winscp.net/eng/download.php
 ````
9. Once you connect to EC2 instance from winscp, we can now copy all code files into /home/ubuntu/ folder. The full path of your root folder is now: /home/ubuntu/us_rent_prediction
10. After copying code on EC2 server now we can point nginx to load our rent_prediction website by default. For below steps,
   i.   Create this file /etc/nginx/sites-available/usr.conf. The file content looks like this,
    ````
    
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
   
      ````
   ii. Create symlink for this file in /etc/nginx/sites-enabled by running this command,
    ````
            sudo ln -v -s /etc/nginx/sites-available/usr.conf
    ````
  
   iii. Remove symlink for default file in /etc/nginx/sites-enabled directory,
    ````
            sudo unlink default
    ````
   
   iv. Restart nginx,
    ````
            sudo service nginx restart
    ````

11. Now install python packages and start flask server
````
   sudo apt-get install python3-pip
   sudo pip3 install -r /home/ubuntu/us_rent_prediction/server/requirements.txt
   python3 /home/ubuntu/us_rent_prediction/client/server.py
````
    
12. Running last command above will prompt that server is running on port 5000.
13. Now just load your cloud url provided by AWS in a browser http://ec2-3-133-88-210.eu-central-1.compute.amazonaws.com/ and this will be fully functional website running in production cloud environment.
