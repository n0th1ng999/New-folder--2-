from ast import arg
from cgitb import text
from distutils import command
from textwrap import fill, wrap
from tkinter import *
from tkinter.simpledialog import SimpleDialog
from turtle import title
from PIL import ImageTk,Image
from tkinter import ttk





ESMAD = Tk()
ESMAD.geometry("1920x1080")   
ESMAD.state("zoomed")
canvas = Canvas(ESMAD, width = 1600, height = 1600)  
canvas.pack()  
img = ImageTk.PhotoImage(Image.open(r"imagens//ESMAD//PROJ_ESMAD_LOGO.png")) 
canvas.create_image(250,20, anchor=NW, image=img)
    

def paginaFaculdadesESMAD():
        cursoESMAD.withdraw()

def paginaFaculdades2ESMAD():
        curso2ESMAD.withdraw()
        
class ScrollBar:
    #ISTO TEM QUE SER MUDADO!!!!!!!!!!!!!!!!!!!
    def paginaCurso(NomeUni,NomeCurso):
        global cursoESMAD


        f = open("InfoCursos\\"+NomeUni+"\\"+NomeCurso+".txt","r", encoding='utf-8')
        Textos=[]
        for l in f:
            a = l
            Textos.append(a)
        f.close()

        

        cursoESMAD = Tk()
        cursoESMAD.geometry("1980x1600") 
        cursoESMAD.state("zoomed")
        v = Scrollbar(cursoESMAD)
        v.pack(side = RIGHT,fill = Y)
        textoCurso1ESMAD = Text(cursoESMAD, width = 1980,height = 1600,wrap = NONE,relief = FLAT, font = "200",yscrollcommand = v.set)
        textoCurso1ESMAD.insert(END,'''\n\n\n\n\n
                    Ano 1\n\n\t\t\t\t\t\t
                    Unidade curricular\t\t\t\t\t\t\tPeríodo\t\t\t\t\t\t\tCréditos ECTS\n\n\n\n\t\t\t\t\t\t
                    Algoritmia e Estruturas de Dados\t\t\t\t\t\t\t1º Semestre\t\t\t\t\t\t\t7\n\n\n\n\t\t\t\t\t\t
                    Fundamentos de Design\t\t\t\t\t\t\t1º Semestre\t\t\t\t\t\t\t6\n\n\n\n\t\t\t\t\t\t
                    Matemática I\t\t\t\t\t\t\t1º Semestre\t\t\t\t\t\t\t5\n\n\n\n\t\t\t\t\t\t
                    Sistemas Computacionais\t\t\t\t\t\t\t1º Semestre\t\t\t\t\t\t\t  5   \n\n\n\n\t\t\t\t\t\t
                    Tecnologias Web\t\t\t\t\t\t\t1º Semestre\t\t\t\t\t\t\t7'''+
                    '''\n\n\n\n
                        \n\n\t\t\t\t\t\tUnidade curricular\t\t\t\t\t\t\tPeríodo\t\t\t\t\t\t\tCréditos ECTS\n\n\n\n\t\t\t\t\t\t
                        Conceção e Produção Multimédia\t\t\t\t\t\t\t2º Semestre\t\t\t\t\t\t\t5\n\n\n\n\t\t\t\t\t\t
                        Interfaces e Design para Aplicações\t\t\t\t\t\t\t2º Semestre\t\t\t\t\t\t\t6\n\n\n\n\t\t\t\t\t\t
                        Matemática II\t\t\t\t\t\t\t2º Semestre\t\t\t\t\t\t\t5\n\n\n\n\t\t\t\t\t\t
                        Programação Orientada a Objetos\t\t\t\t\t\t\t2º Semestre\t\t\t\t\t\t\t7\n\n\n\n\t\t\t\t\t\t
                        Projeto I\t\t\t\t\t\t\t2º Semestre\t\t\t\t\t\t\t7\n\n\n\n
        \t\t\t\t\t\tTotal\t\t\t\t\t\t\t\t\t\t\t\t\t\t60\n\n\n\n
                    Ano 2\n\n\t\t\t\t\t\tUnidade curricular\t\t\t\t\t\t\tPeríodo\t\t\t\t\t\t\tCréditos ECTS\n\n\n\n\t\t\t\t\t\t
                    Bases de Dados\t\t\t\t\t\t\t1º Semestre\t\t\t\t\t\t\t5\n\n\n\n\t\t\t\t\t\t
                    Computação Gráfica\t\t\t\t\t\t\t1º Semestre\t\t\t\t\t\t\t7\n\n\n\n\t\t\t\t\t\t
                    Engenharia de Software\t\t\t\t\t\t\t1º Semestre\t\t\t\t\t\t\t6\n\n\n\n\t\t\t\t\t\t
                    Ergonomia Cognitiva e Design de Interação\t\t\t\t\t0\t\t1º Semestre\t\t\t\t\t\t\t5\n\n\n\n\t\t\t\t\t\t
                    Programação Web I\t\t\t\t\t\t\t1º Semestre\t\t\t\t\t\t\t7\n\n\n\n
                        \n\n\t\t\t\t\t\tUnidade curricular\t\t\t\t\t\t\tPeríodo\t\t\t\t\t\t\tCréditos ECTS\n\n\n\n\t\t\t\t\t\t
                        Inteligência Artificial\t\t\t\t\t\t\t2º Semestre\t\t\t\t\t\t\t6\n\n\n\t\t\t\t\t\t
                        Programação Web II\t\t\t\t\t\t\t2º Semestre\t\t\t\t\t\t\t6\n\n\n\n\t\t\t\t\t\t
                        Projeto II\t\t\t\t\t\t\t2º Semestre\t\t\t\t\t\t\t6\n\n\n\n\t\t\t\t\t\t
                        Testes e Performance Web\t\t\t\t\t\t\t2º Semestre\t\t\t\t\t\t\t6\n\n\n\n\t\t\t\t\t\t
                        Análise de Filmes (opcional)\t\t\t\t\t\t\t2º Semestre\t\t\t\t\t\t\t6\n\n\n\n
        \t\t\t\t\t\tTotal\t\t\t\t\t\t\t\t\t\t\t\t\t\t60\n\n\n\n            
                    Ano 3\n\n\t\t\t\t\t\tUnidade curricular\t\t\t\t\t\t\tPeríodo\t\t\t\t\t\t\tCréditos ECTS\n\n\n\n\t\t\t\t\t\t
                    Avaliação Psicológica I\t\t\t\t\t\t\t1º Semestre\t\t\t\t\t\t\t6\n\n\n\t\t\t\t\t\t
                    Contextos de Aplicação em Psicologia I\t\t\t\t\t\t\tPSIC\t\t\t\t\t\t\t6\n\n\n\n\t\t\t\t\t\t
                    Prática de Investigação I\t\t\t\t\t\t\t1º Semestre\t\t\t\t\t\t\t6\n\n\n\n\t\t\t\t\t\t
                    Psicopatologia I: Criança e Adolescente\t\t\t\t\t\t\t1º Semestre\t\t\t\t\t\t\t6\n\n\n\n\t\t\t\t\t\t
                    Raciocínio e Tomada de Decisão\t\t\t\t\t\t\t1º Semestre\t\t\t\t\t\t\t6\n\n\n\n
                         \n\n\t\t\t\t\t\tUnidade curricular\t\t\t\t\t\t\tPeríodo\t\t\t\t\t\t\tCréditos ECTS\n\n\n\n\t\t\t\t\t\t
                         Avaliação Psicológica II\t\t\t\t\t\t\t2º Semestre\t\t\t\t\t\t\t6\n\n\n\n\t\t\t\t\t\t
                         Contextos de Aplicação em Psicologia II\t\t\t\t\t\t\t
                         PSIC\t\t\t\t\t\t\t6\n\n\n\n\t\t\t\t\t\t
                         Prática de Investigação II\t\t\t\t\t\t\t2º Semestre\t\t\t\t\t\t\t6\n\n\n\n\t\t\t\t\t\t
                         Psicopatologia II: Adulto e Idoso\t\t\t\t\t\t\t2º Semestre\t\t\t\t\t\t\t6\n\n\n\n\t\t\t\t\t\t
                         Opção\n\n\n\n\t\t\t\t\t\t\t
                         ·Introdução à Cronopsicologia\t\t\t\t\t\t2º Semestre\t\t\t\t\t\t\t6\n\n\n\n\t\t\t\t\t\t\t
                         ·Modificação do Comportamento\t\t\t\t\t\tPSIC\t\t\t\t\t\t\t6\n\n\n\n\t\t\t\t\t\t\t
                         ·Psicologia da Família e Redes Sociais\t\t\t\t\t\tPSIC\t\t\t\t\t\t\t6\n\n\n\n\t\t\t\t\t\t\t
                         ·Psicologia do Bem-estar Pessoal\t\t\t\t\t\tPSIC\t\t\t\t\t\t\t6\n\n\n\n\t\t\t\t\t\t\t
                         ·Psiconeuroimunologia\t\t\t\t\t\tPSIC\t\t\t\t\t\t\t6\n\n\n\n
        \t\t\t\t\t\tTotal\t\t\t\t\t\t\t\t\t\t\t\t\t\t60\n\n\n\n
                LEGENDA:\n\t\tCTS = Ciências e Tecnologias da saúde\n\t\tPSIC = Psicologia\n\t\tM = Matemática\n\t\tB = Biologia''')
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
        v = Scrollbar(curso2ESMAD)
        v.pack(side = RIGHT,fill = Y)
        texoCurso2ESMAD = Text(curso2ESMAD, width = 1980, height = 1600,wrap = NONE,relief = FLAT,font = "200",yscrollcommand = v.set)
        texoCurso2ESMAD.insert(END,'''\n\n\n\n\n
                    Ano 1\n\n\t\t\t\t\t\tUnidade curricular\t\t\t\t\t\t\tPeríodo\t\t\t\t\t\t\tCréditos ECTS\n\n\n\n\t\t\t\t\t\tEconomia I\t\t\t\t\t\t\tE\t\t\t\t\t\t\t6\n\n\n\n\t\t\t\t\t\tGestão de Empresas\t\t\t\t\t\t\tGES\t\t\t\t\t\t\t6\n\n\n\n\t\t\t\t\t\tCálculo I\t\t\t\t\t\t\tM\t\t\t\t\t\t\t6\n\n\n\n\t\t\t\t\t\tGestão da Informação\t\t\t\t\t\t\tGES\t\t\t\t\t\t\t6\n\n\n\n\t\t\t\t\t\tDireito das Empresas I\t\t\t\t\t\t\tCJ\t\t\t\t\t\t\t6\n\n\n\n
                         \n\n\t\t\t\t\t\tUnidade curricular\t\t\t\t\t\t\tPeríodo\t\t\t\t\t\t\tCréditos ECTS\n\n\n\n\t\t\t\t\t\tEconomia II\t\t\t\t\t\t\tE\t\t\t\t\t\t\t6\n\n\n\n\t\t\t\t\t\tComportamento Organizacional\t\t\t\t\t\t\tGES\t\t\t\t\t\t\t6\n\n\n\n\t\t\t\t\t\tCálculo II\t\t\t\t\t\t\tM\t\t\t\t\t\t\t6\n\n\n\n\t\t\t\t\t\tTeoria da Contabilidade\t\t\t\t\t\t\tC\t\t\t\t\t\t\t6\n\n\n\n\t\t\t\t\t\tTeoria das Organizações\t\t\t\t\t\t\tGES\t\t\t\t\t\t\t6\n\n\n\n
        \t\t\t\t\t\tTotal\t\t\t\t\t\t\t\t\t\t\t\t\t\t60\n\n\n\n
                    Ano 2\n\n\t\t\t\t\t\tUnidade curricular\t\t\t\t\t\t\tPeríodo\t\t\t\t\t\t\tCréditos ECTS\n\n\n\n\t\t\t\t\t\tContabilidade e Informação Financeira\t\t\t\t\t\t\tC\t\t\t\t\t\t\t6\n\n\n\n\t\t\t\t\t\tGestão de Recursos Humanos\t\t\t\t\t\t\tGES\t\t\t\t\t\t\t6\n\n\n\n\t\t\t\t\t\tIntrodução Ao Marketing\t\t\t\t\t\t\tGES\t\t\t\t\t\t\t6\n\n\n\n\t\t\t\t\t\tDireito de Empresas II\t\t\t\t\t\t\tCJ\t\t\t\t\t\t\t6Gestão Financeira I\t\t\t\t\t\t\tGES\t\t\t\t\t\t\t6\n\n\n\n
                         \n\n\t\t\t\t\t\tUnidade curricular\t\t\t\t\t\t\tPeríodo\t\t\t\t\t\t\tCréditos ECTS\n\n\n\n\t\t\t\t\t\tInvestigação Operacional\t\t\t\t\t\t\tEGI\t\t\t\t\t\t\t6\n\n\n\n\t\t\t\t\t\tGestão de Marketing\t\t\t\t\t\t\tGES\t\t\t\t\t\t\t6\n\n\n\n\t\t\t\t\t\tMétodos Quantitativos em Gestão\t\t\t\t\t\t\tGES\t\t\t\t\t\t\t6\n\n\n\n\t\t\t\t\t\tContabilidade Analítica\t\t\t\t\t\t\tC\t\t\t\t\t\t\t6\n\n\n\n\t\t\t\t\t\tTecnologia e Sistemas de Informação em Gestão\t\t\t\t\t\t\tGES\t\t\t\t\t\t\t6\n\n\n\n
        \t\t\t\t\t\tTotal\t\t\t\t\t\t\t\t\t\t\t\t\t\t60\n\n\n\n
                    Ano 3\n\n\t\t\t\t\t\tUnidade curricular\t\t\t\t\t\t\tPeríodo\t\t\t\t\t\t\tCréditos ECTS\n\n\n\n\t\t\t\t\t\t
                    Gestão de Operações\t\t\t\t\t\t\t
                    EGI\t\t\t\t\t\t\t6\n\n\n\n\t\t\t\t\t\t
                    Empreendedorismo\t\t\t\t\t\t\tGES\t\t\t\t\t\t\t6\n\n\n\n\t\t\t\t\t\t
                    Gestão Integrada de Projectos\t\t\t\t\t\t\tGES\t\t\t\t\t\t\t6\n\n\n\n\t\t\t\t\t\t
                    Auditoria\t\t\t\t\t\t\tC\t\t\t\t\t\t\t6\n\n\n\n\t\t\t\t\t\t
                    Gestão Financeira II\t\t\t\t\t\t\tGES\t\t\t\t\t\t\t6\n\n\n\n
                         \n\n\t\t\t\t\t\tUnidade curricular\t\t\t\t\t\t\tPeríodo\t\t\t\t\t\t\tCréditos ECTS\n\n\n\n\t\t\t\t\t\t
                         Logística\t\t\t\t\t\t\tEGI\t\t\t\t\t\t\t6\n\n\n\n\t\t\t\t\t\tControlo de Gestão\t\t\t\t\t\t\tC\t\t\t\t\t\t\t6\n\n\n\n\t\t\t\t\t\tFiscalidade\t\t\t\t\t\t\tC\t\t\t\t\t\t\t6\n\n\n\n\t\t\t\t\t\tGestão da Qualidade\t\t\t\t\t\t\tEGI\t\t\t\t\t\t\t6\n\n\n\n\t\t\t\t\t\tOpção\n\n\n\n\t\t\t\t\t\t\t·Contabilidade Analitica Avançada\t\t\t\t\t\tC\t\t\t\t\t\t\t6\n\n\n\n\t\t\t\t\t\t\t.Gestão de Serviços\t\t\t\t\t\tGES\t\t\t\t\t\t\t6\n\n\n\n\t\t\t\t\t\t\t.Gestão Estratégica\t\t\t\t\t\tGES\t\t\t\t\t\t\t6\n\n\n\n\t\t\t\t\t\t\t.Novas Formas de Negócio\t\t\t\t\t\tGES\t\t\t\t\t\t\t6\n\n\n\n
        \t\t\t\t\t\tTotal\t\t\t\t\t\t\t\t\t\t\t\t\t\t60\n\n\n\n
                LEGENDA:\n\t\t E = Economia\n\t\tGES = Gestão\n\t\tM = Matemática\n\t\tCJ = Ciências Jurídicas\n\t\tC = Contabilidade''')

        texoCurso2ESMAD.pack(side = TOP,fill = X)
        v.config(command= texoCurso2ESMAD.yview)
        voltarAtras2 = Button(texoCurso2ESMAD, text = "Voltar atrás", font = (20), command = paginaFaculdades2ESMAD)
        voltarAtras2.place(x=20, y= 20)
        texoCurso2ESMAD.config(state = DISABLED)
        
        
        Comment = Frame(curso2ESMAD, width = 1980, height = 300,text="ola")
        Comment.pack(side = TOP,fill = X)
        

