import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df=pd.read_csv("Week6/FastFoodRestaurants.csv",delimiter=",",index_col="address")
print(df)
dffilter=df.head(20)
sns.set_style(style="whitegrid")

g=sns.displot(data=dffilter,x="longitude",y="latitude")
g.figure.suptitle("sns.displot(data=dffilter,x=longitude,y=latitude)")
g.figure.show()
read=input("Wait for me...")

g=sns.scatterplot(data=dffilter,x="longitude",y="latitude")
g.figure.suptitle('sns.scatterplot(data=dffilter,x=longitude,y=latitude)')
g.figure.show()
read=input("Wait for me....")

g=sns.boxplot(data=dffilter,x="province",y="latitude")
g.figure.suptitle("sns.boxplot(data=dffilter,x=province,y=latitude)")
g.figure.show()
read=input("Wait for me....")

g=sns.histplot(data=dffilter,x="latitude",bins=30,kde=True)
g.figure.suptitle("sns.histplot(data=dffilter,x=latitude,bins=30,kde=True)")
g.figure.show()
read=input("Wait for me....")

g=sns.lineplot(data=dffilter,x="longitude",y="latitude")
g.figure.suptitle("sns.lineplot(data=dffilter,x=longitude,y=latitude)")
g.figure.show()
read=input("Wait for me.....")

g=sns.kdeplot(data=dffilter,x="longitude",y="latitude" ,fill=True ,cmap="Reds")
g.figure.suptitle("sns.kdeplot(data=dffilter,x=longitude,y=latitude ,fill=True ,cmap=Reds)")
g.figure.show()
read=input("Wait for me...")

g=sns.catplot(data=dffilter,x="province",y="latitude")
g.figure.suptitle("sns.catplot(data=dffilter,x=province,y=latitude)")
g.figure.show()
read=input("Wait for me....")

glue=dffilter.pivot(columns="city",values="latitude")
g=sns.heatmap(glue)
g.figure.suptitle("sns.heatmap(glue)-dffilter.pivot(columns=city,values=latitude)")
g.figure.show()
read=input("Wait for me...")

