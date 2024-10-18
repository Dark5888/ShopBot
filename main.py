from selenium_stealth import stealth
import time 
import random
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import tkinter as tk
from tkinter import messagebox 

#test code
''' https://www.bestbuy.com/site/apple-airpods-pro-2-white/6447382.p?skuId=6447382 product url'''

def start_bot(first_name, last_name, address, email, phone, card, expiration, cvv, product_url):

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
    
    driver.get(product_url) 
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
    for i in first_name:
        firstName.send_keys(i)
        time.sleep(random.uniform(0, 0.5))

    # randomizes time and inputs last name
    lastName = driver.find_element(By.NAME, "lastName")
    for i in last_name:
        lastName.send_keys(i)
        time.sleep(random.uniform(0, 0.5))
    time.sleep(1)

    # inputs address with random times inputs
    street = driver.find_element(By.NAME, "street")
    for i in address:
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
    emailAddress.send_keys(email)
    time.sleep(1)

    # inputs phone number
    phone_input_ele = driver.find_element(By.ID, "user.phone")
    phone_input_ele.send_keys(phone)

    # clicks for payment method
    payInfoButton = driver.find_element(By.CLASS_NAME, "button--continue")
    payInfoButton.click()
    time.sleep(4)

    # enters card info
    cardInfo = driver.find_element(By.ID, "number")
    cardInfo.send_keys(card)
    time.sleep(3)

    # enters expirationDate
    expirationDate = driver.find_element(By.ID , "expirationDate")
    expirationDate.send_keys(expiration)

    # Enters CVV 

    cardCVV = driver.find_element(By.ID, "cvv")
    cardCVV.send_keys(cvv)

    # Completes payment
    finishPay = WebDriverWait(driver, 120).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "btn-primary"))
    )
    finishPay.click()

    # confirms 
    time.sleep(60)

    # Quit driver
    driver.quit()

def create_interface():
    gui = tk.Tk()
    gui.title("Best Buy Purchase Boy")
    
    #Labels for user inputs
    tk.Label(gui, text="Product URL").grid(row=0)
    tk.Label(gui, text="First Name").grid(row=1)
    tk.Label(gui, text="Last Name").grid(row=2)
    tk.Label(gui, text="Address").grid(row=3)
    tk.Label(gui, text="Email").grid(row=4)
    tk.Label(gui, text="Phone").grid(row=5)
    tk.Label(gui, text="Card Number").grid(row=6)
    tk.Label(gui, text="Expiration Date (MMYY)").grid(row=7)
    tk.Label(gui, text="CVV").grid(row=8)

    product_url = tk.Entry(gui)
    first_name = tk.Entry(gui)
    last_name = tk.Entry(gui)
    address = tk.Entry(gui)
    email = tk.Entry(gui)
    phone = tk.Entry(gui)
    card_number = tk.Entry(gui)
    expiration_date = tk.Entry(gui)
    cvv = tk.Entry(gui)

    product_url.grid(row = 0 ,column=1)
    first_name.grid(row=1, column=1)
    last_name.grid(row=2,column=1)
    address.grid(row=3, column=1)
    email.grid(row=4, column=1)
    phone.grid(row=5, column=1)
    card_number.grid(row=6, column=1)
    expiration_date.grid(row=7, column=1)
    cvv.grid(row=8, column=1)

    def submit_button():
        #get input values

        product = product_url.get()
        fname = first_name.get()
        lname = last_name.get()
        addres = address.get()
        email_input = email.get()
        phone_number = phone.get()
        card = card_number.get()
        exp = expiration_date.get()
        cvv_input = cvv.get()

        start_bot(fname,lname,addres,email_input,phone_number,card,exp,cvv_input, product)
    
    submit_button = tk.Button(gui, text="Submit", command=submit_button)
    submit_button.grid(row=9, column = 1)

    gui.mainloop()


create_interface()


