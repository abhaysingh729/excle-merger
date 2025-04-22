import requests
from bs4 import BeautifulSoup
import csv

url = "http://quotes.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

quotes_data = []

quotes = soup.find_all('div', class_='quote')

for quote in quotes:
    text = quote.find('span', class_='text').get_text(strip=True)
    author = quote.find('small', class_='author').get_text(strip=True)
    tags = [tag.get_text(strip=True) for tag in quote.find_all('a', class_='tag')]
    quotes_data.append([text, author, ', '.join(tags)])

# Save to CSV
with open('quotes.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['Quote', 'Author', 'Tags'])
    writer.writerows(quotes_data)

print("Quotes saved to quotes.csv")
