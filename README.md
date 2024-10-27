# DigitalClock
A simple digital clock application built using Python's Tkinter library. This program displays the current time and date, updating every second.

## Features

- Displays the current time in HH:MM:SS format.
- Shows the current date in a readable format (e.g., "Friday, October 26, 2024").
- Simple and clean user interface with customizable styles.

## Requirements

- Python 3.x
- Tkinter (comes pre-installed with most Python distributions)

## How to Run

1. Make sure you have Python installed on your system.
2. Copy the provided code into a Python file (e.g., `digital_clock.py`).
3. Run the script using the command:
   ```bash
   python digital_clock.py
A window will appear displaying the current time and date.
Code Explanation
Importing Modules: The code imports necessary modules from the Tkinter library and the strftime function from the time module.

Creating the Main Window: The Tkinter window is initialized with a title "Digital Computer Clock".

Time Function:

The time function retrieves the current time and date, formats them, and updates the label every second using the after method.
Label Widget: A label widget is created to display the time and date with specified font size and colors.

Main Loop: The application enters the main loop, waiting for user interaction.

Customization
Feel free to customize the following aspects of the code:

Font Size and Style: Change the font settings in the Label widget to adjust appearance.
Background and Text Colors: Modify the bg and fg parameters in the Label widget to suit your preferences.
