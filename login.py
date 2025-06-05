import random
import string
import tkinter as tk

usuarios_cadastrados = {} # lista de usuários cadastrados


# objeto do usuário
class User:
    def __init__(self, cpf, nome_empresa, username, email, password, endereco):
        self.cpf = cpf
        self.nome_empresa = nome_empresa
        self.username = username
        self.email = email
        self.password = password
        self.endereco = endereco
        self.coletas = []

class PaginaLogin:
    def __init__(self,root,app):
        self.root = root
        self.app = app
        self.frame = tk.Frame(self.root)

        header = tk.Label(self.frame,text= "Recycle Barber") # bota uma linha de texto como conteúdo da janela
        header.pack(fill="x",padx=20,pady=10,expand=True,anchor="center") # adiciona o objeto criado, ancorando ao centro

        texto_login = tk.Label(self.frame,text= "Login") # mesma coisa que o anterior
        texto_login.pack(fill="x",padx=20,expand=True,anchor="n")
        logn = tk.Entry(self.frame,width=20) # cria uma caixa de texto para entrada do usuário
        logn.pack(fill="x",padx=20,pady=10,expand=True,anchor="n")

        texto_senha = tk.Label(self.frame,text= "Senha") # mesma coisa que o anterior
        texto_senha.pack(fill="x",padx=20,expand=True,anchor="n")
        senha = tk.Entry(self.frame,width=20)
        senha.pack(fill="x",padx=20,pady=10,expand=True,anchor="n")

        def logar(): # Função que vai rodar ao apertar o botâo
            lg = logn.get()
            sn = senha.get()

        def cadastrar():
            self.abrir_cadastro()

        botao_login = tk.Button(self.frame,text="Entrar",width=20,command=logar,anchor="n")
        botao_login.pack()

        texto_cadastro_opc = tk.Button(self.frame,width=30,text="Não tem conta? Cadastre-se.",command=cadastrar)
        texto_cadastro_opc.pack()

    def abrir(self):
        self.frame.pack(fill="x",expand=True)
    
    def abrir_cadastro(self):
        self.frame.pack_forget()
        self.app.abrir_pag_cadastro()

class PaginaCadastro:
    def __init__(self,root,app):
        self.root = root
        self.app = app
        self.frame = tk.Frame(self.root)
        
        header = tk.Label(self.frame,text= "Se cadastre no Recycle Barber!")
        header.pack(fill="x",padx=20,pady=10,expand=True,anchor="n")

        texto_cpf = tk.Label(self.frame,text= "CPF: ")
        texto_cpf.pack(padx=20,expand=True,anchor="w")
        cpf = tk.Entry(self.frame,width=20)
        cpf.pack(fill="x",padx=20,pady=10,expand=True,anchor="n")

        texto_nomeempresa = tk.Label(self.frame,text= "Nome da empresa: ")
        texto_nomeempresa.pack(padx=20,expand=True,anchor="w")
        nomeempresa = tk.Entry(self.frame,width=20)
        nomeempresa.pack(fill="x",padx=20,pady=10,expand=True,anchor="n")

        texto_nome = tk.Label(self.frame,text= "Nome do empresário: ")
        texto_nome.pack(padx=20,expand=True,anchor="w")
        nome = tk.Entry(self.frame,width=20)
        nome.pack(fill="x",padx=20,pady=10,expand=True,anchor="n")

        texto_senha = tk.Label(self.frame,text= "Senha: ")
        texto_senha.pack(padx=20,expand=True,anchor="w")
        senha = tk.Entry(self.frame,width=20)
        senha.pack(fill="x",padx=20,pady=10,expand=True,anchor="n")

        texto_senhaconfirma = tk.Label(self.frame,text= "Confirme sua senha: ")
        texto_senhaconfirma.pack(padx=20,expand=True,anchor="w")
        senhaconfirma = tk.Entry(self.frame,width=20)
        senhaconfirma.pack(fill="x",padx=20,pady=10,expand=True,anchor="n")

        texto_endereco = tk.Label(self.frame,text= "Endereço: ")
        texto_endereco.pack(padx=20,expand=True,anchor="w")
        
        endereco = tk.Frame(self.frame)
        endereco.pack(fill="x", padx=20, pady=10, expand=True, anchor="n")

        estado = tk.Entry(endereco,width=20)
        estado.insert(0,"Estado")
        estado.grid(column=0,row=0)

        cidade = tk.Entry(endereco,width=20)
        cidade.insert(0,"Cidade")
        cidade.grid(column=0,row=1)

        bairro = tk.Entry(endereco,width=20)
        bairro.insert(0,"Bairro")
        bairro.grid(column=1,row=0)

        cep = tk.Entry(endereco,width=20)
        cep.insert(0,"CEP")
        cep.grid(column=1,row=1)

        rua = tk.Entry(endereco,width=20)
        rua.insert(0,"Rua")
        rua.grid(column=2,row=0)
        
        numero = tk.Entry(endereco,width=20)
        numero.insert(0,"Número")
        numero.grid(column=2,row=1)
        
        complemento = tk.Entry(endereco,width=20)
        complemento.insert(0,"Complemento (Opcional)")
        complemento.grid(column=3,row=0)

        texto_confirmar = tk.Label(self.frame,width=20)
        texto_confirmar.pack(fill="x",padx=20,pady=10,expand=True,anchor="n")

        #def cadastrar():
            #try

        texto_cadastro = tk.Button(self.frame,width=30,text="Cadastrar",command=cadastrar)
        texto_cadastro.pack()

    def abrir(self):
        self.frame.pack(fill="x",expand=True)


