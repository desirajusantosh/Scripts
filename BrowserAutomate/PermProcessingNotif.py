# Email forwarding code from: https://dev.to/mraza007/sending-sms-using-python-jkd

import selenium

from selenium import webdriver
from selenium.common.exceptions import NoSuchAttributeException
from selenium.webdriver.common.keys import Keys
import os,time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
URL = 'https://flag.dol.gov/processingtimes'

driver = webdriver.Chrome(executable_path='/path/to/chromedriver' )
driver.get(URL)


value = driver.find_elements_by_tag_name('TD')
count = 0
for i in value:
    count+=1
    if i.text == "Analyst Review":
        #print(value[count].text)
        date = value[count].text
        break
        print(date)

def send_mail():
    email = "your_email@yahoo.com"
    pas = ""

    sms_gateway = '1234567890@txt.att.net'
    # The server we use to send emails in our case it will be gmail but every email provider has a different smtp # and port is also provided by the email provider.
    smtp = "smtp.mail.yahoo.com"
    port = 587
    # This will start our email server
    server = smtplib.SMTP(smtp,port)
    # server.set_debuglevel(1)
    # Starting the server
    server.starttls()
    # Now we need to login
    server.login(email,pas)

    # Now we use the MIME module to structure our message.
    msg = MIMEMultipart()
    msg['From'] = email
    msg['To'] = sms_gateway
    # Make sure you add a new line in the subject
    msg['Subject'] = date
    msg['Subject'] = date
    # Make sure you also add new lines to your body
    print(date)
    body = date
    # and then attach that body furthermore you can also send html content.
    msg.attach(MIMEText(body, 'plain'))

    sms = msg.as_string()
    print("+++++++++++++++++++++++++++++")
    print(sms)
    server.sendmail(email,'your_email@gmail.com',sms)
    server.sendmail(email,sms_gateway,sms)

    #lastly quit the server
    server.quit()

send_mail()


