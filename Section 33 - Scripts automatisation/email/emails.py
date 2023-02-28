import smtplib
import emails_config
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_mails(user_mail, sujet, message):
    
    multipart_message = MIMEMultipart()
    multipart_message["Subject"] = sujet
    multipart_message["From"] = emails_config.config_email
    multipart_message["To"] = user_mail
    multipart_message.attach(MIMEText(message, "plain")) # plain = format txt et html = format html
    
    
    server_mail = smtplib.SMTP(emails_config.config_server, emails_config.config_server_port)
    server_mail.starttls() # Pour la sécurité on doit faire starttls
    server_mail.login(emails_config.config_email, emails_config.config_password)
    server_mail.sendmail(emails_config.config_email, user_mail, multipart_message.as_string())
    server_mail.quit()


message_email = """Hello baby,

N'oublie jamais que tu es l'amour de ma vie.

Je t'aime <3

Ton dersh
"""
send_mails("xxxx@gmail.com", "Juste un spam de love", message_email)