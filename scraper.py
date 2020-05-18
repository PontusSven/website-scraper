import requests
from bs4 import BeautifulSoup
import smtplib

URL = 'https://www.dustinhome.se/product/5011144715/playstation-4-pro'
title = ""

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}

def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productName").get_text()
    price = soup.find("span", {"class": "price"}).get_text()

    converted_price = price.replace(" ","")
    converted_price = converted_price.replace("kr","")
    converted_price = int(converted_price)

    if(converted_price > 3000):
        send_mail()

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('pontussvensson92@gmail.com', 'vcocawfrajvyolfo')

    subject = "The price fell down on " + title
    body = 'Check the link :' + URL 

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'pontussvensson92@gmail.com',
        'pontussvensson92@gmail.com',
        msg
    )

    print("EMAIL HAS BEEN SENT!")

    server.quit()

check_price()