# PyRoulette

PyRoulette is a Python-based GUI application that simulates a roulette wheel. It allows users to add elements, spin the roulette, and get the result in seconds.

## Description

The code in this repository creates a graphical interface using Tkinter to simulate a roulette wheel. Here's an overview of the different parts of the code:

### Functions

- **add_name():**
  - Adds entered elements to the roulette.
- **spin_roulette():**
  - Simulates the spinning of the roulette by randomly selecting an element.

### GUI Setup

- **Root Window Configuration:** 
  - Sets the window title, background color, and minimum window size.
- **Frame and Labels:** 
  - Creates labels for instructions, added elements, and result display.
- **Entry Field and Buttons:** 
  - Provides an entry field and functional buttons for user interaction.
- **Listbox Display:** 
  - Displays added elements in a listbox.
- **Clickable Link Label:** 
  - Configures a clickable link to the GitHub repository for PyRoulette.

### Callback Function

- **open_link(event):**
  - Opens the GitHub repository link in the default web browser when clicked.

## Features

- **Add Elements:** 
  - Users can input elements and add them to the roulette.
- **Spin Roulette:** 
  - Simulates the spinning effect and displays a randomly selected result.
- **GitHub Repository Link:** 
  - Provides easy access to the project's GitHub repository.

## Usage

1. Enter elements into the provided field.
2. Click "Add" to add elements to the roulette.
3. Click "Spin" to start the spinning animation.
4. Access the [GitHub repository](https://www.github.com/ngdplnk/pyroulette) for more information and updates.

## Installation

1. Ensure Python is installed.
2. Clone this repository.
3. Run the application using Python.

## Code Explanation

The code is organized into functions that handle adding elements, spinning the roulette, and GUI setup. It uses Tkinter for creating the graphical interface, allowing user interaction with buttons, entry fields, and labels.

### Description of the Code:
1. Importing Libraries:
  - tkinter: Imported as tk for creating the graphical user interface (GUI).
  - webbrowser: Imported to enable opening links in the default web browser.
  - random: Imported for generating random numbers.
  - time: Imported to introduce delays in the spinning animation.
2. Functions:
  - add_name() Function: Adds the text entered into the entry field to the listbox as a new item when the "Add" button is clicked.
  - spin_roulette() Function: Simulates spinning the roulette by randomly selecting an item from the list of added elements for a specified number of spins when the "Spin" button is clicked. Displays the spinning effect by rapidly updating the displayed text. Finally, shows the randomly selected item as the result.
3. GUI Setup:
  - Root Window Configuration: Sets the window title, background color, and minimum window size.
  - Error Handling for Icon (Optional): Attempts to load an icon for the window; prints an error message if the icon is not found.
  - Frame and Labels: Creates a frame to organize elements within the window. Generates labels for the title, input instructions, added elements, and result display.
  - Entry Field and Buttons: Provides an entry field for user input. Includes functional buttons ("Add" and "Spin") for user interaction.
  - Listbox Display: Displays added elements in a listbox with a dark-themed background and white text.
  - Clickable Link Label: Sets up a label displaying a clickable link to the GitHub repository for the pyroulette project. Configures the label to open the GitHub repository when clicked.
4. Callback Function for Clickable Link:
  - Defines a callback function to handle opening the GitHub link when the label is clicked.
5. Root Window Loop:
  - Enters the main event loop to start the GUI application, waiting for user interactions.

Feel free to explore the code and modify it according to your preferences.

For any issues or suggestions, please open an issue in the GitHub repository.

### © 2024 - NGDPL Nk
Icon: <a href="https://www.flaticon.es/iconos-gratis/ruleta" title="ruleta iconos">"Ruleta iconos" created by Freepik - Flaticon</a>
