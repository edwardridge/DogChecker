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
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login("dogchekerthorpebank@gmail.com", password)
        
        sender_email = "dogchekerthorpebank@gmail.com"
        receiver_email = ["bronacanavan20@gmail.com","edwardridge@gmail.com"]
        message = MIMEMultipart("alternative")
        message["Subject"] = "WOOF WOOF POTENTIAL NEW DOG"
        message["From"] = sender_email
        message["To"] = ", ".join(receiver_email)

        text = urlLink
        part1 = MIMEText(text, "plain")
        message.attach(part1)

        server.sendmail(sender_email, receiver_email, message.as_string())

def repeatDogCheck(urls, textToSearch):
    previousCount = 10000
    while True:
        dogCount = 0
        for url in urls:
             dogCount += checkDogCount(url, textToSearch)
       
        if dogCount > previousCount:
            sendEmail(", ".join(urls))
            sys.stdout.write(f"WOOF WOOF POTENTIAL NEW DOG: {dogCount}")
            sys.stdout.flush()
            previousCount = dogCount
        if dogCount < previousCount:
            sys.stdout.write(f"Dog count changed: {dogCount}")
            sys.stdout.flush()
            previousCount = dogCount

        sys.stdout.write(f"-")
        sys.stdout.flush()
        time.sleep(30)
    
def main():
    urls = ["https://www.pets4homes.co.uk/search/?type_id=3&advert_type=1&location=london&distance=30&results=10&sort=creatednew"]
    textToSearch = "poo"
    repeatDogCheck(urls, textToSearch)
  
if __name__== "__main__":
  main()