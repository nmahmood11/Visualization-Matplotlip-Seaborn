#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import os


# In[3]:


movies = pd.read_csv(r"C:\Users\Noman Mahmood\Desktop\DS\MR\Movie-Rating.csv")


# In[5]:


movies


# In[7]:


len(movies)


# In[8]:


movies.head()


# In[9]:


movies.tail()


# In[10]:


movies.columns


# In[11]:


movies.columns = ['Film', 'Genre', 'CriticRating', 'AudienceRating','BudgetMillions','Year']


# In[12]:


movies.head() # Removed spaces & % removed noise characters


# In[13]:


movies.info() 


# In[14]:


movies.describe() 
# if you look at the year the data type is int but when you look at the mean value it showing 2009 which is meaningless
# we have to change to categroy type 
# also from object datatype we will convert to category datatypes


# In[15]:


movies['Film']
#movies['Audience Ratings %']


# In[16]:


movies.Film


# In[17]:


movies.Film = movies.Film.astype('category')


# In[18]:


movies.Film


# In[19]:


movies.head()


# In[20]:


movies.info()

# now the same thing we will change genra to category & year to category


# In[21]:


movies.Genre = movies.Genre.astype('category')
movies.Year = movies.Year.astype('category')


# In[22]:


movies.Genre


# In[23]:


movies.Year # is it real no. year you can take average,min,max but out come have no meaning 


# In[24]:


movies.info()


# In[25]:


movies.Genre.cat.categories


# In[26]:


movies.describe() 
#now when you see the describt you will get only integer value mean, standard deviation which is meaning full


# In[27]:


# How to working with joint plots

from matplotlib import pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')
import warnings
warnings.filterwarnings('ignore')


# In[28]:


j = sns.jointplot( data = movies, x = 'CriticRating', y = 'AudienceRating')
# Audience rating is more dominant then critics rating
# Based on this we find out as most people are most liklihood to watch audience rating & less likely to wathc critics rating
# let me explain the excel - if you filter audience rating & critic rating. critic rating has very low values compare to audience rating 


# In[29]:


j = sns.jointplot( data = movies, x = 'CriticRating', y = 'AudienceRating', kind='hex')

#j = sns.jointplot( data = movies, x = 'CriticRating', y = 'AudienceRating', kind='reg')


# In[30]:


#Histograms

# <<< chat1

m1 = sns.distplot(movies.AudienceRating)

#y - axis generated by seaborn automatically that is the powefull of seaborn gallery


# In[31]:


sns.set_style('darkgrid')


# In[32]:


m2 = sns.distplot(movies.AudienceRating, bins = 15)


# In[33]:


#sns.set_style('darkgrid')
n1 = plt.hist(movies.AudienceRating, bins=15)


# In[34]:


sns.set_style('white') #normal distribution & called as bell curve
n1 = plt.hist(movies.AudienceRating, bins=20)


# In[35]:


n1 = plt.hist(movies.CriticRating, bins=20) #uniform distribution


# In[36]:


# <<< chat - 2

# Creating stacked histograms & this is bit tough to understand


# In[37]:


#h1 = plt.hist(movies.BudgetMillions)

plt.hist(movies.BudgetMillions)
plt.show()


# In[38]:


plt.hist(movies[movies.Genre == 'Drama'].BudgetMillions)
plt.show()


# In[39]:


movies.head()


# In[40]:


#movies.Genre.unique()


# In[41]:


# Below plots are stacked histogram becuase overlaped

plt.hist(movies[movies.Genre == 'Action'].BudgetMillions, bins = 20)
plt.hist(movies[movies.Genre == 'Thriller'].BudgetMillions, bins = 20)
plt.hist(movies[movies.Genre == 'Drama'].BudgetMillions, bins = 20)
plt.legend()
plt.show()  


# In[42]:


plt.hist([movies[movies.Genre == 'Action'].BudgetMillions,          movies[movies.Genre == 'Drama'].BudgetMillions,           movies[movies.Genre == 'Thriller'].BudgetMillions,           movies[movies.Genre == 'Comedy'].BudgetMillions],
         bins = 20, stacked = True)
plt.show()  


# In[43]:


# if you have 100 categories you cannot copy & paste all the things

for gen in movies.Genre.cat.categories:
    print(gen)


# In[44]:


vis1 = sns.lmplot(data=movies, x='CriticRating', y='AudienceRating',                 fit_reg=False)


# In[45]:


vis1 = sns.lmplot(data=movies, x='CriticRating', y='AudienceRating',                 fit_reg=False, hue = 'Genre')


# In[46]:


vis1 = sns.lmplot(data=movies, x='CriticRating', y='AudienceRating',                 fit_reg=False, hue = 'Genre', size = 10,aspect=1) 


# In[47]:


# Kernal Density Estimate plot ( KDE PLOT) 
# how can i visulize audience rating & critics rating . using scatterplot


# In[48]:


k1 = sns.kdeplot(movies.CriticRating,movies.AudienceRating)

# where do u find more density and how density is distibuted across from the the chat 
# center point is kernal this is calld KDE & insteade of dots it visualize like this
# we can able to clearly see the spread at the audience ratings


# In[49]:


k1 = sns.kdeplot(movies.CriticRating,movies.AudienceRating,shade = True,shade_lowest=False,cmap='Reds')


# In[50]:


