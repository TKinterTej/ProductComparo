import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import tkinter
from tkinter import*

def send_Email():

    global email,password,recipient,subject,message,attachment,image2
    
    email_Entry            =      []
    password_Entry         =      []
    recipient_Entry        =      []
    subject_Entry          =      []
    message_Entry          =      []
    attachment_Entry       =      []

    your_Email      = email.get()
    your_Password   = password.get()
    your_Recipient  = recipient.get()
    your_Subject    = subject.get()
    your_Message    = message.get()
    your_Attachment = attachment.get()
    
    email_Entry.append(your_Email)
    email_Sorted       = (email_Entry[0])

    password_Entry.append(your_Password)
    password_Sorted    = (password_Entry[0])

    recipient_Entry.append(your_Recipient)
    recipient_Sorted   = (recipient_Entry[0])

    subject_Entry.append(your_Subject)
    subject_Sorted     = (subject_Entry[0])

    message_Entry.append(your_Message)
    message_Sorted     = (message_Entry[0])

    attachment_Entry.append(your_Attachment)
    attachment_Sorted  = (attachment_Entry[0])

    status = Tk()
    status.geometry('435x100')
    status.configure(bg='Blue')

    if len(email_Sorted) or len(password_Sorted) or len(recipient_Sorted) or len(subject_Sorted) or len(message_Sorted) or len(attachment_Sorted) == 0:
        Label(status, font='Cooper 12 bold underline',text='Your email was not sent. One of your entries were blank.',bg='Green',relief=RAISED).grid(row=1, column=1)
    else:
        Label(status, font='Cooper 12 bold underline',text='Congratulations, your email has been sent!',bg='Green',relief=RAISED).grid(row=1, column=1)

    email_user     = (email_Sorted)
    email_password = (password_Sorted)
    email_send     = (recipient_Sorted)
    subject        = (subject_Sorted)

    msg = MIMEMultipart()

    msg['From'] = email_user
    msg['To']   = email_send
    msg['Subject'] = subject

    body = (message_Sorted)

    msg.attach(MIMEText(body,'plain'))

    filename = (attachment_Sorted)
    attachment = open(filename,'rb')

    part = MIMEBase('application','octet-stream')

    part.set_payload((attachment).read())

    encoders.encode_base64(part)

    part.add_header('Content-Disposition',"attachment; filename= "+filename)

    msg.attach(part)

    text = msg.as_string()

    server = smtplib.SMTP('smtp.gmail.com',587)

    server.starttls()

    server.login(email_user,email_password)

    server.sendmail(email_user,email_send,text)

    server.quit()

main_Win = Tk()
main_Win.configure(bg='Black')
main_Win.geometry('875x350')

image = PhotoImage(file='python-logo-png-python-logo-450.gif')
Label(main_Win, image=image).grid(row=7, column=3)

image1 = PhotoImage(file='Gmail-logo-color.gif')
Label(main_Win, image=image1).grid(row=7, column=0)

Label(main_Win, text="Python Gmail Engine",bg='White',fg='Red',font='Showcard 24 italic underline bold',relief=SUNKEN).grid(row=0, column=1)
Label(main_Win, text="Your Email:",background='White',fg='Red',font='Cooper 10 bold underline',relief=RIDGE).grid(row=1)
Label(main_Win, text="Your Email Password:",background='White',fg='Red',font=' Cooper 10 bold underline',relief=RIDGE).grid(row=2)
Label(main_Win, text="Recipients Email:",background='White',fg='Red',font=' Cooper 10 bold underline',relief=RIDGE).grid(row=3)
Label(main_Win, text="Email Subject:",background='White',fg='Red',font='Cooper 10 bold underline',relief=RIDGE).grid(row=4)
Label(main_Win, text="Email Body:",background='White',fg='Red',font=' Cooper 10 bold underline',relief=RIDGE).grid(row=5)
Label(main_Win, text="Attachment:",background='White',fg='Red',font=' Cooper 10 bold underline',relief=RIDGE).grid(row=6)

image2 = PhotoImage(file='mail_foward-512.gif')
Button(main_Win,image=image2,command=send_Email,cursor='circle').grid(row=7, column=1)

email = Entry(main_Win, width=75,cursor='cross',fg='red')
password = Entry(main_Win, width=75,cursor='cross',fg='red')
recipient = Entry(main_Win, width=75,cursor='cross',fg='red')
subject = Entry(main_Win, width=75,cursor='cross',fg='red')
message = Entry(main_Win, width=75,cursor='cross',fg='red')
attachment = Entry(main_Win, width=75,cursor='cross',fg='red')

email.grid(row=1, column=1)
password.grid(row=2, column=1)
recipient.grid(row=3, column=1)
subject.grid(row=4, column=1)
message.grid(row=5, column=1)
attachment.grid(row=6, column=1)




