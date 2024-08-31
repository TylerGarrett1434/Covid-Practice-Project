#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
print('Modules are imported')


# In[141]:


corona_dataset_csv = pd.read_csv("Datasets/covid19_Confirmed_dataset.csv")
corona_dataset_csv.head(8)


# In[142]:


corona_dataset_csv.shape


# In[143]:


corona_dataset_csv.drop(["Lat","Long"],axis=1,inplace=True)


# In[144]:


corona_dataset_csv.head(8)


# In[145]:


corona_dataset_aggregated=corona_dataset_csv.groupby("Country/Region").sum()


# In[146]:


corona_dataset_aggregated.head(8)


# In[147]:


corona_dataset_aggregated.shape


# In[148]:


corona_dataset_aggregated.loc["China"].plot()
corona_dataset_aggregated.loc["Afghanistan"].plot()
corona_dataset_aggregated.loc["Spain"].plot()
plt.legend()


# In[149]:


corona_dataset_aggregated.loc["China"][:3].plot()


# In[150]:


corona_dataset_aggregated.loc["China"].diff().plot()


# In[151]:


corona_dataset_aggregated.loc["China"].diff().max()


# In[152]:


corona_dataset_aggregated.loc["Brazil"].diff().max()


# In[153]:


countries= list(corona_dataset_aggregated.index)
max_infection_rates=[]
for c in countries :
    max_infection_rates.append(corona_dataset_aggregated.loc[c].diff().max())
max_infection_rates


# In[154]:


corona_dataset_aggregated["max_infection_rate"]=max_infection_rates


# In[155]:


corona_dataset_aggregated.head()


# In[156]:


corona_data=pd.DataFrame(corona_dataset_aggregated["max_infection_rate"])


# In[157]:


corona_data.head()


# In[158]:


corona_data.tail()


# In[164]:


happiness_report_csv=pd.read_csv("Datasets/worldwide_happiness_report.csv")
happiness_report_csv.head()


# In[160]:





# In[161]:





# In[165]:


useless_cols=["Overall rank","Score", "Generosity","Perceptions of corruption"]


# In[167]:


happiness_report_csv.drop(useless_cols, axis=1, inplace=True)


# In[168]:


happiness_report_csv.head()


# In[169]:


happiness_report_csv.set_index("Country or region", inplace=True)


# In[170]:


corona_data.shape


# In[171]:


happiness_report_csv.shape


# In[172]:


data=corona_data.join(happiness_report_csv,how="inner")
data.head()


# In[173]:


data.corr()


# In[174]:


data.head()


# In[ ]:




