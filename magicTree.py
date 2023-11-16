from cgitb import enable
from lib2to3.pgen2.token import NUMBER
from tkinter import *
import tkinter as tk
from tkinter import ttk, Text
from random import randint
from time import sleep
from tkinter.messagebox import showerror, showinfo
from tkinter.tix import IMAGETEXT
from venv import create

#macros de valores
NODE_RADIUS = 30
BACKGROUND_COLOR = "white"
NODE_COLOR = "black"
HIGHLIGHT_COLOR = "green"
HIGHLIGHT_TEXT_COLOR = "yellow"
TEXT_COLOR = "red"
LINE_COLOR = "black"
FONT_SIZE = 20
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 700
X_PADDING = 150
Y_PADDING = NODE_RADIUS * 4 + 5
#MAX_DEPTH maior q 4 gera erro de desenho, ainda não consegui resolver esse problema
MAX_DEPTH = 4
MAX_VALUE = 100
MIN_VALUE = 0
ANIMATION_DELAY = 1


noduloRaiz = None

class Nodulo:
    def __init__(self, valor):
        self.valor = valor
        self.filho_esquerda = None
        self.filho_direita = None


def calcularPosicaoFilhoEsquerda(raizPosicaoX, raizPosicaoY, noduloAltura):
    """
    Calcula a posição do filho à esquerda de um nódulo em uma árvore binária.

    Parameters:
    - raizPosicaoX (float): A coordenada X da posição da raiz do nódulo.
    - raizPosicaoY (float): A coordenada Y da posição da raiz do nódulo.
    - noduloAltura (int): A altura do nódulo na árvore.

    Returns:
    tuple: Uma tupla contendo as coordenadas (X, Y) do filho à esquerda.
    """
    
    posicaoFihloEsquerdaX = (raizPosicaoX - ( (WINDOW_WIDTH - X_PADDING) / pow(2, noduloAltura) ) / 2)
    posicaoFilhoEsquerdaY = raizPosicaoY + NODE_RADIUS * 4
    
    return (posicaoFihloEsquerdaX, posicaoFilhoEsquerdaY)

def calcularPosicaoFilhoDireita(raizPosicaoX, raizPosicaoY, noduloAltura):
    """
    Calcula a posição do filho à direita em uma árvore binária com base na posição da raiz e na altura do nódulo.

    Parâmetros:
    - raizPosicaoX (float): A coordenada X da posição da raiz.
    - raizPosicaoY (float): A coordenada Y da posição da raiz.
    - noduloAltura (int): A altura do nódulo na árvore.

    Retorna:
    tuple: Uma tupla contendo as coordenadas (X, Y) do filho à direita.
    """
    
    posicaoFilhoDireitaX = (raizPosicaoX + ( (WINDOW_WIDTH - X_PADDING) / pow(2, noduloAltura) ) / 2)
    posicaoFilhoDireitaY = raizPosicaoY + NODE_RADIUS * 4
    
    return (posicaoFilhoDireitaX, posicaoFilhoDireitaY)

def inserirNodulo(noduloRaiz, valor, posicaoRaizX, posicaoRaizY, noduloAltura, canvas, window):
    """
    Insere um novo nó em uma árvore binária de busca.

    Parameters:
    - noduloRaiz (Nodulo): O nó raiz da árvore onde o novo nó será inserido.
    - valor (int): O valor do novo nó a ser inserido na árvore.
    - posicaoRaizX (int): A posição X do nó raiz na interface gráfica.
    - posicaoRaizY (int): A posição Y do nó raiz na interface gráfica.
    - noduloAltura (int): A altura atual do nó na árvore.
    - canvas: O objeto de tela onde os elementos gráficos serão desenhados.
    - window: A janela gráfica onde a árvore será exibida.

    Returns:
    - Nodulo: O nó raiz da árvore após a inserção do novo nó.

    Raises:
    - tkinter.TclError: Se ocorrer um erro relacionado ao canvas ou à janela gráfica.
    - tkinter.messagebox.showinfo: Se a altura máxima da árvore for atingida, uma mensagem será exibida.

    """

    if noduloAltura > MAX_DEPTH:
        showinfo(title="Inserir", message="Altura Máxima alcançada")
        
        return noduloRaiz

    if noduloRaiz is None:
        noduloRaiz = Nodulo(valor)
        
        return noduloRaiz

    createOvalWithText(
        canvas,
        posicaoRaizX, 
        posicaoRaizY - 3 * NODE_RADIUS, 
        NODE_RADIUS, HIGHLIGHT_COLOR, 
        valor, 
        HIGHLIGHT_TEXT_COLOR, 
        FONT_SIZE,
    )
    window.update()
    sleep(ANIMATION_DELAY)

    if valor < noduloRaiz.valor:
        createRectangleWithText(
            canvas,
            posicaoRaizX,
            posicaoRaizY - 1.5 * NODE_RADIUS,
            NODE_RADIUS / 1.5,
            NODE_RADIUS / 1.5,
            HIGHLIGHT_COLOR,
            "<",
            HIGHLIGHT_TEXT_COLOR,
            FONT_SIZE,
        )
        window.update()
        sleep(ANIMATION_DELAY)

        posicaoFihloEsquerdaX, posicaoFilhoEsquerdaY = calcularPosicaoFilhoEsquerda(posicaoRaizX, posicaoRaizY, noduloAltura + 1)
        
        noduloRaiz.filho_esquerda = inserirNodulo(noduloRaiz.filho_esquerda,valor,posicaoFihloEsquerdaX,posicaoFilhoEsquerdaY,noduloAltura + 1,canvas,window)
    
    elif valor > noduloRaiz.valor:
        createRectangleWithText(
            canvas,
            posicaoRaizX,
            posicaoRaizY - 1.5 * NODE_RADIUS,
            NODE_RADIUS / 1.5,
            NODE_RADIUS / 1.5,
            HIGHLIGHT_COLOR,
            ">",
            HIGHLIGHT_TEXT_COLOR,
            FONT_SIZE,
        )
        window.update()
        sleep(ANIMATION_DELAY)

        posicaoFilhoDireitaX, posicaoFilhoDireitaY = calcularPosicaoFilhoDireita(posicaoRaizX, posicaoRaizY, noduloAltura + 1)
        noduloRaiz.filho_direita = inserirNodulo(noduloRaiz.filho_direita, valor, posicaoFilhoDireitaX, posicaoFilhoDireitaY, noduloAltura + 1, canvas, window)
    
    elif valor == noduloRaiz.valor:
        showinfo(title="Inserir", message="Nodulo já está na árvore")

    return noduloRaiz

