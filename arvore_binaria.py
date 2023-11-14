import macros
from tkinter.messagebox import showerror, showinfo
from tkinter import *
import tkinter as tk
from primeira_janela import clearCanvasAndDrawTree, createRectangleWithText, createOvalWithText
from time import sleep

rootNode = None

class Nodulo:
    
    def __init__(self, value):
        self.Value = value
        self.Ponteiro_esquerda = None
        self.Ponteiro_direita = None
        self.Dano_ataque = None
        self.Dano_defesa = None
        self.Eh_magico = None
        self.Nome = ""
        self.Descricao = ""


def Calcular_posicao_ponteiro_esquerda(posicao_x_pai, posicao_y_pai, nodulo_altura):
        """_summary_

        Args:
            posicao_x_pai (_type_): _description_
            posicao_y_pai (_type_): _description_
            nodulo_altura (_type_): _description_

        Returns:
            _type_: _description_
        """
    
        posicao_x_nodulo_esquerda = posicao_x_pai - ((macros.WINDOW_WIDTH - macros.X_PADDING) / pow(2, nodulo_altura))
        posicao_y_nodulo_esquerda = posicao_y_pai + macros.NODE_RADIUS * 4
        return (posicao_x_nodulo_esquerda, posicao_y_nodulo_esquerda)
    
def Calcular_posicao_ponteiro_direita(posicao_x_pai, posicao_y_pai, nodulo_altura):
        """_summary_

        Args:
            posicao_x_pai (_type_): _description_
            posicao_y_pai (_type_): _description_
            nodulo_altura (_type_): _description_

        Returns:
            _type_: _description_
        """
        
        posicao_x_nodulo_direita = posicao_x_pai + ((macros.WINDOW_WIDTH - macros.X_PADDING) / pow(2, nodulo_altura)) / 2
        posicao_y_nodulo_direita = posicao_y_pai + macros.NODE_RADIUS * 4
        return (posicao_x_nodulo_direita, posicao_y_nodulo_direita)


def Inserir_nodulo(Raiz_no, valor_nodulo, posicao_raiz_x, posicao_raiz_y, nodulo_altura, canvas, window):
        if nodulo_altura > macros.MAX_DEPTH:
            showinfo(title = "Inserir", message = "Profundidade máxima alcançada")
            return Raiz_no

        if Raiz_no is None:
            Raiz_no = Nodulo()
            return Raiz_no

            createOvalWithText(canvas, posicao_raiz_x, posicao_raiz_y - 3 * macros.NODE_RADIUS,
                            macros.NODE_RADIUS, macros.HIGHLIGHT_COLOR,
                            value, macros.HIGHLIGHT_TEXT_COLOR, macros.FONT_SIZE)

            windows.update()
            sleep(macros.ANIMATION_DELAY)

        elif valor_nodulo < Raiz_no.Value:
            createRectangleWithText(canvas, posicao_raiz_x, posicao_raiz_y - 1.5 * macros.NODE_RADIUS, macros.NODE_RADIUS / 1.5, macros.NODE_RADIUS / 1.5, macros.HIGHLIGHT_COLOR, "<", macros.HIGHLIGHT_TEXT_COLOR, macros.FONT_SIZE)
            window.update()
            sleep(macros.ANIMATION_DELAY)

            posicao_ponteiro_esquerda_x, posicao_ponteiro_esquerda_y = Calcular_posicao_ponteiro_esquerda(posicao_raiz_x, posicao_raiz_y, nodulo_altura + 1)
            Raiz_no.Ponteiro_esquerda = Inserir_nodulo(Raiz_no.Ponteiro_esquerda, valor_nodulo, 
                                            posicao_ponteiro_esquerda_x, posicao_ponteiro_esquerda_y, 
                                            nodulo_altura + 1, 
                                            canvas, window)


        elif valor_nodulo > Raiz_no.Valuealue:
            createRectangleWithText(canvas, posicao_raiz_x, posicao_raiz_y - 1.5 * macros.NODE_RADIUS,
                                    macros.NODE_RADIUS / 1.5, macros.NODE_RADIUS / 1.5, macros.HIGHLIGHT_COLOR,
                                    ">", macros.HIGHLIGHT_TEXT_COLOR, macros.FONT_SIZE)
            window.update()
            sleep(macros.ANIMATION_DELAY)
            
            posicao_ponteiro_esquerda_x, posicao_ponteiro_esquerda_y = Calcular_posicao_ponteiro_direita(posicao_raiz_x, posicao_raiz_y, nodulo_altura + 1)
            Raiz_no.rightChild = Inserir_nodulo(Raiz_no.rightChild, nodulo_valor, 
                                            posicao_ponteiro_esquerda_x, posicao_ponteiro_esquerda_y,
                                            nodulo_altura + 1, 
                                            canvas, window)
            

        elif valor_nodulo == Raiz_no.value:
            showinfo(title="Insert", message="Node already in tree")

        
        return Raiz_no


