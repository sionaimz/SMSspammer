import smtplib
import random
import multiprocessing

spammeremail = "example@gmail.com"
password = "password"

message = input("Hey: ")
messagecount = int(input("100: "))
target = input('2193343815@tmomail.net (the email can be found at https://freecarrierlookup.com/ as the "SMS Gateway address"): ')

s=smtplib.SMTP("smtp.gmail.com",587)
s.starttls()
s.login(spammeremail,password)
x=0

def spam():
    for x in range(0,messagecount):
        print("sending message "+str(x))
        s.sendmail(spammeremail,target,message)
        x+=1
    s.quit()

process = multiprocessing.Process(target=spam)
process.start()

if x not in range(0,messagecount):
    process.terminate
