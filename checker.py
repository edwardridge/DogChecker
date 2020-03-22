import requests
import sys
import time
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def checkDogCount(urll, textToSearch):
    r = requests.get(urll)
    countText = r.text.count(textToSearch)
    return countText

def sendEmail(urlLink):
    port = 465  # For SSL
    password = "dogchecker"
    # Create a secure SSL context
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login("dogchekerthorpebank@gmail.com", password)
        # TODO: Send email here
        sender_email = "dogchekerthorpebank@gmail.com"
        receiver_email = "edwardridge@gmail.com"
        message = MIMEMultipart("alternative")
        message["Subject"] = "POTENTIAL NEW DOG"
        message["From"] = sender_email
        message["To"] = receiver_email

        text = urlLink
        part1 = MIMEText(text, "plain")
        message.attach(part1)

        server.sendmail(sender_email, receiver_email, message.as_string())

def repeatDogCheck(urll, textToSearch):
    previousCount = 0
    while True:
        dogCount = checkDogCount(urll, textToSearch)

        if dogCount > previousCount:
            sendEmail(urll)
            sys.stdout.write("POTENTIAL NEW DOG")
            previousCount = dogCount
        if dogCount < previousCount:
            previousCount = dogCount

        time.sleep(5)
    
def main():
    urll = "https://www.pets4homes.co.uk/search/?type_id=3&advert_type=1&location=london&distance=30&results=10&sort=creatednew"
    textToSearch = "poo"
    repeatDogCheck(urll, textToSearch)
  
if __name__== "__main__":
  main()