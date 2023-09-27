import tkinter
from tkinter import messagebox

window = tkinter.Tk()
window.title("Login form")
window.geometry('340x340')
window.configure(bg='#333333')

def login():
    
    username = "Wanganya"
    password = "12345"

    if username_entry.get()==username and password_entry.get()==password:
       #print("succesfully loged in")
       messagebox.showinfo(title="Log in",message="you have successfully logged in")
    else:
       # print("invalid login")
       messagebox.showinfo(title="Error",message="Invalid log in")




frame = tkinter.Frame(bg='#333333')


#Label = tkinter.Label(window, text = "Login")
#Label.pack() #Geometry manager: Label.pack(),Label.place(),Labelgrid()


#creating widgets
login_label = tkinter.Label(frame,text="Login",bg='#333333',fg='#FF3399',font=("aerial",20))
username_label = tkinter.Label(frame,text = "username",fg="#FFFFFF",bg='#333333',font=("aerial",12))
username_entry = tkinter.Entry(frame,font=("aerial",12))
password_entry = tkinter.Entry(frame,show = "*",font=("aerial",12)) 
password_label = tkinter.Label(frame,text = "password",bg='#333333',fg="#FFFFFF",font=("aerial",12 ) )
login_button = tkinter.Button(frame,text = "login",bg='#FF3399',fg="#FFFFFF",command=login)

#placing widgets on the screen

login_label.grid(row = 0,column=0, columnspan=2,sticky='news',pady =20) 
username_label.grid(row=1, column=0)
username_entry.grid(row=1,column=1,pady=5)
password_entry.grid(row=2,column=1,pady=5)
password_label.grid(row=2,column=0)
login_button.grid(row=3,column=0,columnspan=2,pady=10)

frame.pack()

window.mainloop()