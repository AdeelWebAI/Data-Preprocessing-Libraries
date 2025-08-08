import pandas as pd



#  a. Series (1D Data)


# data = [1,2,3,4,5,6]

# series = pd.Series(data,index=['a','b','c','d','e','f'])
# print(series)  
# print(series['d'])     # 4
# print(series[3])      # 4


# b. DataFrame (2D Data)

# data = {
#     "names":["adeel","bahawal","jamshed"],
#     "marks":[56,76,87],
#     "salary":[98000,98989,87668,]
# }

# df = pd.DataFrame(data)
# print(df)

# Loading Data:

# df.to_json("new.json", index=False)
# df = pd.read_csv("COVID.csv")
# df.to_excel("covid.xlsx")
# df = pd.read_excel("LYALLPUR.xlsx")
# df.to_excel("E_post.xlsx")
# print(df) 


# 3. DataFrame Operations

# a. Basic Inspection

df = pd.read_excel("E_post.xlsx")
# df.head()       # First 5 rows
# df.tail()       # Last 5 rows
# df.info()       # Summary of the DataFrame
# df.describe()   # Statistical summary
# df.shape        # Rows and columns count
# df.columns      # List of column names
# df.dtypes       # Data types of columns

# b. Selecting Data

# Column Selection

# print(df["Name"])
# print(df[["Name","Username"]])

# Row Selection
# print(df.loc[9]) # selecting rows by location (index number)
# print(df.loc[df["Random"] < 5])  # selecting and filtering rows

# 4. Data Manipulation

# a. Adding and Removing Columns

# df["Bonus"] = df["Random"] * 10  # adding columns
# df.drop("Bonus",axis=1, inplace=True) # removing columns
# print(df) 
# df2=df.drop("Bonus",axis=1) # removing columns
# print(df2) 


# b. Adding and Removing Rows

# df.loc[3] = ["Adeel",40,40,23,234,34,34,23,34] # Adding rows
# df.drop(3, axis=0, inplace=True) 
# print(df)


# 5. Handling Missing Data

# a. Checking for Missing Data
# print(df.isnull().sum()) # Count of missing values in each column

# df.fillna(0,inplace=True) # Replace NaN with 0
# df.fillna(df.mean(), inplace=True) #Replace NaN with column mean

# df.dropna(inplace=True) # drop rows with NaN Values
# df.dropna(axis=1,inplace=True) # drop columns with NaN Values

# print(df.isnull().sum()) # Count of missing values in each column

# 6. Grouping and Aggregation

# a. Grouping Data

print(df.groupby("Random"))    # Group by Random column 

# print(df.groupby("Random")["Random2"].sum())