from email.message import EmailMessage
import smtplib
import ssl

def send_email(subject, body, to_email, cc_email=None, bcc_email=None):
    smtp_server = "smtp.gmail.com"
    smtp_port = 465
    email_sender_name = 'Viet Do'
    email_sender = 'vietdo1807@gmail.com'
    email_password = 'Your App Password'

    em = EmailMessage()
    em['From'] = f"{email_sender_name} <{email_sender}>"
    em['To'] = to_email
    em['Subject'] = subject
    em.set_content(body)

    recipients = to_email.split(',')
    if cc_email:
        em['Cc'] = cc_email
        recipients += cc_email.split(',')
    if bcc_email:
        recipients += bcc_email.split(',')

    context = ssl.create_default_context()

    try:
        with smtplib.SMTP_SSL(smtp_server, smtp_port, context=context) as smtp:
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, recipients, em.as_string())
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")

subject = 'Project Email Sender using Python'
body = """
    Have a good day, bro!
"""
to_email = 'to_email@gmail.com'
cc_email = 'cc1_email@gmail.com, cc2_email@gmail.com'
bcc_email = 'bcc_email@gmail.com'
send_email(subject, body, to_email, cc_email, bcc_email)