import os
from posixpath import split
from tkinter.simpledialog import SimpleDialog
from tkinter import *
from turtle import bgcolor
from PIL import ImageTk,Image


def UniPage(nomeUni,nomesCursos):
    

    TextoIntrodutorio = "texto introdutorio"
    ESMAD = Tk()
    ESMAD.geometry("1920x1080")   
    ESMAD.state("zoomed")
    canvas = Canvas(ESMAD, width = 1080, height = 1600)  
    canvas.pack()  
    

    
    #path To txt 
    txtpath="InfoCursos\\"+nomeUni+"\\"

    for (dirpath, dirnames, filenames) in os.walk("InfoCursos\\ESMAD"):
        break

    
    for files in filenames:
        f = open(txtpath+"\\"+files,"r",encoding="Utf-8")
        content = f.read()
        content_list = content.splitlines()
        f.close()

        CursoFile = txtpath+"\\"+files
        
        Title = content_list[0]
        Intro = content_list[1]
        cursoESMAD = Button(canvas, text = Title, relief = "flat" ,font="Helvetica 20 underline" ,command= lambda CursoFile=CursoFile : PAGE_ONCLICK(CursoFile))
        cursoESMAD.pack()
        msgCursoESMAD = Message(canvas,text = Intro ,width = 1500)
        msgCursoESMAD.pack()
        

    ESMAD.mainloop()




    



  ############################################################################################################

