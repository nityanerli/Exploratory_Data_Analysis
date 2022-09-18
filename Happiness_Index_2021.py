#!/usr/bin/env python
# coding: utf-8

# In[8]:


#importing libraries

import numpy as num
import pandas as pan
import seaborn as sbrn
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[9]:


sbrn.set_style('darkgrid')
plt.rcParams['font.size'] = 15
plt.rcParams['figure.figsize'] = (10,7)
plt.rcParams['figure.facecolor'] = '#FFE5B4'


# In[69]:


#reading the dataset

happy_index = pan.read_csv('world-happiness-report-2021.csv')
happy_index.head(5)


# In[70]:


happy_index.shape 


# In[71]:


happy_index_columns=['Country name','Regional indicator','Ladder score','Logged GDP per capita','Social support','Healthy life expectancy','Freedom to make life choices','Generosity','Perceptions of corruption']


# In[72]:


happy_index = happy_index[happy_index_columns].copy()


# In[81]:


happy_index_df= happy_index.rename(columns={'Country name':'country_name','Regional indicator':'regional_indicator','Ladder score':'ladder_score','Logged GDP per capita':'logged_GDP_per_capita','Social support':'social_support','Healthy life expectancy':'life_expectancy','Freedom to make life choices':'Freedom','Generosity':'Generosity','Perceptions of corruption':'perceptions_of_corruption'})


# In[ ]:





# In[82]:


happy_index_df.head()


# In[83]:


happy_index_df.head()


# In[84]:


happy_index_df.isnull().sum() # to check if there are null values#1st vis


# In[87]:


#1st visiualization:plot b/w happiness and GDP

plt.rcParams['figure.figsize']=(15,7)
plt.title('Plot b/w Happiness Score and GDP')
sbrn.scatterplot(x=happy_index_df.ladder_score,y=happy_index_df.logged_GDP_per_capita,hue = happy_index_df.regional_indicator,s= 200);

plt.legend(loc = 'upper left',fontsize = '10')
plt.xlabel('Happiness Score')
plt.ylabel('GDP Per Capita')


# In[88]:


#we shall now see the pipe plot GDP by region higgest GDP 

gdp_region = happy_index_df.groupby('regional_indicator')['logged_GDP_per_capita'].sum()
gdp_region


# In[89]:


gdp_region.plot.pie(autopct = '%1.1f%%')
plt.title('GDP by Region')
plt.ylabel('')


# Sub-Saharan Africa has 30+ countries that are contributing to the World GDP hence their contribution is 20.7%. The second highest contirbutor is Western European with 16.2% . Followed by Central and Eastern Europe that includes Czech Republic,Slovenia,Kosovo,Polandetc.North America has lowest contribution with 3.1%   along with ANZ Region (i.e : Australia and New Zealand) combined.

# In[92]:


#total no of countries in each region (pandas)

total_country = happy_index_df.groupby('regional_indicator')[['country_name']].count()
print(total_country)


# In[98]:


#creating a corelation map
#compute the co relation matrix
cor = happy_index_df.corr(method = 'pearson')
f,ax = plt.subplots(figsize =(10,5))
sbrn.heatmap(cor,mask =num.zeros_like(cor,dtype=num.bool),
                     cmap= 'Blues',square =True,ax=ax)


# In[101]:


#visualize Bar plot corruption in regions

corruption = happy_index_df.groupby('regional_indicator')[['perceptions_of_corruption']].mean()
print(corruption)


# In[105]:


plt.rcParams['figure.figsize'] = (12,8)
plt.title('Perception of Corruption in Various Regions')
plt.xlabel ('Regions',fontsize = 15)
plt.ylabel("Corruption Index",fontsize = 15)
plt.xticks(rotation = 30, ha = 'right')
plt.bar(corruption.index, corruption.perceptions_of_corruption)


# In[ ]:





# In[106]:


#life expectancy of top 10 and bottom 10


# In[107]:


top10 = happy_index_df.head(10)
bottom10 = happy_index_df.tail(10)


# In[112]:


fig,axes = plt.subplots(1,2 ,figsize =(16,6))
plt.tight_layout(pad =2)

xlabel = top10.country_name
axes[0].set_title('Top 10 happiest countries Life Expectancy')
axes[0].set_xticklabels(xlabel,rotation =45, ha ='right')
sbrn.barplot(x=top10.country_name,y=top10.life_expectancy,ax=axes[0])
axes[0].set_xlabel('Country Name')
axes[0].set_ylabel('Life Expectancy')

xlabels= bottom10.country_name
axes[1].set_title('Bottom 10 happy countries Life Expectancy')
axes[1].set_xticklabels(xlabel,rotation = 45, ha='right')
sbrn.barplot(x=bottom10.country_name,y=bottom10.life_expectancy)
axes[1].set_xlabel('Country Name')
axes[1].set_ylabel('Life Expectancy')


# In[ ]:





# In[113]:


#freedom to make life choices and happiness index

plt.rcParams['figure.figsize']=(15,7)
sbrn.scatterplot(x= happy_index_df.Freedom,y= happy_index_df.ladder_score,hue = happy_index_df.regional_indicator,s=200);
plt.legend(loc='upper left',fontsize = 12)
plt.xlabel('Freedom to make life choices')
plt.ylabel('Happiness Score')


# In[116]:


#top 10 most corrupt countries

#sort perception of corruption column

country = happy_index_df.sort_values(by = 'perceptions_of_corruption').tail(10)
plt.rcParams['figure.figsize'] =(12,6)
plt.title('Top 10 Countries that have highest Corruption Value')
plt.xlabel('Country',fontsize = 13)
plt.ylabel('Corruption Index',fontsize =13)
plt.xticks(rotation = 30 , ha='right')
plt.bar(country.country_name,country.perceptions_of_corruption)


# In[117]:


#scatter plot that will tell us the corruption affect on happiness score


plt.rcParams['figure.figsize'] =(15,7)
sbrn.scatterplot(x= happy_index_df.ladder_score,y = happy_index_df.perceptions_of_corruption, hue = happy_index_df.regional_indicator,s=200);
plt.title('Happy Score vs Corruption Index')

plt.legend(loc= 'lower left', fontsize = 14)
plt.xlabel('Happiness Score')
plt.ylabel('Corruption Index')


# In[ ]:




