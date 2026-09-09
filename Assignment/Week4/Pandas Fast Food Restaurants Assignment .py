import pandas as pd
df=pd.read_csv("Week4/FastFoodRestaurants.csv",delimiter=",")
print(df)
print("Data type of Dataframe =",df.dtypes)
print("Info of Dataframwe =",df.info())

# Print Last three rows
print("Last three rows =",df.tail(3))

# Print First three rows 
print("First three rows =",df.head(3))

# Summary of Statistic of Dataframe using describe() method 
print("Summary of Statistic of dataframe =",df.describe())

# Counting the rows and columns of Dataframe by using shape() method
print("Counting the rows and columns =",df.shape)

# Access the column by name 
print("Access the single Column =",df["city"])

# Access Multiple columns by name 
print("Access the multiple Columns =",df[['city','country']])

# Selecting a single row by using .loc
print("Selecting a single row using .loc =",df.loc[0])

# Selecting multiple rows by using .loc
print("Selecting multiple rows using .loc =",df.loc[[2,3]])

# Conditional selection of rows using .loc
print("Conditional selection of rows =",df.loc[df["city"]=="Massena"])

# Selecting a single column using .loc
print("Selecing a single column using .loc =",df.loc[:7,'city'])

# Selecting multiple columns using .loc
print("Selecting multiple columns using .loc =",df.loc[:10,["city","country"]])

# Selecting a slice of columns using .loc
print("Selecting a slice of columns =",df.loc[:,"address":"name"])

# Combined row and column selection using .loc
print("Combining rows and columns selection =",df.loc[df["city"]=="Massena","name"])

# Taking index column
df_col_index=pd.read_csv("Week4/FastFoodRestaurants.csv",delimiter=",",index_col="address")
print(df_col_index)
print("Data type of df_index_col",df_col_index.dtypes)
print("Info of df_index_col =",df_col_index.info())

# Selecting a single row using .loc
print("Selecting a single row using .loc =",df_col_index.loc['401 N Jennings St'])

# Selecting multiple rows using .loc
print("Selecting multiple rows using .loc =",df_col_index.loc[['613 W Center St','301 University Blvd']])

# Selecting a slice of rows using .loc
print("Selecting a slice of rows using .loc =",df_col_index.loc['324 Main St':'125 Towne Center Dr'])

# Conditional selection of rows using .loc
print("Conditional selection of rows using .loc =",df_col_index.loc[df_col_index['city']=='Massena'])

# Selecting a single column using .loc
print("Selecting a single column using .loc =",df_col_index.loc[:'613 W Center St','latitude'])

# Selecting multiple columns using .loc
print("Selecting multiple column using .loc =",df_col_index.loc[:'512 Highway 425 S Lot B',['city','country']])

# Selecting a slice of columns using .loc
print("Selectig a slice of columns using .loc =",df_col_index.loc[:'401 N Jennings St',"city":"name"])

# Combined row and column selection using .loc
print("combining row and column using .loc =",df_col_index.loc[df_col_index['name']=="McDonald's",'province'])

# Selecting a single row using .iloc
print("Selecting a single row using .iloc =",df_col_index.iloc[0])

# Selecting multiple rows using .iloc
print("Selecting multiple rows using .iloc =",df_col_index.iloc[[1,2]])

# Selecting a slice of rows using .iloc
print("Selecting a slice of rows using .iloc =",df_col_index.iloc[2:5])

# Selecting a single column using .iloc
print("Selecting a single column using .iloc =",df_col_index.iloc[:,0])

# Selecting multiple columns using .iloc
print("Selecting Multiple columns using .iloc =",df_col_index.iloc[:,[2,5]])

# Selecting a slice of columns using .iloc
print("Selecting a slice of columns using .iloc =",df_col_index.iloc[:,0:3])

# Combined row and column selection using .iloc
print("Combinig the rows and columns using .iloc =",df_col_index.iloc[[2,3,4],2:6])

#Add a New Row to a Pandas DataFrame
# add a new row
df.loc[len(df.index)]=["24444 Main St","Masseeeena","USA","uuuus/nnny/massena/32544mainst/-111999",99.9213,-99.89021,"McDoooonald's",13662,"NY","http://mcdonaldddds.com,http://www.mcdonalds.com/?cid=RF:YXT_FM:TP::Yext:Referralid",67777,333,5666,45566,4555]
print(df)

# Remove Rows from a Pandas DataFrame using drop with axis
df.drop(1,axis=0,inplace=True)
df.drop(index=2,inplace=True)

# Remove Multiple Rows using drop with axis
df.drop([3,4,5],axis=0,inplace=True)
print("After Drop the rows =",df)

# Delete Columns from a pandas DataFrame using drop
df.drop("Class",axis=1,inplace=True)
df.drop(columns="Fees",inplace=True)

# Delete Multiple columns using drop
df.drop(['Admission','Table'],axis=1,inplace=True)

# Rename Labels in a DataFrame
# rename column 'Name' to 'First_Name'
df.rename(columns={"LLMS":"LMS_ID"},inplace=True)

# rename multiple columns
df.rename(mapper={"province":"province_Name","postalCode":"postal_Code"},axis=1,inplace=True)
print(df)

#Example: Rename Row Labels
# rename row one index label
df.rename(index={'139 Columbus Rd':'1434 hcolumbus Rd'},inplace=True)
# remane multiple rows by index
df.rename(mapper={"590 S Main St":"50 BHakkar Road St","613 W Center St":"61113 Center Street"})
print(df)

# query() to Select Data
# The query() method in Pandas allows you to select data using a more SQL-like syntax.
# select the rows where the age is greater than 25
Selection_row=df.query("country==\'USA\' or latitude >= 44")
print(Selection_row.to_string())
print(len(Selection_row))

# sort DataFrame by Keys in ascending order
Sorted_df=df.sort_values(by="keys")
print(Sorted_df.to_string(index=False))
print(Sorted_df)

# sorted Dataframe by Keys and city
df1=df.sort_values(by=['keys','city'])
print(Sorted_df.to_string(index=True))
print(df1)

#Pandas groupby
# In Pandas, the groupby operation lets us group data based on specific columns. This means we can divide a DataFrame into smaller groups based on the values in these columns.
# group the DataFrame by the location_id column and
# calculate the sum of price for each category
grouped=df.groupby("city")['country'].sum()
print(grouped.to_string())
print(len(grouped))

# use dropna() to remove rows with any missing values
cleaned=df.dropna()
print("Cleaned data of missing values =",cleaned)

# filling NaN values with '0' and missing
text_cols=df.select_dtypes(include=['object','string']).columns
df[text_cols]=df[text_cols].fillna("missing")

num_cols=df.select_dtypes(include=['number']).columns
df[num_cols]=df[num_cols].fillna(0)

# create a list named data
data=[1,2,3,5]
array1=pd.array(data)
print(array1)

# creating a pandas.array of integers
int_array=pd.array([1,2,5,7,8],dtype="int")
print(int_array)



