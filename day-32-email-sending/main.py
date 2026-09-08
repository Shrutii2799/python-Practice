import smtplib
import datetime as dt
import random

MY_EMAIL="spacexx.9999@gmail.com"
MY_PASSWORD="qtym dfqf dcyg qmlz"

now=dt.datetime.now()
weekday= now.weekday()
if weekday==0:
    with open("quotes.txt") as quote_file:
        all_quotes= quote_file.readlines()
        quote=random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com",587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL,MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=MY_EMAIL,
                            msg=f"Subject:Monday Motivation\n\n{quote}"
                            )























# import smtplib
#
# my_email="spacexx.9999@gmail.com"
# password="qtym dfqf dcyg qmlz"
#
# with smtplib.SMTP("smtp.gmail.com",587) as connection:
#     connection.starttls()
#     connection.login(user=my_email,password=password)
#     connection.sendmail(from_addr=my_email,
#                         to_addrs=my_email,
#                         msg="hello\n\n this is the body of my email"
#                         )

#
# import datetime as dt
#
# now=dt.datetime.now()
# year=now.year
# # if year==2026:
# #     print("yeyy")
# month=now.month
# day_of_week=now.weekday()
# print(day_of_week)
#
# date_of_birth=dt.datetime(year=2005,month=11,day=27,hour=7)
# print(date_of_birth)