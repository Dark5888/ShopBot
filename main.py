from selenium_stealth import stealth
import time 
import random
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

opt = webdriver.ChromeOptions()
opt.add_experimental_option("excludeSwitches", ["enable-automation"])
opt.add_argument("--profile-directory=Michael")
opt.add_experimental_option('useAutomationExtension', False)
opt.add_argument("disable-popup-blocking")
driver = webdriver.Chrome(options=opt)


# selenium stealth settings
stealth(driver, 
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win64",
        webgl_vendor="NVIDIA",
        renderer="NVIDIA GeForce GTX 1060",
        fix_hairline=True,
        )

driver.get("https://www.bestbuy.com/site/apple-airpods-pro-2-white/6447382.p?skuId=6447382")
time.sleep(1)

foundButton = False

# While loop looks for add to cart button and refreshes page until found
while not(foundButton):

    AddCartButtons = driver.find_elements(By.CLASS_NAME , "add-to-cart-button")

    foundButton = False

    for button in AddCartButtons:

        if("c-button-lg" in button.get_attribute("class") and ("c-button-disabled" not in button.get_attribute("class"))):
            button.click()
            foundButton = True
            break

    else:
        time.sleep(1)
        driver.refresh()


# waits for go to cart
goToCartButton = WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.LINK_TEXT, "Go to Cart")))
goToCartButton.click()


# waits for shipping option
shippingRadioButton = WebDriverWait(driver, 120).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "input[id*='fulfillment-shipping']"))
)
shippingRadioButton.click()


# randomizes time 
time.sleep(random.uniform(0, 1))

# checkout button slelector
checkoutButton = driver.find_element(By.CSS_SELECTOR, ".btn-primary.btn-lg")
checkoutButton.click()


# Continue as guest
guestButton = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "guest"))
)
guestButton.click()

# inputs first name and radomizes key inputs
firstName = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((By.NAME, "firstName"))
)
for i in "Michael":
    firstName.send_keys(i)
    time.sleep(random.uniform(0, 0.5))

# randomizes time and inputs last name
lastName = driver.find_element(By.NAME, "lastName")
for i in "Liu":
    lastName.send_keys(i)
    time.sleep(random.uniform(0, 0.5))
time.sleep(1)

# inputs address with random times inputs
street = driver.find_element(By.NAME, "street")
for i in "245 Blu":
    street.send_keys(i)
    time.sleep(random.uniform(0, 0.5))

# autocompletes address
auto = driver.find_element(By.CSS_SELECTOR, ".tb-input.autocomplete__input")
auto.send_keys(Keys.ARROW_DOWN)
time.sleep(random.uniform(0, 1))
auto.send_keys(Keys.ENTER)
time.sleep(random.uniform(0, 1))
time.sleep(1)

# clicks apply
apply = driver.find_element(By.CSS_SELECTOR, ".c-button.c-button-secondary.c-button-md.new-address-form__button")
apply.click()
time.sleep(2)

# inputs email  
emailAddress = driver.find_element(By.ID, "user.emailAddress")
emailAddress.send_keys("thebestbuybot@protonmail.com")

# inputs phone number
phone = driver.find_element(By.ID, "user.phone")
phone.send_keys("3048990040")

# clicks for payment method
payInfoButton = driver.find_element(By.CLASS_NAME, "button--continue")
payInfoButton.click()
time.sleep(4)

# enters card info
cardInfo = driver.find_element(By.ID, "number")
cardInfo.send_keys("4008179602448249")
time.sleep(3)

# enters expirationDate
expirationDate = driver.find_element(By.ID , "expirationDate")
expirationDate.send_keys("1223")

# Enters CVV 

cardCVV = driver.find_element(By.ID, "cvv")
cardCVV.send_keys("490")

# Completes payment
finishPay = WebDriverWait(driver, 120).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "btn-primary"))
)
finishPay.click()

# confirms 
time.sleep(60)

# Quit driver
driver.quit()
