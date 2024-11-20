import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for request errors

        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Example: Extract all headings from the webpage
        
        headings = soup.find_all(["p"])
        for heading in headings:
            print(heading.get_text())

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

# Example usage
scrape_website('https://judd.online')

