import json
import smtplib


SUBJECT = 'Price has changed'


def send_email(to, sender, password, items):
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465, timeout=10)

    body = '\r\n'.join(['To: %s' % to,
                        'From: %s' % sender,
                        'Subject: %s' % SUBJECT,
                        '', json.dumps(items, sort_keys=True, indent=4)])

    try:
        server.login(sender, password)
        server.sendmail(sender, to, body)
        print("email sent")
    except Exception as e:
        print(str(e))
    finally:
        server.quit()
