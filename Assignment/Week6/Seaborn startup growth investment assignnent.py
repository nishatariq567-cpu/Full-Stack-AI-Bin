import numpy as np
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt

df=pd.read_csv("Week6/startup_growth_investment_data.csv",delimiter=",",index_col="Startup Name")
print(df)
dffilter=df.head(10)
sns.set_theme(style="whitegrid")

g=sns.displot(data=dffilter,x="Investment Amount (USD)",y="Industry")
g.figure.suptitle("sns.displot(data=dffilter,x=Investment Amount (USD),y=Industry)")
g.figure.show()
read=input("Wait for me...")

g=sns.barplot(data=dffilter,x="Investment Amount (USD)",y="Funding Rounds")
g.figure.suptitle("sns.barplot(data=dffilter,x=Investment Amount (USD),y=Funding Rounds)")
g.figure.show()
read=input("Wait for me...")

g=sns.boxplot(data=dffilter,x="Number of Investors",y="Industry")
g.figure.suptitle("sns.barplot(data=dffilter,x=Number of Investors,y=Industry)")
g.figure.show()
read=input("Wait for me....")

g=sns.lineplot(data=dffilter,x="Growth Rate (%)",y="Year Founded")
g.figure.suptitle("sns.lineplot(data=dffilter,x=Growth Rate (%),y=Year Founded)")
g.figure.show()
read=input("Wait for me....")

g=sns.histplot(data=dffilter,x="Investment Amount (USD)",bins=30,kde=True)
g.figure.suptitle("sns.histplot(data=dffilter,x=Investment Amount (USD),bins=30,kde=True)")
g.figure.show()
read=input("Wait for me...")

g=sns.kdeplot(data=dffilter,x="Year Founded",y="Investment Amount (USD)",fill=True,cmap="Reds")
g.figure.suptitle("sns.kdeplot(data=dffilter,x=Year Founded,y=Investment Amount (USD),fill=True,cmap=Reds)")
g.figure.show()
read=input("Wait for me...")

g=sns.catplot(data=dffilter,x="Number of Investors",y="Funding Rounds")
g.figure.suptitle("sns.catplot(data=dffilter,x=Number of Investors,y=Funding Rounds)")
g.figure.show()
read=input("Wait for me....")

glue=dffilter.pivot(columns="Country",values="Funding Rounds")
g=sns.heatmap(glue)
g.figure.suptitle("sns.heatmap(glue)-dffilter.pivot(columns=Country,values=Funding Rounds)")
g.figure.show()
read=input("Wait for me...")
