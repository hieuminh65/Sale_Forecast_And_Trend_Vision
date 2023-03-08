import pandas as pd
import numpy as np
import csv
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
import function_main as fm
data= pd.read_csv('US_Retail_Sales_1992_2014.csv')


data['Kind of business'] = data['Kind of business'].astype('string')
data['NAICS Code'] = data['NAICS Code'].astype('string')
data.iloc[:, 2:] = data.iloc[:, 2:].astype('string')
data.iloc[: ,2:] = data.iloc[: ,2:].apply(lambda num: (num.str.replace(',','')))
data.iloc[:, 2:] = data.iloc[:, 2:].astype('float64')

fm.flip_year(data)
data['Kind of business']=data['Kind of business'].apply(lambda str: str.strip())
data.to_csv('Cleaned_Data.csv')

code_kind_df = pd.DataFrame(data.iloc[:, 0:2]) 
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
print(code_kind_df)


code_kind = fm.filter_input(code_kind_df)

data_draw = pd.DataFrame(data.iloc[0, 2:]).reset_index()
data_draw.columns=['Year','Revenue']
data_draw.iloc[:, 0] = data_draw.iloc[:, 0].astype("float64")


print(data_draw)


fm.draw_scatter_graph(data_draw, code_kind)

# year = (data_draw['Year']).values.reshape(-1,1)

year = np.array((data_draw['Year'])).reshape(-1,1)
revenue = np.array((data_draw['Revenue'])).reshape(-1,1)


line_fitter = LinearRegression()
line_fitter.fit(year, revenue)
revenue_predict = line_fitter.predict(year)
plt.plot(year, revenue_predict)
plt.plot(year, revenue, 'o')

predict_years = 0
while predict_years <= 2014:
    predict_years = int(input("You want to predict until: "))

m = line_fitter.coef_
b = line_fitter.intercept_ 
new_years = np.array(range(2015, predict_years+1)).reshape(-1,1)
revenue_predict = line_fitter.predict(new_years)
plt.plot(new_years, revenue_predict)
plt.show()
print(f"Accuracy score: {100*line_fitter.score(year,revenue):.2f}%")