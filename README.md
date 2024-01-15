# N64 Button Tracker in Python

## Overview
This project is dedicated to tracking and visualizing button clicks in Super Smash Bros 64 matches. The primary goal is to gain insights into Human-Computer Interaction (HCI) within these matches and apply these insights to design an innovative, musically interactive performance piece. This interactive experience will take input from two players, creating a unique blend of gaming and musical expression.

## Features
- **Button Tracking:** Tracks every button press during Super Smash Bros 64 matches.
- **Data Visualization:** Utilizes `matplotlib` for plotting button click data.
- **Musical Interaction:** Designs an interactive performance piece based on player input.

## Technical Details
- **Language:** Written in Python.
- **Libraries:** Utilizes `pandas` for data handling and `matplotlib` for data visualization.
- **Input Handling:** Receives input data from a MaxMSP patch.
- **Data Storage:** Button inputs are written to a CSV file by the MaxMSP patch, which is then read and processed by the Python script.

## How It Works
1. **Data Collection:** A MaxMSP patch captures all button inputs during a Super Smash Bros 64 match and writes them to a CSV file.
2. **Data Processing:** The Python script reads the CSV file, processes the button input data using `pandas`.
3. **Visualization:** The script then visualizes the data using `matplotlib`, providing insights into player interaction patterns.
4. **Musical Interaction Design:** Based on the visualized data and insights, an interactive musical performance piece is designed, responsive to the input from two players.

![Example Output](https://media.licdn.com/dms/image/D4E22AQGgLyNnwg7ZNg/feedshare-shrink_1280/0/1699982323696?e=1707955200&v=beta&t=UkVSYg7usymHZsOHOLgXwPujvNS_JS5SykKrekL90ik "Example Output")
