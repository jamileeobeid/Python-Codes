import requests  
from bs4 import BeautifulSoup 

# Step 1: Fetch the HTML content from the URL.
URL = "https://en.m.wikipedia.org/wiki/Dubai"  # Define the URL of the webpage.
response = requests.get(URL)  # Send a GET request to the URL.
html_content = response.text  # Get the text (HTML content) from the response.

# Step 2: Parse the fetched HTML content using BeautifulSoup.
soup = BeautifulSoup(html_content, 'html.parser')  # Parse the HTML with BeautifulSoup.

# Step 3: Print and analyze various parts of the HTML content.
print(soup)

# Find and print the first <title> tag and its text content.
print(soup.find('title'))  # Print the <title> tag.
print(soup.find('title').getText())  # Print the text inside the <title> tag.

# Find and print the first <h1> tag and its text content.
print(soup.find('h1'))  # Print the <h1> tag.
print(soup.find('h1').getText())  # Print the text inside the <h1> tag.
