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
     
      4.	Feature Encoding
      
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
an apartment or a home is available at rent.

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


  
