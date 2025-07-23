from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

def scrape_statefarm_jobs():
    url = "https://jobs.statefarm.com/main/jobs"
    keywords = ['python', 'sql', 'tableau', 'data analyst', 'data scientist']

    options = Options()
    options.add_argument("--headless")  # Run in headless mode
    driver = webdriver.Chrome(options=options)
    
    try:
        driver.get(url)
        time.sleep(5)  # wait for page to load JS
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        results = []

        for job_card in soup.find_all('a', href=True):
            title = job_card.text.strip().lower()
            link = job_card['href']
            if any(kw in title for kw in keywords):
                full_link = f"https://jobs.statefarm.com{link}" if link.startswith("/") else link
                results.append(f"{title.title()}: {full_link}")

        if results:
            print("🔥 Matching Jobs Found:")
            for job in results:
                print(job)
        else:
            print("No relevant jobs found this run.")

    except Exception as e:
        print(f"❌ Scraping failed: {e}")
    finally:
        driver.quit()

