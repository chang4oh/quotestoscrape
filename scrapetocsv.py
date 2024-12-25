# IMPORT LIBRARIES
from bs4 import BeautifulSoup
import requests
import csv

# OPEN A NEW CSV FILE WITH UTF-8 ENCODING
file = open('scraped_quotes.csv', 'w', encoding='utf-8-sig')
# CREATE A VARIABLE FOR WRITING TO THE CSV
writer = csv.writer(file)

# CREATE THE HEADER ROW OF THE CSV
writer.writerow(['Quote', 'Author'])

# REQUEST WEBPAGE AND SET THE CORRECT ENCODING
page_to_scrape = requests.get("http://quotes.toscrape.com")
page_to_scrape.encoding = 'utf-8'

# USE BEAUTIFULSOUP TO PARSE THE HTML
soup = BeautifulSoup(page_to_scrape.text, 'html.parser')

# FIND ALL THE QUOTES AND AUTHORS
quotes = soup.findAll('span', attrs={'class': 'text'})
authors = soup.findAll('small', attrs={'class': 'author'})

# LOOP THROUGH BOTH LISTS AND WRITE TO THE CSV
for quote, author in zip(quotes, authors):
    print(quote.text + " - " + author.text)
    writer.writerow([quote.text, author.text])

# CLOSE THE CSV FILE
file.close()
