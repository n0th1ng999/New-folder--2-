from ast import arg
from cgitb import grey, text
from distutils import command
import re
from textwrap import fill, wrap
from tkinter import *
from tkinter.simpledialog import SimpleDialog
from turtle import bgcolor, title
from PIL import ImageTk,Image
from tkinter import ttk





ESMAD = Tk()
ESMAD.geometry("1920x1080")   
ESMAD.state("zoomed")
canvas = Canvas(ESMAD, width = 1600, height = 1600)  
canvas.pack()  
img = ImageTk.PhotoImage(Image.open(r"imagens//ESMAD//PROJ_ESMAD_LOGO.png")) 
canvas.create_image(480,20, anchor=NW, image=img)
    

def paginaFaculdadesESMAD():
        cursoESMAD.withdraw()

def paginaFaculdades2ESMAD():
        curso2ESMAD.withdraw()
        
class ScrollBar:
    #ISTO TEM QUE SER MUDADO!!!!!!!!!!!!!!!!!!!
    def paginaCurso(NomeUni,NomeCurso):
        global cursoESMAD

        #isto tem que ser mudado consoante o botao que é pressionado
        f = open("InfoCursos\\"+NomeUni+"\\"+NomeCurso+".txt","r", encoding='utf-8')
        Textos=[]
        for l in f:
            Textos.append(l)
        f.close()
        
        

        cursoESMAD = Tk()
        cursoESMAD.geometry("1980x2000") 
        cursoESMAD.state("zoomed")
        frameCursoESMAD = Frame(cursoESMAD,width = 400,height = 100,relief = "sunken")
        frameCursoESMAD.pack(side = TOP)
        espaço = Label(cursoESMAD,text = "")
        espaço.pack()
        espaço = Label(cursoESMAD,text = "")
        espaço.pack()
        comentarioLabel = Label(cursoESMAD,text = "Comentarios",font = "200")
        comentarioLabel.pack()
        espaço = Label(cursoESMAD,text = "")
        espaço.pack()
        frameComentariosESMAD = Frame(cursoESMAD,width=400,height=5,relief = "sunken")
        frameComentariosESMAD.pack(side = BOTTOM)
        v = Scrollbar(frameCursoESMAD)
        v.pack(side = RIGHT,fill = Y)
        comentarios = Text(frameComentariosESMAD,width = 100, height = 20,wrap = NONE)
        comentarios.insert(END,"dfugdsgdsugfi")
        comentarios.pack()
        textoCurso1ESMAD = Text(frameCursoESMAD, width = 200,height = 35,wrap = NONE,relief = FLAT, font = "200",yscrollcommand = v.set)
        textoCurso1ESMAD.insert(END,'''\n\n\n\n\n
                    Ano 1\n\n\t\t\t\t\t\tUnidade Curricular\t\t\t\t\t\t\tPeríodo\t\t\t\t\t\t\tCréditos ECTS\n\n\n\n\t\t\t\t\t\tAlgoritmia e Estruturas de Dados\t\t\t\t\t\t\t1º Semestre\t\t\t\t\t\t\t7\n\n\n\n\t\t\t\t\t\tFundamentos de Design\t\t\t\t\t\t\t1º Semestre\t\t\t\t\t\t\t6\n\n\n\n\t\t\t\t\t\tMatemática I\t\t\t\t\t\t\t1º Semestre\t\t\t\t\t\t\t5\n\n\n\n\t\t\t\t\t\tSistemas Computacionais\t\t\t\t\t\t\t1º Semestre\t\t\t\t\t\t\t5\n\n\n\n\t\t\t\t\t\tTecnologias Web\t\t\t\t\t\t\t1º Semestre\t\t\t\t\t\t\t7'''+'''\n\n\n\n
                         \n\n\t\t\t\t\t\tUnidade Curricular\t\t\t\t\t\t\tPeríodo\t\t\t\t\t\t\tCréditos ECTS\n\n\n\n\t\t\t\t\t\tConceção e Produção Multimédia\t\t\t\t\t\t\t2º Semestre\t\t\t\t\t\t\t5\n\n\n\n\t\t\t\t\t\tInterfaces e Design para Aplicações\t\t\t\t\t\t\t2º Semestre\t\t\t\t\t\t\t6\n\n\n\n\t\t\t\t\t\tMatemática II\t\t\t\t\t\t\t2º Semestre\t\t\t\t\t\t\t5\n\n\n\n\t\t\t\t\t\tProgramação Orientada a Objetos\t\t\t\t\t\t\t2º Semestre\t\t\t\t\t\t\t7\n\n\n\n\t\t\t\t\t\tProjeto I\t\t\t\t\t\t\t2º Semestre\t\t\t\t\t\t\t7\n\n\n\n
        \t\t\t\t\t\tTotal\t\t\t\t\t\t\t\t\t\t\t\t\t\t60\n\n\n\n
                    Ano 2\n\n\t\t\t\t\t\tUnidade Curricular\t\t\t\t\t\t\tPeríodo\t\t\t\t\t\t\tCréditos ECTS\n\n\n\n\t\t\t\t\t\tBases de Dados\t\t\t\t\t\t\t1º Semestre\t\t\t\t\t\t\t5\n\n\n\n\t\t\t\t\t\tComputação Gráfica\t\t\t\t\t\t\t1º Semestre\t\t\t\t\t\t\t7\n\n\n\n\t\t\t\t\t\tEngenharia de Software\t\t\t\t\t\t\t1º Semestre\t\t\t\t\t\t\t6\n\n\n\n\t\t\t\t\t\tErgonomia Cognitiva e Design de Interação\t\t\t\t\t\t\t1º Semestre\t\t\t\t\t\t\t5\n\n\n\n\t\t\t\t\t\tProgramação Web I\t\t\t\t\t\t\t1º Semestre\t\t\t\t\t\t\t7\n\n\n\n
                         \n\n\t\t\t\t\t\tUnidade Curricular\t\t\t\t\t\t\tPeríodo\t\t\t\t\t\t\tCréditos ECTS\n\n\n\n\t\t\t\t\t\tInteligência Artificial\t\t\t\t\t\t\t2º Semestre\t\t\t\t\t\t\t6\n\n\n\t\t\t\t\t\tProgramação Web II\t\t\t\t\t\t\t2º Semestre\t\t\t\t\t\t\t7\n\n\n\n\t\t\t\t\t\tProjeto II\t\t\t\t\t\t\t2º Semestre\t\t\t\t\t\t\t6\n\n\n\n\t\t\t\t\t\tTestes e Performance Web\t\t\t\t\t\t\t2º Semestre\t\t\t\t\t\t\t6\n\n\n\n\t\t\t\t\t\tVídeo I\t\t\t\t\t\t\t2º Semestre\t\t\t\t\t\t\t5\n\n\n\n
        \t\t\t\t\t\tTotal\t\t\t\t\t\t\t\t\t\t\t\t\t\t60\n\n\n\n            
                    Ano 3\n\n\t\t\t\t\t\tUnidade Curricular\t\t\t\t\t\t\tPeríodo\t\t\t\t\t\t\tCréditos ECTS\n\n\n\n\t\t\t\t\t\tComputação Móvel e Ubíqua\t\t\t\t\t\t\t1º Semestre\t\t\t\t\t\t\t6\n\n\n\t\t\t\t\t\tInovação e Empreendedorismo\t\t\t\t\t\t\t1º Semestre\t\t\t\t\t\t\t5\n\n\n\n\t\t\t\t\t\tNegócio Eletrónico e Segurança\t\t\t\t\t\t\t1º Semestre\t\t\t\t\t\t\t6\n\n\n\n\t\t\t\t\t\tPrototipagem Avançada em Plataformas Digitais\t\t\t\t\t\t\t1º Semestre\t\t\t\t\t\t\t6\n\n\n\n\t\t\t\t\t\tServiços e Interfaces para a Cloud\t\t\t\t\t\t\t1º Semestre\t\t\t\t\t\t\t7\n\n\n\n
                         \n\n\t\t\t\t\t\tUnidade Curricular\t\t\t\t\t\t\tPeríodo\t\t\t\t\t\t\tCréditos ECTS\n\n\n\n\t\t\t\t\t\tMarketing Digital\t\t\t\t\t\t\t2º Semestre\t\t\t\t\t\t\t3\n\n\n\n\t\t\t\t\t\tProjeto Final/Estágio\t\t\t\t\t\t\t2º Semestre\t\t\t\t\t\t\t23\n\n\n\n\t\t\t\t\t\tUsabilidade e User Experience\t\t\t\t\t\t\t2º Semestre\t\t\t\t\t\t\t4\n\n\n\n\t\t\t\t\t\t
        \t\t\t\t\t\tTotal\t\t\t\t\t\t\t\t\t\t\t\t\t\t60\n\n\n\n''')
        textoCurso1ESMAD.pack(side = TOP,fill = X)
        v.config(command=textoCurso1ESMAD.yview)
        voltarAtras1 = Button(textoCurso1ESMAD,text = "Voltar atrás",font = 20, command = paginaFaculdadesESMAD)
        voltarAtras1.place(x=20,y=20)

       


        textoCurso1ESMAD.config(state = DISABLED)
        
    

    def paginaCurso2ESMAD():
        global curso2ESMAD
        curso2ESMAD = Tk()
        curso2ESMAD.geometry("1980x1600")
        curso2ESMAD.state("zoomed")
        frameCurso2ESMAD = Frame(curso2ESMAD,width = 400,height = 100,relief = "sunken")
        frameCurso2ESMAD.pack(side = TOP)
        espaço = Label(curso2ESMAD,text = "")
        espaço.pack()
        espaço = Label(curso2ESMAD,text = "")
        espaço.pack()
        comentarioLabel = Label(curso2ESMAD,text = "Comentarios",font = "200")
        comentarioLabel.pack()
        espaço = Label(curso2ESMAD,text = "")
        espaço.pack()

        frameComentarios2ESMAD = Frame(curso2ESMAD,width=400,height=5,relief = "sunken")
        frameComentarios2ESMAD.pack(side = BOTTOM)
        v = Scrollbar(frameCurso2ESMAD)
        v.pack(side = RIGHT,fill = Y)
        comentarios = Text(frameComentarios2ESMAD,width = 100, height = 20,wrap = NONE)
        comentarios.insert(END,"dfugdsgdsugfi")
        comentarios.pack()
        
        texoCurso2ESMAD = Text(frameCurso2ESMAD, width = 200, height = 35,relief = FLAT,font = "200",yscrollcommand = v.set)
        texoCurso2ESMAD.insert(END,'''\n\n\n\n\n
                    Ano 1\n\n\t\t\t\t\t\tUnidade Curricular\t\t\t\t\t\t\tPeríodo\t\t\t\t\t\t\tCréditos ECTS\n\n\n\n\t\t\t\t\t\tAnimação I\t\t\t\t\t\t\t1º Semestre\t\t\t\t\t\t\t6\n\n\n\n\t\t\t\t\t\tFotografia I\t\t\t\t\t\t\t1º Semestre\t\t\t\t\t\t\t5\n\n\n\n\t\t\t\t\t\tInformática Aplicada\t\t\t\t\t\t\t1º Semestre\t\t\t\t\t\t\t6\n\n\n\n\t\t\t\t\t\tSemiótica I\t\t\t\t\t\t\t1º Semestre\t\t\t\t\t\t\t3\n\n\n\n\t\t\t\t\t\tTecnologias Multimédia\t\t\t\t\t\t\t1º Semestre\t\t\t\t\t\t\t6\n\n\n\n\t\t\t\t\t\tTeoria da Comunicação Multimédia\t\t\t\t\t\t\t1º Semestre\t\t\t\t\t\t\t3'''+'''\n\n\n\n
                         \n\n\t\t\t\t\t\tUnidade Curricular\t\t\t\t\t\t\tPeríodo\t\t\t\t\t\t\tCréditos ECTS\n\n\n\n\t\t\t\t\t\tDesign da Comunicação I\t\t\t\t\t\t\t2º Semestre\t\t\t\t\t\t\t4\n\n\n\n\t\t\t\t\t\tLaboratório I\t\t\t\t\t\t\t2º Semestre\t\t\t\t\t\t\t7\n\n\n\n\t\t\t\t\t\tProgramação I\t\t\t\t\t\t\t2º Semestre\t\t\t\t\t\t\t7\n\n\n\n\t\t\t\t\t\tSemiótica II\t\t\t\t\t\t\t2º Semestre\t\t\t\t\t\t\t3\n\n\n\n\t\t\t\t\t\tSom I\t\t\t\t\t\t\t2º Semestre\t\t\t\t\t\t\t5\n\n\n\n\t\t\t\t\t\tVideo I\t\t\t\t\t\t\t2º Semestre\t\t\t\t\t\t\t5\n\n\n\n
        \t\t\t\t\t\tTotal\t\t\t\t\t\t\t\t\t\t\t\t\t\t60\n\n\n\n
                    Ano 2\n\n\t\t\t\t\t\tUnidade Curricular\t\t\t\t\t\t\tPeríodo\t\t\t\t\t\t\tCréditos ECTS\n\n\n\n\t\t\t\t\t\tCultura Digital\t\t\t\t\t\t\t1º Semestre\t\t\t\t\t\t\t3\n\n\n\n\t\t\t\t\t\tDesign da Comunicação II\t\t\t\t\t\t\t1º Semestre\t\t\t\t\t\t\t4\n\n\n\n\t\t\t\t\t\tDesign de Interfaces\t\t\t\t\t\t\t1º Semestre\t\t\t\t\t\t\t4\n\n\n\n\t\t\t\t\t\tFotografia II\t\t\t\t\t\t\t1º Semestre\t\t\t\t\t\t\t5\n\n\n\n\t\t\t\t\t\tProgramação II\t\t\t\t\t\t\t1º Semestre\t\t\t\t\t\t\t6\n\n\n\n\t\t\t\t\t\tSom II\t\t\t\t\t\t\t1º Semestre\t\t\t\t\t\t\t5\n\n\n\n\t\t\t\t\t\tVideo II\t\t\t\t\t\t\t1º Semestre\t\t\t\t\t\t\t5\n\n\n\n
                         \n\n\t\t\t\t\t\tUnidade Curricular\t\t\t\t\t\t\tPeríodo\t\t\t\t\t\t\tCréditos ECTS\n\n\n\n\t\t\t\t\t\tAnimação II\t\t\t\t\t\t\t2º Semestre\t\t\t\t\t\t\t6\n\n\n\t\t\t\t\t\tArte e Cultura Contemporânea\t\t\t\t\t\t\t2º Semestre\t\t\t\t\t\t\t3\n\n\n\n\t\t\t\t\t\tLaboratório II\t\t\t\t\t\t\t2º Semestre\t\t\t\t\t\t\t7\n\n\n\n\t\t\t\t\t\tMultimédia I\t\t\t\t\t\t\t2º Semestre\t\t\t\t\t\t\t6\n\n\n\n\t\t\t\t\t\tProgramação III\t\t\t\t\t\t\t2º Semestre\t\t\t\t\t\t\t6\n\n\n\n
        \t\t\t\t\t\tTotal\t\t\t\t\t\t\t\t\t\t\t\t\t\t60\n\n\n\n            
                    Ano 3\n\n\t\t\t\t\t\tUnidade Curricular\t\t\t\t\t\t\tPeríodo\t\t\t\t\t\t\tCréditos ECTS\n\n\n\n\t\t\t\t\t\tAnimação III\t\t\t\t\t\t\t1º Semestre\t\t\t\t\t\t\t8\n\n\n\t\t\t\t\t\tLaboratório III\t\t\t\t\t\t\t1º Semestre\t\t\t\t\t\t\t9\n\n\n\n\t\t\t\t\t\tMultimédia II\t\t\t\t\t\t\t1º Semestre\t\t\t\t\t\t\t9\n\n\n\n\t\t\t\t\t\tPós-Produção\t\t\t\t\t\t\t1º Semestre\t\t\t\t\t\t\t8\n\n\n\n
                         \n\n\t\t\t\t\t\tUnidade Curricular\t\t\t\t\t\t\tPeríodo\t\t\t\t\t\t\tCréditos ECTS\n\n\n\n\t\t\t\t\t\tLegislação e Autoria\t\t\t\t\t\t\t2º Semestre\t\t\t\t\t\t\t2\n\n\n\n\t\t\t\t\t\tMarketing e Gestão de Projectos\t\t\t\t\t\t\t2º Semestre\t\t\t\t\t\t\t2\n\n\n\n\t\t\t\t\t\tProjecto\t\t\t\t\t\t\t2º Semestre\t\t\t\t\t\t\t20\n\n\n\n\t\t\t\t\t\tSeminário\t\t\t\t\t\t\t2º Semestre\t\t\t\t\t\t\t2\n\n\n\n\t\t\t\t\t\t
        \t\t\t\t\t\tTotal\t\t\t\t\t\t\t\t\t\t\t\t\t\t60\n\n\n\n''')

        texoCurso2ESMAD.pack()
        v.config(command= texoCurso2ESMAD.yview)
        voltarAtras2 = Button(texoCurso2ESMAD, text = "Voltar atrás", font = (20), command = paginaFaculdades2ESMAD)
        voltarAtras2.place(x=20, y= 20)
        texoCurso2ESMAD.config(state = DISABLED)
        
        
        Comment = Frame(curso2ESMAD, width = 1980, height = 300,text="ola")
        Comment.pack(side = TOP,fill = X)
        

