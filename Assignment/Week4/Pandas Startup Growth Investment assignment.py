import pandas as pd

df=pd.read_csv("Week4/startup_growth_investment_data.csv",delimiter=",")
print("Data type of Dataframe =",df.dtypes)
print("Dataframe info is here =",df.info())

# Print last three rows
print("Last three rows is here =",df.tail(3))

# Print First three rows 
print("first three rows is here =",df.head(3))

# Summary of Statistic of Dataframe using describe() method 
print("Summary of Statistic dataframe =",df.describe())

# Counting the rows and columns of Dataframe by using shape() method 
print("Countign of rows and columns =",df.shape)

# Access the column by name 
print("Access column by name =",df['Industry'])

# Access Multiple columns by name 
print("Access multiple columns by name =",df[['Funding Rounds','Investment Amount (USD)']])

# Selecting a single row by using .loc
print("Selecting a single row =",df.loc[0])

# Selecting multiple rows by using .loc
print("Selecting multiple rows =",df.loc[[2,3]])

# Conditional selection of rows using .loc
print("Conditional selection of rows =",df.loc[df["Funding Rounds"]==3])

# Selecting a single column using .loc
print("Selecting a single column using loc =",df.loc[:7,'Valuation (USD)'])

# Selecting multiple columns using .loc
print("Selecting multiple columns using loc =",df.loc[:10,["Funding Rounds","Industry"]])

# Selecting a slice of columns using .loc
print("Selecting a slice of columns using .loc =",df.loc[:,'Startup Name':'Valuation (USD)'])

# Combined row and column selection using .loc
print("Combining row and column selection using .loc =",df.loc[df["Funding Rounds"]==3,'Number of Investors'])

# Taking index column
df_index_col=pd.read_csv("Week4/startup_growth_investment_data.csv",delimiter=",",index_col="Startup Name")
print(df_index_col)
print("Data type of df_index_col",df_index_col.dtypes)
print("Info of df_index_col =",df_index_col.info())

# Selecting a single row using .loc
print("Selecting a single row =",df_index_col.loc["Startup_16"])

# Selecting multiple rows using .loc
print("Selecting multiple rows =",df_index_col.loc[["Startup_17","Startup_19"]])

# Selecting a slice of rows using .loc
print("Selecting a slice of rows =",df_index_col.loc["Startup_17":"Startup_22"])

# Conditional selection of rows using .loc
print("Conditional selection of rows =",df_index_col.loc[df_index_col['Funding Rounds']==3])

# Selecting a single column using .loc
print("Selecting a single column =",df_index_col.loc[:"Startup_19","Valuation (USD)"])

# Selecting multiple columns using .loc
print("Selecting multiple columns =",df_index_col.loc[:"Startup_7",["Industry","Growth Rate (%)"]])

# Selecting a slice of columns using .loc
print("Selecting a slice of columns using .loc =",df_index_col.loc[:"Startup_16","Valuation (USD)":"Growth Rate (%)"])

# Combined row and column selection using .loc
print("combining row and column using .loc =",df_index_col.loc[df_index_col["Funding Rounds"]==3,'Year Founded'])

# Selecting a single row using .iloc
print("Selecting a single row using .iloc =",df_index_col.iloc[0])

# Selecting multiple rows using .iloc
print("Selecting multiple rows using .iloc =",df_index_col.iloc[[1,2,3]])

# Selecting a slice of rows using .iloc
print("Selecting a slice of rows using .iloc =",df_index_col.iloc[5:7])

# Selecting a single column using .iloc
print("Selecting a single column using .iloc =",df_index_col.iloc[:,0])

# Selecting multiple columns using .iloc
print("Selecting multiple column using .iloc =",df_index_col.iloc[:,[2,5]])

# Selecting a slice of columns using .iloc
print("Selecting a slice of columns using .iloc =",df_index_col.iloc[:,2:7])

# Combined row and column selection using .iloc
print("Combining row and column using .iloc =",df_index_col.iloc[[2,3,4],2:4])

#Add a New Row to a Pandas DataFrame
# add a new row
df.loc[len(df.index)]=["Startup_55000","Fintech",5,40800669.12,126466287292.17991,66,"France",2050,9.44]
print(df)

# Remove Rows from a Pandas DataFrame using drop with axis
df.drop(1,axis=0,inplace=True)
df.drop(index=2,inplace=True)

# Remove Multiple Rows using drop with axis
df.drop([4,5],axis=0,inplace=True)
print("After removing multiple rows",df)

# Delete Columns from a pandas DataFrame using drop
df.drop("Growth Rate (%)",axis=1,inplace=True)
df.drop(columns="Year Founded",inplace=True)

# Delete Multiple columns using drop
df.drop(["Number of Investors","Valuation (USD)"],axis=1,inplace=True)
print("Deleting multiple columns =",df)

# Rename Labels in a DataFrame
# rename column 'Name' to 'First_Name'
df.rename(columns={"Industry":"Industry_Names"},inplace=True)

# rename multiple columns
df.rename(mapper={"Country":"Country_Name","Investment Amount (USD)":"Investment_Amount_(USD)"},axis=1,inplace=True)
print(df)

#Example: Rename Row Labels
# rename row one index label
df.rename(index={"Startup_1":"Startup_1111111"},inplace=True)
# remane multiple rows by index
df.rename(mapper={"Startup_2":"Startup_222222","Startup_4":"Startup_444444"},axis=1,inplace=True)
print(df)

# query() to Select Data
# The query() method in Pandas allows you to select data using a more SQL-like syntax.
# select the rows where the age is greater than 25
Selection_row = df.query("Country_Name == 'France' or `Startup Name` == 'Startup_1111111'")
print(Selection_row.to_string())
print(len(Selection_row))

# sort DataFrame by Funding Rounds in ascending order
sorted_df=df.sort_values(by="Investment_Amount_(USD)")
print(sorted_df.to_string(index=False))
print(sorted_df)

# sorted Dataframe by Funding Rounds and Country_Name
df1=df.sort_values(by=["Investment_Amount_(USD)","Country_Name"])
print(df1.to_string(index=False))
print(df1)

#Pandas groupby
# In Pandas, the groupby operation lets us group data based on specific columns. This means we can divide a DataFrame into smaller groups based on the values in these columns.
# group the DataFrame by the location_id column and
# calculate the sum of price for each category
grouped=df.groupby("Startup Name")["Industry_Names"].sum()
print(grouped.to_string())
print(len(grouped))

# use dropna() to remove rows with any missing values
cleaned_data=df.dropna()
print("Cleaned Data: \n",cleaned_data)

# filling NaN values with '0'
df.fillna(0,inplace=True)
print("After filling NaN with 0 =",df)

# create a list named data
data=[1,2,3,5]
array1=pd.array(data)
print(array1)

# creating a pandas.array of integers
int_array=pd.array([1,2,5,7,8],dtype="int")
print(int_array)

