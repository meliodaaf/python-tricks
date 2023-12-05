import os
import smtplib


def sample_func():
    try:
        1 / 0
    except ZeroDivisionError as err:
        title = "Error on function sample_func()"
        message = f"An error has occured: {err}"
        emailer(title, message)
    

def emailer(title, msg):
	mailer = smtplib.SMTP('smtp.gmail.com', 587)
 
	sender = "ramentosubia11@gmail.com"
 	# from .bashrc --> export GMAIL_PASS="GMAIL APP PASSWORD"
	password = os.environ.get("GMAIL_PASS") 

	receiver = "subiaclarence96@gmail.com"
	email_title = title

	# start TLS for security
	mailer.starttls()
	
	# Authentication
	mailer.login(sender, password)

	# Header
	header = f"To:{receiver}\nFrom:{sender}\nsubject:{email_title}\n"
	
	# message to be sent
	message = msg

	# Email Content
	email_content = header + message

	# sending the mail
	mailer.sendmail(sender, receiver, email_content)
	
	# terminating the session
	mailer.quit()
 
 
if __name__ == "__main__":
    sample_func()