def Inserir_nodulo_sem_animacao(Raiz_No, value, nodulo_altura):
        if nodulo_altura > macros.MAX_DEPTH:
            return Raiz_No

        if Raiz_No is None:
            Raiz_No = Nodulo()
            return Raiz_No

        if value < Raiz_No.value:
            Raiz_No.Ponteiro_esquerda = Inserir_nodulo_sem_animacao(Raiz_No.Ponteiro_esquerda, Raiz_No.value, nodulo_altura + 1)
        
        elif value > Raiz_No.value:
            Raiz_No.Ponteiro_direita = Inserir_nodulo_sem_animacao(Raiz_No.Ponteiro_direita, Raiz_No.value, nodulo_altura + 1)

        return Raiz_No


def searchTree(Raiz_No, value, rootPositionX, rootPositionY, nodeDepth, canvas, window):
    if Raiz_No is None:
        showinfo(title="Search", message="Node not found")
        return

    createOvalWithText(canvas, rootPositionX, rootPositionY - 3 * macros.NODE_RADIUS,
                        macros.NODE_RADIUS, macros.HIGHLIGHT_COLOR,
                        value, macros.HIGHLIGHT_TEXT_COLOR, macros.FONT_SIZE)
    window.update()
    sleep(macros.ANIMATION_DELAY)

    if value < Raiz_No.value:
        createRectangleWithText(canvas, rootPositionX, rootPositionY - 1.5 * macros.NODE_RADIUS,
                                macros.NODE_RADIUS / 1.5, macros.NODE_RADIUS / 1.5, macros.HIGHLIGHT_COLOR,
                                "<", macros.HIGHLIGHT_TEXT_COLOR, macros.FONT_SIZE)
        window.update()
        sleep(macros.ANIMATION_DELAY)

        leftChildPositionX, leftChildPositionY = calculateLeftChildPosition(rootPositionX, rootPositionY, nodeDepth + 1)
        searchTree(Raiz_No.leftChild, value, 
                    leftChildPositionX, leftChildPositionY, 
                    nodeDepth + 1, 
                    canvas, window)
    elif value > Raiz_No.value:
        createRectangleWithText(canvas, rootPositionX, rootPositionY - 1.5 * macros.NODE_RADIUS,
                                macros.NODE_RADIUS / 1.5, macros.NODE_RADIUS / 1.5, macros.HIGHLIGHT_COLOR,
                                ">", macros.HIGHLIGHT_TEXT_COLOR, macros.FONT_SIZE)
        window.update()
        sleep(macros.ANIMATION_DELAY)
        
        rightChildPositionX, rightChildPositionY = calculateRightChildPosition(rootPositionX, rootPositionY, nodeDepth + 1)
        searchTree(Raiz_No.rightChild, value, 
                    rightChildPositionX, rightChildPositionY,
                    nodeDepth + 1, 
                    canvas, window)
    elif value == Raiz_No.value:
        createRectangleWithText(canvas, rootPositionX, rootPositionY - 1.5 * macros.NODE_RADIUS,
                                macros.NODE_RADIUS / 1.5, macros.NODE_RADIUS / 1.5, macros.HIGHLIGHT_COLOR,
                                "=", macros.HIGHLIGHT_TEXT_COLOR, macros.FONT_SIZE)
        createOvalWithText(canvas, rootPositionX, rootPositionY,
                            macros.NODE_RADIUS, macros.HIGHLIGHT_COLOR,
                            value, macros.HIGHLIGHT_TEXT_COLOR, macros.FONT_SIZE)
        window.update()
        sleep(macros.ANIMATION_DELAY)


def deleteNode(Raiz_No, value, rootPositionX, rootPositionY, nodeDepth, canvas, window):
    if Raiz_No is None:
        showinfo(title="Delete", message="Node not found")
        return None

    createOvalWithText(canvas, rootPositionX, rootPositionY - 3 * macros.NODE_RADIUS,
                        macros.NODE_RADIUS, macros.HIGHLIGHT_COLOR,
                        value, macros.HIGHLIGHT_TEXT_COLOR, macros.FONT_SIZE)
    window.update()
    sleep(macros.ANIMATION_DELAY)

    if value < Raiz_No.value:
        createRectangleWithText(canvas, rootPositionX, rootPositionY - 1.5 * macros.NODE_RADIUS,
                                macros.NODE_RADIUS / 1.5, macros.NODE_RADIUS / 1.5, macros.HIGHLIGHT_COLOR,
                                "<", macros.HIGHLIGHT_TEXT_COLOR, macros.FONT_SIZE)
        window.update()
        sleep(macros.ANIMATION_DELAY)

        leftChildPositionX, leftChildPositionY = calculateLeftChildPosition(rootPositionX, rootPositionY, nodeDepth + 1)
        Raiz_No.leftChild = deleteNode(Raiz_No.leftChild, value, 
                                        leftChildPositionX, leftChildPositionY, 
                                        nodeDepth + 1, 
                                        canvas, window)
    elif value > Raiz_No.value:
        createRectangleWithText(canvas, rootPositionX, rootPositionY - 1.5 * macros.NODE_RADIUS,
                                macros.NODE_RADIUS / 1.5, macros.NODE_RADIUS / 1.5, macros.HIGHLIGHT_COLOR,
                                ">", macros.HIGHLIGHT_TEXT_COLOR, macros.FONT_SIZE)
        window.update()
        sleep(macros.ANIMATION_DELAY)
        
        rightChildPositionX, rightChildPositionY = calculateRightChildPosition(rootPositionX, rootPositionY, nodeDepth + 1)
        Raiz_No.rightChild = deleteNode(Raiz_No.rightChild, value, 
                                        rightChildPositionX, rightChildPositionY,
                                        nodeDepth + 1, 
                                        canvas, window)
    elif value == Raiz_No.value:
        createRectangleWithText(canvas, rootPositionX, rootPositionY - 1.5 * macros.NODE_RADIUS,
                                macros.NODE_RADIUS / 1.5, macros.NODE_RADIUS / 1.5, macros.HIGHLIGHT_COLOR,
                                "=", macros.HIGHLIGHT_TEXT_COLOR, macros.FONT_SIZE)
        createOvalWithText(canvas, rootPositionX, rootPositionY,
                            macros.NODE_RADIUS, macros.HIGHLIGHT_COLOR,
                            value, macros.HIGHLIGHT_TEXT_COLOR, macros.FONT_SIZE)
        window.update()
        sleep(macros.ANIMATION_DELAY)
        
        if Raiz_No.leftChild is None and Raiz_No.rightChild is None:
            return None

        clearCanvasAndDrawTree()

        if Raiz_No.rightChild is not None:
            createRectangleWithText(canvas, rootPositionX, rootPositionY - 1.5 * macros.NODE_RADIUS,
                                    6.5 * macros.NODE_RADIUS, macros.NODE_RADIUS / 1.5, macros.HIGHLIGHT_COLOR,
                                    "Substituindo com o menor", macros.HIGHLIGHT_TEXT_COLOR, macros.FONT_SIZE / 1.5)

            window.update()
            sleep(macros.ANIMATION_DELAY)

            rightChildPositionX, rightChildPositionY = calculateRightChildPosition(rootPositionX, rootPositionY, nodeDepth + 1)
            Raiz_No.value = getMinNodeValue(Raiz_No.rightChild, 
                                         rightChildPositionX, rightChildPositionY, 
                                         nodeDepth + 1, 
                                         canvas, window)

            createOvalWithText(canvas, rootPositionX, rootPositionY,
                            macros.NODE_RADIUS, macros.HIGHLIGHT_COLOR,
                            Raiz_No.value, macros.HIGHLIGHT_TEXT_COLOR, macros.FONT_SIZE)
            window.update()
            sleep(macros.ANIMATION_DELAY)

            clearCanvasAndDrawTree()

            createRectangleWithText(canvas, rootPositionX, rootPositionY - 1.5 * macros.NODE_RADIUS,
                                    6.5 * macros.NODE_RADIUS, macros.NODE_RADIUS / 1.5, macros.HIGHLIGHT_COLOR,
                                    "Deletando", macros.HIGHLIGHT_TEXT_COLOR, macros.FONT_SIZE / 1.5)

            window.update()
            sleep(ANIMATION_DELAY)

            Raiz_No.rightChild = deleteNode(Raiz_No.rightChild, Raiz_No.value,
                                             rightChildPositionX, rightChildPositionY,
                                             nodeDepth + 1,
                                             canvas, window)
        else:
            createRectangleWithText(canvas, rootPositionX, rootPositionY - 1.5 * macros.NODE_RADIUS,
                                    6.5 * macros.NODE_RADIUS, macros.NODE_RADIUS / 1.5, macros.HIGHLIGHT_COLOR,
                                    "Substituindo pelo maior", macros.HIGHLIGHT_TEXT_COLOR, macros.FONT_SIZE / 1.5)

            window.update()
            sleep(macros.ANIMATION_DELAY)

            leftChildPositionX, leftChildPositionY = calculateLeftChildPosition(rootPositionX, rootPositionY, nodeDepth + 1)
            Raiz_No.value = getMaxNodeValue(Raiz_No.leftChild, 
                                         leftChildPositionX, leftChildPositionY, 
                                         nodeDepth + 1, 
                                         canvas, window)

            createOvalWithText(canvas, rootPositionX, rootPositionY,
                            macros.NODE_RADIUS, macros.HIGHLIGHT_COLOR,
                            Raiz_No.value, macros.HIGHLIGHT_TEXT_COLOR, macros.FONT_SIZE)
            window.update()
            sleep(macros.ANIMATION_DELAY)

            clearCanvasAndDrawTree()

            createRectangleWithText(canvas, rootPositionX, rootPositionY - 1.5 * macros.NODE_RADIUS,
                                    6.5 * macros.NODE_RADIUS, macros.NODE_RADIUS / 1.5, macros.HIGHLIGHT_COLOR,
                                    "<< DELETE DUPLICATE", macros.HIGHLIGHT_TEXT_COLOR, macros.FONT_SIZE / 1.5)

            window.update()
            sleep(macros.ANIMATION_DELAY)

            Raiz_No.leftChild = deleteNode(Raiz_No.leftChild, Raiz_No.value,
                                             leftChildPositionX, leftChildPositionY,
                                             nodeDepth + 1,
                                             canvas, window)
    return Raiz_No


def getMinNodeValue(Raiz_No, rootPositionX, rootPositionY, nodeDepth, canvas, window):

    if Raiz_No.leftChild is None:
        createRectangleWithText(canvas, rootPositionX, rootPositionY - 1.5 * macros.NODE_RADIUS,
                                macros.NODE_RADIUS, macros.NODE_RADIUS / 1.5, macros.HIGHLIGHT_COLOR,
                                "MIN", macros.HIGHLIGHT_TEXT_COLOR, macros.FONT_SIZE / 1.5)
        createOvalWithText(canvas, rootPositionX, rootPositionY,
                            macros.NODE_RADIUS, macros.HIGHLIGHT_COLOR,
                            Raiz_No.value, macros.HIGHLIGHT_TEXT_COLOR, macros.FONT_SIZE)
        window.update()
        sleep(macros.ANIMATION_DELAY)

        return Raiz_No.value
    else:
        createRectangleWithText(canvas, rootPositionX, rootPositionY - 1.5 * macros.NODE_RADIUS,
                                macros.NODE_RADIUS, macros.NODE_RADIUS / 1.5, macros.HIGHLIGHT_COLOR,
                                "<<", macros.HIGHLIGHT_TEXT_COLOR, macros.FONT_SIZE)
        window.update()
        sleep(macros.ANIMATION_DELAY)

        leftChildPositionX, leftChildPositionY = calculateLeftChildPosition(rootPositionX, rootPositionY, nodeDepth + 1)
        return getMinNodeValue(Raiz_No.leftChild, 
                            leftChildPositionX, leftChildPositionY, 
                            nodeDepth + 1, 
                            canvas, window)

    
def getMaxNodeValue(Raiz_No, rootPositionX, rootPositionY, nodeDepth, canvas, window):

    if Raiz_No.rightChild is None:
        createRectangleWithText(canvas, rootPositionX, rootPositionY - 1.5 * macros.NODE_RADIUS,
                                macros.NODE_RADIUS, macros.NODE_RADIUS / 1.5, macros.HIGHLIGHT_COLOR,
                                "MAX", macros.HIGHLIGHT_TEXT_COLOR, macros.FONT_SIZE / 1.5)
        createOvalWithText(canvas, rootPositionX, rootPositionY,
                            macros.NODE_RADIUS, macros.HIGHLIGHT_COLOR,
                            Raiz_No.value, macros.HIGHLIGHT_TEXT_COLOR, macros.FONT_SIZE)
        window.update()
        sleep(macros.ANIMATION_DELAY)

        return Raiz_No.value
    else:
        createRectangleWithText(canvas, rootPositionX, rootPositionY - 1.5 * macros.NODE_RADIUS,
                                macros.NODE_RADIUS, macros.NODE_RADIUS / 1.5, macros.HIGHLIGHT_COLOR,
                                ">>", macros.HIGHLIGHT_TEXT_COLOR, macros.FONT_SIZE)
        window.update()
        sleep(macros.ANIMATION_DELAY)

        rightChildPositionX, rightChildPositionY = calculateRightChildPosition(rootPositionX, rootPositionY, nodeDepth + 1)
        return getMaxNodeValue(Raiz_No.rightChild, 
                                rightChildPositionX, rightChildPositionY, 
                                nodeDepth + 1, 
                                canvas, window)


