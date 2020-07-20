from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sqlite3
from selenium.webdriver.chrome.options import Options

connection = sqlite3.connect('database.sqlite3')
cur = connection.cursor()

options = Options()
options.add_argument("your chrome credentials folder")
driver = webdriver.Chrome(chrome_options=options)


driver.implicitly_wait(3)
driver.get("https://www.instagram.com/")


db_profiles = cur.execute("your db query to get profiles to unfollow")
db_profiles = list(db_profiles)

keywords = ["list of keywords to search for in description"]

for profile in db_profiles:
    base_url = profile[0]
    driver.get(base_url)
    try:
        description = driver.find_element_by_class_name("-vDIg").text.lower()
        if not any( word in description for word in keywords):
            unfollow = driver.find_element_by_class_name("glyphsSpriteFriend_Follow").click()
            unfolloo_second = driver.find_element_by_class_name("aOOlW").click()
            cur.execute("your delete query",(base_url,))
            connection.commit()
    except:
        pass
connection.close()
driver.close()
