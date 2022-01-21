from email.mime import image
import imp
import re
from textwrap import wrap
from tkinter import *
from PIL import ImageTk,Image
from tkinter import ttk
from tkVideoPlayer import TkinterVideo



UC = Tk()
UC.geometry("1920x1080")
canvas = Canvas(UC,width = 1600,height = 1600)
canvas.pack()
img = ImageTk.PhotoImage(Image.open(r"C:\Users\Silgueira\Desktop\AED Tema B\Imagens\PROJ_UC_LOGO.png"))
canvas.create_image(250,20, anchor = NW,image=img)

def paginaFaculdades1UC():
    curso1UC.withdraw()

def paginaFaculdades2UC():
    curso2UC.withdraw()

class ScrollBar:
    def paginaCurso1UC():
        global curso1UC
        curso1UC = Tk()
        curso1UC.geometry("1980x1600")
        v = Scrollbar(curso1UC)
        v.pack(side = RIGHT,fill = Y)
        textoCurso1UC = Text(curso1UC,width = 1980,height = 1600,wrap = NONE,relief = FLAT,font = "200",yscrollcommand = v.set)
        textoCurso1UC.insert(END,'''\n\n\n
                   Condições de Acesso e Ingresso\n\n\tConcurso Nacional de Acesso e ingresso ao ensino superior (DGES):\n\n\tProvas de Ingresso:\n\tFísica e Química\n\t19 Matemática A\t\t\t\t\t\t\t\t\t\t\t\t\t\tSendo uma Licenciatura de 1º ciclo com 3 anos de duração, espera-se que os\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\testudantes que frequentem este ciclo de estudos adquiram a formação básica em\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tengenharia civil, que lhes permita ingressar num curso de mestrado de 2º ciclo, o\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tqual irá complementar o conhecimento, adquirindo após a frequência destes dois\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tciclos de estudo as valências mínimas para uma fácil integração no mercado de\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\ttrabalho, nacional e internacional, em domínios relacionados com a engenharia civil.\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tAs valências adquiridas nesta Licenciatura podem permitir a integração no mercado\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tde trabalho como técnico superior. Sendo a engenharia uma atividade regulada, o\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\texercício de funções dum licenciado em Engenharia Civil são aquelas permitidas\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tpelas ordens profissionais (OE e OET).\tClassificações Mínimas:\n\tNota de candidatura: 100 pontos (na escala 0-200)\n\tProvas de ingresso: 95 pontos (na escala 0-200)\n\n\tFórmula de Cálculo:\n\tMédia do secundário: 50%\n\tProvas de ingresso: 50%\n\n\tOutras formas de acesso (UC-candidatos):\n\n\t- Regimes de Reingresso e Mudança de Par Instituição/Curso;\n\t- Concurso Especial de Acesso para Maiores de 23 anos;\n\t- Concurso Especial de Acesso para Titulares de Outros Cursos Superiores;\n\t- Concurso Especial para Estudantes Internacionais.\n\n\tA informação disponibilizada não dispensa a consulta à página da Direção Geral do\n\tEnsino Superior (DGES) e/ou a página dos Candidatos. Consultar página web da\n\tDGES e dos Candidatos\n\n''')
        textoCurso1UC.pack(side = TOP,fill = X)
        v.config(command = textoCurso1UC.yview)
        voltarAtras1UC = Button(textoCurso1UC,text = "Voltar atrás",font = 20, command = paginaFaculdades1UC)
        voltarAtras1UC.place(x = 20,y = 20)

        textoCurso1UC.config(state = DISABLED)
        curso1UC.mainloop

    def paginaCurso2UC():
        global curso2UC
        curso2UC = Tk()
        curso2UC.geometry("1980x1600")
        v = Scrollbar(curso2UC)
        v.pack(side = RIGHT,fill = Y)
        textoCurso2UC = Text(curso2UC,width = 1980,height = 1600,wrap = NONE,relief = FLAT,font = "200",yscrollcommand = v.set)
        textoCurso2UC.insert(END,'''\n\n\n
                   Condições de Acesso e Ingresso\n\n\tConcurso Nacional de Acesso e ingresso ao ensino superior (DGES):\n\n\tProvas de Ingresso:\n\tFísica e Química\n\t19 Matemática A\t\t\t\t\t\t\t\t\t\t\t\t\t\tIndústrias de fabricação de equipamentos mecânicos e térmicos; Empresas de produção de energia e\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tclimatização; Atividades de manutenção e gestão de operações; Gestão de manutenção e reparação\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tautomóvel.\n\tClassificações Mínimas:Nota de candidatura: 100 pontos (na escala 0-200)\n\tProvas de ingresso: 95 pontos (na escala 0-200)\n\n\tFórmula de Cálculo:\n\tMédia do secundário: 50%\n\tProvas de ingresso: 50%\n\n\tOutras formas de acesso (UC-candidatos):\n\n\t Regimes de Reingresso e Mudança de Par Instituição/Curso;\n\t- Concurso Especial de Acesso para Maiores de 23 anos;\n\t- Concurso Especial de Acesso para Titulares de Outros Cursos Superiores;\n\t- Concurso Especial para Estudantes Internacionais.\n\n\tA informação disponibilizada não dispensa a consulta à página da Direção Geral do Ensino Superior (DGES)\n\te/ou a página dos Candidatos. Consultar página web da DGES e dos Candidatos''')

        textoCurso2UC.pack(side = TOP,fill = X)
        v.config(command = textoCurso2UC.yview)
        voltarAtras2UC = Button(textoCurso2UC,text = "Voltar atrás",font = 20,command = paginaFaculdades2UC)
        voltarAtras2UC.place(x = 20,y = 20)
        textoCurso2UC.config(state = DISABLED)




    curso1UC = Button(text = "Licenciantura em Engenharia Civil",relief = "flat",font = 20,command = paginaCurso1UC)
    curso1UC.place(x = 20,y = 520)
    msgCurso1UC = Message(UC,text = '''O objetivo geral principal do ciclo de estudos é dar formação básica, mas fundamentada, nos diversos domínios da Engenharia Civil, proporcionando aos estudantes uma formação sólida em áreas estruturantes, tais como matemática, química, física e computação, para além de dar formação básica em áreas específicas da engenharia civil relacionadas com diversas intervenções no território destinadas a preencher as necessidades da sociedade.
Complementarmente, pretende-se encorajar os estudantes a valorizar algumas competências e atitudes pessoais necessárias ao exercício da profissão, nomeadamente o espírito científico, a criatividade, o sentido crítico e de responsabilidade, a capacidade de aprender autonomamente, a capacidade para interagir e trabalhar em grupo e em equipas interdisciplinares, a capacidade de auto adaptação, a capacidade de comunicação e de liderança, a ética profissional, a autoexigência, o ecumenismo cultural, a valorização do conhecimento, bem como fomentar o empreendedorismo e a criação de empresas inovadoras apoiadas em investigação científica.''',width = 1500)
    msgCurso1UC.place(x = 20,y = 550)


    curso2UC = Button(text = "Licenciantura em Engenharia Mecânica", relief = "flat",font = 20,command = paginaCurso2UC)
    curso2UC.place(x = 20,y = 670)
    msgCurso2UC = Message(UC,text = '''A formação académica do Engenheiro Mecânico, na Universidade de Coimbra, visa prepará-lo para o projeto de máquinas e processos; para a conceção e a fabricação de peças e máquinas em geral; para ações de desenvolvimento na área energética e ambiental; para a gestão da produção; para manutenção de equipamentos e também para atuarem como empreendedores nas áreas industriais afins. A formação ao nível do primeiro ciclo confere formação nos vários domínios da engenharia mecânica proporcionando uma base sólida para a prossecução de estudos bem como uma habilitação inicial para a integração no mercado de trabalho.''',width = 1500)
    msgCurso2UC.place(x = 20,y = 700)




s = ScrollBar()
UC.mainloop()