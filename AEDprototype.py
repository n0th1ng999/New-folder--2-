#                                                   Projeto de AED
#
#
#
#               Pretende-se desenvolver uma aplicação que funcione como um gestor (agregador) de cursos/
#               conteúdos de aprendizagem online.
#               A sua aplicação deve suportar o acesso a um catálogo de cursos/conteúdos de aprendizagem,
#               que estão organizados por categorias.
#               Cada utilizador da aplicação deverá poder navegar pelos cursos disponíveis, pontuar e comentar
#               os cursos/conteúdos disponíveis, assinalar como já visto e gerir a sua playlist de favoritos.
#
#
#
#
#               Sistema Roles (Admin and user (*implica login*))
#                       Admin:
#                            Autenticar e gerir utilizadores da aplicação (2 perfis de utilizadores)
#                           Gerir categorias (p.e.: Javascript, Python, HTML, Edição de vídeo, Imagem, etc.)
#                           Gerir catálogo de cursos, associando-os a pelo menos uma categoria
#                          
# 
#                       Admin and User:
# 
#                            Pesquisar no catálogo com filtros combinados, como p.e.:
#                           Por categoria(s)
#                           Por nome de curso/conteúdo de aprendizagem
#                           Ordenar catálogo (pontuação, nº visualizações, ordem alfabética)
#                           Comentar e classificar / gostar
#                           Top de most rated
#                           Criar e gerir lista -pessoal- de favoritos (-favoritos do user-)
#                           Gerar notificações 
#
#                *      login:                                                                                           *
#                            Os utilizadores autenticam-se na aplicação com a sua conta: email e password. Caso o
#                           utilizador ainda não tenha uma conta nesta aplicação, deverá criá-la, indicando os seguintes
#                           dados: nome do utilizador, email e password.
#                           Estes dados são arquivados num ficheiro de texto:
#                 --->      o Nome do ficheiro: --utilizadores.txt--
#                 --->      o --  Formato: nome; email; password; perfil_utilizador  --
#                           
#                *                                                                                                        *           
#
#
#
#                *     ❖GERIR CATÁLOGO:                                                                                    *
#                            Adicionar ou remover cursos/conteúdos de aprendizagem ao catálogo.
#                              Um curso/conteúdo de aprendizagem é constituído por uma sequência própria de objetos
#                           de aprendizagem (normalmente vídeos).
#                              Um curso/conteúdo de aprendizagem tem um título, uma descrição, uma imagem associada
#                           (é opcional) e pode ter um conjunto (variável) de vídeos associados. Isto é, um curso pode
#                           ser constituído por uma sequência de conteúdos. Cada conteúdo é identificado por uma
#                           descrição e o respetivo link (normalmente vídeo do Youtube)
#                                                                                                                        
#
#                       ❖PESQUISA NO CATÁLOGO
#                         A aplicação deve apresentar o catálogo ao utilizador (por omissão os cursos mais recentes).
#                         O utilizador poderá filtrar o catálogo por categoria(s), ou por um determinado título de
#                         curso/conteúdo de aprendizagem.
#                         O catálogo deve poder ser ainda ordenado por número de visualizações ou por pontuação,
#                         por exemplo.
#                         A partir do link associado a cada vídeo, o utilizador poderá visualizá-lo (executá-lo num Web
#                         browser), a partir da sua aplicação.
#
#
#
#
#                       ❖ CLASSIFICAR E COMENTAR
#                          O utilizador poderá comentar ou pontuar um determinado curso/percurso de
#                          aprendizagem. Para tal, é obrigatório que esteja autenticado na plataforma. Poderá ainda
#                          responder a comentários de terceiros, gerando-se uma thread de comentários ao jeito de
#                          uma rede social.
#
#
#
#                       ❖TOP DE MOST RATED
#                          Deve ser apresentado o top (geral) dos cursos/conteúdos mais vistos, assim como o top dos
#                          mais vistos por categoria.
#
#
#                       ❖ CRIAR E GERIR LISTA DE FAVORITOS
#                          Os utilizadores autenticados podem adicionar cursos à sua lista pessoal de favoritos, gerindo
#                          essa mesma lista (acrescentar / remover elementos da lista de favoritos).
#                          Cada utilizador tem acesso apenas à sua lista de favoritos.
#
#
#
#                       ❖ GERAR NOTIFICAÇÕES
#                          Quando um utilizador se autentica na aplicação, poderá receber notificações das últimas
#                          novidades lançadas no catálogo, de acordo com as categorias com que interagiu mais
#                          recentemente, ou eventuais interesses definidos no seu perfil.                                                                                                  *
#                 *                                                                                                            *


