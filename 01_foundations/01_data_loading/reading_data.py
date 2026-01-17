# Titanic Dataset — Data Loading

# %%
import pandas as pd

# %% [markdown]
# used "..//..//" --> to acess the data that was out of the code folder

#%%
df=pd.read_csv("..//..//datasets//titanic.csv")
print("Loaded Titanic dataset:", df.shape)
# %%
df.head()
# %%
df.tail()
# %%
df.shape
# %%
df.columns
# %%
df.info()

