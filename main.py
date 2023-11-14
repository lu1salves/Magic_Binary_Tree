"""
    Esse arquivo contém as principais chamadas de funções para que o programa funcione corretamente
"""
import macros
from tkinter import *
import primeira_janela


janela = Tk()
janela.geometry(str(macros.WINDOW_WIDTH) + "x" + str(macros.WINDOW_HEIGHT) + "+100-100")
janela.resizable(False, False)
janela.title("Visualizador de árvore binária")

canvas = Canvas(janela, bg=macros.BACKGROUND_COLOR)
canvas.pack(side=TOP, fill=BOTH, expand=2)

Gerar_arvore_aleatoria_botao_componente = Button(janela, 
                                                 text="Gerar Aleatório", 
                                                 font=("Arial 15"), 
                                                 command=lambda:primeira_janela.Botao_gerar_arvore_aleatoria())
Gerar_arvore_aleatoria_botao_componente.pack(side=LEFT, fill=X, expand=1)

Inserir_botao_componente = Button(janela, 
                                  text="Inserir", 
                                  font=("Arial 15"), 
                                  command=lambda:primeira_janela.Botao_inserir(Input_espaco.get()))
Inserir_botao_componente.pack(side=LEFT, fill=X, expand=1)

Deletar_botao_componente = Button(janela, 
                                  text="Deletar", 
                                  font=("Arial 15"), 
                                  command=lambda:primeira_janela.Botao_deletar(Input_espaco.get()))
Deletar_botao_componente.pack(side=LEFT, fill=X, expand=1)

Buscar_botao_componente = Button(janela, 
                                 text="Buscar", 
                                 font=("Arial 15"), 
                                 command=lambda:primeira_janela.Botao_busca(Input_espaco.get()))
Buscar_botao_componente.pack(side=LEFT, fill=X, expand=1)

Input_espaco = Entry(janela, font=("Arial 15"))
Input_espaco.pack(side=LEFT, expand=0)

""""
background_image = tk.PhotoImage(file = "INF.png")
limg= Label(janela, i=background_image)
limg.pack()
"""

janela.mainloop()