k2 = sns.kdeplot(movies.CriticRating,movies.AudienceRating,shade_lowest=False,cmap='Greens_r')


# In[51]:


sns.set_style('dark')
k1 = sns.kdeplot(movies.BudgetMillions,movies.AudienceRating,shade_lowest=False,cmap='Greens_r')


# In[52]:


sns.set_style('dark')
k1 = sns.kdeplot(movies.BudgetMillions,movies.AudienceRating)


# In[53]:


k2 = sns.kdeplot(movies.BudgetMillions,movies.CriticRating)


# In[54]:


#subplots

f, ax = plt.subplots(1,2, figsize =(12,6))
#f, ax = plt.subplots(3,3, figsize =(12,6))


# In[55]:


f, axes = plt.subplots(1,2, figsize =(12,6))

k1 = sns.kdeplot(movies.BudgetMillions,movies.AudienceRating,ax=axes[0])
k2 = sns.kdeplot(movies.BudgetMillions,movies.CriticRating,ax = axes[1])


# In[56]:


axes


# In[57]:


#Box plots - 

w = sns.boxplot(data=movies, x='Genre', y = 'CriticRating')


# In[58]:


#violin plot

z = sns.violinplot(data=movies, x='Genre', y = 'CriticRating') 


# In[59]:


w1 = sns.boxplot(data=movies[movies.Genre == 'Drama'], x='Year', y = 'CriticRating')


# In[60]:


z = sns.violinplot(data=movies[movies.Genre == 'Drama'], x='Year', y = 'CriticRating')


# In[61]:


# Createing a Facet grid


# In[62]:


g =sns.FacetGrid (movies, row = 'Genre', col = 'Year', hue = 'Genre') #kind of subplots


# In[63]:


plt.scatter(movies.CriticRating,movies.AudienceRating)


# In[64]:


g =sns.FacetGrid (movies, row = 'Genre', col = 'Year', hue = 'Genre')
g = g.map(plt.scatter, 'CriticRating', 'AudienceRating' ) #scatterplots are mapped in facetgrid


# In[65]:


# you can populated any type of chat. 

g =sns.FacetGrid (movies, row = 'Genre', col = 'Year', hue = 'Genre')
g = g.map(plt.hist, 'BudgetMillions') #scatterplots are mapped in facetgrid


# In[66]:


#
g =sns.FacetGrid (movies, row = 'Genre', col = 'Year', hue = 'Genre')
kws = dict(s=50, linewidth=0.5,edgecolor='black')
g = g.map(plt.scatter, 'CriticRating', 'AudienceRating',**kws ) #scatterplots are mapped in facetgrid


# In[67]:


# python is not vectorize programming language
# Building dashboards (dashboard - combination of chats)

sns.set_style('darkgrid')
f, axes = plt.subplots (2,2, figsize = (15,15))

k1 = sns.kdeplot(movies.BudgetMillions,movies.AudienceRating,ax=axes[0,0])
k2 = sns.kdeplot(movies.BudgetMillions,movies.CriticRating,ax = axes[0,1])

k1.set(xlim=(-20,160))
k2.set(xlim=(-20,160))

z = sns.violinplot(data=movies[movies.Genre=='Drama'], x='Year', y = 'CriticRating', ax=axes[1,0])

k4 = sns.kdeplot(movies.CriticRating,movies.AudienceRating,shade = True,shade_lowest=False,cmap='Reds',ax=axes[1,1])

k4b = sns.kdeplot(movies.CriticRating, movies.AudienceRating,cmap='Reds',ax = axes[1,1])

plt.show()


# In[68]:


# How can you style your dashboard  using different color map

# python is not vectorize programming language
# Building dashboards (dashboard - combination of chats)

sns.set_style('dark',{'axes.facecolor':'black'})
f, axes = plt.subplots (2,2, figsize = (15,15))

#plot [0,0]
k1 = sns.kdeplot(movies.BudgetMillions,movies.AudienceRating,                  shade = True, shade_lowest=True,cmp = 'inferno',                  ax = axes[0,0])
k1b = sns.kdeplot(movies.BudgetMillions, movies.AudienceRating,                  cmap = 'cool',ax = axes[0,0])

#plot [0,1]
k2 = sns.kdeplot(movies.BudgetMillions,movies.CriticRating,                 shade=True, shade_lowest=True, cmap='inferno',                 ax = axes[0,1])
k2b = sns.kdeplot(movies.BudgetMillions,movies.CriticRating,                  cmap = 'cool', ax = axes[0,1])

#plot[1,0]
z = sns.violinplot(data=movies[movies.Genre=='Drama'],                    x='Year', y = 'CriticRating', ax=axes[1,0])

#plot[1,1]
k4 = sns.kdeplot(movies.CriticRating,movies.AudienceRating,                  shade = True,shade_lowest=False,cmap='Blues_r',                  ax=axes[1,1])

k4b = sns.kdeplot(movies.CriticRating, movies.AudienceRating,                   cmap='gist_gray_r',ax = axes[1,1])


k1.set(xlim=(-20,160))
k2.set(xlim=(-20,160))

plt.show()


# Conclusion we use so far for visualization - 1> category datatype in python 2> jointplots 3> histogram 4> stacked histograms 5> Kde plot 6> subplot 7> violin plots 8> Factet grid 9> Building dashboards

# EAD completed yay :)