#for 
    cursoESMAD = Button(text = "Licenciatura em Tecnologias e Sistemas de Informação Para a Web", relief = "flat" ,font="Helvetica 20 underline", command = paginaCurso("ESMAD","1")  )
    cursoESMAD.place(x= 20,y= 500)
    msgCurso1ESMAD = Message(ESMAD,text = '''A licenciatura assenta numa visão contemporânea e multidisciplinar da Web, agregando competências focadas na conceção, design e desenvolvimento de produtos e software para a Web. Procura dotar os estudantes de conhecimento e competências práticas que lhes permitam o domínio de áreas emergentes como os serviços centrados na cloud, a computação móvel e ubíqua, ou plataformas Web e de negócio eletrónico, sem descurar competências hoje em dia fundamentais, como ergonomia e design de interação, usabilidade e user experience ou prototipagem de plataformas digitais.
Esta característica de aliar competências relacionadas com o desenvolvimento de produtos a conceitos emergentes relacionados com o design de interfaces (user interface & user experience) é uma característica distintiva desta licenciatura e um dos motivos do seu grande sucesso!
Esta é ainda uma área de atuação onde a empregabilidade está próxima do pleno emprego. De acordo com estudo realizado em 2019 junto dos diplomados desta licenciatura, a taxa de desemprego foi de 0%, isto é, verificou-se uma situação de pleno emprego!
O curso privilegia ainda uma vertente eminentemente prática, como o demonstram os projetos incluídos no seu plano de estudos desde o 1.º ano, assim como uma forte ligação ao meio empresarial. Prova disso é o alargado leque de parceiros tecnológicos do curso, como a IOTech, ikuTeam, Helppier, Xing, Zalox, Ground Contro Studios, e-Goi, Nonius Software, BindTuning, FMQ, Increase Time, Interactive Brand, InovaMais, TechPitch, Blip, GoWeb, Planeta Virtual, INESC_TEC, Samsys, MGS, Celfocus, touchIT, MOG Technologies, entre outras.
''',width = 1500)
    msgCurso1ESMAD.place(x=20,y=550) 
    


    curso2ESMAD = Button(text = "Licenciatura em Multimédia", relief = "flat",font="Helvetica 20 underline", command = paginaCurso2ESMAD )
    curso2ESMAD.place(x = 20, y = 660)
    msgcurso2 = Message(ESMAD,text = '''A Licenciatura em Multimédia assenta numa visão contemporânea e interdisciplinar. Fundindo várias áreas numa interseção que incluí arte, tecnologia, comunicação e cultura, bem como a música, o teatro, o cinema e o audiovisual, numa plataforma de comunicação diferenciadora e inovadora, capaz de produzir, veicular e transmitir conteúdos a partir de diferentes aplicações, plataformas e suportes. Orienta-se numa dimensão artística, criativa e de inovação tecnológica e persegue uma filosofia de conhecimento transversal, promovida pelas várias disciplinas que compõem o curso.
''',width = 1500)
    msgcurso2.place(x = 20, y = 710)




    
s = ScrollBar()


   



        




ESMAD.mainloop()
s = ScrollBar()