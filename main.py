import matplotlib.pyplot as plt
import pandas as pd

dataframe = pd.read_csv("company_sales_data.csv")

class Column:
    def __init__(self, label, marker = "o", linewidth=3):
        self.data = dataframe[label].tolist()
        self.label = label
        self.marker = marker
        self.linewidth = 3

data = []
for title in list(dataframe.columns):
    if "total" not in title:
        data.append(Column(title))
        if "month" in title:
            monthList = data[-1].data

def graph_time(data):
    for column in data:
        if "month" in column.label:
            pass
        else:
            try:
                plt.plot(monthList,
                        column.data,
                        label = column.label,
                        marker = column.marker,
                        linewidth = column.linewidth)

            except:
                print("No month list available")
                break

    plt.xlabel('Month Number')
    plt.ylabel('Sales units in number')
    plt.legend(loc='upper left')
    plt.xticks(monthList)
    plt.title('Sales data')
    plt.show()

if __name__ == '__main__':
    graph_time(data)