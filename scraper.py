# scraper.py

import os
import random
import requests
from bs4 import BeautifulSoup
import web_scraper 

def scrape_real_words(num_words):
    wordlists = get_wordlists()

    if wordlists:
        return random.sample(wordlists, min(num_words, len(wordlists)))
    else:
        return []

def load_list_file(list_file_name):
    if os.path.exists(list_file_name):
        with open(list_file_name, "r") as file:
            username_list = file.read().splitlines()
        return username_list
    else:
        return []

def save_to_list_file(username_list):
    list_file_name = f"list-{len(username_list)}.txt"
    with open(list_file_name, "w") as file:
        file.write("\n".join(username_list))

    return list_file_name

def delete_list_file(list_file_name):
    if os.path.exists(list_file_name):
        os.remove(list_file_name)

def get_wordlists():
    # Fetch wordlists from GitHub repositories and other sources
    github_wordlists = find_wordlist_urls()
    
    # You can add more sources or custom logic here if needed
    
    return github_wordlists

def find_wordlist_urls():
    # Use the web_scraper to find wordlist URLs
    return web_scraper.find_wordlist_urls()  # Import the web_scraper module


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

def save_to_list_file(username_list):
    list_file_name = f"list-{len(username_list)}.txt"
    with open(list_file_name, "w") as file:
        file.write("\n".join(username_list))

    return list_file_name

def load_list_file(list_file_name):
    if os.path.exists(list_file_name):
        with open(list_file_name, "r") as file:
            username_list = file.read().splitlines()
        return username_list
    else:
        return []

def delete_list_file(list_file_name):
    if os.path.exists(list_file_name):
        os.remove(list_file_name)
