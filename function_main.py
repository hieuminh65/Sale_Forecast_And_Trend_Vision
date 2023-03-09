import matplotlib.pyplot as plt

def flip_year(data):
    data.iloc[:, 2:] = data.iloc[:, 2:].values[:, ::-1]
    column_list = list(data.columns)
    for i in range(0, (len(column_list)-2)//2):
        temp = column_list[-1-i]
        column_list[-1-i]=column_list[i+2]
        column_list[i+2]=temp
    data.columns=column_list



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
        

def draw_scatter_graph(graph, code, kind):
    plt.scatter(x=graph['Year'], y=graph['Revenue'])
    plt.xlabel("Year")
    plt.ylabel("Revenue")
    plt.title(f"NAICS: {code}, {kind}")
    plt.show()
    plt.close()
    
