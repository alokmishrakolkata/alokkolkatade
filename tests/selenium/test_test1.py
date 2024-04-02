from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

import time

def wait_for_page_load(driver):
    # Return True or False based on your custom condition
    return driver.find_element(By.XPATH, "//span[@title='Setup']")


def test_sample1():
    # Set up Chrome options
    chrome_options = Options()

    chrome_driver_path = "/Users/alokmishra/Documents/Alok_Data/Learning/SeleniumDriver/chromedriver_mac_arm64/chromedriver"

    # Initialize Chrome WebDriver with the correct path to chromedriver executable
    # Set up service
    service = Service(executable_path=chrome_driver_path)

    # Initialize the driver with the service and options
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # Set page load timeouts
    driver.set_page_load_timeout(50)

    #driver.get("https://qavbox.github.io/demo")
    driver.get("https://login.salesforce.com")

    # Wait up to 30 seconds for the page title to contain "QAVBOX"
    #assert "QAVBOX" in driver.title
    assert "Login | Salesforce" in driver.title

    # Click on the 'Signup Form' link
    #driver.find_element(By.LINK_TEXT, "SignUp Form").click()

    #login in to salesforce########
    username_field = driver.find_element(By.ID, "username")
    username_field.send_keys("alokmishrakolkatasc@gmail.com")

    # Enter password
    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys("Alok@1234")

    # Click the login button
    login_button = driver.find_element(By.ID, "Login")
    login_button.click()
    time.sleep(15)
    wait_for_page_load(driver)

    #click the waffle icon
    # Wait for the home page to load by checking for the presence of the waffle icon (App Launcher)
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, "slds-icon-waffle")))

    # Click on the waffle icon (App Launcher)
    driver.find_element(By.CLASS_NAME, "slds-icon-waffle").click()

    # Wait for the App Launcher menu to be visible
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, "appLauncher")))

    # Click on the "Service" option
    # Note: This might require adjusting the selector based on your Salesforce setup
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//p[text()='Service']"))).click()
    time.sleep(10)
    WebDriverWait(driver, 20).until(lambda d: d.execute_script('return document.readyState') == 'complete')
    #click on cases
    # Wait for the Service page to load and for the "Cases" tab to become clickable
    #WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//a[@title='Cases']"))).click()
    #case_link = WebDriverWait(driver, 20).until(
    #    EC.presence_of_element_located((By.XPATH, "//span[@class='slds-truncate'][normalize-space()='Cases']"))
    #)
    #case_link.click()
    driver.execute_script('document.evaluate("//a[@title=\'Cases\']", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue.click();')

    #click on new case button
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@title='New']"))).click()

    #click on billable option
    WebDriverWait(driver, 10).until((EC.element_to_be_clickable((By.XPATH, "//label[@for='012900000019Yl1AAE']//span[@class='slds-radio--faux']")))).click()

    #click on next
    WebDriverWait(driver, 10).until((EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Next']")))).click()
    time.sleep(5)
    WebDriverWait(driver, 10).until(
        lambda d: d.execute_script('return document.readyState') == 'complete'
    )
    #find the subject field
    wait = WebDriverWait(driver, 10)
    modal_element = WebDriverWait(driver, 20).until(
    EC.visibility_of_element_located((By.XPATH, "//div[@data-target-selection-name='sfdc:RecordField.Case.Subject']//input[@type='text']"))
)

    # Now that the modal is open and the element is visible, interact with it
    modal_element.send_keys("Test Created By Selenium")

    # find the Description field
    #desc_field = driver.find_element(By.XPATH, 'driver.findElement(By.xpath("/html[1]/body[1]/div[4]/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/records-modal-lwc-detail-panel-wrapper[1]/records-record-layout-event-broker[1]/slot[1]/records-lwc-detail-panel[1]/records-base-record-form[1]/div[1]/div[2]/div[1]/div[1]/records-lwc-record-layout[1]/forcegenerated-detailpanel_case___012900000019yl1aae___full___create___recordlayout2[1]/records-record-layout-block[1]/slot[1]/records-record-layout-section[4]/div[1]/div[1]/div[1]/slot[1]/records-record-layout-row[2]/slot[1]/records-record-layout-item[1]/div[1]/span[1]/slot[1]/records-record-layout-text-area[1]/lightning-textarea[1]/div[1]/textarea[1]"))')
    #desc_field.send_keys('Test Created By Selenium')

    # click on next
    WebDriverWait(driver, 10).until(
        (EC.element_to_be_clickable((By.XPATH, "//button[@name='SaveEdit']")))).click()

    # Save screenshot
    driver.save_screenshot("test.png")

    # Wait for 3 seconds (just for demonstration purposes)
    time.sleep(3)

    driver.quit()