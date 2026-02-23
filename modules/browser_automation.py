from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


def handle_browser(task):
    task_type = task.get("type")

    driver = webdriver.Chrome()

    if task_type == "google_search":
        query = task.get("query")

        driver.get("https://www.google.com")
        time.sleep(2)

        search_box = driver.find_element(By.NAME, "q")
        search_box.send_keys(query)
        search_box.send_keys(Keys.RETURN)

        time.sleep(3)

        driver.quit()
        return f"Searched Google for {query}"

    driver.quit()
    return "Browser task not supported."