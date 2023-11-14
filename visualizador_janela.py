import macros
from tkinter.messagebox import showerror
from tkinter import *
from time import sleep
from random import randint
import arvore_binaria
from main import janela, canvas

def Desenha_arvore(Nodulo_raiz, Raiz_posicao_x, Raiz_posicao_y, Nodulo_altura, canvas, janela):
    if Nodulo_raiz is None:
        return

    if Nodulo_raiz.ponteiro_esquerda is not None:
        Ponteiro_esquerda_x, Ponteiro_esquerda_y = arvore_binaria.Calcular_posicao_ponteiro_esquerda(Raiz_posicao_x, Raiz_posicao_y, Nodulo_altura + 1)
        canvas.create_line(Raiz_posicao_x, Raiz_posicao_y,
                           Ponteiro_esquerda_x, Ponteiro_esquerda_y, 
                           fill=macros.LINE_COLOR, width=5)
        Desenha_arvore(Nodulo_raiz.ponteiro_esquerda, 
                 Ponteiro_esquerda_x, Ponteiro_esquerda_y, 
                 Nodulo_altura + 1,
                 canvas, janela)

    if Nodulo_raiz.ponteiro_direita is not None:
        Ponteiro_direita_x, Ponteiro_esquerda_y = arvore_binaria.Calcular_posicao_ponteiro_direita(Raiz_posicao_x, Raiz_posicao_y, Nodulo_altura + 1)
        canvas.create_line(Raiz_posicao_x, Raiz_posicao_y,
                           Ponteiro_direita_x, Ponteiro_esquerda_y, 
                           fill=macros.LINE_COLOR, width=5)
        Desenha_arvore(Nodulo_raiz.ponteiro_direita, 
                 Ponteiro_direita_x, Ponteiro_esquerda_y, 
                 Nodulo_altura + 1,
                 canvas, janela)

    createOvalWithText(canvas, Raiz_posicao_x, Raiz_posicao_y, 
                     macros.NODE_RADIUS, macros.NODE_COLOR, 
                     Nodulo_raiz.value, macros.TEXT_COLOR, macros.FONT_SIZE)
    janela.update()


def Limpar_Canvas_e_desenha_arvore():
        Posicao_arvore_x = macros.WINDOW_WIDTH/2
        Posicao_arvore_y = macros.Y_PADDING
        canvas.delete("all")
        Desenha_arvore(Nodulo_raiz, Posicao_arvore_x, Posicao_arvore_y, 0, canvas, janela)


def createOvalWithText(canvas, centerX, centerY, radius, ovalColor, text, textColor, fontSize):
    oval = canvas.create_oval(centerX - radius, centerY - radius,
                       centerX + radius, centerY + radius,
                       fill=ovalColor, width=0)
    text = canvas.create_text(centerX, centerY,
                       text=text, fill=textColor, font=("Arial " + str(int(fontSize)) + " bold"))


def createRectangleWithText(canvas, centerX, centerY, width, height, rectangleColor, text, textColor, fontSize):
    canvas.create_rectangle(centerX - width / 2, centerY - height / 2,
                            centerX + width / 2, centerY + height / 2,
                            fill=rectangleColor, width=0)
    canvas.create_text(centerX, centerY,
                       text=text, fill=textColor, font=("Arial " + str(int(fontSize)) + " bold"))


def Validar_input(value) -> bool:
    try:
        value = int(value)
    
    except ValueError:
        showerror(title="ERROR", message="Entrada Inválida")
        return False

    if value > macros.MAX_VALUE:
        showerror(title="ERROR", message="Entrada excedeu o máximo permitido")
        return False
    
    if value < macros.MIN_VALUE:
        showerror(title="ERROR", message="Entrada ficou abaixo do mínimo permitido")
        return False
    
    return True


def Botao_inserir(value):
    global Nodulo_raiz

    if not Validar_input(value):
        return

    value = int(value)

    Raiz_posicao_x = macros.WINDOW_WIDTH/2
    Raiz_posicao_y = macros.Y_PADDING

    Desabilitar_interface()

    Nodulo_raiz = arvore_binaria.Inserir_nodulo(Nodulo_raiz, value, Raiz_posicao_x, Raiz_posicao_y, 0, canvas, janela)

    sleep(1)

    canvas.delete("all")
    Desenha_arvore(Nodulo_raiz, Raiz_posicao_x, Raiz_posicao_y, 0, canvas, janela)

    Habilitar_interface()


def Botao_busca(value):
    if not Validar_input(value):
        return

    value = int(value)

    Raiz_posicao_x = macros.WINDOW_WIDTH/2
    Raiz_posicao_y = macros.Y_PADDING

    Desabilitar_interface()

    arvore_binaria.busca_nodulo_arvore(Nodulo_raiz, value, Raiz_posicao_x, Raiz_posicao_y, 0, canvas, janela)

    sleep(1)

    canvas.delete("all")
    Desenha_arvore(Nodulo_raiz, Raiz_posicao_x, Raiz_posicao_y, 0, canvas, janela)
    
    Habilitar_interface()


def Botao_deletar(value):
    global Nodulo_raiz

    if not Validar_input(value):
        return

    value = int(value)

    Raiz_posicao_x = macros.WINDOW_WIDTH/2
    Raiz_posicao_y = macros.Y_PADDING

    Desabilitar_interface()

    Nodulo_raiz = arvore_binaria.busca_nodulo_arvore(Nodulo_raiz, value, Raiz_posicao_x, Raiz_posicao_y, 0, canvas, janela)

    sleep(1)

    canvas.delete("all")
    Desenha_arvore(Nodulo_raiz, Raiz_posicao_x, Raiz_posicao_y, 0, canvas, janela)
    
    Habilitar_interface()


def Botao_gerar_arvore_aleatoria():
    global Nodulo_raiz

    Nodulo_raiz = None

    numero_insercoes = randint(100, 100)

    for x in range(numero_insercoes):
        nodeValue = randint(macros.MIN_VALUE, macros.MAX_VALUE)
        Nodulo_raiz = arvore_binaria.Inserir_nodulo_sem_animacao(Nodulo_raiz, nodeValue, 0)
    
    Raiz_posicao_x = macros.WINDOW_WIDTH/2
    Raiz_posicao_y = macros.Y_PADDING

    canvas.delete("all")
    Desenha_arvore(Nodulo_raiz, Raiz_posicao_x, Raiz_posicao_y, 0, canvas, janela)


def Desabilitar_interface():
    Botao_inserir["state"] = DISABLED
    Botao_gerar_arvore_aleatoria["state"] = DISABLED
    Botao_deletar["state"] = DISABLED
    Botao_busca["state"] = DISABLED
    Botao_inserir["state"] = DISABLED


def Habilitar_interface():
    Botao_inserir["state"] = NORMAL
    Botao_gerar_arvore_aleatoria["state"] = NORMAL
    Botao_deletar["state"] = NORMAL
    Botao_busca["state"] = NORMAL
    Botao_inserir["state"] = NORMAL