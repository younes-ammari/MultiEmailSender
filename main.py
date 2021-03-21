from tkinter import scrolledtext
from tkinter import *
import yagmail


bg='#069c3f'
fg_win='black'
fg_entry='white'

bg_mail='white'
fg_mail='black'
font_labels = 'arial 13 bold'

invalide_mail_or_username =r"(535, b'5.7.8 Username and Password not accepted. Learn more at\n5.7.8  https://support.google.com/mail/?p=BadCredentials c26sm16319750wrb.87 - gsmtp')"
win = Tk()
win.title('MultiEmailSender')
win.geometry('752x560+200+50')
win.maxsize(752,560)
win.minsize(752,560)
win.config(bg= bg)
i = 0

def mark() :
    if var.get() == 1 :
        password_entry.configure(show = "")
    elif var.get() == 0 :
        password_entry.configure(show = "*")


def send_emails():
    global emails
    emails_values = emails.get('0.0',"end-1c")
    emails_list = list(emails_values.split('\n'))
    if emails_list[-1]=='': emails_list.pop()
    else: 
        pass
    
    usermail = usermail_entry.get('0.0',"end-1c")
    password = password_entry.get()
    subject = subject_text.get('0.0',"end-1c")
    content = content_text.get('0.0',"end-1c")

    usermail_entry.config( highlightthickness=0)
    password_entry.config( highlightthickness=0)
    status.config(fg='#bf001a', state='normal')
    usermail_entry.config(highlightthickness=0)
    password_entry.config(highlightthickness=0)
    subject_text.config(highlightthickness=0)
    emails.config(highlightthickness=0)
    content_text.config(highlightthickness=0)

    if len(usermail) < 8  or len(password) < 8 or len(subject)< 4 or len(emails_values)< 8 or len(content)<5:
        if len(usermail) < 8:
            usermail_entry.config(highlightthickness=1)
            empty = 'usermail'
        elif len(password) < 8:
            password_entry.config(highlightthickness=1)
            empty = 'password'
        elif len(subject) < 4:
            subject_text.config(highlightthickness=1)
            empty = 'subject'
        elif len(emails_values) < 8:
            emails.config(highlightthickness=1)
            empty = 'emails'
        else :
            content_text.config(highlightthickness=1)
            empty = 'content'            
        
        message = 'Please fill all the entries ... \ninvalide '+ empty
    else:
        if not box.get(ANCHOR)=='HTML': 
            content = list(content.split('\n'))
        else:
            pass
        try:
            yag = yagmail.SMTP(user=usermail, password=password, host='smtp.gmail.com')
            yag.send(emails_list, subject, content)
            status.config(fg='white', state='normal')
            message = 'sent successfully'
            yag.close()
        except Exception as e:
            #e = "(535, b'5.7.8 Username and Password not accepted. Learn more at\n5.7.8  https://support.google.com/mail/?p=BadCredentials c26sm16319750wrb.87 - gsmtp')"
            if str(e) =='[Errno 11001] getaddrinfo failed':
                message = 'check internet connection'
            elif (str(e).split(','))[0].split('(')[1] == '535' :
                usermail_entry.config(highlightbackground='red', highlightthickness=1)
                password_entry.config(highlightbackground='red', highlightthickness=1)
                message = 'invalide usermail or password! ...'
            else:
                message = 'ERROR' + ' \ndetails: \n' + str(e)

        box.config(highlightbackground=bg)

    status.delete(0.0, END)
    status.insert(END, message)
    status.config(state='disabled') 

var = IntVar()
# relief must be flat, groove, raised, ridge, solid, or sunken

#usermail 
width = 27
usermail_label = Label(win, text=' Usermail: ', fg=fg_win, bg=bg, font=font_labels).place(x=7, y=20)
usermail_entry = Text(win, height = 1, width=width, highlightbackground='red', insertbackground='red', undo=True, relief='solid', pady=3, padx=5, bg=bg, fg=fg_entry, font='arial 13')
usermail_entry.place(x=97, y=20)

#password
password_label = Label(win, text=' Password: ', fg=fg_win, bg=bg, font=font_labels).place(x=387, y=20)
password_entry = Entry(win, width=23, vcmd=3, highlightbackground='red', insertbackground='red',show='*', relief='solid', bg=bg, fg=fg_entry, font='arial 13')
password_entry.place(x=487, y=20, height =27)

#checkbutton
checkbutton = Checkbutton(win, bg=bg, command = mark, offvalue = 0, onvalue = 1, variable = var)
checkbutton.place(x = 710, y = 20)

#subject
lbl_subject = Label(win, text=' Subject :', fg=fg_win, bg=bg, font=font_labels).place(x=7, y=60)
subject_text = Text(win, height= 1, width=44, highlightbackground='red', bg=bg, fg=fg_entry, relief='solid', insertbackground='red', font='arial 16', pady=3, padx=5, undo=True)
subject_text.place(x=97, y=60)

#Box
box = Listbox(win, font='arial 9 bold', highlightbackground='white', bg='white', height=2, width=10, relief='solid')
box.insert(1, "Body")
box.insert(2, "HTML")
box.place(x=660, y=58)


#Content
lbl_content = Label(win, text=' Content :', fg=fg_win, bg=bg, font=font_labels).place(x=7, y=91)
content_text = Text(win, height= 10, width=60, highlightbackground='red', bg=bg, fg=fg_entry, relief='solid', insertbackground='red', 
font='arial 16', pady=3, padx=5, undo=True)
content_text.place(x=10, y=120)

#Emails
lbl_email = Label(win, text='Put Your Emails Here (text box):', fg=fg_win, bg=bg, font=font_labels)
lbl_email.place(x=7, y=378)

emails = Text(win, height= 7, width=35, bg=bg_mail, fg=fg_mail, font='arial 11', insertbackground='red',
 relief='solid' , highlightbackground='red', pady=3, padx=5, undo=True)
emails.place(x=10, y=408)

#Status
lbl_status = Label(win, text='Email Status :', fg=fg_win, bg=bg, font=font_labels).place(x=320, y=378)

status = Text(win, height= 7, width=35, bg=bg, fg=fg_mail, relief='solid', 
xscrollcommand=True, font='arial 11', pady=3, padx=5, state='disabled', undo=True)
status.place(x=320, y=408)

#Buttons
send = Button(win, text='SEND', fg='white', bg=bg, relief='solid', font='arial 14', 
height= 2, width=7, command=send_emails, activebackground =bg)
send.place(x=620, y=408)

exit = Button(win, text='EXIT', fg='white', bg='red', relief='solid', font='arial 14',
 command=win.destroy, height= 2, width=7, activebackground ='red')
exit.place(x=620, y=474)

#credit
credit = Label(win, text='''-------------------------------------------------------------- created by: younes.ammari ....... viva Algeria ---------------------------------------------------------------------
''', fg='#1f1f1f', bg=bg, font='arial 8').place(x=0, y=540)

usermail_entry.insert(END, 'usermail@gmail.com')
password_entry.insert(END, 'passwordmail')
subject_text.insert(END, 'Write a Subject')
content_text.insert(END, 'Write your message here ...')
emails.insert(END, 'email0@gmail.com\nemail1@gmail.com\nemail2@gmail.com\nemail3@gmail.com\n')

win.mainloop()