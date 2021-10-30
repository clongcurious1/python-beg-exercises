import pandas as pd
import matplotlib.pyplot as plt

#display horizontal bar chart using pandas
data = pd.read_csv("csv.dogs2visualize.csv")
df = pd.DataFrame(data)

X = list(df.iloc[:, 0])
Y = list(df.iloc[:, 1])

plt.barh(X,Y, color = 'g')
#rotate y-labels and align horizontally with bar
plt.xticks(rotation=20, horizontalalignment="center")
plt.title("Shelter Dogs - Intake Reasons")
plt.xlabel('Number of Dogs')
plt.ylabel("Intake Reasons")
plt.show()