def inserirNoduloSemAnimacao(noduloRaiz, valor, noduloAltura):
    """
    Insere um novo nódulo em uma árvore binária de busca sem animação.

    Args:
    - noduloRaiz (Nodulo): A raiz da árvore onde o novo nódulo será inserido.
    - valor (any): O valor a ser armazenado no novo nódulo.
    - noduloAltura (int): A altura atual do nódulo na árvore.

    Returns:
    - Nodulo: A raiz da árvore atualizada após a inserção do novo nódulo.

    Note:
    - Se a altura do nódulo atingir o limite definido por MAX_DEPTH, a inserção será interrompida.
    - A função assume que a classe Nodulo já foi definida com atributos 'valor', 'filho_esquerda' e 'filho_direita'.
    """
    
    if noduloAltura > MAX_DEPTH:
        return noduloRaiz

    if noduloRaiz is None:
        noduloRaiz = Nodulo(valor)
        return noduloRaiz

    if valor < noduloRaiz.valor:
        noduloRaiz.filho_esquerda = inserirNoduloSemAnimacao(
            noduloRaiz.filho_esquerda, valor, noduloAltura + 1
        )
    elif valor > noduloRaiz.valor:
        noduloRaiz.filho_direita = inserirNoduloSemAnimacao(
            noduloRaiz.filho_direita, valor, noduloAltura + 1
        )

    return noduloRaiz

def buscaArvore(noduloRaiz, valor, posicaoRaizX, posicaoRaizY, noduloAltura, canvas, window):
    """
    Busca um valor em uma árvore binária e destaca visualmente a busca.

    Parameters:
    - noduloRaiz (TreeNode): O nó raiz da árvore.
    - valor (int): O valor a ser procurado na árvore.
    - posicaoRaizX (float): A posição X do nó raiz no canvas.
    - posicaoRaizY (float): A posição Y do nó raiz no canvas.
    - noduloAltura (int): A altura do nó raiz na árvore.
    - canvas (Canvas): O objeto Canvas onde desenhar a árvore.
    - window (Tk): A janela principal da aplicação.

    Returns:
    - None

    Destaca visualmente a busca na árvore, exibindo setas e realçando nós conforme a busca é realizada.
    """
    
    if noduloRaiz is None:
        showinfo(title="Buscar", message="Nodulo não encontrado")
        return

    createOvalWithText(
        canvas,
        posicaoRaizX,
        posicaoRaizY - 3 * NODE_RADIUS,
        NODE_RADIUS,
        HIGHLIGHT_COLOR,
        valor,
        HIGHLIGHT_TEXT_COLOR,
        FONT_SIZE,
    )
    window.update()
    sleep(ANIMATION_DELAY)

    if valor < noduloRaiz.valor:
        createRectangleWithText(
            canvas,
            posicaoRaizX,
            posicaoRaizY - 1.5 * NODE_RADIUS,
            NODE_RADIUS / 1.5,
            NODE_RADIUS / 1.5,
            HIGHLIGHT_COLOR,
            "<",
            HIGHLIGHT_TEXT_COLOR,
            FONT_SIZE,
        )
        window.update()
        sleep(ANIMATION_DELAY)

        posicaoFihloEsquerdaX, posicaoFilhoEsquerdaY = calcularPosicaoFilhoEsquerda(
            posicaoRaizX, posicaoRaizY, noduloAltura + 1
        )
        buscaArvore(
            noduloRaiz.filho_esquerda,
            valor,
            posicaoFihloEsquerdaX,
            posicaoFilhoEsquerdaY,
            noduloAltura + 1,
            canvas,
            window,
        )
    elif valor > noduloRaiz.valor:
        createRectangleWithText(
            canvas,
            posicaoRaizX,
            posicaoRaizY - 1.5 * NODE_RADIUS,
            NODE_RADIUS / 1.5,
            NODE_RADIUS / 1.5,
            HIGHLIGHT_COLOR,
            ">",
            HIGHLIGHT_TEXT_COLOR,
            FONT_SIZE,
        )
        window.update()
        sleep(ANIMATION_DELAY)

        posicaoFilhoDireitaX, posicaoFilhoDireitaY = calcularPosicaoFilhoDireita(
            posicaoRaizX, posicaoRaizY, noduloAltura + 1
        )
        buscaArvore(
            noduloRaiz.filho_direita,
            valor,
            posicaoFilhoDireitaX,
            posicaoFilhoDireitaY,
            noduloAltura + 1,
            canvas,
            window,
        )
    elif valor == noduloRaiz.valor:
        createRectangleWithText(
            canvas,
            posicaoRaizX,
            posicaoRaizY - 1.5 * NODE_RADIUS,
            NODE_RADIUS / 1.5,
            NODE_RADIUS / 1.5,
            HIGHLIGHT_COLOR,
            "=",
            HIGHLIGHT_TEXT_COLOR,
            FONT_SIZE,
        )
        createOvalWithText(
            canvas,
            posicaoRaizX,
            posicaoRaizY,
            NODE_RADIUS,
            HIGHLIGHT_COLOR,
            valor,
            HIGHLIGHT_TEXT_COLOR,
            FONT_SIZE,
        )
        window.update()
        sleep(ANIMATION_DELAY)

