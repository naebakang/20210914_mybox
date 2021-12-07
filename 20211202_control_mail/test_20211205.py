# File encoding: UTF-8

import imaplib
import email
from email.header import decode_header, make_header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib


def main(password):
    imap_host = "imap.gmail.com"
    smtp_host = "smtp.gmail.com"
    smtp_port = 465
    user = "pjbtkk@gmail.com"
    passwd = password
    from_addr = "pjbtkk@gmail.com"
    to_addr = "pjbtkk@ajou.ac.kr"

    # open IMAP connection and fetch message with id msgid
    # store message data in email_data
    client = imaplib.IMAP4_SSL('imap.gmail.com')
    client.login(user, passwd)
    a, b = client.select()
    c, d = client.search(None, 'ALL')

    smtp = smtplib.SMTP_SSL(smtp_host, smtp_port)
    smtp.login(user, passwd)

    list_date_want = ['2016', '2017']
    list_index_send = []
    all_email = d[0].split()
    for idx, mail in enumerate(all_email):
        result, data = client.fetch(mail, '(RFC822)')
        raw_email = data[0][1]
        raw_email_string = raw_email.decode('utf-8', 'ignore')
        email_message = email.message_from_string(raw_email_string)
        for i in list_date_want:
            if i in str(email_message['Date']):
                list_index_send.append(idx)

    print(list_index_send)
    print(len(list_index_send))

    for i in list_index_send:
        print('for i: {}'.format(i))
        msg = MIMEMultipart()

        e, f = client.fetch(all_email[i], '(RFC822)')

        frd = email.message_from_bytes(f[0][1])
        fromm = str(make_header(decode_header(frd.get('FROM'))))
        date = str(make_header(decode_header(frd.get('Date'))))
        subject = str(make_header(decode_header(frd.get('Subject'))))
        to = str(make_header(decode_header(frd.get('To'))))
        msg.attach(MIMEText(fromm))
        msg.attach(MIMEText(date))
        msg.attach(MIMEText(subject))
        msg.attach(MIMEText(to))

        email_data = f[0][1].decode('utf-8', 'ignore')
        message = email.message_from_string(email_data)
        msg.attach(message)

        msg['From'] = from_addr
        msg['Subject'] = subject
        msg['To'] = to_addr

        msg_en = msg.as_string().encode('utf-8').strip()

        smtp.sendmail(from_addr, to_addr, msg_en)

    client.close()
    client.logout()
    smtp.quit()


if __name__ == '__main__':
    main(password='')
