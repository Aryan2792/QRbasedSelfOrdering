import re
import smtplib
from email.message import EmailMessage
import http.client


def sendEmail(to, message, subject):
    msg = EmailMessage()
    msg.set_content(message)
    msg['Subject'] = subject
    msg['To'] = to
    msg['From'] = 'softdev2568@gmail.com'
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('softdev2568@gmail.com', 'softdev.ml')

    server.send_message(msg)
    print('Mail Sent')
    server.quit()


def sendMsg(mobile, message):
    message = message.replace(" ", "%20")
    conn = http.client.HTTPConnection("server1.vmm.education")
    conn.request("GET",
                 "http://server1.vmm.education/VMMCloudMessaging/AWS_SMS_Sender?username=" + 'smstester123' + "&password="
                 + 'QBSAH60R' + "&message=" + message + "&phone_numbers=" + mobile)

    response = conn.getresponse()
    if response == 200:
        return True
    else:
        return False


# sendEmail('nishu.k2989153@gmail.com', 'Hello World', 'Email Testing')

def verifyMail(email):
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if (re.fullmatch(pattern, email)):
        print("Valid Email")

    else:
        print("Invalid Email")


def verifyContact(mobile):
    Pattern = re.compile("(0|91)?[6-9][0-9]{9}")
    result = Pattern.match(mobile)
    if result:
        return True
    else:
        return False


# verifyContact('19874569856')
# verifyMail('aryan@gmail.com')

def verifyName(name):
    for i in name:
        if i.isdigit():
            print('Invalid')
            break
    else:
        print('Valid')


verifyName('karam56')

# if len(email)==0 or len(mobile)==0 or verifyMail(email) or verifyName(name) or verifyContact(mobile)
