import requests
from bs4 import BeautifulSoup
import pandas as pd  # For creating and saving the DataFrame

# URL of the website containing the job listings
URL = "https://realpython.github.io/fake-jobs/"

# Fetch the HTML content of the page
response = requests.get(URL)
html_content = response.text

# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Lists to store job details
titles = []
companies = []
locations = []
dates = []

# Extract job title, company, location, and date
job_cards = soup.find_all('div', class_='card-content')  # Each job is inside a "card-content" div
for job in job_cards:
    # Extract job title
    title = job.find('h2', class_='title is-5').getText()
    titles.append(title)
    
    # Extract company
    company = job.find('h3', class_='subtitle is-6 company').getText()
    companies.append(company)
    
    # Extract location
    location = job.find('p', class_='location').getText()
    locations.append(location)
    
    # Extract date (if present, assuming it's inside a 'time' tag)
    date = job.find('time').getText() if job.find('time') else 'Unknown'
    dates.append(date)

# Create a DataFrame
jobs_df = pd.DataFrame({
    'Job Title': titles,
    'Company': companies,
    'Location': locations,
    'Date': dates
})

# Save the DataFrame to a CSV file
jobs_df.to_csv('job_listings.csv', index=False)

# Print the DataFrame (first 5 rows for preview)
print(jobs_df.head())
