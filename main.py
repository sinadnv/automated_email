import pandas as pd
from datetime import date
import smtplib


def csvread(date_csv_file, names_csv_file):
    dates = pd.read_csv(date_csv_file)
    dates_dict = dict(zip(dates.Date, dates.SessionOrdinal))
    names = pd.read_csv(names_csv_file)
    email_address = names['Email Address']
    list_email_address = email_address.values.tolist()
    return dates_dict, list_email_address


def check_date(day, list_class_dates):
    if day in list_class_dates:
        return True
    else:
        return False


def send_email(sender, password, recipients, message):
    smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtp_server.ehlo()
    smtp_server.login(sender, password)
    smtp_server.sendmail(sender, recipients, message)
    smtp_server.close()


# Reading Dates and Corresponding Session Number
# Created a dictionary to easily correlate between the date and session number
# Zoom Meeting Link To be Updated
zoom_link = 'Zoom Link Goes Here'

# read .csv files
date_csv_file = ''
names_csv_file = ''

# Gmail Credentials
gmail_user_name = 'Youremailgoeshere'
gmail_password = 'Yourpasswordgoeshere'

dates_dict, list_email_address = csvread(date_csv_file, names_csv_file)
class_dates = [class_date for class_date in dates_dict]

recipients = ['Recipient']
# recipients = ['Recipient']

if check_date(str(date.today()), class_dates):
    message = 'Subject: Python Class Reminder \n\n' \
              'Dear Python enthusiasts, \n' \
              'This is a friendly reminder that the {number} session of the Python Course takes place today at 6PM.\n' \
              'Below is a link to the class:\n' \
              '{link} \n\n' \
              'Regards, \n' \
              'Sina Daneshvar \n' \
        .format(number=dates_dict[str(date.today())], link=zoom_link)
    send_email(gmail_user_name,gmail_password,recipients,message)
    for recipient in recipients:
        print('Email Sent to {receiver}'.format(receiver = recipient))

