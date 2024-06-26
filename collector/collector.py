# run: python3 test.py

# https://www.scrapingbee.com/blog/selenium-python/
# https://serpapi.com/blog/selenium-web-scraping-python/
# install Selenium
# download WebDriver

# -----------------------------------------------------------
# initialize WebDriver (ensure chromedriver is in your PATH)
from selenium import webdriver
from selenium.webdriver.common.by import By

# driver = webdriver.Chrome()

# headless mode:
# Add --headless=new in the add_argument method before launching the browser.
from selenium.webdriver.chrome.options import Options as ChromeOptions
options = ChromeOptions()
options.add_argument("--headless=new")
driver = webdriver.Chrome(options=options)

# -----------------------------------------------------------
# define the URL to be scraped
url = 'https://www.scrapethissite.com/pages/forms'

# -----------------------------------------------------------
# open the URL in the browser
driver.get(url)
# print the title of the page
print(driver.title)

# -----------------------------------------------------------
# fill q
q = driver.find_element("id", "q") # check for it in Chorome
# fill with keyword "kings"
q.send_keys("kings")
# submit
q.submit() 
# read current url
print(driver.current_url)

# -----------------------------------------------------------
# open main page again
driver.get(url)
# search form submission
q = driver.find_element(By.ID, "q")
q.send_keys("kings")
q.submit()
# print all table values
table = driver.find_element(By.CLASS_NAME, "table")
print(table.text)

# -----------------------------------------------------------
table = driver.find_element(By.CLASS_NAME, "table")
# screenshot specific area
table.screenshot("screenshot1.png")
# screenshot whole area
driver.save_screenshot('screenshot2.png')
# screenshot whole page
driver.execute_script("document.body.style.zoom='50%'")
driver.save_screenshot('screenshot3.png')

# -----------------------------------------------------------
# close the browser
driver.quit()
