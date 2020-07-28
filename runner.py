import os
import csv
import argparse
import yagmail

gmail_address = os.environ.get('MY_GMAIL_USERNAME')
gmail_password = os.environ.get('MY_GMAIL_PASSWORD')

parser = argparse.ArgumentParser(description='Sending emails using gmail')

parser.add_argument('recipients', action="store", type=str, help=
"a path to a csv file containing the recipient names and emails")
parser.add_argument('body', action="store", type=str, help=
"a path to a txt file containg the body, closing, and signature of the email")
parser.add_argument('subject', action='store',type=str, help=
"the subject of the email - ex: 'Concern regarding bill 1.1.1'" )
parser.add_argument('intro', action="store",type=str, help=
"the intro or greeting - ex: 'Dear', 'Hello', 'Good Morning'" )

#get all arguments
args = parser.parse_args()
recipients_path = args.recipients
body_path = args.body
intro = args.intro
subject = args.subject


#get body in string
txtfile = open(body_path)
body_str = txtfile.read()
txtfile.close()
#print(body_str)

#get csv to dict
csvfile = open(recipients_path)
reader = csv.reader(csvfile)
next(reader) #skip the header
recip_dict = {}
for row in reader:
  recip_dict[row[0]]=row[1]
csvfile.close()

#send emails
with yagmail.SMTP(gmail_address, gmail_password) as yag:
    for email, name in recip_dict.items():
      body = intro + " " + name + ",\n\n" + body_str
      yag.send(email, subject, body)
    