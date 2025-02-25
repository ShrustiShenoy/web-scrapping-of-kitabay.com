
import requests

from bs4 import BeautifulSoup

import csv

web = 'https://kitabay.com/collections/fictional-children'

requests = requests.get(web)

page_cont = requests.text

web_info = BeautifulSoup(page_cont, 'html.parser')

condition=[]

row = 'svg_loader_container'
div = web_info.find('div', id = row)


import requests

from bs4 import BeautifulSoup

import csv

web = 'https://kitabay.com/collections/fictional-children'

requests = requests.get(web)

page_cont = requests.text

web_info = BeautifulSoup(page_cont, 'html.parser')

condition=[]

row = 'collection_content'
div = web_info.find('div', id='row')  # Replace with the actual class name

if div:
    # Process content inside the div
    items = div.find_all('div')  # Adjust this based on the HTML structure
    for item in items:
        text = item.text.strip()  # Extract and clean text content
        condition.append(text)
        print(text)
else:
    print(f"No div found with id {row}")

    import pandas as pd

 
# Create a DataFrame
data = pd.DataFrame({'CONDITION': condition})

# Save to CSV
data.to_csv('kids.csv', index=False)
print("Data saved to kids.csv")





 