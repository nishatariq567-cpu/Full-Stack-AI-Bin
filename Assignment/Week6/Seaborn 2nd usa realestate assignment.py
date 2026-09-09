import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df=pd.read_csv("Week6/Real_Estate_Sales_2001-2022_GL-Short.csv",delimiter=",",index_col="Serial Number")
print(df)
dffilter=df.head(40)
sns.set_theme(style="whitegrid")

g=sns.barplot(data=dffilter,x="Sale Amount",y="Town")
g.figure.suptitle("sns.barplot(data=dffilter,x=Town,y=Sale Amount)")
g.figure.show()
read=input("Wait for me...")

g=sns.scatterplot(data=dffilter,x="Assessed Value",y="Sale Amount")
g.figure.suptitle("sns.scatterplot(data=dffilter,x=Assessed Value,y=Sale Amount)")
g.figure.show()
read=input("Wait for me....")

g=sns.boxplot(data=dffilter,x="Property Type",y="Sale Amount")
g.figure.suptitle("sns.boxplot(data=dffilter,x=Property Type,y=Sale Amount)")
g.figure.show()
read=input("Wait for me....")

g=sns.lineplot(data=dffilter,x="List Year",y="Sale Amount")
g.figure.suptitle("sns.lineplot(data=dffilter,x=List Year,y=Sale Amount)")
g.figure.show()
read=input("Wait for me....")

g=sns.displot(data=dffilter, x='Sales Ratio', kde=True, color='purple')
g.figure.suptitle("sns.displot(data=dffilter, x=Sales Ratio, kde=True, color=purple)")
g.figure.show()
read=input("Wait for me...")

g=sns.histplot(data=dffilter, x='Sale Amount', bins=30, kde=True)
g.figure.suptitle("sns.histplot(data=dffilter, x=Sale Amount, bins=30, kde=True)")
g.figure.show()
read=input("Wait for me...")

g=sns.kdeplot(data=dffilter, x='Assessed Value', y='Sale Amount', fill=True, cmap='Blues')
g.figure.suptitle("sns.kdeplot(data=dffilter, x=Assessed Value, y=Sale Amount, fill=True, cmap=Blues)")
g.figure.show()
read=input("Wait for me...")

g=sns.catplot(data=dffilter, x='Property Type', y='Sale Amount')
g.figure.suptitle("sns.catplot(data=df, x=Property Type, y=Sale Amount)")
g.figure.show()
read=input("Wait for me....")

glue=dffilter.pivot(columns="Property Type",values="Sale Amount")
g=sns.heatmap(glue)
g.figure.suptitle("sns.heatmap(glue)-dffilter.pivot(columns=Property Type,values=ale Amount)")
g.figure.show()
read=input("Wait for me....")

