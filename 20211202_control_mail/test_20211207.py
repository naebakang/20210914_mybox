# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

"""
20211203, 하 결국 메일을 전달 하는 기능을 구현 하는 건 포기 한다. 개빡치네.
"""

import smtplib
import imaplib
import email
from email.header import decode_header, make_header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

imap_host = "imap.gmail.com"
smtp_host = "smtp.gmail.com"
smtp_port = 465
user = "pjbtkk@gmail.com"
passwd = ""
msgid = 7
from_addr = "pjbtkk@gmail.com"
to_addr = "pjbtkk@ajou.ac.kr"

# open IMAP connection and fetch message with id msgid
# store message data in email_data
client = imaplib.IMAP4_SSL('imap.gmail.com')
client.login(user, passwd)
a,b = client.select()

# test
c, d = client.search(None, 'ALL')

b = [b'402']
c, d = client.fetch(b[0], 'RFC822')
mee = email.message_from_bytes(d[0][1])

email_data = d[0][1].decode('utf-8', 'ignore')
# create a Message instance from the email data
message = email.message_from_string(email_data)

subject = make_header(decode_header(mee.get('Subject')))
to = make_header(decode_header(mee.get('To')))
fromm = make_header(decode_header(mee.get('FROM')))
date = make_header(decode_header(mee.get('Date')))
text = 'aa'

msg = MIMEMultipart()
msg.attach(message)
msg.attach(MIMEText(text))
smtp = smtplib.SMTP_SSL(smtp_host, smtp_port)
# smtp.starttls()

msg_ende = msg.as_string().encode('utf-8').strip()
smtp.login(user, passwd)
smtp.sendmail(from_addr, to_addr, msg_ende)
# smtp.send_message(mee)
smtp.quit()

tpy, data = client.search(None, 'ALL')

for num in data[0].split():
    tpy, data = client.fetch(num, '(RFC822)')
    print(num, email.message_from_string(data[0][1]))

client.close()
client.logout()



client.list_folders()
client.select_folder('INBOX', readonly=True)
lss = client.search(['TO', 'pjbtkk@naver.com'])

status, data = client.fetch(msgid, "(RFC822)")
email_data = data[0][1]
client.close()
client.logout()

# create a Message instance from the email data
message = email.message_from_string(email_data)

# replace headers (could do other processing here)
message.replace_header("From", from_addr)
message.replace_header("To", to_addr)

# open authenticated SMTP connection and send message with
# specified envelope from and to addresses
smtp = smtplib.SMTP(smtp_host, smtp_port)
smtp.starttls()
smtp.login(user, passwd)
smtp.sendmail(from_addr, to_addr, message.as_string())
smtp.quit()


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