def deletarNodulo(noduloRaiz, valor, posicaoRaizX, posicaoRaizY, noduloAltura, canvas, window):
    """
    Deleta um nódulo com um valor específico de uma árvore binária de busca.

    Parameters:
    - noduloRaiz (Node): O nódulo raiz da árvore.
    - valor (int): O valor a ser deletado.
    - posicaoRaizX (float): A posição X do nódulo raiz no canvas.
    - posicaoRaizY (float): A posição Y do nódulo raiz no canvas.
    - noduloAltura (int): A altura atual do nódulo na árvore.
    - canvas (Canvas): O objeto de tela onde a árvore está sendo desenhada.
    - window (Tk): A janela Tkinter associada ao canvas.

    Returns:
    - Node or None: O nódulo raiz atualizado após a deleção.
    """

    if noduloRaiz is None:
        showinfo(title="Deletar", message="Nodulo não encontrado")
        
        return None

    createOvalWithText(
        canvas,
        posicaoRaizX,
        posicaoRaizY - 3 * NODE_RADIUS,
        NODE_RADIUS,
        HIGHLIGHT_COLOR,
        valor,
        HIGHLIGHT_TEXT_COLOR,
        FONT_SIZE,
    )
    window.update()
    sleep(ANIMATION_DELAY)

    if valor < noduloRaiz.valor:
        createRectangleWithText(
            canvas,
            posicaoRaizX,
            posicaoRaizY - 1.5 * NODE_RADIUS,
            NODE_RADIUS / 1.5,
            NODE_RADIUS / 1.5,
            HIGHLIGHT_COLOR,
            "<",
            HIGHLIGHT_TEXT_COLOR,
            FONT_SIZE,
        )
        window.update()
        sleep(ANIMATION_DELAY)

        posicaoFihloEsquerdaX, posicaoFilhoEsquerdaY = calcularPosicaoFilhoEsquerda(posicaoRaizX, posicaoRaizY, noduloAltura + 1)

        noduloRaiz.filho_esquerda = deletarNodulo(noduloRaiz.filho_esquerda, valor, posicaoFihloEsquerdaX, posicaoFilhoEsquerdaY, noduloAltura + 1, canvas, window)
    
    elif valor > noduloRaiz.valor:
        createRectangleWithText(
            canvas,
            posicaoRaizX,
            posicaoRaizY - 1.5 * NODE_RADIUS,
            NODE_RADIUS / 1.5,
            NODE_RADIUS / 1.5,
            HIGHLIGHT_COLOR,
            ">",
            HIGHLIGHT_TEXT_COLOR,
            FONT_SIZE,
        )
        window.update()
        sleep(ANIMATION_DELAY)

        posicaoFilhoDireitaX, posicaoFilhoDireitaY = calcularPosicaoFilhoDireita(posicaoRaizX, posicaoRaizY, noduloAltura + 1)
        noduloRaiz.filho_direita = deletarNodulo(noduloRaiz.filho_direita,valor,posicaoFilhoDireitaX,posicaoFilhoDireitaY,noduloAltura + 1,canvas,window,
        )
    elif valor == noduloRaiz.valor:
        createRectangleWithText(
            canvas,
            posicaoRaizX,
            posicaoRaizY - 1.5 * NODE_RADIUS,
            NODE_RADIUS / 1.5,
            NODE_RADIUS / 1.5,
            HIGHLIGHT_COLOR,
            "=",
            HIGHLIGHT_TEXT_COLOR,
            FONT_SIZE,
        )
        createOvalWithText(
            canvas,
            posicaoRaizX,
            posicaoRaizY,
            NODE_RADIUS,
            HIGHLIGHT_COLOR,
            valor,
            HIGHLIGHT_TEXT_COLOR,
            FONT_SIZE,
        )
        window.update()
        sleep(ANIMATION_DELAY)

        if noduloRaiz.filho_esquerda is None and noduloRaiz.filho_direita is None:
            return None

        clearCanvasAndDrawTree()

        if noduloRaiz.filho_direita is not None:
            createRectangleWithText(
                canvas,
                posicaoRaizX,
                posicaoRaizY - 1.5 * NODE_RADIUS,
                6.5 * NODE_RADIUS,
                NODE_RADIUS / 1.5,
                HIGHLIGHT_COLOR,
                "Substituindo pelo menor >>",
                HIGHLIGHT_TEXT_COLOR,
                FONT_SIZE / 1.5,
            )

            window.update()
            sleep(ANIMATION_DELAY)

            posicaoFilhoDireitaX, posicaoFilhoDireitaY = calcularPosicaoFilhoDireita(posicaoRaizX, posicaoRaizY, noduloAltura + 1)
            noduloRaiz.valor = pegarMenorValorNodulo(
                noduloRaiz.filho_direita,
                posicaoFilhoDireitaX,
                posicaoFilhoDireitaY,
                noduloAltura + 1,
                canvas,
                window,
            )

            createOvalWithText(
                canvas,
                posicaoRaizX,
                posicaoRaizY,
                NODE_RADIUS,
                HIGHLIGHT_COLOR,
                noduloRaiz.valor,
                HIGHLIGHT_TEXT_COLOR,
                FONT_SIZE,
            )
            window.update()
            sleep(ANIMATION_DELAY)

            clearCanvasAndDrawTree()

            createRectangleWithText(
                canvas,
                posicaoRaizX,
                posicaoRaizY - 1.5 * NODE_RADIUS,
                6.5 * NODE_RADIUS,
                NODE_RADIUS / 1.5,
                HIGHLIGHT_COLOR,
                "Deletando Duplicata >>",
                HIGHLIGHT_TEXT_COLOR,
                FONT_SIZE / 1.5,
            )

            window.update()
            sleep(ANIMATION_DELAY)

            noduloRaiz.filho_direita = deletarNodulo(noduloRaiz.filho_direita,noduloRaiz.valor,posicaoFilhoDireitaX,posicaoFilhoDireitaY,noduloAltura + 1,canvas,window)
        
        else:
            createRectangleWithText(
                canvas,
                posicaoRaizX,
                posicaoRaizY - 1.5 * NODE_RADIUS,
                6.5 * NODE_RADIUS,
                NODE_RADIUS / 1.5,
                HIGHLIGHT_COLOR,
                "<< Substituindo pelo maior",
                HIGHLIGHT_TEXT_COLOR,
                FONT_SIZE / 1.5,
            )

            window.update()
            sleep(ANIMATION_DELAY)

            posicaoFihloEsquerdaX, posicaoFilhoEsquerdaY = calcularPosicaoFilhoEsquerda(posicaoRaizX, posicaoRaizY, noduloAltura + 1)
            
            noduloRaiz.valor = pegarMaiorValorNodulo(noduloRaiz.filho_esquerda,posicaoFihloEsquerdaX,posicaoFilhoEsquerdaY,noduloAltura + 1,canvas,window)

            createOvalWithText(
                canvas,
                posicaoRaizX,
                posicaoRaizY,
                NODE_RADIUS,
                HIGHLIGHT_COLOR,
                noduloRaiz.valor,
                HIGHLIGHT_TEXT_COLOR,
                FONT_SIZE,
            )
            window.update()
            sleep(ANIMATION_DELAY)

            clearCanvasAndDrawTree()

            createRectangleWithText(
                canvas,
                posicaoRaizX,
                posicaoRaizY - 1.5 * NODE_RADIUS,
                6.5 * NODE_RADIUS,
                NODE_RADIUS / 1.5,
                HIGHLIGHT_COLOR,
                "<< Deletando Duplicata",
                HIGHLIGHT_TEXT_COLOR,
                FONT_SIZE / 1.5,
            )

            window.update()
            sleep(ANIMATION_DELAY)

            noduloRaiz.filho_esquerda = deletarNodulo(noduloRaiz.filho_esquerda,noduloRaiz.valor,posicaoFihloEsquerdaX,posicaoFilhoEsquerdaY,noduloAltura + 1,canvas,window)
    
    return noduloRaiz

