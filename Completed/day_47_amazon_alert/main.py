import requests
import smtplib
from bs4 import BeautifulSoup
import lxml
import lxml.html.soupparser

your_name = "My name"  # Change to your name
my_email = "my_email@gmail.com"  # Enter your email address here
my_password = "mypassword"  # Enter your password here
smtp_server = "smtp.gmail.com"  # SMTP Server Address
smtp_port = 587

url = "https://www.amazon.co.uk/Apple-iPhone-13-Pro-512GB/dp/B09G954JZY/ref=sr_1_10?crid=31FU7T904E789&keywords=iphone+14+pro+max&qid=1670287706&sprefix=iphone%2Caps%2C101&sr=8-10"
header = {
    "Accept-Language": "lt-LT,lt;q=0.9,en-US;q=0.8,en;q=0.7,ru;q=0.6,pl;q=0.5",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=header)

soup = BeautifulSoup(response.content, "lxml")
# print(soup.prettify())

price = soup.find(name="span", class_="a-offscreen").text
print(price)

# # Format price
bare_price = price.split("£")[1].split(",")
current_price = float(f"{bare_price[0]}{bare_price[1]}")
#
price_want = 1250.0
# print(current_price)
message = f" iPhone 13 Pro Max Price went down from £{price_want} to: {current_price}"
if float(current_price) < float(price_want):
    print(f" iPhone 13 Pro Max Price went down from £{price_want} to: {current_price}")
    with smtplib.SMTP(smtp_server, port=smtp_port) as connection:
        connection.starttls()
        connection.login(my_email, my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="myemail@gmail.com",
            msg=f"Subject:{your_name}! Price DOWN!\n\n{message}\n £{current_price}".encode('utf-8')
        )