import os
import tkinter 
import math
import random



def clear():
    os.system("cls")

def cabeçalho(txt):
    print("\t\t\t"+txt)



def MenuPreEntry():
    op=2
    while op!=0:
        clear() 
        cabeçalho("Entre na aplicação")
        print("\n\n\n\t\t\tFAÇA LOGIN: 1")
        print("\t\t\tFAÇA REGISTER: 2\n\n\n")
        print("\t\t\tSair: 0 \n\n\n")
        op=input("\t\t\tOpcao:")
        

#                           Estes dados são arquivados num ficheiro de texto:
#                 --->      o Nome do ficheiro: --utilizadores.txt--
#                 --->      o --  Formato: nome; email; password; perfil_utilizador  --
def register():
    
    Error = False
    while Error == False:
        NameRegister=input("\nNome:")
        EmailRegister=input("\nEmail:")
        PasswordRegister=input("\nPassword:")
        UsernameRegister=input("\nPerfil_utilizador (Username):")

        
                   
       

        #Se a verificação for bem sucedida:
    
        Account=str(NameRegister+";"+EmailRegister+";"+PasswordRegister+";"+UsernameRegister+"\n")

        try:
            LoginInfoFile = open("LoginInfo.txt" , "x" )
            LoginInfoFile = open("LoginInfo.txt" , "r+" , encoding="utf-8")
            
        except:
            LoginInfoFile = open("LoginInfo.txt" , "r+" , encoding="utf-8")
        
        #Fazer check de email e nickname
        for line in LoginInfoFile:
            Info = line.split(";") 
            if Info[1] == EmailRegister:
                print("\n\Já existe uma conta com esse Username")
                Error=False
                break
            else:
                Error=True

            if Info[3] == UsernameRegister:
                print("\n\Já existe uma conta com esse Username")
                Error=False
                break
            else:
                Error=True

        if Error:
            LoginInfoFile.write(Account)
        else:
            print("\nConta com esse nome/email já existe existe")






        #Verificação de parametros(Regras pra cada 1 + verificação de existencia na "base de dados")
        #if len(NameRegister)<=3 :
        #     print("\n\nNome que registou é demasiado pequeno")
            
            
        # if  EmailRegister.find("@")==-1 or EmailRegister.find(".")==-1:
        #     print("\n\nO email que registou não é válido")
            

        # if  len(PasswordRegister)<=5: #or PasswordRegister.find("1")==-1 or NameRegister.find(".")==-1:
        #     print("\n\nA Password que registou não é válida")
              

        # if len(UsernameRegister)<=3:
        #     print("\n\nO Username que registou não é válido")

        

        LoginInfoFile.close()


def login():
    print("\n\n\t\tLogin . . . ")
    LoginUsername=input("\n\nUsername:")
    LoginPassword=input("\n\nPassword:")


    #abrir ficheiro infoLogin
    LoginInfoFile=open("LoginInfo.txt", "r")


    
    # --> Nome;mail@example.com;Password;Username  <--
    
    for line in LoginInfoFile:
            Info = line.split(";") 
            if Info[3] == LoginUsername and Info[2] == LoginPassword:
                print("\n \nA logar . . .")
            else:
                print("\n\n\t\tLogin . . . ")
                LoginUsername=input("\n\nUsername:")
                LoginPassword=input("\n\nPassword:")

    LoginInfoFile.close
    


register()


