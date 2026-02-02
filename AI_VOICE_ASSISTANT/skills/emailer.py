import smtplib, os
from dotenv import load_dotenv
load_dotenv()

def send_email(to,subject,msg):
    email = os.getenv("EMAIL")
    password = os.getenv("EMAIL_PASS")
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login(email,password)
    server.sendmail(email,to,f"Subject:{subject}\n\n{msg}")
    server.quit()
