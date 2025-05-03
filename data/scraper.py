import requests
from bs4 import BeautifulSoup

def scrape_gitlab_data():
    # URLs for GitLab's Handbook and Direction pages
    urls = [
        "https://about.gitlab.com/handbook/",
        "https://about.gitlab.com/direction/"
    ]

    data = []
    for url in urls:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        # Extract relevant text from the page
        text = soup.get_text()
        data.append(text)

    return data
