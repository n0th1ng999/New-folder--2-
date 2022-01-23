
import builtins
from tkinter import *
from tkinter import *
from tkinter import messagebox
import tkinter as tk
import re
import os


global admin
def register_user():
    usernameInfo = username.get()
    passwordInfo = password.get()
    emailInfo    = email.get()
    nicknameInfo = nickname.get()

    

    file = open("utilizadores.txt","a")

    file.write(usernameInfo+";")
    file.write(passwordInfo+";")
    file.write(emailInfo+";")
    file.write(nicknameInfo+";")


    file.write("\n")

    file.close
    usernameEntry.delete(0,END)
    passwordEntry.delete(0,END)
    emailEntry.delete(0,END)
    nicknameEntry.delete(0,END)
    Label(screen1,text = "Registration Sucess").pack()


def validateReg():
    while True:
        userRegValidate = username.get()
        passRegValidate = password.get()
        emailRegValidate= email.get()
        nickRegValidate = nickname.get()
        validForm = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        
        if len(userRegValidate) < 4:
            messagebox.showerror("Invalid Username!", "Username needs to be at least 4 characters long!")
            username.set("")
            password.set("")
            email.set("")
            nickname.set("")
            break
        
        if len(passRegValidate) < 6:
            messagebox.showerror("Invalid Password!", "Password should be at least 6 chatacters long!")
            username.set("")
            password.set("")
            email.set("")
            nickname.set("")
            break
        
        if len(nickRegValidate) < 4:
            messagebox.showerror("Invalid Nickname", "Your nickname needs to be at least 4 characters long!")
            username.set("")
            password.set("")
            email.set("")
            nickname.set("")
            break
        
        if (re.fullmatch(validForm, emailRegValidate)):
            register_user()
            break
            
        else:
            messagebox.showerror("Invalid E-Mail", "Your E-Mail must include the characters '@' and '.'")
            username.set("")
            password.set("")
            email.set("")
            nickname.set("")
        
    
    
                                       
def register():
    global screen1
    screen1 = Toplevel(screen)
    screen1.title("Register")
    screen1.geometry("300x250")
    global username
    global password
    global email
    global nickname
    global usernameEntry
    global passwordEntry
    global emailEntry
    global nicknameEntry

    username = StringVar()
    password = StringVar()
    email    = StringVar()
    nickname = StringVar()
    Label(screen1,text="Please enter your information").pack()
    Label(screen1,text="").pack()
    Label(screen1,text="Username *(Min 4 char)").pack()
    usernameEntry = Entry(screen1,textvariable = username)
    usernameEntry.pack()
    Label(screen1,text="Password *(Min 6 char)").pack()
    passwordEntry = Entry(screen1,textvariable = password)

    passwordEntry = Entry(screen1,textvariable = password, show = "*")

    passwordEntry.pack()
    Label(screen1,text="E-mail *(Must include '@' and '.')").pack()
    emailEntry = Entry(screen1,textvariable = email)
    emailEntry.pack()
    Label(screen1,text="Nickname *(Min 4 char)").pack()
    nicknameEntry = Entry(screen1,textvariable = nickname)
    nicknameEntry.pack()
    Label(text="").pack()

    Button(screen1, text = "Register", width = 10, height = 1, command = validateReg).pack()



    

def login():
    print("Login session started")

    Button(screen1, text = "Register", width = 10, height = 1, command = validateReg).pack()
    


def loginSuccess():
    messagebox.showinfo("Login was successfull!", "your credentials are correct!")

#def loginSuccess():
#    message = tk.Tk()
#    message.title("Your login was Successfull")
#    message.geometry("150x100")
#    Label(message,text = "You have logged in successfully").pack()
#    Button(message,text = "Ok",command = lambda:message.destroy()).pack()
def invalidPassword():
    messagebox.showerror("Invalid password", "Your password is invalid!")
