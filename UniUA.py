from cgitb import text
from distutils import command
from textwrap import fill, wrap
from tkinter import *
from tkinter.simpledialog import SimpleDialog
from turtle import title
from PIL import ImageTk,Image
from tkinter import ttk





UA = Tk()
UA.geometry("1920x1080")   
canvas = Canvas(UA, width = 1600, height = 1600)  
canvas.pack()  
img = ImageTk.PhotoImage(Image.open(r"UC1Users\Silgueira\Desktop\AED Tema B\Imagens\PROJ_UA_LOGO.png")) 
canvas.create_image(250,20, anchor=NW, image=img)
    

def paginaFaculdades1UA():
        curso1UA.withdraw()

def paginaFaculdades2UA():
        curso2UA.withdraw()
        
class ScrollBar:
    def paginaCurso1UA():
        global curso1UA

        curso1UA = Tk()
        curso1UA.geometry("1980x1600")
        v = Scrollbar(curso1UA)
        v.pack(side = RIGHT,fill = Y)
        textoCurso1UA = Text(curso1UA, width = 1980,height = 1600,wrap = NONE,relief = FLAT, font = "200",yscrollcommand = v.set)
        textoCurso1UA.insert(END,'''\n\n\n\n\n
                    Ano 1\n\n\t\t\t\t\t\t1º Semestre\t\t\t\t\t\t\tÁrea Científica\t\t\t\t\t\t\tCréditos ECTS\n\n\n\n\t\t\t\t\t\tAnatomo-fisiologia I\t\t\t\t\t\t\tCTS\t\t\t\t\t\t\t6\n\n\n\n\t\t\t\t\t\tIntrodução à Psicologia\t\t\t\t\t\t\tPSIC\t\t\t\t\t\t\t6\n\n\n\n\t\t\t\t\t\tMatemáticas Gerais I\t\t\t\t\t\t\tM\t\t\t\t\t\t\t6\n\n\n\n\t\t\t\t\t\tMetodologia de Investigação em Psicologia\t\t\t\t\t\t\tPSIC\t\t\t\t\t\t\t6\n\n\n\n\t\t\t\t\t\tGenética e Evolução\t\t\t\t\t\t\tB\t\t\t\t\t\t\t6'''+'''\n\n\n\n
                         \n\n\t\t\t\t\t\t2º Semestre\t\t\t\t\t\t\tÁrea Científica\t\t\t\t\t\t\tCréditos ECTS\n\n\n\n\t\t\t\t\t\tAnatomo-fisiologia II\t\t\t\t\t\t\tCTS\t\t\t\t\t\t\t6\n\n\n\n\t\t\t\t\t\tMatemáticas Gerais II\t\t\t\t\t\t\tM\t\t\t\t\t\t\t6\n\n\n\n\t\t\t\t\t\tPsicobiologia\t\t\t\t\t\t\tPSIC\t\t\t\t\t\t\t6\n\n\n\n\t\t\t\t\t\tPsicologia da Atenção e da Percepção\t\t\t\t\t\t\tPSIC\t\t\t\t\t\t\t6\n\n\n\n\t\t\t\t\t\tPsicologia da Memória\t\t\t\t\t\t\tPSIC\t\t\t\t\t\t\t6\n\n\n\n
        \t\t\t\t\t\tTotal\t\t\t\t\t\t\t\t\t\t\t\t\t\t60\n\n\n\n
                    Ano 2\n\n\t\t\t\t\t\t1º Semestre\t\t\t\t\t\t\tÁrea Científica\t\t\t\t\t\t\tCréditos ECTS\n\n\n\n\t\t\t\t\t\tProbabilidade e Estatística\t\t\t\t\t\t\tM\t\t\t\t\t\t\t6\n\n\n\n\t\t\t\t\t\tPsicologia da Emoção e da Motivação\t\t\t\t\t\t\tPSIC\t\t\t\t\t\t\t6\n\n\n\n\t\t\t\t\t\tPsicologia da Aprendizagem\t\t\t\t\t\t\tPSIC\t\t\t\t\t\t\t6\n\n\n\n\t\t\t\t\t\tModelos Teóricos em Psicologia I: Dinâmicos e Sistémicos\t\t\t\t\t\t\tPSIC\t\t\t\t\t\t\t6\n\n\n\n\t\t\t\t\t\tPsicologia do Desenvolvimento I: Criança e Adolescente\t\t\t\t\t\t\tPSIC\t\t\t\t\t\t\t6\n\n\n\n
                         \n\n\t\t\t\t\t\t2º Semestre\t\t\t\t\t\t\tÁrea Científica\t\t\t\t\t\t\tCréditos ECTS\n\n\n\n\t\t\t\t\t\tNeuropsicologia\t\t\t\t\t\t\tPSIC\t\t\t\t\t\t\t6\n\n\n\t\t\t\t\t\tPsicologia Social\t\t\t\t\t\t\tPSIC\t\t\t\t\t\t\t6\n\n\n\n\t\t\t\t\t\tFundamentos de Ética para Psicólogos\t\t\t\t\t\t\tPSIC\t\t\t\t\t\t\t6\n\n\n\n\t\t\t\t\t\tModelos Teóricos em Psicologia II: Comportamentais e Cognitivos\t\t\t\t\t\t\tPSIC\t\t\t\t\t\t\t6\n\n\n\n\t\t\t\t\t\tPsicologia do Desenvolvimento II: Adulto e Idoso\t\t\t\t\t\t\tPSIC\t\t\t\t\t\t\t6\n\n\n\n
        \t\t\t\t\t\tTotal\t\t\t\t\t\t\t\t\t\t\t\t\t\t60\n\n\n\n            
                    Ano 3\n\n\t\t\t\t\t\t1º Semestre\t\t\t\t\t\t\tÁrea Científica\t\t\t\t\t\t\tCréditos ECTS\n\n\n\n\t\t\t\t\t\tAvaliação Psicológica I\t\t\t\t\t\t\tPSIC\t\t\t\t\t\t\t6\n\n\n\t\t\t\t\t\tContextos de Aplicação em Psicologia I\t\t\t\t\t\t\tPSIC\t\t\t\t\t\t\t6\n\n\n\n\t\t\t\t\t\tPrática de Investigação I\t\t\t\t\t\t\tPSIC\t\t\t\t\t\t\t6\n\n\n\n\t\t\t\t\t\tPsicopatologia I: Criança e Adolescente\t\t\t\t\t\t\tPSIC\t\t\t\t\t\t\t6\n\n\n\n\t\t\t\t\t\tRaciocínio e Tomada de Decisão\t\t\t\t\t\t\tPSIC\t\t\t\t\t\t\t6\n\n\n\n
                         \n\n\t\t\t\t\t\t2º Semestre\t\t\t\t\t\t\tÁrea Científica\t\t\t\t\t\t\tCréditos ECTS\n\n\n\n\t\t\t\t\t\tAvaliação Psicológica II\t\t\t\t\t\t\tPSIC\t\t\t\t\t\t\t6\n\n\n\n\t\t\t\t\t\tContextos de Aplicação em Psicologia II\t\t\t\t\t\t\tPSIC\t\t\t\t\t\t\t6\n\n\n\n\t\t\t\t\t\tPrática de Investigação II\t\t\t\t\t\t\tPSIC\t\t\t\t\t\t\t6\n\n\n\n\t\t\t\t\t\tPsicopatologia II: Adulto e Idoso\t\t\t\t\t\t\tPSIC\t\t\t\t\t\t\t6\n\n\n\n\t\t\t\t\t\tOpção\n\n\n\n\t\t\t\t\t\t\t·Introdução à Cronopsicologia\t\t\t\t\t\tPSIC\t\t\t\t\t\t\t6\n\n\n\n\t\t\t\t\t\t\t·Modificação do Comportamento\t\t\t\t\t\tPSIC\t\t\t\t\t\t\t6\n\n\n\n\t\t\t\t\t\t\t·Psicologia da Família e Redes Sociais\t\t\t\t\t\tPSIC\t\t\t\t\t\t\t6\n\n\n\n\t\t\t\t\t\t\t·Psicologia do Bem-estar Pessoal\t\t\t\t\t\tPSIC\t\t\t\t\t\t\t6\n\n\n\n\t\t\t\t\t\t\t·Psiconeuroimunologia\t\t\t\t\t\tPSIC\t\t\t\t\t\t\t6\n\n\n\n
        \t\t\t\t\t\tTotal\t\t\t\t\t\t\t\t\t\t\t\t\t\t60\n\n\n\n
                LEGENDA:\n\t\tCTS = Ciências e Tecnologias da saúde\n\t\tPSIC = Psicologia\n\t\tM = Matemática\n\t\tB = Biologia''')
        textoCurso1UA.pack(side = TOP,fill = X)
        v.config(command=textoCurso1UA.yview)
        voltarAtras1 = Button(textoCurso1UA,text = "Voltar atrás",font = 20, command = paginaFaculdades1UA)
        voltarAtras1.place(x=20,y=20)
        textoCurso1UA.config(state = DISABLED)
    
    def paginaCurso2UA():
        global curso2UA
        curso2UA = Tk()
        curso2UA.geometry("1980x1600")
        v = Scrollbar(curso2UA)
        v.pack(side = RIGHT,fill = Y)
        texoCurso2UA = Text(curso2UA, width = 1980, height = 1600,wrap = NONE,relief = FLAT,font = "200",yscrollcommand = v.set)
        texoCurso2UA.insert(END,'''\n\n\n\n\n
                    Ano 1\n\n\t\t\t\t\t\t1º Semestre\t\t\t\t\t\t\tÁrea Científica\t\t\t\t\t\t\tCréditos ECTS\n\n\n\n\t\t\t\t\t\tEconomia I\t\t\t\t\t\t\tE\t\t\t\t\t\t\t6\n\n\n\n\t\t\t\t\t\tGestão de Empresas\t\t\t\t\t\t\tGES\t\t\t\t\t\t\t6\n\n\n\n\t\t\t\t\t\tCálculo I\t\t\t\t\t\t\tM\t\t\t\t\t\t\t6\n\n\n\n\t\t\t\t\t\tGestão da Informação\t\t\t\t\t\t\tGES\t\t\t\t\t\t\t6\n\n\n\n\t\t\t\t\t\tDireito das Empresas I\t\t\t\t\t\t\tCJ\t\t\t\t\t\t\t6\n\n\n\n
                         \n\n\t\t\t\t\t\t2º Semestre\t\t\t\t\t\t\tÁrea Científica\t\t\t\t\t\t\tCréditos ECTS\n\n\n\n\t\t\t\t\t\tEconomia II\t\t\t\t\t\t\tE\t\t\t\t\t\t\t6\n\n\n\n\t\t\t\t\t\tComportamento Organizacional\t\t\t\t\t\t\tGES\t\t\t\t\t\t\t6\n\n\n\n\t\t\t\t\t\tCálculo II\t\t\t\t\t\t\tM\t\t\t\t\t\t\t6\n\n\n\n\t\t\t\t\t\tTeoria da Contabilidade\t\t\t\t\t\t\tC\t\t\t\t\t\t\t6\n\n\n\n\t\t\t\t\t\tTeoria das Organizações\t\t\t\t\t\t\tGES\t\t\t\t\t\t\t6\n\n\n\n
        \t\t\t\t\t\tTotal\t\t\t\t\t\t\t\t\t\t\t\t\t\t60\n\n\n\n
                    Ano 2\n\n\t\t\t\t\t\t1º Semestre\t\t\t\t\t\t\tÁrea Científica\t\t\t\t\t\t\tCréditos ECTS\n\n\n\n\t\t\t\t\t\tContabilidade e Informação Financeira\t\t\t\t\t\t\tC\t\t\t\t\t\t\t6\n\n\n\n\t\t\t\t\t\tGestão de Recursos Humanos\t\t\t\t\t\t\tGES\t\t\t\t\t\t\t6\n\n\n\n\t\t\t\t\t\tIntrodução Ao Marketing\t\t\t\t\t\t\tGES\t\t\t\t\t\t\t6\n\n\n\n\t\t\t\t\t\tDireito de Empresas II\t\t\t\t\t\t\tCJ\t\t\t\t\t\t\t6Gestão Financeira I\t\t\t\t\t\t\tGES\t\t\t\t\t\t\t6\n\n\n\n
                         \n\n\t\t\t\t\t\t2º Semestre\t\t\t\t\t\t\tÁrea Científica\t\t\t\t\t\t\tCréditos ECTS\n\n\n\n\t\t\t\t\t\tInvestigação Operacional\t\t\t\t\t\t\tEGI\t\t\t\t\t\t\t6\n\n\n\n\t\t\t\t\t\tGestão de Marketing\t\t\t\t\t\t\tGES\t\t\t\t\t\t\t6\n\n\n\n\t\t\t\t\t\tMétodos Quantitativos em Gestão\t\t\t\t\t\t\tGES\t\t\t\t\t\t\t6\n\n\n\n\t\t\t\t\t\tContabilidade Analítica\t\t\t\t\t\t\tC\t\t\t\t\t\t\t6\n\n\n\n\t\t\t\t\t\tTecnologia e Sistemas de Informação em Gestão\t\t\t\t\t\t\tGES\t\t\t\t\t\t\t6\n\n\n\n
        \t\t\t\t\t\tTotal\t\t\t\t\t\t\t\t\t\t\t\t\t\t60\n\n\n\n
                    Ano 3\n\n\t\t\t\t\t\t1º Semestre\t\t\t\t\t\t\tÁrea Científica\t\t\t\t\t\t\tCréditos ECTS\n\n\n\n\t\t\t\t\t\tGestão de Operações\t\t\t\t\t\t\tEGI\t\t\t\t\t\t\t6\n\n\n\n\t\t\t\t\t\tEmpreendedorismo\t\t\t\t\t\t\tGES\t\t\t\t\t\t\t6\n\n\n\n\t\t\t\t\t\tGestão Integrada de Projectos\t\t\t\t\t\t\tGES\t\t\t\t\t\t\t6\n\n\n\n\t\t\t\t\t\tAuditoria\t\t\t\t\t\t\tC\t\t\t\t\t\t\t6\n\n\n\n\t\t\t\t\t\tGestão Financeira II\t\t\t\t\t\t\tGES\t\t\t\t\t\t\t6\n\n\n\n
                         \n\n\t\t\t\t\t\t2º Semestre\t\t\t\t\t\t\tÁrea Científica\t\t\t\t\t\t\tCréditos ECTS\n\n\n\n\t\t\t\t\t\tLogística\t\t\t\t\t\t\tEGI\t\t\t\t\t\t\t6\n\n\n\n\t\t\t\t\t\tControlo de Gestão\t\t\t\t\t\t\tC\t\t\t\t\t\t\t6\n\n\n\n\t\t\t\t\t\tFiscalidade\t\t\t\t\t\t\tC\t\t\t\t\t\t\t6\n\n\n\n\t\t\t\t\t\tGestão da Qualidade\t\t\t\t\t\t\tEGI\t\t\t\t\t\t\t6\n\n\n\n\t\t\t\t\t\tOpção\n\n\n\n\t\t\t\t\t\t\t·Contabilidade Analitica Avançada\t\t\t\t\t\tC\t\t\t\t\t\t\t6\n\n\n\n\t\t\t\t\t\t\t.Gestão de Serviços\t\t\t\t\t\tGES\t\t\t\t\t\t\t6\n\n\n\n\t\t\t\t\t\t\t.Gestão Estratégica\t\t\t\t\t\tGES\t\t\t\t\t\t\t6\n\n\n\n\t\t\t\t\t\t\t.Novas Formas de Negócio\t\t\t\t\t\tGES\t\t\t\t\t\t\t6\n\n\n\n
        \t\t\t\t\t\tTotal\t\t\t\t\t\t\t\t\t\t\t\t\t\t60\n\n\n\n
                LEGENDA:\n\t\t E = Economia\n\t\tGES = Gestão\n\t\tM = Matemática\n\t\tCJ = Ciências Jurídicas\n\t\tC = Contabilidade''')

        texoCurso2UA.pack(side = TOP,fill = X)
        v.config(command= texoCurso2UA.yview)
        voltarAtras2 = Button(texoCurso2UA, text = "Voltar atrás", font = (20), command = paginaFaculdades2UA)
        voltarAtras2.place(x=20, y= 20)
        texoCurso2UA.config(state = DISABLED)

    curso1UA = Button(text = "Licenciatura em Psicologia", relief = "flat",font= (20), command = paginaCurso1UA)
    curso1UA.place(x= 20,y= 500)
    msgCurso1UA = Message(UA,text = '''A licenciatura em Psicologia pretende proporcionar uma base sólida de conhecimentos e competências no domínio desta área científica numa perspetiva de ciência natural do comportamento que possibilite uma efetiva interdisciplinaridade com outras domínios das ciências naturais, exatas e sociais, bem como uma sólida preparação teórica e em investigação laboratorial e de campo, para uma aprendizagem eficaz dos conhecimentos e das competências a desenvolver na formação posterior ao nível dos 2º e 3º ciclos em Psicologia.
Com efeito, a formação em Psicologia na UA assume-se como um projeto próprio marcado por uma sólida formação científica de base. Entende-se esta "formação científica" à semelhança do que ocorre nas outras ciências naturais (biologia, química, por exemplo). Ou seja, preconiza-se uma Psicologia enquanto ciência natural do comportamento que procura desenvolver teorias e modelos do comportamento e testá-los experimentalmente, com treino laboratorial sistemático, nomeadamente ao nível do primeiro ciclo de formação, para além dos estudos de coorte, de caso-controlo e também experimentais de campo (modalidade de "ensaio") a predominarem no 2º ciclo de cariz profissionalizante.
''',width = 1500)
    msgCurso1UA.place(x=20,y=530) 
    


    curso2UA = Button(text = "Licenciatura em Gestão", relief = "flat",font = (20), command = paginaCurso2UA)
    curso2UA.place(x = 20, y = 650)
    msgcurso2 = Message(UA,text = '''O objetivo da Licenciatura em Gestão da Universidade de Aveiro é contribuir para a formação de técnicos com base de formação sólida e diversificada focalizada na moderna gestão das empresas e organizações, de acordo com o paradigma do desenvolvimento sustentável, mas, simultaneamente, atentos às novas formas de gestão e de negócio que o desenvolvimento tecnológico e organizacional, entretanto verificado, exigem no exercício das suas funções, com espírito criativo e empreendedor.
O curso continuará a apostar na formação para o empreendedorismo e para o trabalho em rede em organizações globais de estrutura complexa e variável, só possível com um investimento forte e lúcido na gestão da informação e do conhecimento e em tecnologias e sistemas da informação e comunicação, o que pressupõe a formação de profissionais aptos a tomar decisões neste domínio.
O plano proposto cobre todas as áreas principais da Gestão, dá a oportunidade aos alunos de aprenderem e utilizarem metodologias e ferramentas indispensáveis na sua futura vida profissional, incentiva-os a aprender a aprender e prepara-os para uma especialização ao nível do 2º ciclo.
''',width = 1500)
    msgcurso2.place(x = 20, y = 680)




    
s = ScrollBar()


   



        




UA.mainloop()
s = ScrollBar()