def PAGE_ONCLICK(CursoFile):
    


    f = open(CursoFile,"r",encoding="Utf-8")
    content = f.read()
    content_list = content.splitlines()
    f.close()
    InfoDisciplinas=    [           ]
    NomeDisciplina=     [           ]
    Periodo=            [           ]
    Ects=               [           ]
    Peri=""
  
    for i in range(2,len(content_list)):
        InfoDisciplinas.append(content_list[i].split(";"))
        NomeDisciplina.append(InfoDisciplinas[i-2][0])
        print(InfoDisciplinas[i-2][0])
        Periodo.append(InfoDisciplinas[i-2][1])
        print(InfoDisciplinas[i-2][1])
        Ects.append(InfoDisciplinas[i-2][2])
        print(InfoDisciplinas[i-2][2])
    
    
    
        
        
        

    root = Tk()
    root.geometry("1920x1080")   
    root.state("zoomed")
    root.title('Pagina do curso '+ content_list[0])


    # Create A Main Frame
    main_frame = Frame(root)
    main_frame.pack(fill=BOTH, expand=1)

    # Create A Canvas
    my_canvas = Canvas(main_frame)
    my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

    # Add A Scrollbar To The Canvas
    my_scrollbar = Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT, fill=Y)

    # Configure The Canvas
    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))

    # Create ANOTHER Frame INSIDE the Canvas
    second_frame = Frame(my_canvas)


    # Add that New frame To a Window In The Canvas
    my_canvas.create_window((0,0), window=second_frame, anchor="nw")


    my_label = Label(second_frame, text="It's Friday Yo!").grid(row=3, column=2)
    
    Texto=''''''
    
    # xex = 0
    # for i in range(len(InfoDisciplinas)):
    #     if xex % 13 == 0:
    #         e = 2
    #         TotalEcts = 0
    #         while(e <= 15 ):
    #            
    #             TotalEcts = + int(InfoDisciplinas[i-e][2])
    #         Texto = Texto + '''\t\t\t\t\t\tTotal\t\t\t\t\t\t\t\t\t\t\t\t\t\t'''+ str(TotalEcts) +'''\n\n\n\n'''
    #
    #     if xex % 6:
    #         Texto = Texto + '''\n\n\n\n\n'''
    #     if xex % 12 == 0:
    #         xex =+ 1
    #         Ano = int(xex / 12)
    #         Ano+1
    #         Texto = Texto +'''\n\n\n\n\nAno ''' + Ano + '''\t\t\t\t\t\tUnidade Curricular\t\t\t\t\t\t\tPeríodo\t\t\t\t\t\t\tCréditos ECTS'''    
    #     xex =+ '''\n\n\n\n\t\t\t\t\t\t'''+InfoDisciplinas[i-2][0]+'''\t\t\t\t\t\t\t'''+InfoDisciplinas[i-2][1]+'''\t\t\t\t\t\t\t'''+InfoDisciplinas[i-2][2]
    # xex+=1
    SomaEctsAno1=0
    SomaEctsAno2=0
    SomaEctsAno3=0

    for i in range(-1,12):
        SomaEctsAno1 += int(Ects[i])
    for i in range(11,24):
        SomaEctsAno2 +=int(Ects[i])
    for i in range(23,36):
        SomaEctsAno3 += int(Ects[i])



    textoCurso1ESMAD = Text(my_canvas ,relief = FLAT, font = "200")
    textoCurso1ESMAD.pack(side=TOP, fill=BOTH, expand=1)
    textoCurso1ESMAD.insert(END,'''
                \n\n\n\n\n
                Ano 1\t\t\t\t\t\tUnidade Curricular\t\t\t\t\t\t\tPeríodo\t\t\t\t\t\t\tCréditos ECTS
                \n\n\n\n\t\t\t\t\t\t'''+NomeDisciplina[0]+'''\t\t\t\t\t\t\t'''+Periodo[0]+'''\t\t\t\t\t\t\t'''+Ects[0]+'''
                \n\n\n\n\t\t\t\t\t\t'''+NomeDisciplina[1]+'''\t\t\t\t\t\t\t'''+Periodo[1]+'''\t\t\t\t\t\t\t'''+Ects[1]+'''
                \n\n\n\n\t\t\t\t\t\t'''+NomeDisciplina[2]+'''\t\t\t\t\t\t\t'''+Periodo[2]+'''\t\t\t\t\t\t\t'''+Ects[2]+'''
                \n\n\n\n\t\t\t\t\t\t'''+NomeDisciplina[3]+'''\t\t\t\t\t\t\t'''+Periodo[3]+'''\t\t\t\t\t\t\t'''+Ects[3]+'''
                \n\n\n\n\t\t\t\t\t\t'''+NomeDisciplina[4]+'''\t\t\t\t\t\t\t'''+Periodo[4]+'''\t\t\t\t\t\t\t'''+Ects[4]+'''
                \n\n\n\n\t\t\t\t\t\t'''+NomeDisciplina[5]+'''\t\t\t\t\t\t\t'''+Periodo[5]+'''\t\t\t\t\t\t\t'''+Ects[5]+'''
                \n\n\n\n\n
                \t\t\t\t\t\tUnidade Curricular\t\t\t\t\t\t\tPeríodo\t\t\t\t\t\t\tCréditos ECTS
                \n\n\n\n\t\t\t\t\t\t'''+NomeDisciplina[6]+'''\t\t\t\t\t\t\t'''+Periodo[6]+'''\t\t\t\t\t\t\t'''+Ects[6]+'''
                \n\n\n\n\t\t\t\t\t\t'''+NomeDisciplina[7]+'''\t\t\t\t\t\t\t'''+Periodo[7]+'''\t\t\t\t\t\t\t'''+Ects[7]+'''
                \n\n\n\n\t\t\t\t\t\t'''+NomeDisciplina[8]+'''\t\t\t\t\t\t\t'''+Periodo[8]+'''\t\t\t\t\t\t\t'''+Ects[8]+'''
                \n\n\n\n\t\t\t\t\t\t'''+NomeDisciplina[9]+'''\t\t\t\t\t\t\t'''+Periodo[9]+'''\t\t\t\t\t\t\t'''+Ects[9]+'''
                \n\n\n\n\t\t\t\t\t\t'''+NomeDisciplina[10]+'''\t\t\t\t\t\t\t'''+Periodo[10]+'''\t\t\t\t\t\t\t'''+Ects[10]+'''
                \n\n\n\n\t\t\t\t\t\t'''+NomeDisciplina[11]+'''\t\t\t\t\t\t\t'''+Periodo[11]+'''\t\t\t\t\t\t\t'''+Ects[11]+'''
                \n\n\n\n\n
                \t\t\t\t\t\tTotal\t\t\t\t\t\t\t\t\t\t\t\t\t\t'''+str(SomaEctsAno1)+'''\n\n\n\n'''
                +
                '''
                \n\n\n\n\n
                Ano 2\t\t\t\t\t\tUnidade Curricular\t\t\t\t\t\t\tPeríodo\t\t\t\t\t\t\tCréditos ECTS
                \n\n\n\n\t\t\t\t\t\t'''+NomeDisciplina[12]+'''\t\t\t\t\t\t\t'''+Periodo[12]+'''\t\t\t\t\t\t\t'''+Ects[12]+'''
                \n\n\n\n\t\t\t\t\t\t'''+NomeDisciplina[13]+'''\t\t\t\t\t\t\t'''+Periodo[13]+'''\t\t\t\t\t\t\t'''+Ects[13]+'''
                \n\n\n\n\t\t\t\t\t\t'''+NomeDisciplina[14]+'''\t\t\t\t\t\t\t'''+Periodo[14]+'''\t\t\t\t\t\t\t'''+Ects[14]+'''
                \n\n\n\n\t\t\t\t\t\t'''+NomeDisciplina[15]+'''\t\t\t\t\t\t\t'''+Periodo[15]+'''\t\t\t\t\t\t\t'''+Ects[15]+'''
                \n\n\n\n\t\t\t\t\t\t'''+NomeDisciplina[16]+'''\t\t\t\t\t\t\t'''+Periodo[16]+'''\t\t\t\t\t\t\t'''+Ects[16]+'''
                \n\n\n\n\t\t\t\t\t\t'''+NomeDisciplina[17]+'''\t\t\t\t\t\t\t'''+Periodo[17]+'''\t\t\t\t\t\t\t'''+Ects[17]+'''
                \n\n\n\n\n
                \t\t\t\t\t\tUnidade Curricular\t\t\t\t\t\t\tPeríodo\t\t\t\t\t\t\tCréditos ECTS
                \n\n\n\n\t\t\t\t\t\t'''+NomeDisciplina[18]+'''\t\t\t\t\t\t\t'''+Periodo[18]+'''\t\t\t\t\t\t\t'''+Ects[18]+'''
                \n\n\n\n\t\t\t\t\t\t'''+NomeDisciplina[19]+'''\t\t\t\t\t\t\t'''+Periodo[19]+'''\t\t\t\t\t\t\t'''+Ects[19]+'''
                \n\n\n\n\t\t\t\t\t\t'''+NomeDisciplina[20]+'''\t\t\t\t\t\t\t'''+Periodo[20]+'''\t\t\t\t\t\t\t'''+Ects[20]+'''
                \n\n\n\n\t\t\t\t\t\t'''+NomeDisciplina[21]+'''\t\t\t\t\t\t\t'''+Periodo[21]+'''\t\t\t\t\t\t\t'''+Ects[21]+'''
                \n\n\n\n\t\t\t\t\t\t'''+NomeDisciplina[22]+'''\t\t\t\t\t\t\t'''+Periodo[22]+'''\t\t\t\t\t\t\t'''+Ects[22]+'''
                \n\n\n\n\t\t\t\t\t\t'''+NomeDisciplina[23]+'''\t\t\t\t\t\t\t'''+Periodo[23]+'''\t\t\t\t\t\t\t'''+Ects[23]+'''
                \n\n\n\n\n
                \t\t\t\t\t\tTotal\t\t\t\t\t\t\t\t\t\t\t\t\t\t'''+str(SomaEctsAno2)+'''\n\n\n\n'''
                +'''
                \n\n\n\n\n
                Ano 3\t\t\t\t\t\tUnidade Curricular\t\t\t\t\t\t\tPeríodo\t\t\t\t\t\t\tCréditos ECTS
                \n\n\n\n\t\t\t\t\t\t'''+NomeDisciplina[24]+'''\t\t\t\t\t\t\t'''+Periodo[24]+'''\t\t\t\t\t\t\t'''+Ects[24]+'''
                \n\n\n\n\t\t\t\t\t\t'''+NomeDisciplina[25]+'''\t\t\t\t\t\t\t'''+Periodo[25]+'''\t\t\t\t\t\t\t'''+Ects[26]+'''
                \n\n\n\n\t\t\t\t\t\t'''+NomeDisciplina[26]+'''\t\t\t\t\t\t\t'''+Periodo[26]+'''\t\t\t\t\t\t\t'''+Ects[26]+'''
                \n\n\n\n\t\t\t\t\t\t'''+NomeDisciplina[27]+'''\t\t\t\t\t\t\t'''+Periodo[27]+'''\t\t\t\t\t\t\t'''+Ects[27]+'''
                \n\n\n\n\t\t\t\t\t\t'''+NomeDisciplina[28]+'''\t\t\t\t\t\t\t'''+Periodo[28]+'''\t\t\t\t\t\t\t'''+Ects[28]+'''
                \n\n\n\n\t\t\t\t\t\t'''+NomeDisciplina[29]+'''\t\t\t\t\t\t\t'''+Periodo[29]+'''\t\t\t\t\t\t\t'''+Ects[29]+'''
                \n\n\n\n\n
                \t\t\t\t\t\tUnidade Curricular\t\t\t\t\t\t\tPeríodo\t\t\t\t\t\t\tCréditos ECTS
                \n\n\n\n\t\t\t\t\t\t'''+NomeDisciplina[30]+'''\t\t\t\t\t\t\t'''+Periodo[30]+'''\t\t\t\t\t\t\t'''+Ects[30]+'''
                \n\n\n\n\t\t\t\t\t\t'''+NomeDisciplina[31]+'''\t\t\t\t\t\t\t'''+Periodo[31]+'''\t\t\t\t\t\t\t'''+Ects[31]+'''
                \n\n\n\n\t\t\t\t\t\t'''+NomeDisciplina[32]+'''\t\t\t\t\t\t\t'''+Periodo[32]+'''\t\t\t\t\t\t\t'''+Ects[32]+'''
                \n\n\n\n\t\t\t\t\t\t'''+NomeDisciplina[33]+'''\t\t\t\t\t\t\t'''+Periodo[33]+'''\t\t\t\t\t\t\t'''+Ects[33]+'''
                \n\n\n\n\t\t\t\t\t\t'''+NomeDisciplina[34]+'''\t\t\t\t\t\t\t'''+Periodo[34]+'''\t\t\t\t\t\t\t'''+Ects[34]+'''
                \n\n\n\n\t\t\t\t\t\t'''+NomeDisciplina[35]+'''\t\t\t\t\t\t\t'''+Periodo[35]+'''\t\t\t\t\t\t\t'''+Ects[35]+'''
                \n\n\n\n\n
                \t\t\t\t\t\tTotal\t\t\t\t\t\t\t\t\t\t\t\t\t\t'''+str(SomaEctsAno3)+'''\n\n\n\n''')  

    curso=[]
    User=[]
    text=[]
    
    textoCurso1ESMAD.insert(END,'''\n\t\t\t--Comentarios--\n\n\t\t\t''')
    

    file = open("Comments.txt","r",encoding="Utf-8")
    
    for l in file:
        Comentario=l.split(";")
        print(Comentario[0])
        print(content_list[0])
        if Comentario[0] == content_list[0]:
            print(Comentario[0])
            print(content_list[0])
            textoCurso1ESMAD.insert(END,'''\n\n\t\t\tComentario de '''+Comentario[1]+'''\n\n\t\t\t'''+Comentario[2])
            
    file.close()
    

    frameComentarios2UA = Frame(my_canvas,width=1080,height=5,relief = "sunken")
    frameComentarios2UA.pack(side = BOTTOM)
    frameComentarios2UA.config(background='white') 
    
    comentarios = Text(frameComentarios2UA,wrap = NONE, height=3)
    comentarios.pack()
    Sendbutton = Button(frameComentarios2UA, text="EnviarComentario" )
    Sendbutton.pack()

    root.mainloop()


  ############################################################################################################

    
    

