# PROJECT DONE INDIVIDUALLY BY: JAMILE OBEID


#############################################################
### use this file to implement the web scrapper in part 1 ###
#############################################################

# IMPORTING LIBRARIES (BEAUTIFULSOUP, REQUESTS, SELENIUM, PANDAS)
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager

# USING SELENIUM TO OPEN URL & CLICK "Load More" 5 TIMES
def load_full_page():
    url = "https://www.rit.edu/dubai/directory"
    
    # USING WEBDRIVER_MANAGER TO AUTOMATICALLY MANAGE THE CHROMEDRIVER
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(url)
    wait = WebDriverWait(driver, 20)

    try:
        # HANDLING COOKIE BANNER
        try:
            cookie_consent = wait.until(EC.presence_of_element_located((By.ID, "cookie-consent")))
            dismiss_button = cookie_consent.find_element(By.TAG_NAME, "button")
            dismiss_button.click()
        except Exception as e:
            pass

        # CLICKING "LOAD MORE" 5 TIMES
        for click_number in range(5):
            try:
                load_more_button = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "see-more")))
                print(f"click number {click_number}")  # PRINTING THE CURRENT CLICK NUMBER

                driver.execute_script("arguments[0].scrollIntoView();", load_more_button)
                load_more_button.click()
                time.sleep(3)  # ALLOWING TIME FOR NEW CONTENT TO LOAD
            except Exception as e:
                break

        # WAITING FOR EMPLOYEE ARTICLES TO BE PRESENT
        wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "card person-directory")))

    except Exception as e:
        pass
    finally:
        page_source = driver.page_source
        driver.quit()
        return page_source

# USING REQUESTS TO FETCH HTML CODE
def fetch_html_using_requests():
    url = "https://www.rit.edu/dubai/directory"

    # ADDING A "User-Agent" TO MIMIC A BROWSER & AVOID BEING BLOCKED BY THE SERVER
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36"
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # RAISING AN EXCEPTION FOR BAD HTTP STATUS CODES
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching the URL using requests: {e}")
        return None

# USING BEAUTIFULSOUP TO EXTRACT INFORMATION
def scrape_employee_data(html_content):
    soup = BeautifulSoup(html_content, "html.parser")

    employees = []

    # THE CLASS ".card.person-directory" WAS OBTAINED BY GOING TO THE WEBSITE
    # (right-click -> inspect) TO FIND THE CLASS WITH EMPLOYEE INFO
    rows = soup.select(".card.person-directory")

    if not rows:
        print("No employee rows found. Please check the HTML structure.")
        return employees

    for row in rows:
        try:
            # IN THE BELOW LINES, THE CLASSES "pb-2" & "pb-2 directory-text-small" WERE OBTAINED 
            # BY GOING TO THE WEBSITE (right-click -> inspect)

            # EXTRACTING NAME
            name_tag = row.find("div", class_="pb-2").find("a")
            name = name_tag.get_text(strip=True) if name_tag else " "  # LEAVING A WHITE SPACE IF NAME IS EMPTY

            # EXTRACTING JOB TITLE
            title_tag = row.find("div", class_="pb-2 directory-text-small")
            title = title_tag.get_text(strip=True) if title_tag else " "  # LEAVING A WHITE SPACE IF TITLE IS EMPTY

            # EXTRACTING EMAIL
            email_tag = row.find("a", href=lambda x: x and x.startswith("mailto:"))
            email = email_tag.get("href").replace("mailto:", "") if email_tag else " "  # LEAVING A WHITE SPACE IF EMAIL IS EMPTY

            # APPENDING TO EMPLOYEE LIST
            employees.append({"Name": name, "Title": title, "Email": email})
        except Exception as e:
            pass

    return employees

# SAVING DATA TO CSV USING PANDAS
def save_to_csv(data, filename="employees.csv"):
    if not data:
        print("No data to save.")
        return
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)

# EXECUTING THE SCRIPT
if __name__ == "__main__":
    
    html_content_selenium = load_full_page()
    employee_data = scrape_employee_data(html_content_selenium) # SCRAPING EMPLOYEE DATA

    if employee_data:
        print(f"number of entries: {len(employee_data)}")
        save_to_csv(employee_data)
    else:
        print("No data to save.")
