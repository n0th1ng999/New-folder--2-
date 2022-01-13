from tkinter import *
import os
def register_user():
    usernameInfo = username.get()
    passwordInfo = password.get()
    emailInfo    = email.get()
    nicknameInfo = nickname.get()
    

    file = open("utilizadores.txt","w")
    file.write(usernameInfo+";")
    file.write(passwordInfo+";")
    file.write(emailInfo+";")
    file.write(nicknameInfo+";")
    file.close
    usernameEntry.delete(0,END)
    passwordEntry.delete(0,END)
    emailEntry.delete(0,END)
    nicknameEntry.delete(0,END)
    Label(screen1,text = "Registration Sucess").pack()



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
    passwordEntry.pack()
    Label(screen1,text="E-mail *(Must include '@' and '.')").pack()
    emailEntry = Entry(screen1,textvariable = email)
    emailEntry.pack()
    Label(screen1,text="Nickname *(Min 4 char)").pack()
    nicknameEntry = Entry(screen1,textvariable = nickname)
    nicknameEntry.pack()
    Label(text="").pack()
    Button(screen1, text = "Register", width = 10, height = 1, command = register_user).pack()


def loginValidation():
    username1 = usernameValidation.get()
    password1 = passwordValidation.get()
    usernameEntry1.delete(0,END)
    passwordEntry1.delete(0,END)

    #List_of_files = os.listdir()

    file1 = open("utilizadores.txt", "r") 
    validation = file1.readlines()
    file1.close()
    for user in validation:
        Fields = user.split(";")
        if username1 == Fields[0]:
            if password1 == Fields[1]:
                print("Login  sucessfull")
                return
            else:
                print("The password you entered is not valid!")
    
    print("User not found")
    

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
    passwordEntry1 = Entry(screen2, textvariable = passwordValidation)
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