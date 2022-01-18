from cgitb import text
from tkinter import *
from turtle import title
from PIL import ImageTk,Image
from tkinter import ttk



UA = Tk()
UA.geometry("1980x1600")   
canvas = Canvas(UA, width = 1600, height = 1600)  
canvas.pack()  
img = ImageTk.PhotoImage(Image.open(r"C:\Users\Silgueira\Desktop\AED Tema B\Imagens\PROJ_UA_LOGO.png")) 
canvas.create_image(250,20, anchor=NW, image=img)

def paginaFaculdades1():
    curso1.withdraw()

def paginaFaculdades2():
    curso2.withdraw()
    

def paginaCurso1():
    global curso1

    curso1 = Tk()
    curso1.geometry("1980x1600")
    voltarAtras = Button(curso1, text = "Voltar atrás", font = (20), command = paginaFaculdades1)
    voltarAtras.place(x = 20,y = 20)
    tituloCurso1 = Message(curso1,text = "Ano 1",font= "500")
    tituloCurso1.place(x = 200,y = 50)
    tituloCurso1_1 = Message(curso1,text = "Ano 2",font= "500")
    tituloCurso1_1.place(x = 200,y = 700)
    infoCurso1 = Message(curso1, text= "1º Semestre\n\nAnatomo-fisiologia I\n\nIntrodução à Psicologia\n\nMatemáticas Gerais I\n\nMetodologia de Investigação em Psicologia\n\nGenética e Evolução\n\n\n\n2º Semestre\n\nAnatomo-fisiologia II\n\nMatemáticas Gerais II\n\nPsicobiologia\n\nPsicologia da Atenção e da Percepção\n\nPsicologia da Memória\n\n\nTotal\n\n\n\n\n\n",font = "200")
    infoCurso1.place(x = 400, y = 100)
    infoCurso1_1 = Message(curso1,text = "Área Científica\n\nCTS\n\nPSIC\n\nM\n\nPSIC\n\nB\n\n\n\nÁrea Científica\n\nCTS\n\nM\n\nPSIC\n\nPSIC\n\nPSIC\n\n\n\n\n\n\n\n\n",font = "200")
    infoCurso1_1.place(x = 950, y = 100)
    infoCurso1_2 = Message(curso1, text = "Créditos ECTS\n\n6\n\n6\n\n6\n\n6\n\n6\n\n\n\nCréditos ECTS\n\n6\n\n6\n\n6\n\n6\n\n6\n\n\n60\n\n\n\n\n\n",font = "200")
    infoCurso1_2.place(x = 1250, y = 100)
    

    curso1.mainloop()


def paginaCurso2():
    global curso2
    curso2 = Tk()
    curso2.geometry("1980x1600")
    voltarAtras = Button(curso2, text = "Voltar atrás",font = 20,command = paginaFaculdades2)
    voltarAtras.place(x = 20,y = 20)

    curso2.mainloop()



curso1 = Button(text = "Licenciatura em Gestão", relief = "flat",font= (20), command = paginaCurso1)
curso1.place(x= 20,y= 500)
msgCurso1 = Message(UA,text = "O objetivo da Licenciatura em Gestão da Universidade de Aveiro é contribuir para a formação de técnicos com base de formação sólida e diversificada focalizada na moderna gestão das empresas e organizações, de acordo com o paradigma do desenvolvimento sustentável, mas, simultaneamente, atentos às novas formas de gestão e de negócio que o desenvolvimento tecnológico e organizacional, entretanto verificado, exigem no exercício das suas funções, com espírito criativo e empreendedor. O curso continuará a apostar na formação para o empreendedorismo e para o trabalho em rede em organizações globais de estrutura complexa e variável, só possível com um investimento forte e lúcido na gestão da informação e do conhecimento e em tecnologias e sistemas da informação e comunicação, o que pressupõe a formação de profissionais aptos a tomar decisões neste domínio. O plano proposto cobre todas as áreas principais da Gestão, dá a oportunidade aos alunos de aprenderem e utilizarem metodologias e ferramentas indispensáveis na sua futura vida profissional, incentiva-os a aprender a aprender e prepara-os para uma especialização ao nível do 2º ciclo.",width = 1500)
msgCurso1.place(x=20,y=530)


curso2 = Button(text = "Licenciatura em Psicologia", relief = "flat",font = (20), command = paginaCurso2)
curso2.place(x = 20, y = 650)
msgcurso2 = Message(UA,text = "A licenciatura em Psicologia pretende proporcionar uma base sólida de conhecimentos e competências no domínio desta área científica numa perspetiva de ciência natural do comportamento que possibilite uma efetiva interdisciplinaridade com outras domínios das ciências naturais, exatas e sociais, bem como uma sólida preparação teórica e em investigação laboratorial e de campo, para uma aprendizagem eficaz dos conhecimentos e das competências a desenvolver na formação posterior ao nível dos 2º e 3º ciclos em Psicologia. Com efeito, a formação em Psicologia na UA assume-se como um projeto próprio marcado por uma sólida formação científica de base. Entende-se esta 'formação científica' à semelhança do que ocorre nas outras ciências naturais (biologia, química, por exemplo). Ou seja, preconiza-se uma Psicologia enquanto ciência natural do comportamento que procura desenvolver teorias e modelos do comportamento e testá-los experimentalmente, com treino laboratorial sistemático, nomeadamente ao nível do primeiro ciclo de formação, para além dos estudos de coorte, de caso-controlo e também experimentais de campo (modalidade de 'ensaio') a predominarem no 2º ciclo de cariz profissionalizante.",width = 1500)
msgcurso2.place(x = 20, y = 680)


UA.mainloop()