#!/usr/bin/env python
# coding: utf-8

# In[1]:


import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

client_credentials_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


# In[2]:


import pandas as pd


data = pd.read_csv('new_to_this.csv', delimiter=',' )


# In[3]:


track_id = data['URI']
track_name = data['Track Name']
artist_name = data ['Artist Name']


# In[4]:


df=pd.DataFrame({'artist_name':artist_name,'track_name':track_name,'track_id':track_id})
print(df.shape)
df.head()


# In[5]:


df.info()

#we did this to check if there are null items or not. Check the corresponding document with it to write it in the report.


# In[6]:


df.shape


# In[7]:


rows = []
batchsize = 100
NoneC = 0

for i in range(0,len(df['track_id']),batchsize):
    batch = df['track_id'][i:i+batchsize]
    feature_results = sp.audio_features(batch)
    for i, t in enumerate(feature_results):
        if t == None:
            NoneC = NoneC + 1
        else:
            rows.append(t)
            
print('Number of tracks where no audio features were available:',NoneC)


# In[8]:


print('number of elements in the track_id list:', len(rows))


# In[9]:


df_audio_features = pd.DataFrame.from_dict(rows,orient='columns')
print("Shape of the dataset:", df_audio_features.shape)
df_audio_features.head()


# In[10]:


df_audio_features.info()


# In[11]:


df_audio_features.rename(columns={'id': 'track_id'}, inplace=True)

df_audio_features.shape


# In[12]:


df_audio_features.head()


# In[13]:


dff = pd.merge(df,df_audio_features,on='track_id',how='inner')
print("Shape of the dataset:", df_audio_features.shape)
dff.head()


# In[14]:


dff.to_csv('OmgFinally3.csv')


# <h1>This is the third playlist. Can only have 100 inputs in an excel file. I would recommend that download the track list again for all the playlists and then divide into excel sheets with 100 songs each.

# In[ ]:




