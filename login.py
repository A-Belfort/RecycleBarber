import tkinter as tk
import server

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
        
        botao_voltar = tk.Button(self.frame,text="Voltar",width=10,command=self.voltar,anchor="nw")
        botao_voltar.pack(padx=20,pady=10,expand=True,anchor="nw")

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

        texto_email = tk.Label(self.frame,text= "E-mail: ")
        texto_email.pack(padx=20,expand=True,anchor="w")
        email = tk.Entry(self.frame,width=20)
        email.pack(fill="x",padx=20,pady=10,expand=True,anchor="n")

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

        # cadastro
        def cadastrar():
            user = User(
                cpf=cpf.get(),
                nome_empresa=nomeempresa.get(),
                username=nome.get(),
                email=email.get(),
                password=senha.get(),
                endereco={
                    "UF": estado.get(),
                    "cidade": cidade.get(),
                    "bairro": bairro.get(),
                    "CEP": cep.get(),
                    "rua": rua.get(),
                    "numero": numero.get(),
                    "complemento": complemento.get()
                })
            
            server.usuarios_cadastrados[user.cpf] = user

            #self.frame.pack_forget()
            tk.Label(self.frame, text="Cadastro realizado com sucesso!").pack(pady=20,anchor="center")
            tk.Button(self.frame, text="Voltar", command=self.voltar).pack(pady=10,anchor="center")

        texto_cadastro = tk.Button(self.frame,width=30,text="Cadastrar",command=cadastrar)
        texto_cadastro.pack()

    def abrir(self):
        self.frame.pack(fill="x",expand=True)

    def voltar(self):
        self.frame.pack_forget()
        self.app.abrir_pag_login()


def mostrar_perfil(usuario):
    print("-----------")
    print(f"CPF cadastrado:\n{usuario.cpf}")
    print(f"Nome da empresa:\n{usuario.nome_empresa}")
    print(f"Nome do usuário:\n{usuario.username}")
    print(f"E-mail:\n{usuario.email}")
    print(f"Endereço:\n{usuario.endereco['rua']}, {usuario.endereco['numero']} {usuario.endereco['complemento']}")
    print(f"{usuario.endereco['CEP']}")
    print(f"{usuario.endereco['bairro']}, {usuario.endereco['cidade']}, {usuario.endereco['UF']}")