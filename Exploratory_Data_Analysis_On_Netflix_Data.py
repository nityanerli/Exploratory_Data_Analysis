#!/usr/bin/env python
# coding: utf-8

# In[2]:


#importing liabraries
import numpy as np
import pandas as pd
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[3]:


#reading the dataset
df = pd.read_csv('netflix_titles.csv')
df.head()


# In[4]:


df.shape #tells us the rows and columns


# In[5]:


df.describe() #basic statistic of the column and rows


# In[6]:


df.info() #shows us the count and datatypes of our columns by default int 


# Missing Values

# In[7]:


df.isna()


# In[8]:


df.isna().sum()


# # UPDATE DATE_ADDED TO DETERMINE AND CHECK

# In[9]:


#convert the data type from object to datetime64
df['date_added'] = pd.to_datetime(df['date_added'])


# In[10]:


df.head()


# # Handling the missing Values

# In[11]:


df.fillna({'ratings':'Unavailable','cast':'Unavailable','country':'Unavailable','director':'Unavailable'},inplace = True)


# In[12]:


df.isna().sum()


# In[13]:


df[df.date_added.isnull()]


# In[14]:


most_recent_entry_date=df['date_added'].max()
df.fillna({'date_added':most_recent_entry_date},inplace=True)


# Proof of concept that the date filled in the null date_added from a show_id example that previously was missing the date_added 

# In[15]:


df[df.show_id == 's6067']


# Additional Data Cleaning

# Duration Data Input error
# 
# The missing durations are all movies my Louis C K. Normally, we would likely fill the duration with the mean duration of movies from the tables. In this case it appears that the actual duration was input into rating columns, so one solution is to move the rating data to the duration and make the rating information 'Unavailable' like other nulls.

# In[16]:


df[df.duration.isnull()]


# Check to make sure that there is no other content with the same directorto avoid accidental overwriting

# In[17]:


df[df.director == 'Louis C.K.'].head()


# Overwrite and check

# In[18]:


#loc helps us in accessing the columns by names 
df.loc[df['director']== 'Louis C.K.' , 'duration'] = df['rating']
df[df.director =='Louis C.K.'].head()


# second overwrite and check

# In[19]:


df.loc[df['director'] == 'Louis C.K.','rating'] ='Unavailable'
df[df.director =='Louis C.K.'].head()


# # Visualization 

# Lets take a look at types of Shows that has been watched on Netflix

# In[20]:


df.type.value_counts() # value_counts function/method shows us the count of different categories in a given column  


# In[21]:


#countplot helps us to graphically represent the given data
sns.countplot(x ='type',data = df)
plt.title('Count vs Type of Shows')


# On Netflix there are more no.of Movies as compaired to TV shows

# # Country Analysis

# In[22]:


df['country'].value_counts().head(10)


# In[23]:


plt.figure(figsize =(12,6))
sns.countplot(y='country',order = df['country'].value_counts().index[0:10],data =df)
plt.title('Country Wise Content on Netflix')


# In[29]:


#now checking type of content based on the country
movies_countries= df[df['type']=='Movie']
tv_shows = df[df['type']=='TV Show']


# In[30]:


plt.figure(figsize=(12,6))
sns.countplot(y='country',order=df['country'].value_counts().index[0:10],data=movies_countries)
plt.title('Top 10 Countries producing Movies in Netflix')


plt.figure(figsize=(12,6))
sns.countplot(y='country',order=df['country'].value_counts().index[0:10],data=tv_shows)
plt.title('Top 10 Countries producing Tv Shows in Netflix')


# Lets check what are the major ratings on Netflix shows

# In[31]:


df.rating.value_counts()


# In[33]:


plt.figure(figsize=(9,6))
sns.countplot(x='rating',order = df['rating'].value_counts().index[0:10],data=df)
plt.title('Ratings of the shows in Netflix')


# Most of the shows are for Mature Audience (TV-MA) and for audiences that are above age 14 (TV-14)

# In[36]:


#release year of the most content in Netflix
df.release_year.value_counts()[:20]


# In[39]:


plt.figure(figsize =(10,6))
sns.countplot(x='release_year',order = df['release_year'].value_counts().index[0:20],data=df)
plt.title('Content Release in Years on Netflix vs count')


# # Popular Genres Analysis

# In[40]:


df.listed_in.value_counts()[:20]


# In[42]:


plt.figure(figsize =(10,6))
sns.countplot(y='listed_in',order = df['listed_in'].value_counts().index[0:10],data =df)
plt.title("Popular Genres in Netflix")


# # Summary

# so far we have performed lot of operations over the dataset to find out some very basic but useful information from Netflix Dataset.
# To conclude:
# 
# 
# 
# 
# •Netflix has mre movies than TV Shows
# 
# •Most number of Movies and Tvshows are produced in United States, followed by India that has produced second highest number of Movies
# 
# •Most of the content on Netflix is for Mature Audiences
# 
# •2018 was the highest content producing year
# 
# •International Movies and Dramas is listed high that other Genres on Netflix
# 

# 
