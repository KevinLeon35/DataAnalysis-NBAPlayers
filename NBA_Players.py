#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#import all modules
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[ ]:


#read the date file into a dataframe called NBA from a csv file called all_seasons.csv
#This csv file is in the same folder with this notebook file
NBA = pd.read_csv('all_seasons.csv')


# In[ ]:


#show the top 5 rows of the NBA dataframe
NBA.head(5)


# In[ ]:


#Shows column info of each column
NBA.info()


# In[ ]:


# Remove the "Unnamed: 0" Column since it is duplicate with the index column
NBA = NBA.drop('Unnamed: 0', axis = 1)


# In[ ]:


#show the top 5 rows of the NBA dataframe again, no "Unnamed: 0" column again this time, looks better.
NBA.head(5)


# In[ ]:


#How many records in total
NBA["player_name"].count()


# In[ ]:


#How many teams in total
NBA['team_abbreviation'].nunique()


# In[ ]:


#What are team abbreviations of each team
NBA['team_abbreviation'].unique()


# In[ ]:


# Oldest age among all player records
NBA['age'].max()


# In[ ]:


#Who is the oldest player among all player records
NBA[NBA['age'] == NBA['age'].max()]['player_name']


# In[ ]:


#Who is the youngest player among all player records, return all if there are more than one.
NBA[NBA['age'] == NBA['age'].min()]['player_name']


# In[ ]:


#Each country has how many player records
NBA['country'].value_counts()


# In[ ]:


#Average points of all player records
NBA['pts'].mean()


# In[ ]:


#Count of players per season
NBA.groupby(by = 'season')['player_name'].nunique()


# In[ ]:


#Each team's highest player average points
NBA.groupby(by = 'team_abbreviation')['pts'].max()


# In[ ]:


#A hist plot of Each team's highest player average points
NBA.groupby(by = 'team_abbreviation')['pts'].max().plot.hist()


# In[ ]:


#A box plot of Each team's highest player average points
NBA.groupby(by = 'team_abbreviation')['pts'].max().plot.box()


# In[ ]:


#A kde plot of Each team's highest player average points
NBA.groupby(by = 'team_abbreviation')['pts'].max().plot.kde()


# In[ ]:


# Because the NBA dataframe has too many records, now I am generating another dataframe from the NBA dataframe.
#Get a sub dataframe of the NBA datafream where only season 2018-19 and 2019-20's 1st round drafted players' record are selected.
NBA2 = NBA[((NBA['season'] == '2019-20') | (NBA['season'] == '2018-19')) & (NBA['draft_round'] == '1')]


# In[ ]:


#Generate a jointplot betweeb age and pts of the NBA2 dataframe.
sns.jointplot(x='age', y = 'pts', data=NBA2)


# In[ ]:


#A distplot of player height of the NBA2 dataframe, with the kde line.
sns.distplot(NBA2['player_height'], bins=30, kde=True, color='blue')


# In[ ]:


#A boxplot showing relationship between each team and player's rebound stats, data frame is NBA2
plt.figure(figsize=(20,10))
sns.boxplot(x = 'team_abbreviation', y ='reb', data=NBA2, palette = 'rainbow')


# In[ ]:


# A sub dataframe NBA3 which has player records of season 2019-20 but only with players who were drafted in round 1 or round 2
NBA3 = NBA[(NBA['season'] == '2019-20')  & ((NBA['draft_round'] == '1') | (NBA['draft_round'] == '2'))]


# In[ ]:


#A swarmplot showing relationship between draft years and player's assist stats, hue indicator is draft round,data frame is NBA3
plt.figure(figsize=(20,10))
sns.swarmplot(x='draft_year',y='ast',data=NBA3,palette='Set2', hue='draft_round')


# In[ ]:


#count of player records of all times per round, dataframe is NBA
sns.countplot(x = 'draft_round', data=NBA)


# In[ ]:


# Heat map of dataframe NBA3
sns.heatmap(NBA3.corr(), cmap='coolwarm')
plt.title('NBA3.corr()')


# In[ ]:


N = sns.FacetGrid(data=NBA3, col = 'draft_round')
N.map(plt.hist, 'age')


# In[ ]:


#Warning:  This may take a while to run since the dataframe NBA is big to generate a pairplot
sns.pairplot(data=NBA)


# In[ ]:




