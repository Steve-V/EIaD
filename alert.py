import smtplib
from email.message import EmailMessage


def email_alert(whofrom, password, subject, body, to):
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = to

    user = whofrom
    msg['from'] = 'Some Young Guy'
    password = password

    server = smtplib.SMTP("smtp.gmail.com", 587)

    server.starttls()
    server.login(user, password)
    server.send_message(msg)

    server.quit()


if __name__ == '__main__':
    exit(-2)