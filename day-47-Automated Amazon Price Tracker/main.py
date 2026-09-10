import smtplib
from bs4 import BeautifulSoup
import requests

practice_url = "https://appbrewery.github.io/instant_pot/"
live_url = "https://www.amazon.com/dp/B01NBKTPTS?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"

response = requests.get(practice_url)

MY_EMAIL="spacexx.9999@gmail.com"
MY_PASSWORD="qtym dfqf dcyg qmlz"

soup = BeautifulSoup(response.content, "html.parser")
# print(soup.prettify())

price = soup.find(class_="a-offscreen").get_text()

# Remove the dollar sign using split
price_without_currency = price.split("$")[1]

# Convert to floating point number
price_as_float = float(price_without_currency)
print(price_as_float)

title = soup.find(id="productTitle").get_text()
title = " ".join(title.split( ))

print(title)

BUY_PRICE = 100

if price_as_float < BUY_PRICE:
    message = f"""Subject: Price Drop 🔥

{title}

Current price: {price}
"""


with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.starttls()
    connection.login(MY_EMAIL, MY_PASSWORD)
    connection.sendmail(from_addr=MY_EMAIL,
                        to_addrs=MY_EMAIL,
                        msg=message.encode("utf-8")

                        )