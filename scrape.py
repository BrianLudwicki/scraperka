import random
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

# Define the options for the headless browser
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")

# Define the user agents to rotate through
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; AS; rv:11.0) like Gecko",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0",
]

# Define the URL of the Amazon page to scrape
url_template = "https://www.amazon.com/dp/{}"

# Define the path to the chromedriver executable
chromedriver_path = "C:/Users/48783/Desktop/TOPTIMIZER/chromium.exe"

# Set up the webdriver with the headless options and user agent
service = Service(chromedriver_path)
service.start()
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.execute_cdp_cmd('Network.setUserAgentOverride', {'userAgent': random.choice(user_agents)})

# Define a function to print the product titles
def print_product_titles(product_titles):
    title_list = [title.text for title in product_titles]
    print(", ".join(title_list))

my_list = []

try:
    # Load the Amazon page for each ASIN and print the product title
    asins = ["B07Y45NJ83","B0002KHU3I"]
    for asin in asins:
        url = url_template.format(asin)
        driver.get(url)
        product_title = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "productTitle")))
        my_list.append([product_title.text])

except Exception as e:
    print(e)

finally:
    # Quit the webdriver and add a random sleep time before quitting
    time.sleep(random.uniform(1, 3))
    driver.quit()
    service.stop()

print(my_list)

#jestemkitowcem