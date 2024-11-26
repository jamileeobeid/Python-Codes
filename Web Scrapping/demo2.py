import requests  # For fetching the webpage
from bs4 import BeautifulSoup  # For parsing HTML

# URL of the website containing the job listings
URL = "https://realpython.github.io/fake-jobs/"

# Fetch the HTML content of the page
response = requests.get(URL)
html_content = response.text

# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Find all <h2> tags with the class "title is-5"
job_titles = soup.find_all('h2', class_='title is-5')

# Print each job title
print("Job Titles:")
for title in job_titles:
    print(title.getText())
