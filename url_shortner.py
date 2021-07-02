from tkinter import *
import pyshorteners as ps
import pyperclip
from PIL import ImageTk, Image


# Creating Tkinter GUI 
root = Tk()
root.title("URL Shortener")
root.geometry("862x519")
canvas = Canvas(root,bg="#3A7FF6",height=519,width=862,bd=0, highlightthickness=0,relief="ridge")
canvas.place(x=0,y=0)
canvas.create_rectangle(431, 0, 431 + 431, 0 + 519, fill="#FCFCFC",outline="")
canvas.create_rectangle(40, 160, 40 + 60, 160 + 5, fill="#FCFCFC",outline="")

root.configure(background='white')
root.resizable(False,False)

orignalURL = StringVar(root)
shortenedURL = StringVar(root)


# Function for shortening URL
def shorten():
    orignalString=str(orignalURL.get())
    print(orignalString)
    shortM = ps.Shortener()
    result = shortM.tinyurl.short(orignalString)
    global shortenedURL
    shortenedURL.set(str(result))

def copy_to_clipboard():
    pyperclip.copy(shortenedURL.get())



#Creating the texts in our Canvas 

labelIntro=Label(root,text='Instagram : @aneeshawadhiya',bg='white',fg='black')
label1 = Label(root,text='Enter the URL: ',bg='white',fg='black')
text1 = Entry(root,textvariable=orignalURL,width=50,bg='#dfe3eb',fg='black')

button1 = Button(root,text="Shorten",command=shorten,width=20,bg='#3A7FF6',fg='white')

label2 = Label(root,text='Shortened URL: ',bg='white',fg='black')
text2 = Entry(root,textvariable=shortenedURL,width=50,bg='#dfe3eb',fg='black')
button2 = Button(root,text="Copy",command=copy_to_clipboard,width=20,bg='#3A7FF6',fg='white')
button3 = Button(root,text="Quit",command=root.destroy,width=20,bg='#3A7FF6',fg='white')

smallTitle = Label(text="WELCOME", bg="#3A7FF6",justify='left',fg="white",font=("Arial-BoldMT",int(10.0)))
smallTitle.place(x=35.0,y=90.0)

title = Label(text="URL SHORTNER", bg="#3A7FF6",justify='left',fg="white",font=("Arial-BoldMT",int(20.0)))
title.place(x=35.0,y=115.0)

info_text = Label(text="URL Shortner\n"
                   "to shorten any url\n"
                   "using tinyURL\n\n"
                   
                   "Github :\n"
                   "@aneeshawadhiya",
              bg="#3A7FF6",fg="white",justify="left",font=("Arial-BoldMT",int(16.0)))

info_text.place(x=35.0,y=200.0)

labelIntro.place(x=675.0,y=486.0)
label1.place(x=500.0,y=126.0)
text1.place(x=500.0,y=156.0)
button1.place(x=500.0,y=186.0)


label2.place(x=500.0,y=216.0)
text2.place(x=500.0,y=246.0)

button2.place(x=500.0,y=276.0)
button3.place(x=500.0,y=306.0)



root.mainloop()