import smtplib
from datetime import datetime
import random
import pandas as pd

your_name = "REDRUM"                 # Change to your name
file = "birthdays.csv"               # File link to birthdays.csv
my_email = "your@email.com"          # Enter your email address here
my_password = "your_password"        # Enter your password here
smtp_server = "smtp.gmail.com"       # SMTP Server Address
smtp_port = 587

# Current date in tuple (month, day)
today = (datetime.now().month, datetime.now().day)

# Open CSV with pandas as pd and get month and day to compare with current date
df = pd.read_csv(file)
birthdays = {(data_row.month,data_row.day): data_row for (index, data_row) in df.iterrows()}

# Check if today have any birthdays. Choose random template if True.
if today in birthdays:
    receiver = birthdays[today]
    template = f"letter_templates/letter_{random.randint(1,3)}.txt"
    # Replace [NAME] from random chosen letter template
    with open(template) as letter:
        contents = letter.read()
        letter = contents.replace("[NAME]", receiver["name"])
        subject_title = f"Happy Birthday {receiver['name']}"      # Change to your subject title.
        with smtplib.SMTP(smtp_server, port=smtp_port) as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=receiver["email"],
                msg=f"Subject:{subject_title}!\n\n{letter}"
            )