def pegarMenorValorNodulo(noduloRaiz, posicaoRaizX, posicaoRaizY, noduloAltura, canvas, window):
    """
    Retorna o menor valor presente na árvore a partir do nódulo raiz.

    Parameters:
        noduloRaiz (Nodulo): O nódulo raiz da árvore.
        posicaoRaizX (float): A posição X do centro do nódulo raiz no canvas.
        posicaoRaizY (float): A posição Y do centro do nódulo raiz no canvas.
        noduloAltura (int): A altura atual do nódulo na árvore.
        canvas (Canvas): O objeto de canvas onde os elementos visuais serão desenhados.
        window (Tkinter.Tk): A janela da aplicação.

    Returns:
        int: O menor valor presente na árvore.

    Note:
        Esta função assume a existência de funções auxiliares, como `createRectangleWithText`,
        `createOvalWithText`, e `calcularPosicaoFilhoEsquerda`, para criar elementos visuais
        na interface gráfica.
    """

    if noduloRaiz.filho_esquerda is None:
        createRectangleWithText(
            canvas,
            posicaoRaizX,
            posicaoRaizY - 1.5 * NODE_RADIUS,
            NODE_RADIUS,
            NODE_RADIUS / 1.5,
            HIGHLIGHT_COLOR,
            "Menor",
            HIGHLIGHT_TEXT_COLOR,
            FONT_SIZE / 1.5,
        )
        createOvalWithText(
            canvas,
            posicaoRaizX,
            posicaoRaizY,
            NODE_RADIUS,
            HIGHLIGHT_COLOR,
            noduloRaiz.valor,
            HIGHLIGHT_TEXT_COLOR,
            FONT_SIZE,
        )
        window.update()
        sleep(ANIMATION_DELAY)

        return noduloRaiz.valor
    else:
        createRectangleWithText(
            canvas,
            posicaoRaizX,
            posicaoRaizY - 1.5 * NODE_RADIUS,
            NODE_RADIUS,
            NODE_RADIUS / 1.5,
            HIGHLIGHT_COLOR,
            "<<",
            HIGHLIGHT_TEXT_COLOR,
            FONT_SIZE,
        )
        window.update()
        sleep(ANIMATION_DELAY)

        posicaoFihloEsquerdaX, posicaoFilhoEsquerdaY = calcularPosicaoFilhoEsquerda(posicaoRaizX, posicaoRaizY, noduloAltura + 1)
        
        return pegarMenorValorNodulo(noduloRaiz.filho_esquerda,posicaoFihloEsquerdaX,posicaoFilhoEsquerdaY,noduloAltura + 1,canvas,window)

