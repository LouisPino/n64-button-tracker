import sys
import pandas as pd
import matplotlib.pyplot as plt

button_mapping = {'A': 1, 'B': 2, 'S': 3, "An_L": 4, "An_R": 5, "An_U": 6, "An_D": 7, "R": 8, "L": 9, "Z": 10}
reverse_button_mapping = {v: k for k, v in button_mapping.items()}



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

csv_data = """
369, 1.492611, Z;
370, 1.592611, A;
371, 1.672611, R;
372, 1.672611, B;
373, 1.852611, Z;
374, 1.942611, S;
375, 2.022611, R;
376, 2.022611, A;
377, 2.152611, Z;
378, 2.292611, R;
379, 2.292611, A;
380, 2.312611, B;
381, 2.502611, A;
382, 2.522611, Z;
383, 2.522611, B;
384, 2.692611, A;
385, 2.732611, R;
386, 2.762611, B;
387, 2.982611, L;
388, 3.132611, A;
389, 3.292611, Z;
390, 3.512611, S;
391, 3.642611, L;
392, 3.832611, A;
393, 3.912611, R;
394, 3.942611, Z;
395, 4.102611, R;
396, 4.122611, B;
397, 4.212611, Z;
398, 4.452611, Z;
399, 4.552611, S;
400, 4.632611, A;
401, 4.732611, B;
402, 4.762611, R;
403, 4.812611, Z;
404, 5.032611, R;
405, 5.062611, B;
"""

def readCSV(csv_file, character, opponent):
    data = []
    for line in csv_data.strip().split(';'):
        parts = line.split(',')
        if len(parts) == 3:
            index, x, button = parts
            data.append((float(x.strip()), button_mapping[button.strip()]))

    # Plotting
    plt.figure(figsize=(10, 6))

# We need to create a reverse mapping from button numbers to button names
    reverse_button_mapping = {v: k for k, v in button_mapping.items()}

    for x, button_id in data:
        plt.scatter(x, button_id, color=colors[button_id], marker=shapes[button_id])

    plt.xlabel("X-axis (Time)")
    plt.ylabel("Button")

    # Create the Y-axis labels using the reverse mapping
    plt.yticks(list(button_mapping.values()), [reverse_button_mapping[id] for id in button_mapping.values()])

    plt.title(f"{character} vs. {opponent}")
    plt.show()
    

if __name__ == "__main__" and sys.argv[1] == "read":
    csv_location = sys.argv[2]
    character = sys.argv[3]
    opponent = sys.argv[4]
    readCSV(csv_location, character, opponent)
    
