# Importing the Matplotlib pyplot module 
import matplotlib.pyplot as plt

# Define a function that reverses the year columns in the dataframe.
def flip_year(data):
    data.iloc[:, 2:] = data.iloc[:, 2:].values[:, ::-1] # Selecting all rows and columns from index 2 onwards
                                                       # and assigning the reverse of these columns to them. 
    column_list = list(data.columns) # Create a list 'column_list' consisting of all columns of the dataframe.
    
    # Loop over half the length of the list and swap the elements of opposite ends. 
    for i in range(0, (len(column_list)-2)//2):
        temp = column_list[-1-i]
        column_list[-1-i]=column_list[i+2]
        column_list[i+2]=temp
        
    data.columns=column_list  # Assign the resulting modified column order to the original dataframe.

# Define a function to filter input from the user.
def filter_input(data):
    while True:
        input1 = str(input("Enter the NAICS Code, Kind of business, or the index to predict: "))
        
        if input1 in data['NAICS Code'].tolist():
            kind = data.loc[data['NAICS Code'] == input1, 'Kind of business'].iloc[0]
            return input1, kind
        
        elif input1 in data['Kind of business'].tolist():
            code = data.loc[data['Kind of business'] == input1, 'NAICS Code'].iloc[0]
            return code, input1
        
        if  int(input1) <= len(data):
            code = str(data.iloc[int(input1),0])
            kind = str(data.iloc[int(input1),1])
            return code, kind
        
        else: 
            print("This code or name is invalid.")

# Define a function to plot the graph/scatterplot.
def draw_scatter_graph(graph, code, kind):
    plt.scatter(x=graph['Year'], y=graph['Revenue'])  # Plotting the Year vs Revenue scatter plot.
    plt.xlabel("Year")   # Adding the x-axis label
    plt.ylabel("Revenue")  # Adding the y-axis label
    plt.title(f"NAICS: {code}, {kind}")  # Adding the title.
    plt.show()  # Display the graph
    plt.close()  # Clear the current figure.  
