import requests
from bs4 import BeautifulSoup

def scrape_news_headlines(url):
    # Send a GET request to the specified URL
    response = requests.get(url)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find all <h2> elements
        headlines = soup.find_all('h2')
        
        # Extract and print the text of each headline
        for headline in headlines:
            print(headline.get_text())
    else:
        print("Failed to retrieve webpage")

# URL of the website to scrape
url = 'https://www.bbc.com/news'

# Call the function to scrape news headlines from the specified URL
scrape_news_headlines(url)
