# Machine Learning House Price Predict
## Table Content
1. [Project OverView](#ov)
2. [Tools](#to)
3. [Process](#pro)
4. [Final Product](#fin)
<a name="ov"></a>
## 1. Project Overview
- In this project I've built a software that can predict the price of the house for us we just input some factor like location, number of room, number of bath room and area of the house
<a name="to"></a>
## 2. Tools that i've use
- Pandas library: use to clean data and load dataset
- matplotlib and seaborn: use to visualize 
- sklearn: use to build the model espacially regression model, model_selection,train_test_split..
- Flask Framework : as a server and to make our model to be a product
- Bootstrap: use in frontend to make a beautiful intrface
<a name="pro"></a>
## 3. Process
- first i try to collect data from some source like kaggle then i use pandas library to load the dataset as the original data it is very complex so we need to clean it and most of my time was spending on cleaning in other to clean the data i've use feature engineering 
- that i try to find out which columns should be remove(it doesn't affect of price) in order to make our model more acurrate
- after that i split my data into train and test part
- then i used machine learning regression model like Linear_regression, Dicisiontree_Regression, Lasso 
- after that i need to find out which model have a best performance
- then i save my model as pickle file
- Import my model to Flask 
<a name="fin"></a>
## 4. Final Product
![](/pic.png)
