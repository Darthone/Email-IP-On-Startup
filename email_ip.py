import smtplib
import socket
import datetime
from email.mime.text import MIMEText

def main():
    # Change to your own account information
    to = 'TO_EMAIL'
    gmail_user = 'GMAIL_ACCOUNT'
    gmail_password = 'GMAIL_PASSWORD'
    
    smtpserver = smtplib.SMTP('smtp.gmail.com', 587)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo
    smtpserver.login(gmail_user, gmail_password)
    
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    
    msg = MIMEText(ip)
    msg['Subject'] = 'IP For %s on %s' % (hostname, datetime.date.today())
    msg['From'] = gmail_user
    msg['To'] = to
    smtpserver.sendmail(gmail_user, [to], msg.as_string())
    smtpserver.quit()

if __name__ == "__main__":
    main()