#
    cursoESMAD = Button(text = "Licenciatura em Tecnologias e Sistemas de Informação Para a Web", relief = "flat" ,font="Helvetica 20 underline", command = paginaCurso("ESMAD","1")  )
    cursoESMAD.place(x= 20,y= 500)
    msgCurso1ESMAD = Message(ESMAD,text = '''A licenciatura assenta numa visão contemporânea e multidisciplinar da Web, agregando competências focadas na conceção, design e desenvolvimento de produtos e software para a Web. Procura dotar os estudantes de conhecimento e competências práticas que lhes permitam o domínio de áreas emergentes como os serviços centrados na cloud, a computação móvel e ubíqua, ou plataformas Web e de negócio eletrónico, sem descurar competências hoje em dia fundamentais, como ergonomia e design de interação, usabilidade e user experience ou prototipagem de plataformas digitais.
Esta característica de aliar competências relacionadas com o desenvolvimento de produtos a conceitos emergentes relacionados com o design de interfaces (user interface & user experience) é uma característica distintiva desta licenciatura e um dos motivos do seu grande sucesso!
Esta é ainda uma área de atuação onde a empregabilidade está próxima do pleno emprego. De acordo com estudo realizado em 2019 junto dos diplomados desta licenciatura, a taxa de desemprego foi de 0%, isto é, verificou-se uma situação de pleno emprego!
O curso privilegia ainda uma vertente eminentemente prática, como o demonstram os projetos incluídos no seu plano de estudos desde o 1.º ano, assim como uma forte ligação ao meio empresarial. Prova disso é o alargado leque de parceiros tecnológicos do curso, como a IOTech, ikuTeam, Helppier, Xing, Zalox, Ground Contro Studios, e-Goi, Nonius Software, BindTuning, FMQ, Increase Time, Interactive Brand, InovaMais, TechPitch, Blip, GoWeb, Planeta Virtual, INESC_TEC, Samsys, MGS, Celfocus, touchIT, MOG Technologies, entre outras.
''',width = 1500)
    msgCurso1ESMAD.place(x=20,y=550) 
    


    curso2ESMAD = Button(text = "Licenciatura em Multimédia", relief = "flat",font = (20), command = paginaCurso2ESMAD )
    curso2ESMAD.place(x = 20, y = 650)
    msgcurso2 = Message(ESMAD,text = '''A Licenciatura em Multimédia assenta numa visão contemporânea e interdisciplinar. Fundindo várias áreas numa interseção que incluí arte, tecnologia, comunicação e cultura, bem como a música, o teatro, o cinema e o audiovisual, numa plataforma de comunicação diferenciadora e inovadora, capaz de produzir, veicular e transmitir conteúdos a partir de diferentes aplicações, plataformas e suportes. Orienta-se numa dimensão artística, criativa e de inovação tecnológica e persegue uma filosofia de conhecimento transversal, promovida pelas várias disciplinas que compõem o curso.
''',width = 1500)
    msgcurso2.place(x = 20, y = 680)




    
s = ScrollBar()


   



        




ESMAD.mainloop()
s = ScrollBar()