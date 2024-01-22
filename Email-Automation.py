import smtplib

To = input("Enter the email address of the receiver:-")
message = input("Enter the message you want to send:-") 
def send_Email(To,message):
    server = smtplib.SMTP('smtp.gmail.com',587)  #psssing two prams that will be the host
    server.starttls() #we need to start tls
    server.login('sender"s email','password(for smtp two step on and app password garera)')
    server.sendmail('sender"s email',To, message)  #sendmail : inbuilt-fxn in smtplib, you can pass in string too'receiver's gmail','message'
    server.close()
    
send_Email(To, message)