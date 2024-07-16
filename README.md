# Hex flower to simulate the weather for an Icewind Dale dnd 5e campaign.

## Description

This project was created to help me generate without effort the changing weather of the arctic region of Icewind Dale.
The code can be used to generate other type of environment, it would need the user to modify the content of the JSON and
change the image in /data named : Fleur_Climat_cleaned-coord.png

## Installation

Make sure you have the following installed on your system:

- [Python 3.x](https://www.python.org/downloads/)

### Steps to Install

1. Clone the project or download the files to your local machine.
2. Open a terminal and navigate to the project directory.
3. Create a virtual environment:
    ```bash
    python -m venv venv
    ```
4. Activate the virtual environment:
    - On Windows:
        ```bash
        cd venv/Scripts/activate.bat
        ```
    - On macOS/Linux:
        ```bash
        source venv/bin/activate
        ```
5. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## How to Run the DataExtractor

1. From the terminal, navigate to the project directory.
2. Activate the virtual environment:
    - On Windows:
        ```bash
        cd venv/Scripts/activate.bat
        ```
    - On macOS/Linux:
        ```bash
        source venv/bin/activate
        ```
3. Execute the script:
    ```bash
    python main.py
    ```