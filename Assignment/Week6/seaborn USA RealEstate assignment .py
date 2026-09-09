import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt 

df=pd.read_csv("Week6/RealEstate-USA.csv",delimiter=",",index_col="brokered_by")
print(df.dtypes)
dffilter=df.head(40)
dffilter100=df.head(100)
sns.set_theme(style="darkgrid")
sns.set_theme(style="whitegrid",rc={"axes.facecolor":"grey","grid.color":"white"})

g=sns.displot(data=dffilter, x="price" , y="city")
g.figure.suptitle("sns.displot(data=dffilter, x=price , y=city) ")
g.figure.show()
read = input("Wait for me....")

g=sns.kdeplot(data=dffilter,x="price",y="zip_code")
g.figure.suptitle("sns.displot(data=dffilter, x=price ,y=zip_code)")
g.figure.show()
read=input("wait for me....")

g=sns.histplot(data=dffilter,x="price",y="bath")
g.figure.suptitle("sns.histplot(data=dffilter,x=price,y=bath)")
g.figure.show()
read=input("Wait for me....")

g=sns.scatterplot(data=dffilter,x="price",y="bed")
g.figure.suptitle("sns.scatterplot(data=dffilter,x=price,y=bed)")
g.figure.show()
read=input("Wait for me....")

g=sns.lineplot(data=dffilter,x="zip_code",y="price")
g.figure.suptitle("sns.lineplot(data=dffilter,x=zip_code,y=price)")
g.figure.show()
read=input("Wait for me ....")

g=sns.barplot(data=dffilter,x="price",y="bath")
g.figure.suptitle("sns.barplot(data=dffilter,x=price,y=bath)")
g.figure.show()
read=input("Wait for me....")

g=sns.catplot(data=dffilter,x="bed",y="price")
g.figure.suptitle("sns.catplot(data=dffilter,x=bed,y=price)")
g.figure.show()
read=input("Wait for me....")

g=sns.boxplot(data=dffilter,x="zip_code",y="price")
g.figure.suptitle("sns.boxplot(data=dffilter,x=zip_code,y=price)")
g.figure.show()
read=input("Wait for me....")

g=sns.JointGrid(data=dffilter,x="price",y="bed")
g.figure.suptitle("sns.JointGrid(data=dffilter,x=price,y=bed)")
g.figure.show()
read=input("Wait for me...")

glue=dffilter.pivot(columns="price",values="acre_lot")
g=sns.heatmap(glue)
g.figure.suptitle("sns.heatmap(glue) -glue=dffilter.pivot(columns=price,values=acre_lot)")
g.figure.show()
read=input("Wait for me...")
