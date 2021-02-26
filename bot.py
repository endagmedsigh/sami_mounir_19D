from selenium import webdriver
browser = webdriver.Chrome('/Users/Sami/Documents/chromedriver_win32')

browser.get("https://www.webhallen.com/se/product/331901-MSI-GeForce-RTX-3060-Ventus-2X-OC")

buyButton = False

while not buyButton:
    try:
        addToCartBtn = addButton = browser.find_element_by_class_name("btn-preorder")

        print("Button isnt ready yet.")

        time.sleep(1)
        browser.refresh()

    except:
        
        addToCartBtn = addButton = browser.find_element_by_class_name("btn-buy-green")

        print("Button was clicked.")
        addToCartBtn.click()
        buyButton = True