# cadastro
def cadastrar():
    while True:
        try:
            cpf = input("Insira seu CPF: ")
            cpf = cpf.replace(".","") # retira pontos da string, caso o usuário colocar
            cpf = cpf.replace("-","") # retira traços da string, caso o usuário colocar
            if len(cpf) != 11: raise Exception # um CPF tem 11 digitos, se não tiver, levanta uma exceção
            cpf = int(cpf) # para verificar se o CPF não tem letras ou nada a mais estranho
        except:
            print("Erro: CPF inválido. Por favor, tente novamente.")
        else:
            if str(cpf) in usuarios_cadastrados: # transforma o CPF em string temporariamente para 
                print("CPF já cadastrado. Retornando...")
                break # se o CPF já estiver cadastrado, quebra o loop e cancela o cadastro
            
            nome_empresa = input("Nome da empresa: ")
            username = input("Nome do empresário: ")
            email = input("E-mail da empresa: ").lower() # converte o e-mail em letras minúsculas
            password = input("Insira a sua senha: ")
            
            confirm_password = "" # confirmação de senha
            while confirm_password != password:
                confirm_password = input("Confirme sua senha: ")
                if confirm_password != password: print("A senha entrada foi diferente.")
            
            endereco = {} # cria um dicionário vazio para guardar todas as informações do endereço
            endereco["UF"] = input("Estado: ")
            endereco["cidade"] = input("Cidade: ")
            endereco["bairro"] = input("Bairro: ")
            
            while True:
                try:
                    endereco["CEP"] = input("CEP: ") # mesma lógica de verificação do CPF
                    endereco["CEP"] = endereco["CEP"].replace("-","")
                    if len(endereco["CEP"]) != 8: raise Exception
                    endereco["CEP"] = int(endereco["CEP"])
                except: 
                    print("CEP inválido.")
                else: 
                    break
            
            endereco["rua"] = input("Rua: ")
            endereco["numero"] = input("Número: ")
            endereco["complemento"] = input("(Opcional) Complemento: ")
            
            new_user = User(cpf, nome_empresa, username, email, password, endereco) # cria objeto de usuário
            usuarios_cadastrados[str(cpf)] = new_user
            
            print("Cadastro efetuado com sucesso! Efetuando login...\n")
            
            return new_user # retorna valor booleano para já funcionar com a lógica do main

def mostrar_perfil(usuario):
    print("-----------")
    print(f"CPF cadastrado:\n{usuario.cpf}")
    print(f"Nome da empresa:\n{usuario.nome_empresa}")
    print(f"Nome do usuário:\n{usuario.username}")
    print(f"E-mail:\n{usuario.email}")
    print(f"Endereço:\n{usuario.endereco["rua"]}, {usuario.endereco["numero"]} {usuario.endereco["complemento"]}")
    print(f"{usuario.endereco["CEP"]}")
    print(f"{usuario.endereco["bairro"]}, {usuario.endereco["cidade"]}, {usuario.endereco["UF"]}")