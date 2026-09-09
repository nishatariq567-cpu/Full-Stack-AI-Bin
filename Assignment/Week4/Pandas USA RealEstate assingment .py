import pandas as pd

df=pd.read_csv("Week4/RealEstate-USA.csv",delimiter=",")
print(df)
print("Data type of df =",df.dtypes)
print("df info is here =",df.info())

#print last three rows
print("Last three rows :",df.tail(3))

#print first three rows
print("First three rows :",df.head(3))

##Summary of Statistics of DataFrame using describe() method.
print("SUmmary of statistic of dataframe =",df.describe())

#Counting the rows and columns in DataFrame using shape(). 
print("Countinf the rows and colomns in dataframe =",df.shape)

# access the Name column
print("Access the Column by using its name =",df['status'])

## access multiple columns
print("Access Multiple columns =",df[['price','bed']])

#Selecting a single row using .loc
print("Selecting single row =",df.loc[0])

#Selecting multiple rows using .loc
print("Selecting multiple rows =",df.loc[[1,2]])

#Selecting a slice of rows using .loc
print("selecting slice of rows =",df.loc[5:12])

#Conditional selection of rows using .loc
print("conditional seection of rows =",df.loc[df['status']=='sale'])

#Selecting a single column using .loc
print("selecting a single column using loc =",df.loc[:7,'brokered_by'])

#Selecting multiple columns using .loc
print("selecting multiple columns =",df.loc[:,['city','state']])

#Selecting a slice of columns using .loc
print("selecting a slice of colomns =",df.loc[:,'city':'prev_sold_date'])

#Combined row and column selection using .loc
print("Combination of rows and columns =",df.loc[df["status"]=='sale','price'])

#Taking index column
df_index_col=pd.read_csv('Week4/RealEstate-USA.csv',delimiter=",",index_col='brokered_by')
print(df_index_col)
print(df_index_col.dtypes)
print(df_index_col.info())

#Selecting a single row using .loc
print("Selecting Single Row =",df_index_col.loc[80224])

#Selecting multiple rows using .loc
print("selecting multiple rows =",df_index_col.loc[[103378,1589]])

#Selecting a slice of rows using .loc
print("Selecting a slice of rows =",df_index_col.loc[52709:66561])

#Conditional selection of rows using .loc
print("Conditional Selection of row =",df_index_col.loc[df_index_col["status"]=='sale'])

#Selecting a single column using .loc
print("selecting a single column =",df_index_col.loc[:495412,"state"])

#Selecting multiple columns using .loc
print("Selecting multiple columns =",df_index_col.loc[:495412,['state','city']])

#Selecting a slice of columns using .loc
print("Selecting a slice of columns =",df_index_col.loc[:656722,'street':'house_size'])

#Combined row and column selection using .loc
print("Cobining the rows and columns =",df_index_col.loc[df_index_col["status"]=='sale','city'])

#Selecting a single row using .iloc
print("Selecting a single row using index",df_index_col.iloc[0])

#Selecting multiple rows using .iloc
print("Selecting the multiple rows =",df_index_col.iloc[[0,1,2]])

#Selecting a slice of rows using .iloc
print("Selecting a slice of row =",df_index_col.iloc[2:5])

#Selecting a single column using .iloc
print("Selecting a signle column",df_index_col.iloc[:,0])

#Selecting multiple columns using .iloc
print("Selecting multiple columns using iloc =",df_index_col.iloc[:,[2,4]])

#Selecting a slice of columns using .iloc
print("Selecting a slice of columns using iloc =",df_index_col.iloc[:,2:7])

#Combined row and column selection using .iloc
print("Combined row and columns =",df_index_col.iloc[[2,4,5],3:5])

#Add a New Row to a Pandas DataFrame
# add a new row
df.loc[len(df.index)]=[112244,"for_sale",67777,9,10,0.99,15555,"Juana Diaz","Puerto Rico",999,777, None]
print(df)

#Remove Rows from a Pandas DataFrame
df.drop(1,axis=0,inplace=True)
df.drop(index=2,inplace=True)

#Remove Multiple Rows 
df.drop([4,5],axis=0,inplace=True)
print("After removing rows",df)

#Delete Columns from a pandas DataFrame
df.drop('zip_code',axis=1,inplace=True)
df.drop(columns='bath',inplace=True)

#Delete Multiple columns 
df.drop(['street','city'],axis=1,inplace=True)
print("After Deleting columns",df)

#Rename Labels in a DataFrame
# rename column 'Name' to 'First_Name'
df.rename(columns={'house_size':'house_area'},inplace=True)
#rename multiple columns 
df.rename(mapper={'status':'sale_or_not','brokered_ny':'Brokered_ID'},axis=1,inplace=True)
print(df)

#Example: Rename Row Labels
# rename row one index label
df.rename(index={0:8},inplace=True)
# remane multiple rows by index
df.rename(mapper={5:100,4:200},axis=0,inplace=True)
print(df)

#query() to Select Data
#The query() method in Pandas allows you to select data using a more SQL-like syntax.
# select the rows where the age is greater than 25
Selected_row=df.query('sale_or_not==\'sale\' or price >=1540000')
print(Selected_row.to_string())
print(len(Selected_row))

# sort DataFrame by price in ascending order
sorted_df=df.sort_values(by="price")
print(sorted_df.to_string(index=False))
print(sorted_df)

# sorted Dataframe by price and bed
df1=df.sort_values(by=['price','bed'])
print(df1.to_string(index=False))
print(df1)

#Pandas groupby
#In Pandas, the groupby operation lets us group data based on specific columns. This means we can divide a DataFrame into smaller groups based on the values in these columns.
# group the DataFrame by the location_id column and
# calculate the sum of price for each category

grouped=df.groupby('bed')['price'].sum()
print(grouped.to_string())
print('Grouped is here ',len(grouped))

# use dropna() to remove rows with any missing values
cleaned_data=df.dropna()
print("Cleaned Data :\n",cleaned_data)

# filling NaN values with '0'
df.fillna(0,inplace=True)
print("After filling NaN with 0 =",df)

# create a list named data
data = [2, 4, 6, 8]
array1=pd.array(data)
print(array1)

# creating a pandas.array of integers
int_array=pd.array([1,2,3,4,5],dtype="int")
print(int_array)

