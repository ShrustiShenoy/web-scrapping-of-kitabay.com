# web-scrapping-of-kitabay.com

# Overview
This project contains a Python script that scrapes data from the Kitabay website, specifically the "Fictional Children" collection page (https://kitabay.com/collections/fictional-children). The script extracts text content from a specific <div> element on the page and saves it to a CSV file (kids.csv) using the BeautifulSoup library for HTML parsing and pandas for data handling.

The goal of this script is to demonstrate basic web scraping techniques, focusing on extracting text data from a webpage and storing it in a structured format.

# Prerequisites
To run this script, you need the following Python libraries installed:

requests: For making HTTP requests to fetch the webpage content.
beautifulsoup4: For parsing HTML content.
pandas: For creating a DataFrame and saving data to CSV.
