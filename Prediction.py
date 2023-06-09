#!/usr/bin/env python
# coding: utf-8

# # Name : Riya Jain 
# # Task 1 
## Prediction Using Supervised Machine Learning
# ## In this regression task we will predict the percentage of marks that a student is expected to score based upon the number of hours they studied. This is a simple linear regression task as it involves just two variables.

# ### Importing libraries

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from warnings import filterwarnings
filterwarnings('ignore')


# # Importing data from csv file

# In[2]:


data=pd.read_csv("student_scores_and_hours.csv")


# In[3]:


data


# In[ ]:





# ## SUMMARY OF THE DATA

# In[4]:


data.shape


# In[5]:


data.columns


# In[6]:


data.info()


# In[7]:


data.describe().T


# # FINDING THE MISSING VALUES

# In[8]:


data.isnull().sum()


# * Here we can see that there is no missing value in the data

# # EXPLORATORY DATA ANALYSIS
# # SCATTER PLOT

# In[9]:


plt.figure(figsize = (10,5))
sns.scatterplot(x=data['Hours'],y=data['Scores'])


# ## There is a positive linear realtionship between hours and scores of the students

# # Analysis the Data Using Different Graphs

# In[10]:


sns.swarmplot(x=data['Hours'],y=data['Scores'],)
plt.title('Hours vs Percentage')  
plt.xlabel('Hours Studied')  
plt.ylabel('Percentage Score')  
plt.show()


# In[11]:


sns.pairplot(data)
plt.show()


# # HEATMAP

# In[12]:


data.corr()


# In[13]:


plt.figure(figsize =(10,5))
sns.heatmap(data.corr(),annot = True)


# ## Heatmap tells us the correlation in the data and we can see that our columns are positively correlated 

# In[14]:


sns.set(color_codes = True) 
# gives nice background to the graph


# # SCATTER PLOT
# * it tells the relationship between the variables

# In[15]:


plt.figure(figsize= (10,10))
plt.scatter(data['Hours'], data['Scores'])
plt.title('Scatter plot of students')
plt.xlabel('Hours')
plt.ylabel('Scores')
plt.grid(True)
plt.show()


# # BOX PLOT
# * IT WILL SHOW THE OUTLIERS IN THE DATA

# In[16]:


plt.boxplot(data)
plt.title("Boxplot")
plt.show()


# * IT tells the outliers value present in the data 
# * there is no outliers present in the data

# # DISTPLOT

# In[17]:


# distribution of hours
sns.distplot(data['Hours'], kde = True, rug= True)
plt.title('Distplot For Hours')
plt.show()
#Hours are slightly right Skewed


# In[18]:


# Distplot for Scores

sns.distplot(data['Scores'], kde = True, rug= True)
plt.title('Distplot For Scores')
plt.show()


# # JOINTPLOT

# * IT TELLS THE RELATIONSHIP BETWEEN THE TWO VARIABLES AND CREATE A SCATTERPLOT AND HISTOGRAM

# In[19]:


sns.jointplot(x=data['Hours'], y=data['Scores'])


# # MODEL CREATION
# # Spliting the data 

# In[20]:


# creating feature and target variable 
x = data.drop('Scores', axis = 1).values
y = data['Scores'].values


# In[21]:


from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state = 123)


# In[22]:


x_train.shape, y_train.shape


# In[23]:


x_test.shape, y_test.shape


# # IMPORTING LIBRARIES

# In[24]:


from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error
from math import sqrt
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler


# # FITTING OUR DATA INTO THE MODEL

# In[25]:


model = make_pipeline(StandardScaler(copy=True, with_mean=True, with_std=True), LinearRegression())

model.fit(x_train, y_train)

model.score(x_test, y_test)


# In[26]:


print('Test Score',model.score(x_test,y_test))
print('Training Score',model.score(x_train,y_train))


# In[27]:


y_pred = model.predict(x_test)
y_pred


# In[28]:


pred = pd.DataFrame({'Actual': y_test, 'Pred': y_pred})
pred


# In[29]:


mse = mean_squared_error(y_test, y_pred)
rmse = sqrt(mse)
rmse


# In[30]:


# EVALUATE OUR MODEL


# In[31]:


MSE = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print('Mean squared error: ', MSE)
print('R2 Score: ', r2)

The Mean square error should be as close to zero as possible and the R2 Score should be as close as to 1 as possible
# In[32]:


plt.figure(figsize=(10,5))
plt.title("ACTUAL X PREDICTED")
plt.scatter(x_test, y_test, c="#1597E5")
plt.plot(x_test, y_pred, c="#FF5F7E")


# #  What will be predicted score if a student studies for 9.25 hrs/ day?

# In[33]:


Hours = 9.25
Hrs = np.array(Hours).reshape(-1,1)  
pred = model.predict(Hrs)

print('No. of Hours = {}'.format(Hours))
print('Pred Score = {}'.format(round(pred[0],3)))
Hrs = np.array(Hours).reshape(-1,1)  
pred = model.predict(Hrs)


# # ACCORDING TO THIS MODEL : IF A STUDENT STUDIES FOR 9.25hrs A DAY HE WILL SCORE :    91.108

# In[ ]:





# In[ ]:



