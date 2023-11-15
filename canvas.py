import macros
from tkinter import *

from visualizador_janela import Desenha_arvore

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


def clearCanvasAndDrawTree(Nodulo_raiz, Posicao_arvore_x, Posicao_arvore_y, canvas, janela):
        Posicao_arvore_x = macros.WINDOW_WIDTH/2
        Posicao_arvore_y = macros.Y_PADDING
        canvas.delete("all")
        Desenha_arvore(Nodulo_raiz, Posicao_arvore_x, Posicao_arvore_y, 0, canvas, janela)