def pegarMaiorValorNodulo(noduloRaiz, posicaoRaizX, posicaoRaizY, noduloAltura, canvas, window):
    """
    Encontra e destaca o nódulo com o maior valor na árvore a partir do nódulo raiz.

    Parameters:
    - noduloRaiz (objeto Nodulo): O nódulo raiz da árvore.
    - posicaoRaizX (float): A posição X do nódulo raiz no canvas.
    - posicaoRaizY (float): A posição Y do nódulo raiz no canvas.
    - noduloAltura (int): A altura do nódulo na árvore.
    - canvas (objeto Canvas): O canvas onde os elementos gráficos são desenhados.
    - window (objeto Window): A janela da aplicação.

    Returns:
    - int: O valor do nódulo com o maior valor na árvore.
    """

    if noduloRaiz.filho_direita is None:
        createRectangleWithText(
            canvas,
            posicaoRaizX,
            posicaoRaizY - 1.5 * NODE_RADIUS,
            NODE_RADIUS,
            NODE_RADIUS / 1.5,
            HIGHLIGHT_COLOR,
            "Maior",
            HIGHLIGHT_TEXT_COLOR,
            FONT_SIZE / 1.5,
        )
        createOvalWithText(
            canvas,
            posicaoRaizX,
            posicaoRaizY,
            NODE_RADIUS,
            HIGHLIGHT_COLOR,
            noduloRaiz.valor,
            HIGHLIGHT_TEXT_COLOR,
            FONT_SIZE,
        )
        window.update()
        sleep(ANIMATION_DELAY)

        return noduloRaiz.valor
    else:
        createRectangleWithText(
            canvas,
            posicaoRaizX,
            posicaoRaizY - 1.5 * NODE_RADIUS,
            NODE_RADIUS,
            NODE_RADIUS / 1.5,
            HIGHLIGHT_COLOR,
            ">>",
            HIGHLIGHT_TEXT_COLOR,
            FONT_SIZE,
        )
        window.update()
        sleep(ANIMATION_DELAY)

        posicaoFilhoDireitaX, posicaoFilhoDireitaY = calcularPosicaoFilhoDireita(posicaoRaizX, posicaoRaizY, noduloAltura + 1)
        
        return pegarMaiorValorNodulo(noduloRaiz.filho_direita,posicaoFilhoDireitaX,posicaoFilhoDireitaY,noduloAltura + 1,canvas,window)

def desenhaArvore(noduloRaiz, posicaoRaizX, posicaoRaizY, noduloAltura, canvas, window):
    """
    Desenha uma árvore binária na tela usando a biblioteca tkinter.

    Parâmetros:
    - noduloRaiz (objeto): O nó raiz da árvore a ser desenhada.
    - posicaoRaizX (int): A posição X do nó raiz na tela.
    - posicaoRaizY (int): A posição Y do nó raiz na tela.
    - noduloAltura (int): A altura do nó na árvore.
    - canvas (objeto): O objeto de tela tkinter onde a árvore será desenhada.
    - window (objeto): O objeto de janela tkinter associado à canvas.

    Retorna:
    - None: A função não retorna nenhum valor.

    Comportamento:
    - A função desenha a árvore binária começando pelo nó raiz e conecta os nós
      com linhas representando as relações entre eles.
    - A árvore é desenhada recursivamente, percorrendo os filhos esquerdo e direito
      de cada nó.
    - A função utiliza outras funções auxiliares para calcular as posições dos filhos
      e criar os elementos visuais na tela.

    """
    
    if noduloRaiz is None:
        return

    if noduloRaiz.filho_esquerda is not None:
        posicaoFihloEsquerdaX, posicaoFilhoEsquerdaY = calcularPosicaoFilhoEsquerda(posicaoRaizX, posicaoRaizY, noduloAltura + 1)
        
        canvas.create_line(
            posicaoRaizX,
            posicaoRaizY,
            posicaoFihloEsquerdaX,
            posicaoFilhoEsquerdaY,
            fill=LINE_COLOR,
            width=5,
        )
        
        desenhaArvore(noduloRaiz.filho_esquerda,posicaoFihloEsquerdaX,posicaoFilhoEsquerdaY,noduloAltura + 1,canvas,window)

    if noduloRaiz.filho_direita is not None:
        posicaoFilhoDireitaX, posicaoFilhoDireitaY = calcularPosicaoFilhoDireita(posicaoRaizX, posicaoRaizY, noduloAltura + 1)
        
        canvas.create_line(
            posicaoRaizX,
            posicaoRaizY,
            posicaoFilhoDireitaX,
            posicaoFilhoDireitaY,
            fill=LINE_COLOR,
            width=5,
        )

        desenhaArvore(noduloRaiz.filho_direita,posicaoFilhoDireitaX,posicaoFilhoDireitaY,noduloAltura + 1,canvas,window)

    createOvalWithText(
        canvas,
        posicaoRaizX,
        posicaoRaizY,
        NODE_RADIUS,
        NODE_COLOR,
        noduloRaiz.valor,
        TEXT_COLOR,
        FONT_SIZE,
    )
    window.update()

