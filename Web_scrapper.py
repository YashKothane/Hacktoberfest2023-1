import requests
from bs4 import BeautifulSoup

# URL of the website to scrape
url = 'https://example.com/articles'

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the HTML elements containing the article titles and links
    articles = soup.find_all('div', class_='article')

    # Loop through the articles and extract the title and link
    for article in articles:
        title = article.find('h2').text
        link = article.find('a')['href']

        # Print the title and link
        print(f'Title: {title}')
        print(f'Link: {link}')
        print()

else:
    print(f'Failed to retrieve the page. Status code: {response.status_code}')
