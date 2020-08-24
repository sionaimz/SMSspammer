import smtplib
emailserver = "smtp.gmail.com"
spammeremail = "enter the gmail here"
password = "enter your gmail's password"
emailport = "587"
message = input("what message do you want to send: ")
messagecount = int(input("how many messages do you want to send: "))
target = input("enter target number in email form (the email can be found at https://freecarrierlookup.com/ ): ")
s=smtplib.SMTP(emailserver,emailport)
s.starttls()
s.login(spammeremail,password)
x=0
for x in range(0,messagecount):
    print("sending message "+str(x))
    s.sendmail(spammeremail,target,message)
    x+=1
s.quit()
print("\ntask complete\nquitting")