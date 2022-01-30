import smtplib 
from email.message import EmailMessage
from string import Template
from pathlib import Path 

html = Template(Path('index.html').read_text())

email = EmailMessage()
email['from'] = 'Kalidas Rajendran'
email['to'] = 'kalidasrs@gmail.com'
email['subject'] = 'test python email'

email.set_content(html.substitute({'name': 'TinTin'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('kalidasrajen92@gmail.com', 'password#')
    smtp.send_message(email)
    print('all good')


# Less secure app access should be allowed to login using python
# It is present in manage account -> security option -> less secure app access
# Some apps and devices use less secure sign-in technology, 
# which makes your account vulnerable.
#  You can turn off access for these apps, 
# which we recommend, or turn it on 
# if you want to use them despite the risks.
#  Google will automatically turn this setting OFF 
# if it’s not being used. Learn more
# Allow less secure apps: ON

