import smtplib
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate


def send_email(sender, receivers, subject, body=None,
               attachment_paths=None, server='localhost', email_user=None,
               email_password=None):
    """ Send email function."""
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = COMMASPACE.join(receivers)
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject
    msg.attach(MIMEText(body))

    for f in attachment_paths or []:
        with open(f, "rb") as fil:
            msg.attach(MIMEApplication(
                fil.read(),
                Content_Disposition='attachment; filename="%s"' % basename(f),
                Name=basename(f)
            ))

    try:
        smtp = smtplib.SMTP(server)
        smtp.ehlo()
        smtp.starttls()
        if email_user and email_password:
            smtp.login(email_user, email_password)
        smtp.sendmail(sender, receivers, msg.as_string())
        smtp.close()
        print('Successfully sent the mail')
    except:
        print("Failed to send mail")
