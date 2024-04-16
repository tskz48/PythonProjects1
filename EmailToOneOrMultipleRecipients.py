import smtplib

e=input("Type in an email provider.")
e=e.strip(' ') #removes whitespace that user may have created from input.
user=input("Type in your email.")
pwd = input("Type in your password.")
m=input('Type in the message that you want to send.')
m=m.strip(' ')
server=smtplib.SMTP('smtp.'+str(e)+'.com',587)
server.starttls()
server.login(str(user),str(pwd))
x=input(("How many people do you want to send the email to?"))
for i in range(1,x+1):
    r = input("Type in the email of the reciever.")
    server.sendmail(user,r,m)

server.close()



