
import os
from tkinter import *

from fileinput import filename

import os
from tkinter import Button, Tk, Toplevel
from unicodedata import name


def callback(name):
    fileName = "Uni" + name
    os.system('python '+fileName+'.py')
    print(name)
    
    
    



totalDir = 0
paginaBlah = Tk()

pageUni = r"infoProjects"

pageUni = r"infoCursos"

for base, dirs, files in os.walk(pageUni):
    for directories in dirs:
        totalDir += 1
        naoSei = dirs[totalDir-1]
        Faculdades = Button(paginaBlah,text = naoSei, relief = "flat",font = 20,command = lambda naoSei=naoSei: callback(naoSei))
        Faculdades.pack()
        print(dirs[totalDir-1])
        
       

print("o total blahfsuh e {totalDir}")

paginaBlah.mainloop()
