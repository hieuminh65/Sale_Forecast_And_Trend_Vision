# importing necessary libraries
import pandas as pd              # pandas: library used for data analysis
import numpy as np               # numpy: library used for numerical operations 
import csv                       # csv: library used for reading/writing CSV (Comma-Separated Values) files
import matplotlib.pyplot as plt  # matplotlib: library used for data visualization
import seaborn as sns            # seaborn: library used for statistical graphics plotting 
from sklearn.linear_model import LinearRegression  # library used for linear regression modeling
from sklearn.model_selection import train_test_split # splitting dataset into training and testing 


import function_main as fm       # local python script that contains custom functions


# reading csv file and loading data into a dataframe object
data = pd.read_csv('US_Retail_Sales_1992_2014.csv')


# converting the columns into the desired data types
data['Kind of business'] = data['Kind of business'].astype('string')
data['NAICS Code'] = data['NAICS Code'].astype('string')
data.iloc[:, 2:] = data.iloc[:, 2:].astype('string')

# replacing comma with blank string and converting the columns to float datatype
data.iloc[: ,2:] = data.iloc[: ,2:].apply(lambda num: (num.str.replace(',','')))
data.iloc[:, 2:] = data.iloc[:, 2:].astype('float64')

# calling function from another module
fm.flip_year(data)

# stripping any leading/trailing whitespaces in values of column 'Kind of business' 
data['Kind of business'] = data['Kind of business'].apply(lambda str: str.strip())

# saving the cleaned dataframe to a new CSV file
data.to_csv('Cleaned_Data.csv') 

# extracting the codes & kinds columns for a new dataframe object, printing it to console
code_kind_df = pd.DataFrame(data.iloc[:, 0:2]) 
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
print(code_kind_df)


# calling function to filter input based on user's selection, returning code and kind variables
code, kind = fm.filter_input(code_kind_df)
print(code, kind)


# preparing the desired data for drawing scatter chart by transposing the dataframe
data_draw = data[data['NAICS Code']== code].iloc[:, 2:].T.reset_index()
data_draw.columns=['Year','Revenue']

# converting the 'Year' column to float datatype
data_draw.iloc[:, 0] = data_draw.iloc[:, 0].astype("float64")

# printing the data into console
print(data_draw)

# using custom function to draw scatter graph
fm.draw_scatter_graph(data_draw, code, kind)


# performing linear regression model on the data
year = data_draw[['Year']]
revenue = data_draw[['Revenue']]
line_fitter = LinearRegression()

# splitting the data into train set and test set, model is trained on train set then tested on test set
year_train, year_test, revenue_train, revenue_test = train_test_split(year, revenue, test_size = 0.2, random_state=10)
line_fitter.fit(year_train, revenue_train)
revenue_predict = line_fitter.predict(year)


# plotting predicted revenue from trained model over years against actual revenue
plt.plot(year, revenue_predict)
plt.plot(year, revenue, 'o')

# getting the years till which user wants to predict sales and plotting them
predict_years = 0
while True:
    try:
        predict_years = int(input("You want to predict until: "))
        if predict_years > 2014:
            break
        else:
            print("Please enter a year after 2014.")
    except ValueError:
        print("Please enter a valid integer.")
new_years = np.array(range(2015, predict_years+1)).reshape(-1,1)
revenue_predict = line_fitter.predict(new_years)
plt.plot(new_years, revenue_predict)

# displaying the plot of predicted sales
plt.show()

# printing accuracy score of the model
print(f"Accuracy score: {100*line_fitter.score(year_test,revenue_test):.2f}%")
