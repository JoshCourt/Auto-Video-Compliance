"""emailupdate
https://www.youtube.com/watch?time_continue=5&v=YPiHBtddefI&feature=emb_logo
https://nitratine.net/blog/post/how-to-send-an-email-with-python/

"""


import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os.path
"""
infoallerts deeets
    email = 'infotv.alerts@gmail.com'
    password = 'IIiAAa2020'

"""
def email505(emailaccountfrom, password505, emailaccounttoo, subject505, message505, fileloc):
    email = str(emailaccountfrom)
    password = str(password505)
    send_to_email = str(emailaccounttoo)
    subject = str(subject505)
    message = str(message505)
    file_location = str(fileloc)

    msg = MIMEMultipart()
    msg['From'] = email
    msg['To'] = send_to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(message, 'plain'))

    def attachment(fileloc):
                # Setup the attachment
        filename = os.path.basename(file_location)
        attachment = open(file_location, "rb")
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

        # Attach the attachment to the MIMEMultipart object
        msg.attach(part)
    if not fileloc == "NONE":
        attachment(fileloc)
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email, password)
    text = msg.as_string()
    server.sendmail(email, send_to_email, text)
    server.quit()


#email505('infotv.alerts@gmail.com', 'IIiAAa2020', 'joshua.court@information.tv', 'THIS IS A TEST', 'This message is a test. \nIwant to see if i can add lines ect \n\nyeet', 'NONE')
