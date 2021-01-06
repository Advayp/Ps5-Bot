import smtplib
import os
from time import sleep
from selenium import webdriver

app_pass = os.environ.get("APP")
email = 'advaypatil27@gmail.com'


PATH = 'C:\\New folder\\chromedriver.exe'
driver = webdriver.Chrome(PATH)

ps5 = "https://www.bestbuy.com/site/sony-playstation-5-console/6426149.p?skuId=6426149"
ps4 = "https://www.bestbuy.com/site/sony-playstation-4-1tb-console-black/5850905.p?skuId=5850905"

driver.get(ps5)

a = 0

while True:
    try:
        link = driver.find_element_by_class_name("add-to-cart-button")

        if link.is_enabled():
            break
        else:
            a += 1
            print(a)
            sleep(300)
    except:
        a += 1
        print(a)
        sleep(300)

    driver.refresh()

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login(email, app_pass)

    subject = 'PS5'
    body = 'Go buy it!: https://www.bestbuy.com/site/sony-playstation-5-console/6426149.p?skuId=6426149'

    msg = f'Subject: {subject}\n\n{body}'

    smtp.sendmail(email, email, msg=msg)


sleep(10)
driver.quit()
