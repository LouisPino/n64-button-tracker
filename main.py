import usb.core
import usb.util
import sys
import pandas as pd
import matplotlib.pyplot as plt

button_mapping = {'A': 1, 'B': 2, 'Start': 3, "An_L": 4, "An_R": 5, "An_U": 6, "An_D": 7, "R": 8, "L": 9, "Z": 10}


colors = {
    1: 'blue',  # A button is blue
    2: 'green', # B button is green
    3: 'red' ,   # Start button is red
    4: 'gray' ,   # Start button is red
    5: 'gray' ,   # Start button is red
    6: 'gray',    # Start button is red
    7: 'gray',    # Start button is red
    8: 'gray',    # Start button is red
    9: 'gray',    # Start button is red
    10: 'gray'    # Start button is red
}
shapes = {
    1: '.',  # A button is blue
    2: '.', # B button is green
    3: '.' ,   # Start button is red
    4: '<' ,   # Start button is red
    5: '>' ,   # Start button is red
    6: '^',    # Start button is red
    7: 'v',    # Start button is red
    8: 's',    # Start button is red
    9: 's',    # Start button is red
    10: 'd'    # Start button is red
}



character = "Samus"
opponent = "Pikachu"

def readCSV(path):
    data = pd.read_csv(path, header=None, names=['Value', 'Category'])

    # Create a scatter plot
    plt.figure(figsize=(10, 6))

    # Iterate over each unique category to plot them with different colors
    for category in data['Category'].unique():
        subset = data[data['Category'] == category]
        plt.scatter(subset.index, subset['Value'], label=category)

    # Add labels and title
    plt.xlabel('Index')
    plt.ylabel('Value')
    plt.title('Scatter Plot by Category')
    plt.legend()

    # Show the plot
    plt.show()
    

if __name__ == "__main__" and sys.argv[1] == "read":
    csv_location = sys.argv[2]
    readCSV(csv_location)