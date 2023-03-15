import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
f = open("Networking/password.txt", "r+")
for line in f:
    if "address" in line:
        a = line.strip().split(": ")
        address = a[1]
        print(address)
    elif "password" in line:
        p = line.strip().split(": ")
        password = p[1]
        print(password)
server = smtplib.SMTP_SSL("smtp.mail.yahoo.com", 465)

server.ehlo()


server.login(address, password)

message = MIMEMultipart
message["From"] = "samuel.kostousov@yahoo.com"
message["To"] = address
message["Subject"] = "Test mail sent from python"
with open("Networking/message.txt", "r") as f:
    msg = f.read()
message.attach(MIMEText(message, 'plain'))

filename = "Networking/Rabbi_Daniel_Freund.png"
attachment = open(filename, 'rb')
p = MIMEBase("application", "octet-stream")
p.set_payload(attachment.read())
encoders.encode_base64(p)
p.add_header("Content-Dispostion", f'attachment; filename={filename}')
message.attach(p)

text= message.as_string()
server.sendmail(address, "samuel.kostousov@gmail.com", text)