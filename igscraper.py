from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sqlite3
from selenium.webdriver.chrome.options import Options

connection = sqlite3.connect("yourdatabase.sqlite3")
cur = connection.cursor()

options = Options()
options.add_argument("your chrome credentials folder")
driver = webdriver.Chrome(chrome_options=options)


driver.implicitly_wait(3)
driver.get("https://www.instagram.com/")


db_profiles = cur.execute("your db query to get profiles" )
db_profiles = list(db_profiles)

follow_counter = 0
keywords = ["list of keywords to search for in description"]

for profile in db_profiles:
    if follow_counter >= 30:
        break
    base_url = profile[0]
    driver.get(base_url)
    try:
        description = driver.find_element_by_class_name("-vDIg").text.lower()
        if not any( word in description for word in keywords):
            raise Exception("nope")
        first_pic = driver.find_element_by_class_name("v1Nh3")
        follow = driver.find_element_by_class_name("_5f5mN").click()
        first_pic.click()
        follow_counter += 1
        more_button = driver.find_elements_by_class_name("dCJp8")
    except:
        cur.execute("your query to delete the profile from database",(base_url,))
        connection.commit()
        continue

    if more_button:
        more_counter = 1
        more_button[0].click()
    while more_button and more_counter <= 4:
        more_button = driver.find_elements_by_class_name("dCJp8")
        if more_button and more_counter <= 4:
            more_counter += 1
            more_button[0].click()

    users = driver.find_elements_by_class_name("sqdOP")
    for link in users:
        try:
            href = link.get_attribute("href")
            user_profile = link.text
            if href and href != base_url:
                try:
                    cur.execute("INSERT INTO db_table VALUES (db_columns)",(arguments))
                    connection.commit()
                except:
                    pass
        except:
            pass

    update_query = "your updating a profile row query"
    data = (profile[0],)
    cur.execute(update_query,data)
    connection.commit()

    print(profile)
driver.close()
connection.close()