def clearCanvasAndDrawTree():
    """
    Limpa o conteúdo do canvas e desenha a árvore novamente.

    Esta função define as coordenadas iniciais da árvore no canvas e, em seguida,
    apaga todo o conteúdo atual do canvas. Em seguida, chama a função desenhaArvore
    para desenhar a árvore com base nas informações fornecidas.

    Parameters:
    - Nenhum parâmetro é necessário diretamente, mas a função depende das seguintes variáveis globais:
        - noduloRaiz: O nódulo raiz da árvore a ser desenhada.
        - WINDOW_WIDTH: A largura da janela onde a árvore será desenhada.
        - Y_PADDING: O espaçamento vertical a ser aplicado entre o topo da janela e a árvore.
        - canvas: O objeto de canvas onde a árvore será desenhada.
        - window: A janela principal onde o canvas está contido.

    Returns:
    - Nenhum valor de retorno.

    Exemplo de Uso:
    clearCanvasAndDrawTree()
    """


    treePositionX = WINDOW_WIDTH / 2
    treePositionY = Y_PADDING
    canvas.delete("all")
    desenhaArvore(noduloRaiz, treePositionX, treePositionY, 0, canvas, window)

def createOvalWithText(canvas, centerX, centerY, radius, ovalColor, text, textColor, fontSize):
    """
    Cria um objeto oval preenchido com uma etiqueta de texto no canvas.

    Parâmetros:
    - canvas (Tkinter.Canvas): O canvas no qual o oval e o texto serão criados.
    - centerX (int): A coordenada x do centro do oval.
    - centerY (int): A coordenada y do centro do oval.
    - radius (int): O raio do oval.
    - ovalColor (str): A cor de preenchimento do oval (formato de string, ex: "red").
    - text (str): O texto a ser exibido no centro do oval.
    - textColor (str): A cor do texto (formato de string, ex: "black").
    - fontSize (int): O tamanho da fonte do texto.

    Retorna:
    - None: A função apenas cria objetos no canvas, não retorna valores.
    """
    
    oval = canvas.create_oval(
        centerX - radius,
        centerY - radius,
        centerX + radius,
        centerY + radius,
        fill=ovalColor,
        width=0,
    )
    text = canvas.create_text(
        centerX,
        centerY,
        text=text,
        fill=textColor,
        font=("Arial " + str(int(fontSize)) + " bold"),
    )

def createRectangleWithText(canvas, centerX, centerY, width, height, rectangleColor, text, textColor, fontSize):
    """
    Cria um retângulo com texto em um canvas.

    Parâmetros:
    - canvas: O objeto canvas onde o retângulo com texto será desenhado.
    - centroX: A coordenada X do centro do retângulo.
    - centroY: A coordenada Y do centro do retângulo.
    - largura: A largura do retângulo.
    - altura: A altura do retângulo.
    - corRetangulo: A cor de preenchimento do retângulo (formato '#RRGGBB').
    - texto: O texto a ser exibido no centro do retângulo.
    - corTexto: A cor do texto (formato '#RRGGBB').
    - tamanhoFonte: O tamanho da fonte do texto.
    """
    
    canvas.create_rectangle(
        centerX - width / 2,
        centerY - height / 2,
        centerX + width / 2,
        centerY + height / 2,
        fill=rectangleColor,
        width=0,
    )
    canvas.create_text(
        centerX,
        centerY,
        text=text,
        fill=textColor,
        font=("Arial " + str(int(fontSize)) + " bold"),
    )

def validarEntrada(valor) -> bool:
    """
    Valida a entrada para garantir que seja um número inteiro dentro de limites específicos.

    Parameters:
    - valor: O valor a ser validado.

    Returns:
    - True se a entrada for válida, False caso contrário.
    """

    try:
        valor = int(valor)
    except ValueError:
        showerror(title="Erro!", message="Entrada inválida")
        return False

    if valor > MAX_VALUE:
        showerror(title="Erro!", message="Entrada excedeu o máximo permitido")
        return False
    if valor < MIN_VALUE:
        showerror(title="Erro!", message="Entrada menor que o mínimo permitido")
        return False
    return True

