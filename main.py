# main.py

import os
import csv
import time
from datetime import datetime
from colorama import Fore, Style, init
from scraper import scrape_real_words, load_list_file, save_to_list_file

from web_scraper import find_wordlist_urls, get_wordlists  # Updated import statement
from checker import check_username_availability
from utilities import clear_console

# Initialize colorama for cross-platform ANSI color support
init()

# List of popular social media platforms and services
PLATFORMS = [
    "facebook",
    "twitter",
    "instagram",
    "snapchat",
    "tiktok",
    "youtube",
    "discord",
    "guilded",
    "pinterest",
    "tumblr",
    "reddit",
    "whatsapp",
    "kik",
    "wechat",
    "viber",
    "quora",
    "tinder",
    "grindr",
    "hinge",
    "bumble",
    "okcupid",
    "zoosk",
    "replit",
    "github",
]

LOG_FILE = "username_checker_log.csv"

def print_header():
    header_text = (
        Fore.CYAN + "▄▄▌ ▐ ▄▌▪  ▪  ·▄▄▄▄• ▄▄▄· ▄▄▄  ·▄▄▄▄  ·▄▄▄▄" + Style.RESET_ALL + "\n"
        + Fore.CYAN + "██· █▌▐███ ██ ▪▀·.█▌▐█ ▀█ ▀▄ █·██▪ ██ ██▪ ██" + Style.RESET_ALL + "\n"
        + Fore.CYAN + "██▪▐█▐▐▌▐█·▐█·▄█▀▀▀•▄█▀▀█ ▐▀▀▄ ▐█· ▐█▌▐█· ▐█▌" + Style.RESET_ALL + "\n"
        + Fore.CYAN + "▐█▌██▐█▌▐█▌▐█▌█▌▪▄█▀▐█ ▪▐▌▐█•█▌██. ██ ██. ██" + Style.RESET_ALL + "\n"
        + Fore.CYAN + " ▀▀▀▀ ▀▪▀▀▀▀▀▀·▀▀▀ • ▀  ▀ .▀  ▀▀▀▀▀▀• ▀▀▀▀▀•" + Style.RESET_ALL + "\n"
        + Fore.CYAN + "             Developed by WiIZARDD  " + Style.RESET_ALL + "\n"
        + Fore.CYAN + "       [Note: Spam leads to Rate Limits]" + Style.RESET_ALL + "\n"
    )

    # Get the width of the terminal/console
    terminal_width = os.get_terminal_size().columns

    # Calculate the left padding needed to center-align the text
    left_padding = (terminal_width - len(header_text.splitlines()[0])) // 2

    # Print the header with the calculated padding
    for line in header_text.splitlines():
        print(" " * left_padding + line)




def check_username_with_loading_bar(username_list):
    results = {}

    print("\nChecking usernames:")
    total_usernames = len(username_list)
    loading_bar_width = 40
    for i, username in enumerate(username_list):
        # Update loading bar
        progress = (i + 1) / total_usernames
        bar_length = int(loading_bar_width * progress)
        loading_bar = f"[{'#' * bar_length}{'.' * (loading_bar_width - bar_length)}] {int(progress * 100)}%"
        print(f"\r{loading_bar}", end="")

        # Simulate a loading message to make it more realistic
        loading_messages = [
            "Checking usernames...",
            "Hold on, we're almost there...",
            "Just a moment, checking...",
            "This won't take long...",
        ]
        print(f" {Fore.CYAN}{loading_messages[i % len(loading_messages)]}{Style.RESET_ALL}", end="")
        time.sleep(0.3)  # Adjust the sleep time as needed

        # Implement the code to check username availability on each platform
        platform_result = {"platform": platform, "available": False}
        for platform in PLATFORMS:
            available = check_username_availability(username, platform)
            if available:
                platform_result["available"] = True
                break

        results[username] = platform_result

    print("\nUsername availability checked.")
    return results

# Rest of your code remains the same
# ...

def main():
    os.system("clear" if os.name == "posix" else "cls")
    print_header()

    while True:
        # Get the width of the terminal/console
        terminal_width = os.get_terminal_size().columns

        # Define the border characters and the border width
        border_char = "="
        border_width = 40

        # Calculate the left padding needed for the border
        left_padding = (terminal_width - border_width) // 2

        # Create a centered border
        border = border_char * border_width
        centered_border = " " * left_padding + border

        # Create a centered menu
        centered_menu = [
            f" " * left_padding + f"{Fore.MAGENTA}Menu:{Style.RESET_ALL}",
            f" " * left_padding + f"{Fore.MAGENTA}1. Scrape Usernames and Save to List File{Style.RESET_ALL}",
            f" " * left_padding + f"{Fore.MAGENTA}2. Check Username Availability{Style.RESET_ALL}",
            f" " * left_padding + f"{Fore.MAGENTA}3. View Log{Style.RESET_ALL}",
            f" " * left_padding + f"{Fore.MAGENTA}4. Exit{Style.RESET_ALL}"
        ]

        # Print the centered border
        print(centered_border)

        # Print the centered menu
        for line in centered_menu:
            print(line)

        # Print the centered border
        print(centered_border)

        choice = input(f"{Fore.YELLOW}Enter your choice (1/2/3/4): {Style.RESET_ALL}")

        if choice == "1":
            num_usernames = int(input(f"{Fore.YELLOW}Enter the number of usernames to scrape: {Style.RESET_ALL}"))
            username_list = scrape_real_words(num_usernames)
            list_file_name = save_to_list_file(username_list)
            print(f"{Fore.GREEN}Usernames saved to {list_file_name}.{Style.RESET_ALL}")
        elif choice == "2":
            list_file_name = input(f"{Fore.YELLOW}Enter the name of the list file (without .txt extension): {Style.RESET_ALL}")
            username_list = load_list_file(f"{list_file_name}.txt")
            if not username_list:
                print(f"{Fore.RED}List file not found or empty.{Style.RESET_ALL}")
            else:
                results = check_username_with_loading_bar(username_list)
                save_to_log(username_list, results)
                display_results(results)
        elif choice == "3":
            if os.path.exists(LOG_FILE):
                with open(LOG_FILE, mode="r") as file:
                    print(file.read())
            else:
                print(f"{Fore.RED}Log file not found.{Style.RESET_ALL}")
        elif choice == "4":
            break
        else:
            print(f"{Fore.RED}Invalid choice. Please enter a valid option.{Style.RESET_ALL}")

if __name__ == "__main__":
    main()


