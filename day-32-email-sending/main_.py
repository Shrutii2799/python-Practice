import random
import smtplib
from datetime import datetime
import pandas

today=datetime.now()
today_tuple=(today.month,today.day)
# print(today_tuple)

MY_EMAIL="spacexx.9999@gmail.com"
MY_PASSWORD="qtym dfqf dcyg qmlz"


data= pandas.read_csv("birthdays.csv")

# new_dict={new_key:new_value for (index,data_row) in data.iterrows()}
birthdays_dict={(data_row["month"],data_row["day"]): data_row for (index,data_row)in data.iterrows()}

if today_tuple in birthdays_dict:
    birthday_person=birthdays_dict[today_tuple]
    file_path=f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        context=letter_file.read()
        context=context.replace("[NAME]",birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=MY_EMAIL,
                            msg=f"Happy Birthday!\n\n{context}"
                            )