def botaoInserir(valor):
    """
    Insere um valor na árvore binária global, desenhando a árvore após a inserção.

    Parâmetros:
    - valor (int): O valor a ser inserido na árvore.

    Retorna:
    - None

    A função verifica se a entrada é válida, converte o valor para inteiro,
    desativa a interface gráfica, insere o valor na árvore binária global
    e, em seguida, redesenha a árvore na interface gráfica após a inserção.
    """
    
    global noduloRaiz

    if not validarEntrada(valor):
        return

    valor = int(valor)

    posicaoRaizX = WINDOW_WIDTH / 2
    posicaoRaizY = Y_PADDING

    desativarInterface()

    noduloRaiz = inserirNodulo(
        noduloRaiz, valor, posicaoRaizX, posicaoRaizY, 0, canvas, window
    )

    sleep(1)

    canvas.delete("all")
    desenhaArvore(noduloRaiz, posicaoRaizX, posicaoRaizY, 0, canvas, window)

    habilitarInterface()

def botaoBuscar(valor):
    """
    Realiza uma busca na árvore, destacando o caminho até o nódulo com o valor especificado.

    Parameters:
    - valor (int): O valor a ser buscado na árvore.

    Returns:
    - None

    Raises:
    - Nenhum

    O método valida a entrada, converte o valor para inteiro, e inicia o processo de busca na árvore.
    Após a busca, a interface é desativada temporariamente para destacar o caminho encontrado.
    Após 1 segundo de pausa, a interface é reativada, e a árvore é redesenhada para refletir o estado original.
    """
    
    if not validarEntrada(valor):
        return

    valor = int(valor)

    posicaoRaizX = WINDOW_WIDTH / 2
    posicaoRaizY = Y_PADDING

    desativarInterface()

    buscaArvore(noduloRaiz, valor, posicaoRaizX, posicaoRaizY, 0, canvas, window)

    sleep(1)

    canvas.delete("all")
    desenhaArvore(noduloRaiz, posicaoRaizX, posicaoRaizY, 0, canvas, window)

    habilitarInterface()

def botaoDeletar(valor):
    """
    Função responsável por deletar um nó com o valor especificado da árvore e atualizar a representação gráfica da mesma.

    Parâmetros:
    - valor (int): O valor do nó a ser deletado.

    Global:
    - noduloRaiz: Variável global que representa o nó raiz da árvore.

    Nota:
    Antes de chamar esta função, é necessário garantir que a entrada seja válida usando a função validarEntrada.
    """

    global noduloRaiz

    if not validarEntrada(valor):
        return

    valor = int(valor)

    posicaoRaizX = WINDOW_WIDTH / 2
    posicaoRaizY = Y_PADDING

    desativarInterface()

    noduloRaiz = deletarNodulo(
        noduloRaiz, valor, posicaoRaizX, posicaoRaizY, 0, canvas, window
    )

    sleep(1)

    canvas.delete("all")
    desenhaArvore(noduloRaiz, posicaoRaizX, posicaoRaizY, 0, canvas, window)

    habilitarInterface()

def botaoGerarArvoreAleatoria():
    """
    Gera uma árvore binária de busca aleatória e a desenha no canvas.

    Esta função utiliza a função `inserirNoduloSemAnimacao` para inserir valores
    aleatórios na árvore. A quantidade de inserções é determinada aleatoriamente
    entre 1 e 100 e dependerá do MAX_DEPTH.

    Parameters:
    - Nenhum parâmetro é necessário.

    Global Variables:
    - `noduloRaiz`: A variável global que armazena a raiz da árvore.

    Returns:
    - Nenhum valor é retornado.

    Side Effects:
    - Atualiza a variável global `noduloRaiz`.
    - Limpa o canvas e desenha a árvore gerada.
    """
    
    global noduloRaiz

    noduloRaiz = None

    numberOfInserts = randint(100, 100)

    for x in range(numberOfInserts):
        nodeValue = randint(MIN_VALUE, MAX_VALUE)
        noduloRaiz = inserirNoduloSemAnimacao(noduloRaiz, nodeValue, 0)

    posicaoRaizX = WINDOW_WIDTH / 2
    posicaoRaizY = Y_PADDING

    canvas.delete("all")
    desenhaArvore(noduloRaiz, posicaoRaizX, posicaoRaizY, 0, canvas, window)

def desativarInterface():
    """
    Desativa a interface gráfica ao configurar o estado de diversos elementos.

    Esta função desabilita vários elementos da interface gráfica, tornando-os inativos.

    Exemplo de uso:
    desativarInterface()

    Parâmetros:
    - Nenhum

    Retorno:
    - Nenhum
    """
    
    inserir["state"] = DISABLED
    gerarArvoreAleatoria["state"] = DISABLED
    deletar["state"] = DISABLED
    buscar["state"] = DISABLED
    entrada["state"] = DISABLED

def habilitarInterface():
    """
    Função responsável por habilitar a interface gráfica, tornando os elementos interativos.

    Atributos:
        Nenhum.

    Retorna:
        Nenhum.

    Exemplo:
        habilitarInterface()
    """
   
    inserir["state"] = NORMAL
    gerarArvoreAleatoria["state"] = NORMAL
    deletar["state"] = NORMAL
    buscar["state"] = NORMAL
    entrada["state"] = NORMAL

