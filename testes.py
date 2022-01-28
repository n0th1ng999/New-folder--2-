from textwrap import fill, wrap
from tkinter import *
from tkinter.simpledialog import SimpleDialog
from turtle import bgcolor, title
from PIL import ImageTk,Image
from tkinter import ttk
import os
# TextoIntrodutorio = "texto introdutorio"



# ESMAD = Tk()
# ESMAD.geometry("1920x1080")   
# ESMAD.state("zoomed")
# canvas = Canvas(ESMAD, width = 1600, height = 1600)  
# canvas.pack()  
# img = ImageTk.PhotoImage(Image.open(r"imagens//ESMAD//PROJ_ESMAD_LOGO.png")) 
# canvas.create_image(480,20, anchor=NW, image=img)

# #for 
# cursoESMAD = Button(text = "Licenciatura em Tecnologias e Sistemas de Informação Para a Web", relief = "flat" ,font="Helvetica 20 underline" )
# cursoESMAD.place(x= 20,y= 500)
# msgCurso1ESMAD = Message(ESMAD,text = TextoIntrodutorio,width = 1500)
# msgCurso1ESMAD.place(x=20,y=550) 



# ESMAD.mainloop()

from os import walk

for (dirpath, dirnames, filenames) in walk("InfoCursos\\ESMAD"):
    break
print(filenames)
    