def callback(name):
    #For files in Subdirectory return list of files with the names of the courses .txt
    UniPage(name,1)
    print(name)
    

totalDir = 0
paginaBlah = Tk()
paginaBlah.geometry("1920x1080")
screen_width = paginaBlah.winfo_screenwidth()
screen_height = paginaBlah.winfo_screenheight()
Focus = LabelFrame(paginaBlah, text='' , width= screen_width-200 , height = screen_height-200  , bg = '#fff' ,  borderwidth= 0, highlightcolor='#f43', highlightthickness= 0)
Focus.place(x = 200 , y = 120 )

SideNav = LabelFrame(paginaBlah, text='' , width= 200 , height = screen_height-200  , bg = '#023' ,  borderwidth= 0, highlightcolor='#f43', highlightthickness= 0)
SideNav.place(x = 0 , y = 120 )
Navbar = LabelFrame(paginaBlah, text='' , width= screen_width , height = 130  , bg='#f23',  borderwidth= 0 ,highlightcolor='#f23', highlightthickness= 0  )
Navbar.place(x = 0 , y= 0)
paginaBlah.wm_attributes('-transparentcolor','grey')

pageUni = r"infoCursos"
for base, dirs, files in os.walk(pageUni):
    for directories in dirs:
        totalDir += 1
        naoSei = dirs[totalDir-1]
        Faculdades = Button(text = naoSei, relief = "flat",font = 20,command = lambda naoSei=naoSei: callback(naoSei))
        Faculdades.pack(SideNav, fill=BOTH , expand=1 , anchor = W , pady = 50, padx=70)
        print(dirs[totalDir-1])

#ASSIGNS THE NAME OF THE UNI
paginaBlah.mainloop()