def abrir_janela_principal():
    """
    Fecha a janela de boas-vindas e exibe a janela principal.

    Esta função é responsável por destruir a janela de boas-vindas (janela_bem_vindo)
    e mostrar a janela principal usando a função mostrar_janela_principal().

    Nota:
    Certifique-se de que a função mostrar_janela_principal() esteja definida antes
    de chamar esta função.
    """

    janela_bem_vindo.destroy()
    mostrar_janela_principal()

def mostrar_janela_principal():
    """
    Mostra a janela principal, restaurando-a de um estado minimizado ou oculto.

    Parâmetros:
    - Nenhum

    Retorno:
    - Nenhum

    Exceções:
    - Nenhuma

    Descrição:
    Esta função desminimiza ou desoculta a janela principal que foi anteriormente minimizada
    ou oculta usando a função `iconify` ou `withdraw`. Isso é útil para restaurar a
    visibilidade da janela principal quando necessário.
    """
    
    window.deiconify()

def botaoItens(none):
    """
    Função que cria uma janela gráfica exibindo informações sobre itens mágicos.

    Parâmetros:
    - none: Parâmetro não utilizado.

    A janela exibe descrições e atributos de vários itens mágicos, como espadas, capas e escudos.
    Cada item é apresentado com seu nome, descrição, dano de ataque, dano de defesa e se é mágico.

    Além disso, uma imagem representativa de uma espada é exibida à esquerda da descrição.
    """
    
    janela_item = tk.Tk()
    janela_item.geometry("1200x700")
    janela_item.title("Itens Mágicos")

    description = """A Espada do Gelo de Ned Stark é uma lendária arma forjada com maestria a partir de aço valiriano, um metal precioso e raro. Esta espada é conhecida por sua habilidade única de canalizar o poder do gelo\nDano_ataque = 50\nDano_defesa = 50\nEh_magico = True\nNome = "GELO"\n----------------------------\nDescricao = "Uma capa que torna o usuário invisível. Foi uma das Relíquias da Morte e pertencia a Harry Potter."\nDano_ataque = 0\nDano_defesa = 100\nEh_magico = True\nNome = "Capa da Invisibilidade"\n----------------------------\nDescricao = "Uma série de espadas amaldiçoadas, como a Sandai Kitetsu, a Nidai Kitetsu e a Shodai Kitetsu. Zoro possui a Sandai Kitetsu."\nDano_ataque = 100\nDano_defesa = 0\nEh_magico = True\nNome = "Kitetsu Swords"\n----------------------------\nDescricao = "Um imponente escudo adornado com uma gravura de um sol radiante, simbolizando a luz e a justiça que Leona representa."\nDano_ataque = 20\nDano_defesa = 100\nEh_magico = True\nNome = "Escudo do Dia Quebrado"\n-----------------------------\nDescricao = "As Duplas Espinhosas são um par de pistolas elegantes e mortíferas nas mãos habilidosas de Miss Fortune. Forjadas em uma mistura de metal resistente e encantamentos arcanos."\nDano_ataque = 100\nDano_defesa = 20\nEh_magico = True\nNome = "Duplas Espinhosas"\n----------------------------\n"""

    texto = tk.Label(janela_item, text=description, justify="left", anchor="w")
    texto.pack(pady=20, padx=20)

    image_path = "espadaGELO.jpg"
    imagem1 = Image.open(image_path).resize((50, 50))
    imagem1 = IMAGETEXT.PhotoImage(imagem1)
    label_imagem1 = tk.Label(janela_item, image=imagem1)
    label_imagem1.image = imagem1
    label_imagem1.pack(side=tk.LEFT, padx=10)
    janela_item.mainloop()


janela_bem_vindo = tk.Tk()
janela_bem_vindo.title("Seja Bem-Vindo")
janela_bem_vindo.geometry("1200x700")

label_boas_vindas = ttk.Label(janela_bem_vindo, text="Seja bem-vindo ao Magic Tree!")
label_boas_vindas.pack(pady=20)

botao_iniciar = ttk.Button(
    janela_bem_vindo, text="Iniciar", command=abrir_janela_principal
)
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

# menu lateral
entrada = tk.Entry(menu_frame)
entrada.pack(pady=10)

gerarArvoreAleatoria = ttk.Button(menu_frame, text="Gerar Arvore", command=botaoGerarArvoreAleatoria)
gerarArvoreAleatoria.pack(pady=10)

inserir = ttk.Button(menu_frame, text="Inserir", command=lambda: botaoInserir(entrada.get()))
inserir.pack(pady=10)

deletar = ttk.Button(menu_frame, text="Deletar", command=lambda: botaoDeletar(entrada.get()))
deletar.pack(pady=10)

buscar = ttk.Button(menu_frame, text="Buscar", command=lambda: botaoBuscar(entrada.get()))
buscar.pack(pady=10)

itens = ttk.Button(menu_frame, text="Itens Mágicos", command=lambda: botaoItens(entrada.get()))
itens.pack(pady=10)

# Canvas usando grid
canvas = tk.Canvas(window, width=1000, height=1200, bg="white")
canvas.grid(row=0, column=1, sticky="nsew")

# Configuração de peso para permitir redimensionamento
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)

janela_bem_vindo.mainloop()
