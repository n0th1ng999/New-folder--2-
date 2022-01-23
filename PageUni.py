from fileinput import filename
from importlib.metadata import files
import os
from re import T
from tkinter import Button, Toplevel
from unicodedata import name

def callback(name):
    name = Faculdades['text']
    fileName = "Uni" + name
    os.system('python '+fileName+'.py')
    print(name)
    
    
    



totalDir = 0
paginaBlah = Toplevel()
pageUni = r"infoProjects"
for base, dirs, files in os.walk(pageUni):
    for directories in dirs:
        totalDir += 1
        naoSei = dirs[totalDir-1]
        Faculdades = Button(paginaBlah,text = naoSei, relief = "flat",font = 20,command =lambda: callback(naoSei))
        Faculdades.pack()
        print(dirs[totalDir-1])
        
       

print(f"o total blahfsuh e {totalDir}")

paginaBlah.mainloop()
