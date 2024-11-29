#importing matplotlib
import matplotlib.pyplot as plt
#importing numpy
import numpy as np
#importing seaborn
import seaborn as sns
#importing pandas
import pandas as pd
#Reading dataframe
df=pd.read_csv('bes.csv')
print(df.info())
#checking for null values
df.isnull().any()
#
priceQ1=np.quantile(df['Price'], 0.25)
print(" Q1 is !! " ,priceQ1)
#
priceQ2=np.quantile(df['Price'], 0.50)
print(" Q2 is !! " ,priceQ2)
#
priceQ3=np.quantile(df['Price'], 0.75)
print(" Q3 is!! " ,priceQ3)
#finding intel quantile
I_dont_know_what_to_name_this=priceQ1-priceQ3
print("the intel quantile range is this " ,I_dont_know_what_to_name_this)
#
#
#creating a box plot
sns.set_theme('paper')
sns.set_color_codes('blue')
sns.set_style('darkgrid')
sns.boxplot(df,x='Price',y='User Rating')
plt.show()