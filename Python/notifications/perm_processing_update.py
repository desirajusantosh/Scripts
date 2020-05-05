# smtp connection debug https://stackoverflow.com/questions/17759860/python-2-smtpserverdisconnected-connection-unexpectedly-closed/33121151#33121151
# ATT email to phone number https://www.att.com/support/article/wireless/KM1061254/

import selenium

from selenium import webdriver
from selenium.common.exceptions import NoSuchAttributeException
from selenium.webdriver.common.keys import Keys
import os,time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
URL = 'https://flag.dol.gov/processingtimes'

driver = webdriver.Chrome(executable_path='/Users/desiraju/Desktop/chromedriver' )
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
    email = ""
    pas = ""

    sms_gateway = '8134819468@txt.att.net'
    smtp = "smtp.mail.yahoo.com"
    port = 587
    server = smtplib.SMTP(smtp,port)
    # server.set_debuglevel(1)
    server.starttls()
    server.login(email,pas)

    msg = MIMEMultipart()
    msg['From'] = email
    msg['To'] = sms_gateway
    msg['Subject'] = date
    msg['Subject'] = date
    print(date)
    body = date
    msg.attach(MIMEText(body, 'plain'))

    sms = msg.as_string()
    print("+++++++++++++++++++++++++++++")
    print(sms)
    server.sendmail(email,'',sms)
    server.sendmail(email,sms_gateway,sms)

    server.quit()

send_mail()


