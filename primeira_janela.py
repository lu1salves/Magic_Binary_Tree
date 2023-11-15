<<<<<<< HEAD
import tkinter as tk
from tkinter import ttk

def onClickGenerateRandomTree():
   
    pass

def onClickInsert(value):
    
    pass

def onClickDelete(value):
    
    pass

def onClickSearch(value):
 
    pass

import tkinter as tk
from tkinter import ttk

def abrir_janela_principal():
    janela_bem_vindo.destroy()
    mostrar_janela_principal()

def mostrar_janela_principal():
    window.deiconify()

# Janela de boas-vindas
janela_bem_vindo = tk.Tk()
janela_bem_vindo.title("Seja Bem-Vindo")
janela_bem_vindo.geometry("300x150")

label_boas_vindas = ttk.Label(janela_bem_vindo, text="Seja bem-vindo!")
label_boas_vindas.pack(pady=20)

botao_iniciar = ttk.Button(janela_bem_vindo, text="Iniciar", command=abrir_janela_principal)
botao_iniciar.pack()

# Janela principal (inicialmente oculta)
window = tk.Tk()
window.withdraw()

# Configuração da janela principal
window.title("Binary Search Tree Visualizer")
window.geometry("1200x1200")

# Frame lateral para o menu
menu_frame = tk.Frame(window, width=200, bg="lightgray")
menu_frame.grid(row=0, column=0, sticky="nsew")

#menu lateral
inputField = tk.Entry(menu_frame)
inputField.pack(pady=10)

generateRandomTreeButton = ttk.Button(menu_frame, text="Generate Random Tree", command=onClickGenerateRandomTree)
generateRandomTreeButton.pack(pady=10)

insertButton = ttk.Button(menu_frame, text="Insert", command=lambda: onClickInsert(inputField.get()))
insertButton.pack(pady=10)

deleteButton = ttk.Button(menu_frame, text="Delete", command=lambda: onClickDelete(inputField.get()))
deleteButton.pack(pady=10)

searchButton = ttk.Button(menu_frame, text="Search", command=lambda: onClickSearch(inputField.get()))
searchButton.pack(pady=10)

# Canvas usando grid
canvas = tk.Canvas(window, width=1000, height=1200, bg="white")
canvas.grid(row=0, column=1, sticky="nsew")

# Configuração de peso para permitir redimensionamento
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)

janela_bem_vindo.mainloop()

=======
import tkinter as tk
from tkinter import ttk

def onClickGenerateRandomTree():
   
    pass

def onClickInsert(value):
    
    pass

def onClickDelete(value):
    
    pass

def onClickSearch(value):
 
    pass

import tkinter as tk
from tkinter import ttk

def abrir_janela_principal():
    janela_bem_vindo.destroy()
    mostrar_janela_principal()

def mostrar_janela_principal():
    window.deiconify()

# Janela de boas-vindas
janela_bem_vindo = tk.Tk()
janela_bem_vindo.title("Seja Bem-Vindo")
janela_bem_vindo.geometry("300x150")

label_boas_vindas = ttk.Label(janela_bem_vindo, text="Seja bem-vindo!")
label_boas_vindas.pack(pady=20)

botao_iniciar = ttk.Button(janela_bem_vindo, text="Iniciar", command=abrir_janela_principal)
botao_iniciar.pack()

# Janela principal (inicialmente oculta)
window = tk.Tk()
window.withdraw()

# Configuração da janela principal
window.title("Binary Search Tree Visualizer")
window.geometry("1200x1200")

# Frame lateral para o menu
menu_frame = tk.Frame(window, width=200, bg="lightgray")
menu_frame.grid(row=0, column=0, sticky="nsew")

#menu lateral
inputField = tk.Entry(menu_frame)
inputField.pack(pady=10)

generateRandomTreeButton = ttk.Button(menu_frame, text="Generate Random Tree", command=onClickGenerateRandomTree)
generateRandomTreeButton.pack(pady=10)

insertButton = ttk.Button(menu_frame, text="Insert", command=lambda: onClickInsert(inputField.get()))
insertButton.pack(pady=10)

deleteButton = ttk.Button(menu_frame, text="Delete", command=lambda: onClickDelete(inputField.get()))
deleteButton.pack(pady=10)

searchButton = ttk.Button(menu_frame, text="Search", command=lambda: onClickSearch(inputField.get()))
searchButton.pack(pady=10)

# Canvas usando grid
canvas = tk.Canvas(window, width=1000, height=1200, bg="white")
canvas.grid(row=0, column=1, sticky="nsew")

# Configuração de peso para permitir redimensionamento
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)

janela_bem_vindo.mainloop()

>>>>>>> c16c79c62f2bc36c0461f5a07297d1de67eadf74
