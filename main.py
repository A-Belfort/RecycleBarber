import login
import coleta
import tkinter as tk

root = tk.Tk() # cria instância da interface tkinter
root.wm_geometry("360x640") # determina a resolução
root_name = root.winfo_pathname(root.winfo_id())
root.wm_title("Recycle Barber") # seta o título da janela

class App:
    def __init__(self, root):
        self.root = root
        self.login = login.PaginaLogin(self.root,self)
        self.cadastro = login.PaginaCadastro(self.root,self)
    
    def abrir_pag_login(self):
        self.login.abrir()

    def abrir_pag_cadastro(self):
        self.cadastro.abrir()

app = App(root)
app.abrir_pag_login()

root.mainloop()