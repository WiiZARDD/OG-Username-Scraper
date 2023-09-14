# utilities.py

# Define the clear_console function to clear the console screen
def clear_console():
    if os.name == "posix":
        os.system("clear")
    else:
        os.system("cls")
