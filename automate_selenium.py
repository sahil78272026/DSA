from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Function to search for a location and write a review
def search_and_review(location_name, review_text):
    # Create a new instance of the Chrome driver
    # import pdb
    # pdb.set_trace()
    driver = webdriver.Chrome()

    # Navigate to Google Maps
    driver.get("https://www.google.com/maps")

    # Find the search input field and enter the location name
    search_box = driver.find_element(By.ID, "searchboxinput")
    time.sleep(2)
    search_box.send_keys(location_name)

    # Press Enter to perform the search
    search_box.send_keys(Keys.ENTER)

    # Wait for the search results to load
    time.sleep(1)

    # Click on the "Write a review" button
    write_review_button = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, "//span[contains(@class, 'GMtm7c') and text()='Write a review']"))
)

    write_review_button.click()

    # Wait for the review popup to load
    time.sleep(2)

    # Switch to the review iframe
    driver.switch_to.frame(driver.find_element("iframe[class^='widget']"))

    # Find the review textarea and enter the review text
    review_textarea = driver.find_element("textarea.review-textarea")
    review_textarea.send_keys(review_text)

    # Click on the "Post" button
    post_button = driver.find_element("//span[text()='Post']")
    post_button.click()

    # Wait for the review to be posted
    time.sleep(5)

    # Close the browser
    driver.quit()

# Example usage
search_and_review("Spinny", "Amazing place!")
