import smtplib, imaplib, email

imap_host = "imap.gmail.com"
smtp_host = "smtp.gmail.com"
smtp_port = 465
user = "pjbtkk@gmail.com"
passwd = "okyksbrseddazhjd"
msgid = 7
from_addr = "pjbtkk@gmail.com"
to_addr = "pjbtkk@ajou.ac.kr"

# open IMAP connection and fetch message with id msgid
# store message data in email_data
client = imaplib.IMAP4_SSL(imap_host)
client.login(user, passwd)
a, b = client.select('INBOX')
c, d = client.search(None, 'ALL')

e = [b'380']
status, data = client.fetch(e[0], "(RFC822)")
# str = unicode(str, errors='replace')
email_data = data[0][1].decode('utf-8', 'ignore')


# create a Message instance from the email data
message = email.message_from_string(email_data)

f = [b'379']
status, data = client.fetch(f[0], "(RFC822)")
mee = email.message_from_bytes(data[0][1])

client.close()
client.logout()

# replace headers (could do other processing here)
message.replace_header("From", from_addr)
message.replace_header("To", to_addr)

# open authenticated SMTP connection and send message with
# specified envelope from and to addresses
smtp = smtplib.SMTP_SSL(smtp_host, smtp_port)
# smtp.starttls()
smtp.login(user, passwd)
smtp.sendmail(from_addr, to_addr, message.as_string())
smtp.sendmail(from_addr, to_addr, mee.as_string())
smtp.quit()