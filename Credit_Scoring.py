#%%
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

df = pd.read_csv('Credit_Scoring.csv')
df.info()

# %%
df

# %%
#Thực hiện xử lý giá trị khuyết thiếu
df.isna()

# %%
df.fillna(0, inplace=True)
df
# %%
sns.boxplot(x=df['Unnamed: 0'])

# %%
sns.boxplot(x=df['SeriousDlqin2yrs'])
#%%
sns.boxplot(x=df['RevolvingUtilizationOfUnsecuredLines'])
#%%
sns.boxplot(x=df['age'])
#%%
sns.boxplot(x=df['NumberOfTime30-59DaysPastDueNotWorse'])
#%%
sns.boxplot(x=df['DebtRatio'])
#%%
sns.boxplot(x=df['MonthlyIncome'])
#%%
sns.boxplot(x=df['NumberOfOpenCreditLinesAndLoans'])
#%%
sns.boxplot(x=df['NumberOfTimes90DaysLate'])
#%%
sns.boxplot(x=df['NumberRealEstateLoansOrLines'])

#%%
sns.boxplot(x=df['NumberOfTime60-89DaysPastDueNotWorse'])

#%%
sns.boxplot(x=df['NumberOfDependents'])

#%%
Q1 = df['NumberOfOpenCreditLinesAndLoans'].quantile(0.25)
Q3 = df['NumberOfOpenCreditLinesAndLoans'].quantile(0.75)
IQR = Q3 - Q1
df['outlier'] = ~((df['NumberOfOpenCreditLinesAndLoans'] < (Q1 - 1.5*IQR)) | (df['NumberOfOpenCreditLinesAndLoans'] > (Q3 + 1.5*IQR)))
df = df[df['outlier'] == True]
sns.boxplot(x=df['NumberOfOpenCreditLinesAndLoans'])

# %%
