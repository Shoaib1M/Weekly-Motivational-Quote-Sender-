import smtplib
import datetime as dt
import random

now=dt.datetime.now()
weekday=now.weekday()

if weekday==0:
    with open("quotes.txt") as quote_file:
        all_quotes=quote_file.readlines()
        random_choice=random.choice(all_quotes)
    my_email = "shoaibmunavary@gmail.com"
    pswd = "**********"  

    connection = smtplib.SMTP('smtp.gmail.com', 587, timeout=10)
    connection.starttls()
    connection.login(user=my_email, password=pswd)
    connection.sendmail(
        from_addr=my_email,
        to_addrs=my_email,
        msg=f"Subject:Monday Motivation\n\n{random_choice}"
    )
    connection.close()





