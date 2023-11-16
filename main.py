import sys
import pandas as pd
import matplotlib.pyplot as plt


if "jump" in sys.argv:
    button_mapping = {'A': 1, 'B': 2, 'S': 3, "An_L": 4, "An_R": 5, "An_U": 6, "An_D": 7, "R": 8, "L": 9, "Z": 10, "C_U": 6, "C_D": 6, "C_L": 6, "C_R": 6}
else:
    button_mapping = {'A': 1, 'B': 2, 'S': 3, "An_L": 4, "An_R": 5, "An_U": 6, "An_D": 7, "R": 8, "L": 9, "Z": 10, "C_U": 11, "C_D": 12, "C_L": 13, "C_R": 14}

reverse_button_mapping = {v: k for k, v in button_mapping.items()}



colors = {
    1: 'blue',
    2: 'green',
    3: 'red' ,   
    4: 'gray' ,   
    5: 'gray' ,   
    6: 'gray',    
    7: 'gray',    
    8: 'gray',    
    9: 'gray',    
    10: 'gray',   
    11: 'yellow',    
    12: 'yellow',    
    13: 'yellow',    
    14: 'yellow'    
}
shapes = {
    1: '.',
    2: '.',
    3: '.' ,   
    4: '<' ,   
    5: '>' ,   
    6: '^',    
    7: 'v',    
    8: 's',    
    9: 's',    
    10: 'd',
    11: '^',
    12: 'v',
    13: '<',
    14: '>'
}


def readCSV(csv_file, character, opponent):
 # Read the CSV file into a DataFrame
    df = pd.read_csv(csv_file, header=None)
    data = []

    # Iterate through the DataFrame and process each row
    for index, row in df.iterrows():
        try:
            # Parse the x value (time) and the button identifier
            x = float(row[1])
            button = row[2].strip().rstrip(";")
            if button in button_mapping:
                data.append((x, button_mapping[button]))
            else:
                print(f"Button {button} not in mapping. Skipping row {index}.")
        except Exception as e:
            print(f"Error processing row {index}: {e}")
            continue  # Skip rows that cause an error
    totals = {}
    if "reduce" in sys.argv:
        for row in data:
            if reverse_button_mapping[row[1]] in totals.keys():
                totals[reverse_button_mapping[row[1]]]+= 1
            else:
                totals[reverse_button_mapping[row[1]]] = 1
        print({k: v for k, v in sorted(totals.items(), key=lambda item: item[1])})

    # Plotting
    plt.figure(figsize=(10, 6))


    for x, button_id in data:
        plt.scatter(x, button_id, color=colors[button_id], marker=shapes[button_id])

    plt.xlabel("Time (s)")
    plt.ylabel("Button")
    plt.yticks(list(button_mapping.values()), [reverse_button_mapping[id] for id in button_mapping.values()])
    plt.title(f"{character} vs. {opponent}")

    # Setting the x-axis limits based on the data
    plt.xlim(min(df[1]) - 0.1, max(df[1]) + 0.1)
    plt.savefig(f"{csv_file[:-3]}png", dpi='figure', format=None, metadata=None,
            bbox_inches=None, pad_inches=0.1,
            facecolor='auto', edgecolor='auto',
            backend=None
        )


if __name__ == "__main__" and sys.argv[1] == "read":
    csv_location = sys.argv[2]
    character = sys.argv[3]
    opponent = sys.argv[4]
    readCSV(csv_location, character, opponent)

if "open" in sys.argv:
    plt.show()


# filepath read charater opponent [reduce, jump] 