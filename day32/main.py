import smtplib
import datetime as dt
import random

# Global variables
file = "quotes_texts.txt"     # File to read. Each line of text will be randomly chosen and used as email body text.
weekday_to_check = 6    # Set day of week to check: 0 for Monday to 6 for Sunday
my_email = "your@email.com"     # Enter your email address here
my_password = "your_password"    # Enter your password here
receiver = "receiver@email.com"     # Enter recipient email address
smtp_server = "smtp.gmail.com"      # SMTP Server Address
smtp_port = 587                     # SMTP Server Port
subject_title = "Motivation Quote:"      # Change to your subject title.

# Use the datetime module to obtain the current day of the week
weekday = dt.datetime.now().weekday()

# Check if current day of the week is the is set as default.
if weekday == weekday_to_check:
    # Obtain the file.txt file and obtain a list of text
    with open(file, "r") as f:
        lines = f.readlines()
        random_line = random.choice(lines)

    # Send email with random text.
    with smtplib.SMTP(smtp_server, port=smtp_port) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=receiver,
            msg=f"Subject:{subject_title}:\n\n{random_line}"
        )
