# checker.py

import requests

def check_username_availability(username, platform):
    # Sample username availability check logic (replace with actual checking logic)
    url = f"https://www.{platform}.com/{username}/"
    response = requests.get(url)
    available = response.status_code == 404
    return available
