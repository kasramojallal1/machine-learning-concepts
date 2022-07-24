#%%

import seaborn as sns
df = sns.load_dataset("penguins")
sns.pairplot(df, hue="species")

# %%
