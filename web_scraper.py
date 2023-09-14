# web_scraper.py

import requests
import json
import random
from bs4 import BeautifulSoup

# List of GitHub repositories containing wordlists
GITHUB_REPOSITORIES = [
    "jeanphorn/wordlist",
    "SecLists/SecLists",
    "danielmiessler/SecLists",
    # Add more repositories as needed
]

def get_wordlist_from_github(repository):
    url = f"https://api.github.com/repos/{repository}/contents/"

    # Fetch the list of files in the repository
    response = requests.get(url)
    if response.status_code == 200:
        data = json.loads(response.text)
        files = [item for item in data if item["type"] == "file"]

        if files:
            # Choose a random file from the repository
            selected_file = random.choice(files)
            content_url = selected_file.get("download_url")

            # Fetch the content of the selected file
            response = requests.get(content_url)
            if response.status_code == 200:
                content = response.text
                # Split the content into lines
                wordlist = content.splitlines()
                return wordlist

    return []

def find_wordlist_urls():
    wordlists = []

    # Fetch wordlists from multiple GitHub repositories
    for repository in GITHUB_REPOSITORIES:
        wordlist = get_wordlist_from_github(repository)
        if wordlist:
            wordlists.extend(wordlist)

    return wordlists

def find_txt_links_on_page(url):
    # Find links to TXT files on a webpage
    response = requests.get(url)
    txt_links = []

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        # Modify this logic based on the structure of the webpage
        for link in soup.find_all('a', href=True):
            href = link['href']
            if href.endswith('.txt'):
                txt_links.append(href)

    return txt_links

def scrape_wordlist_from_url(url):
    # Scrape wordlist from the provided URL
    response = requests.get(url)
    if response.status_code == 200:
        return response.text.splitlines()
    else:
        return []

def get_wordlists():
    # This function retrieves wordlists from various sources, including GitHub repositories
    # and any other additional sources you might want to add.
    github_wordlists = find_wordlist_urls()

    # You can add more sources and logic here as needed

    return github_wordlists
