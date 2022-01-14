from cgitb import text
from distutils.command.build import build
from re import T
from tkinter import *
from PIL import ImageTk,Image


UA = Tk()
UA.geometry("1980x720")   
canvas = Canvas(UA, width = 1600, height = 700)  
canvas.pack()  
img = ImageTk.PhotoImage(Image.open(r"C:\Users\Silgueira\Desktop\AED Tema B\Imagens\PROJ_UA_LOGO.png")) 
canvas.create_image(250,20, anchor=NW, image=img)
curso1 = Button(text = "Licenciatura em Gestão", relief = "flat")
curso1.place(x= 20,y= 500)
Message(UA,text = "")

curso2 = Button(text = "Licenciatura em Psicologia", relief = "flat")
curso2.place(x = 20, y = 1000)
Message(UA,text = "")

UA.mainloop() 