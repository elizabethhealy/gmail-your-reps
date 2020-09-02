# Gmail Your Reps

A python script to email your representatives about topics you are passionate about.

## Installation
Make sure you are using python 3
```
python --version
```
Install the dependencies
```
pip install -r requirements.txt
```
Save email address and password in environment as
```
export MY_GMAIL_USERNAME=example@gmail.com
export MY_GMAIL_PASSWORD=ex@mpleP@ssword
```
If you do not have 2 step verification enabled, go to Google Account > Security > Signing in to Google and turn on less secure app access. You will want to turn this off after you ar done. 

If you have 2 step verification enabled, go to Google Account > Security > Signing in to Google. Create app password, you can name it anything you want, then copy the 16 character password and export that as MY_GMAIL_PASSWORD without spaces.

## Usage
The script takes as input a .csv file containing the emails and titles of those to whom you are sending the emails, and a .txt file containing the body, sign off, and signature. 

The csv file should be formatted as below and should include the headers. 
| Email|Name |
|-|-|
| clinton@senate.gov  |Senator Clinton    |
| aoc@house.gov       |Rep. Ocasio-Cortez |
| jsmith@delegates.gov|Del. John Smith    |

Here is an example of the txt file:
```text
My name is Jane Doe and I a do not approve of bill 1.1.1.

Please consider voting against this bill.

Thank you <NAME>.

Sincerely,
Jane Doe

Jane Doe
jane@gmail.com
111-111-1111
```
If you would like to include the name of the recipient anywhere in the body of the email, you can use &lt;NAME&gt; like above. 

Run script:
```
python runner.py recipients.csv email.txt 'Subject Line' 'Dear'
```
Where recipients.csv and email.txt are files or, if they are not in this directory, paths to files described above and in help below.

To get help include --help:
```
usage: runner.py [-h] recipients body subject intro

Sending emails using gmail

positional arguments:
  recipients  a path to a csv file containing the recipient names and emails
  body        a path to a txt file containg the body, closing, and signature
              of the email
  subject     the subject of the email - ex: 'Concern regarding bill 1.1.1'
  intro       the intro or greeting - ex: 'Dear', 'Hello', 'Good Morning'

optional arguments:
  -h, --help  show this help message and exit
```