#def invalidPassword():
#    message1 = tk.Tk()
#    message1.title("Invalid Password!")
#   message1.geometry("150x100")
#    Label(message1,text = "Your password is invalid!").pack()
#    Button(message1,text = "Ok",command = lambda:message1.destroy()).pack()
def userNotFound():
    messagebox.showerror("Invalid username", "The username does not exist!")
#def userNotFound():
#    message2 = tk.Tk()
#    message2.title("Invalid Username")
#    message2.geometry("150x100")
#    Label(message2,text = "The username does not exist").pack()
#   Button(message2,text = "Ok",command = lambda:message2.destroy()).pack()


def loginValidation():
    username1 = usernameValidation.get()
    password1 = passwordValidation.get()
    usernameEntry1.delete(0,END)
    passwordEntry1.delete(0,END)

    #List_of_files = os.listdir()
    global admin
    admin = False
    file1 = open("utilizadores.txt", "r") 
    loginValidation = file1.readlines()
    file1.close()
    for user in loginValidation:
        
        Fields = user.split(";")
        if username1 == Fields[0]:
            if password1 == Fields[1]:
                loginSuccess()
                if username1 == "jose" and password1 == "nogueira":
                    admin = True
                    print("Welcome Admin")
                Main = Toplevel()

#Get the current screen width and height
                screen_width = Main.winfo_screenwidth()
                screen_height = Main.winfo_screenheight()

#
                greeting = tk.Label(text="Hello, Tkinter")
                greeting.pack()

# setting attribute
                Main.attributes('-fullscreen', True)
                Main.resizable(False, False)
                Main.title("")


                Focus = tk.LabelFrame(Main, text='' , width= screen_width-200 , height = screen_height-200  , bg = '#fff' ,  borderwidth= 0, highlightcolor='#f43', highlightthickness= 0)
                Focus.place(x = 200 , y = 200 )

                SideNav = tk.LabelFrame(Main, text='' , width= 300 , height = screen_height-200  , bg = '#023' ,  borderwidth= 0, highlightcolor='#f43', highlightthickness= 0)
                SideNav.place(x = 0 , y = 200 )
                Navbar = tk.LabelFrame(Main, text='' , width= screen_width , height = 200  , bg='#f23',  borderwidth= 0 ,highlightcolor='#f23', highlightthickness= 0  )
                Navbar.place(x = 0 , y= 0)





                Main.mainloop()
                
                return
            else:
                invalidPassword()
        else: userNotFound()
    

def login():
    global screen2
    global usernameEntry1
    global passwordEntry1
    global usernameValidation
    global passwordValidation
    screen2 = Toplevel(screen)
    screen2.title("login")
    screen2.geometry("300x250")
    Label(screen2,text = "Please enter your information").pack()
    Label(screen2,text = "").pack()
    
    
    
    usernameValidation = StringVar()
    passwordValidation = StringVar()

    Label(screen2,text = "Username").pack()
    usernameEntry1 = Entry(screen2, textvariable = usernameValidation)
    usernameEntry1.pack()
    Label(screen2,text = "").pack()
    Label(screen2,text = "Password").pack()
    passwordEntry1 = Entry(screen2, textvariable = passwordValidation,show = "*")
    passwordEntry1.pack()
    Label(screen2,text = "").pack()
    Button(screen2, text = "Login", width = 10, height = 1,command = loginValidation).pack()


    
    
    





def main_screen():
    global screen
    screen = Tk()
    screen.geometry("300x250")
    screen.title("Notes 1.0")
    Label(text = "Notes 1.0", bg = "grey",width = "300",height = "2", font = ("calibri",13)).pack()
    Label(text="").pack()
    Button(text = "Login",height = "2",width = "30",command = login).pack()
    Label(text="").pack()
    Button(text = "Register",height = "2",width = "30",command = register).pack()
    
    
    
    
    screen.mainloop()
 


main_screen()