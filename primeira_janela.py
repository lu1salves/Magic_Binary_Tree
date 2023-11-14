import macros
from tkinter.messagebox import showerror, showinfo
from tkinter import *
import tkinter as tk
from time import sleep
from random import randint
from venv import create

def drawTree(Nodulo_raiz, Raiz_posicao_x, Raiz_posicao_y, Nodulo_altura, canvas, window):
    if Nodulo_raiz is None:
        return

    if Nodulo_raiz.ponteiro_esquerda is not None:
        Ponteiro_esquerda_x, Ponteiro_esquerda_y = calculateLeftChildPosition(Raiz_posicao_x, Raiz_posicao_y, Nodulo_altura + 1)
        canvas.create_line(Raiz_posicao_x, Raiz_posicao_y,
                           Ponteiro_esquerda_x, Ponteiro_esquerda_y, 
                           fill=macros.LINE_COLOR, width=5)
        drawTree(Nodulo_raiz.ponteiro_esquerda, 
                 Ponteiro_esquerda_x, Ponteiro_esquerda_y, 
                 Nodulo_altura + 1,
                 canvas, window)

    if Nodulo_raiz.ponteiro_direita is not None:
        Ponteiro_direita_x, Ponteiro_esquerda_y = calculateRightChildPosition(Raiz_posicao_x, Raiz_posicao_y, Nodulo_altura + 1)
        canvas.create_line(Raiz_posicao_x, Raiz_posicao_y,
                           Ponteiro_direita_x, Ponteiro_esquerda_y, 
                           fill=macros.LINE_COLOR, width=5)
        drawTree(Nodulo_raiz.ponteiro_direita, 
                 Ponteiro_direita_x, Ponteiro_esquerda_y, 
                 Nodulo_altura + 1,
                 canvas, window)

    createOvalWithText(canvas, Raiz_posicao_x, Raiz_posicao_y, 
                     macros.NODE_RADIUS, macros.NODE_COLOR, 
                     Nodulo_raiz.value, macros.TEXT_COLOR, macros.FONT_SIZE)
    window.update()


def clearCanvasAndDrawTree():
        Posicao_arvore_x = macros.WINDOW_WIDTH/2
        Posicao_arvore_y = macros.Y_PADDING
        canvas.delete("all")
        drawTree(Nodulo_raiz, Posicao_arvore_x, Posicao_arvore_y, 0, canvas, window)


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

    disableUI()

    Nodulo_raiz = insertNode(Nodulo_raiz, value, Raiz_posicao_x, Raiz_posicao_y, 0, canvas, window)

    sleep(1)

    canvas.delete("all")
    drawTree(Nodulo_raiz, Raiz_posicao_x, Raiz_posicao_y, 0, canvas, window)

    Habilitar_interface()


def Botao_busca(value):
    if not Validar_input(value):
        return

    value = int(value)

    Raiz_posicao_x = macros.WINDOW_WIDTH/2
    Raiz_posicao_y = macros.Y_PADDING

    disableUI()

    searchTree(Nodulo_raiz, value, Raiz_posicao_x, Raiz_posicao_y, 0, canvas, window)

    sleep(1)

    canvas.delete("all")
    drawTree(Nodulo_raiz, Raiz_posicao_x, Raiz_posicao_y, 0, canvas, window)
    
    Habilitar_interface()


def Botao_deletar(value):
    global Nodulo_raiz

    if not Validar_input(value):
        return

    value = int(value)

    Raiz_posicao_x = macros.WINDOW_WIDTH/2
    Raiz_posicao_y = macros.Y_PADDING

    disableUI()

    Nodulo_raiz = deleteNode(Nodulo_raiz, value, Raiz_posicao_x, Raiz_posicao_y, 0, canvas, window)

    sleep(1)

    canvas.delete("all")
    drawTree(Nodulo_raiz, Raiz_posicao_x, Raiz_posicao_y, 0, canvas, window)
    
    Habilitar_interface()


def Botao_gerar_arvore_aleatoria():
    global Nodulo_raiz

    Nodulo_raiz = None

    numero_insercoes = randint(100, 100)

    for x in range(numero_insercoes):
        nodeValue = randint(macros.MIN_VALUE, macros.MAX_VALUE)
        Nodulo_raiz = insertNodeWithoutAnimation(Nodulo_raiz, nodeValue, 0)
    
    Raiz_posicao_x = macros.WINDOW_WIDTH/2
    Raiz_posicao_y = macros.Y_PADDING

    canvas.delete("all")
    drawTree(Nodulo_raiz, Raiz_posicao_x, Raiz_posicao_y, 0, canvas, window)


def Desabilitar_interface():
    insertButton["state"] = DISABLED
    generateRandomTreeButton["state"] = DISABLED
    deleteButton["state"] = DISABLED
    searchButton["state"] = DISABLED
    inputField["state"] = DISABLED


def Habilitar_interface():
    insertButton["state"] = NORMAL
    generateRandomTreeButton["state"] = NORMAL
    deleteButton["state"] = NORMAL
    searchButton["state"] = NORMAL
    inputField["state"] = NORMAL