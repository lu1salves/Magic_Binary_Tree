from cgitb import enable
from lib2to3.pgen2.token import NUMBER
from tkinter import *
import tkinter as tk
from random import randint
from time import sleep
from tkinter.messagebox import showerror, showinfo
from venv import create
from tkinter import ttk

NODE_RADIUS = 30
BACKGROUND_COLOR = "white"
NODE_COLOR = "black"
HIGHLIGHT_COLOR = "white"
HIGHLIGHT_TEXT_COLOR = "red"
TEXT_COLOR = "red"
LINE_COLOR = "black"
FONT_SIZE = 20

WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 700
X_PADDING = 150
Y_PADDING = NODE_RADIUS * 4 + 5

MAX_DEPTH = 4
MAX_VALUE = 100
MIN_VALUE = 0

ANIMATION_DELAY = 1

rootNode = None
window = Tk()

class Node:
    def __init__(self, value):
        self.value = value
        self.leftChild = None
        self.rightChild = None

#feito
def calculateLeftChildPosition(parentPositionX, parentPositionY, childDepth):
    leftChildPositionX = parentPositionX - ((WINDOW_WIDTH - X_PADDING) / pow(2, childDepth)) / 2
    leftChildPositionY = parentPositionY + NODE_RADIUS * 4
    return (leftChildPositionX, leftChildPositionY)

#feito
def calculateRightChildPosition(parentPositionX, parentPositionY, childDepth):
    rightChildPositionX = parentPositionX + ((WINDOW_WIDTH - X_PADDING) / pow(2, childDepth)) / 2
    rightChildPositionY = parentPositionY + NODE_RADIUS * 4
    return (rightChildPositionX, rightChildPositionY)

#feito
def insertNode(rootNode, value, rootPositionX, rootPositionY, nodeDepth, canvas, window):
    if nodeDepth > MAX_DEPTH:
        showinfo(title="Insert", message="Max depth reached")
        return rootNode

    if rootNode is None:
        rootNode = Node(value)
        return rootNode

    createOvalWithText(canvas, rootPositionX, rootPositionY - 3 * NODE_RADIUS,
                        NODE_RADIUS, HIGHLIGHT_COLOR,
                        value, HIGHLIGHT_TEXT_COLOR, FONT_SIZE)
    window.update()
    sleep(ANIMATION_DELAY)
    
    if value < rootNode.value:
        createRectangleWithText(canvas, rootPositionX, rootPositionY - 1.5 * NODE_RADIUS,
                                NODE_RADIUS / 1.5, NODE_RADIUS / 1.5, HIGHLIGHT_COLOR,
                                "<", HIGHLIGHT_TEXT_COLOR, FONT_SIZE)
        window.update()
        sleep(ANIMATION_DELAY)

        leftChildPositionX, leftChildPositionY = calculateLeftChildPosition(rootPositionX, rootPositionY, nodeDepth + 1)
        rootNode.leftChild = insertNode(rootNode.leftChild, value, 
                                        leftChildPositionX, leftChildPositionY, 
                                        nodeDepth + 1, 
                                        canvas, window)
    elif value > rootNode.value:
        createRectangleWithText(canvas, rootPositionX, rootPositionY - 1.5 * NODE_RADIUS,
                                NODE_RADIUS / 1.5, NODE_RADIUS / 1.5, HIGHLIGHT_COLOR,
                                ">", HIGHLIGHT_TEXT_COLOR, FONT_SIZE)
        window.update()
        sleep(ANIMATION_DELAY)
        
        rightChildPositionX, rightChildPositionY = calculateRightChildPosition(rootPositionX, rootPositionY, nodeDepth + 1)
        rootNode.rightChild = insertNode(rootNode.rightChild, value, 
                                         rightChildPositionX, rightChildPositionY,
                                         nodeDepth + 1, 
                                         canvas, window)
    elif value == rootNode.value:
        showinfo(title="Insert", message="Node already in tree")

    return rootNode


def insertNodeWithoutAnimation(rootNode, value, nodeDepth):
    if nodeDepth > MAX_DEPTH:
        return rootNode

    if rootNode is None:
        rootNode = Node(value)
        return rootNode

    if value < rootNode.value:
        rootNode.leftChild = insertNodeWithoutAnimation(rootNode.leftChild, value, nodeDepth + 1)
    elif value > rootNode.value:
        rootNode.rightChild = insertNodeWithoutAnimation(rootNode.rightChild, value, nodeDepth + 1)

    return rootNode


def searchTree(rootNode, value, rootPositionX, rootPositionY, nodeDepth, canvas, window):
    if rootNode is None:
        showinfo(title="Search", message="Node not found")
        return

    createOvalWithText(canvas, rootPositionX, rootPositionY - 3 * NODE_RADIUS,
                        NODE_RADIUS, HIGHLIGHT_COLOR,
                        value, HIGHLIGHT_TEXT_COLOR, FONT_SIZE)
    window.update()
    sleep(ANIMATION_DELAY)

    if value < rootNode.value:
        createRectangleWithText(canvas, rootPositionX, rootPositionY - 1.5 * NODE_RADIUS,
                                NODE_RADIUS / 1.5, NODE_RADIUS / 1.5, HIGHLIGHT_COLOR,
                                "<", HIGHLIGHT_TEXT_COLOR, FONT_SIZE)
        window.update()
        sleep(ANIMATION_DELAY)

        leftChildPositionX, leftChildPositionY = calculateLeftChildPosition(rootPositionX, rootPositionY, nodeDepth + 1)
        searchTree(rootNode.leftChild, value, 
                    leftChildPositionX, leftChildPositionY, 
                    nodeDepth + 1, 
                    canvas, window)
    elif value > rootNode.value:
        createRectangleWithText(canvas, rootPositionX, rootPositionY - 1.5 * NODE_RADIUS,
                                NODE_RADIUS / 1.5, NODE_RADIUS / 1.5, HIGHLIGHT_COLOR,
                                ">", HIGHLIGHT_TEXT_COLOR, FONT_SIZE)
        window.update()
        sleep(ANIMATION_DELAY)
        
        rightChildPositionX, rightChildPositionY = calculateRightChildPosition(rootPositionX, rootPositionY, nodeDepth + 1)
        searchTree(rootNode.rightChild, value, 
                    rightChildPositionX, rightChildPositionY,
                    nodeDepth + 1, 
                    canvas, window)
    elif value == rootNode.value:
        createRectangleWithText(canvas, rootPositionX, rootPositionY - 1.5 * NODE_RADIUS,
                                NODE_RADIUS / 1.5, NODE_RADIUS / 1.5, HIGHLIGHT_COLOR,
                                "=", HIGHLIGHT_TEXT_COLOR, FONT_SIZE)
        createOvalWithText(canvas, rootPositionX, rootPositionY,
                            NODE_RADIUS, HIGHLIGHT_COLOR,
                            value, HIGHLIGHT_TEXT_COLOR, FONT_SIZE)
        window.update()
        sleep(ANIMATION_DELAY)


def deleteNode(rootNode, value, rootPositionX, rootPositionY, nodeDepth, canvas, window):
    if rootNode is None:
        showinfo(title="Delete", message="Node not found")
        return None

    createOvalWithText(canvas, rootPositionX, rootPositionY - 3 * NODE_RADIUS,
                        NODE_RADIUS, HIGHLIGHT_COLOR,
                        value, HIGHLIGHT_TEXT_COLOR, FONT_SIZE)
    window.update()
    sleep(ANIMATION_DELAY)

    if value < rootNode.value:
        createRectangleWithText(canvas, rootPositionX, rootPositionY - 1.5 * NODE_RADIUS,
                                NODE_RADIUS / 1.5, NODE_RADIUS / 1.5, HIGHLIGHT_COLOR,
                                "<", HIGHLIGHT_TEXT_COLOR, FONT_SIZE)
        window.update()
        sleep(ANIMATION_DELAY)

        leftChildPositionX, leftChildPositionY = calculateLeftChildPosition(rootPositionX, rootPositionY, nodeDepth + 1)
        rootNode.leftChild = deleteNode(rootNode.leftChild, value, 
                                        leftChildPositionX, leftChildPositionY, 
                                        nodeDepth + 1, 
                                        canvas, window)
    elif value > rootNode.value:
        createRectangleWithText(canvas, rootPositionX, rootPositionY - 1.5 * NODE_RADIUS,
                                NODE_RADIUS / 1.5, NODE_RADIUS / 1.5, HIGHLIGHT_COLOR,
                                ">", HIGHLIGHT_TEXT_COLOR, FONT_SIZE)
        window.update()
        sleep(ANIMATION_DELAY)
        
        rightChildPositionX, rightChildPositionY = calculateRightChildPosition(rootPositionX, rootPositionY, nodeDepth + 1)
        rootNode.rightChild = deleteNode(rootNode.rightChild, value, 
                                        rightChildPositionX, rightChildPositionY,
                                        nodeDepth + 1, 
                                        canvas, window)
    elif value == rootNode.value:
        createRectangleWithText(canvas, rootPositionX, rootPositionY - 1.5 * NODE_RADIUS,
                                NODE_RADIUS / 1.5, NODE_RADIUS / 1.5, HIGHLIGHT_COLOR,
                                "=", HIGHLIGHT_TEXT_COLOR, FONT_SIZE)
        createOvalWithText(canvas, rootPositionX, rootPositionY,
                            NODE_RADIUS, HIGHLIGHT_COLOR,
                            value, HIGHLIGHT_TEXT_COLOR, FONT_SIZE)
        window.update()
        sleep(ANIMATION_DELAY)
        
        if rootNode.leftChild is None and rootNode.rightChild is None:
            return None

        clearCanvasAndDrawTree()

        if rootNode.rightChild is not None:
            createRectangleWithText(canvas, rootPositionX, rootPositionY - 1.5 * NODE_RADIUS,
                                    6.5 * NODE_RADIUS, NODE_RADIUS / 1.5, HIGHLIGHT_COLOR,
                                    "REPLACE WITH MIN >>", HIGHLIGHT_TEXT_COLOR, FONT_SIZE / 1.5)

            window.update()
            sleep(ANIMATION_DELAY)

            rightChildPositionX, rightChildPositionY = calculateRightChildPosition(rootPositionX, rootPositionY, nodeDepth + 1)
            rootNode.value = getMinNodeValue(rootNode.rightChild, 
                                         rightChildPositionX, rightChildPositionY, 
                                         nodeDepth + 1, 
                                         canvas, window)

            createOvalWithText(canvas, rootPositionX, rootPositionY,
                            NODE_RADIUS, HIGHLIGHT_COLOR,
                            rootNode.value, HIGHLIGHT_TEXT_COLOR, FONT_SIZE)
            window.update()
            sleep(ANIMATION_DELAY)

            clearCanvasAndDrawTree()

            createRectangleWithText(canvas, rootPositionX, rootPositionY - 1.5 * NODE_RADIUS,
                                    6.5 * NODE_RADIUS, NODE_RADIUS / 1.5, HIGHLIGHT_COLOR,
                                    "DELETE DUPLICATE >>", HIGHLIGHT_TEXT_COLOR, FONT_SIZE / 1.5)

            window.update()
            sleep(ANIMATION_DELAY)

            rootNode.rightChild = deleteNode(rootNode.rightChild, rootNode.value,
                                             rightChildPositionX, rightChildPositionY,
                                             nodeDepth + 1,
                                             canvas, window)
        else:
            createRectangleWithText(canvas, rootPositionX, rootPositionY - 1.5 * NODE_RADIUS,
                                    6.5 * NODE_RADIUS, NODE_RADIUS / 1.5, HIGHLIGHT_COLOR,
                                    "<< REPLACE WITH MAX", HIGHLIGHT_TEXT_COLOR, FONT_SIZE / 1.5)

            window.update()
            sleep(ANIMATION_DELAY)

            leftChildPositionX, leftChildPositionY = calculateLeftChildPosition(rootPositionX, rootPositionY, nodeDepth + 1)
            rootNode.value = getMaxNodeValue(rootNode.leftChild, 
                                         leftChildPositionX, leftChildPositionY, 
                                         nodeDepth + 1, 
                                         canvas, window)

            createOvalWithText(canvas, rootPositionX, rootPositionY,
                            NODE_RADIUS, HIGHLIGHT_COLOR,
                            rootNode.value, HIGHLIGHT_TEXT_COLOR, FONT_SIZE)
            window.update()
            sleep(ANIMATION_DELAY)

            clearCanvasAndDrawTree()

            createRectangleWithText(canvas, rootPositionX, rootPositionY - 1.5 * NODE_RADIUS,
                                    6.5 * NODE_RADIUS, NODE_RADIUS / 1.5, HIGHLIGHT_COLOR,
                                    "<< DELETE DUPLICATE", HIGHLIGHT_TEXT_COLOR, FONT_SIZE / 1.5)

            window.update()
            sleep(ANIMATION_DELAY)

            rootNode.leftChild = deleteNode(rootNode.leftChild, rootNode.value,
                                             leftChildPositionX, leftChildPositionY,
                                             nodeDepth + 1,
                                             canvas, window)
    return rootNode


def getMinNodeValue(rootNode, rootPositionX, rootPositionY, nodeDepth, canvas, window):

    if rootNode.leftChild is None:
        createRectangleWithText(canvas, rootPositionX, rootPositionY - 1.5 * NODE_RADIUS,
                                NODE_RADIUS, NODE_RADIUS / 1.5, HIGHLIGHT_COLOR,
                                "MIN", HIGHLIGHT_TEXT_COLOR, FONT_SIZE / 1.5)
        createOvalWithText(canvas, rootPositionX, rootPositionY,
                            NODE_RADIUS, HIGHLIGHT_COLOR,
                            rootNode.value, HIGHLIGHT_TEXT_COLOR, FONT_SIZE)
        window.update()
        sleep(ANIMATION_DELAY)

        return rootNode.value
    else:
        createRectangleWithText(canvas, rootPositionX, rootPositionY - 1.5 * NODE_RADIUS,
                                NODE_RADIUS, NODE_RADIUS / 1.5, HIGHLIGHT_COLOR,
                                "<<", HIGHLIGHT_TEXT_COLOR, FONT_SIZE)
        window.update()
        sleep(ANIMATION_DELAY)

        leftChildPositionX, leftChildPositionY = calculateLeftChildPosition(rootPositionX, rootPositionY, nodeDepth + 1)
        return getMinNodeValue(rootNode.leftChild, 
                            leftChildPositionX, leftChildPositionY, 
                            nodeDepth + 1, 
                            canvas, window)

    
def getMaxNodeValue(rootNode, rootPositionX, rootPositionY, nodeDepth, canvas, window):

    if rootNode.rightChild is None:
        createRectangleWithText(canvas, rootPositionX, rootPositionY - 1.5 * NODE_RADIUS,
                                NODE_RADIUS, NODE_RADIUS / 1.5, HIGHLIGHT_COLOR,
                                "MAX", HIGHLIGHT_TEXT_COLOR, FONT_SIZE / 1.5)
        createOvalWithText(canvas, rootPositionX, rootPositionY,
                            NODE_RADIUS, HIGHLIGHT_COLOR,
                            rootNode.value, HIGHLIGHT_TEXT_COLOR, FONT_SIZE)
        window.update()
        sleep(ANIMATION_DELAY)

        return rootNode.value
    else:
        createRectangleWithText(canvas, rootPositionX, rootPositionY - 1.5 * NODE_RADIUS,
                                NODE_RADIUS, NODE_RADIUS / 1.5, HIGHLIGHT_COLOR,
                                ">>", HIGHLIGHT_TEXT_COLOR, FONT_SIZE)
        window.update()
        sleep(ANIMATION_DELAY)

        rightChildPositionX, rightChildPositionY = calculateRightChildPosition(rootPositionX, rootPositionY, nodeDepth + 1)
        return getMaxNodeValue(rootNode.rightChild, 
                                rightChildPositionX, rightChildPositionY, 
                                nodeDepth + 1, 
                                canvas, window)


#separar daqui pra frente em outro arquivo
def drawTree(rootNode, rootPositionX, rootPositionY, nodeDepth, canvas, window):
    if rootNode is None:
        return

    if rootNode.leftChild is not None:
        leftChildPositionX, leftChildPositionY = calculateLeftChildPosition(rootPositionX, rootPositionY, nodeDepth + 1)
        canvas.create_line(rootPositionX, rootPositionY,
                           leftChildPositionX, leftChildPositionY, 
                           fill=LINE_COLOR, width=5)
        drawTree(rootNode.leftChild, 
                 leftChildPositionX, leftChildPositionY, 
                 nodeDepth + 1,
                 canvas, window)

    if rootNode.rightChild is not None:
        rightChildPositionX, rightChildPositionY = calculateRightChildPosition(rootPositionX, rootPositionY, nodeDepth + 1)
        canvas.create_line(rootPositionX, rootPositionY,
                           rightChildPositionX, rightChildPositionY, 
                           fill=LINE_COLOR, width=5)
        drawTree(rootNode.rightChild, 
                 rightChildPositionX, rightChildPositionY, 
                 nodeDepth + 1,
                 canvas, window)

    createOvalWithText(canvas, rootPositionX, rootPositionY, 
                     NODE_RADIUS, NODE_COLOR, 
                     rootNode.value, TEXT_COLOR, FONT_SIZE)
    window.update()


def clearCanvasAndDrawTree():
        treePositionX = WINDOW_WIDTH/2
        treePositionY = Y_PADDING
        canvas.delete("all")
        drawTree(rootNode, treePositionX, treePositionY, 0, canvas, window)


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


def isInputValid(value) -> bool:
    try:
        value = int(value)
    except ValueError:
        showerror(title="ERROR", message="Invalid input")
        return False

    if value > MAX_VALUE:
        showerror(title="ERROR", message="Input value exceeding max allowed")
        return False
    if value < MIN_VALUE:
        showerror(title="ERROR", message="Input value under min allowed")
        return False
    return True


def onClickInsert(value):
    global rootNode

    if not isInputValid(value):
        return

    value = int(value)

    rootPositionX = WINDOW_WIDTH/2
    rootPositionY = Y_PADDING

    disableUI()

    rootNode = insertNode(rootNode, value, rootPositionX, rootPositionY, 0, canvas, window)

    sleep(1)

    canvas.delete("all")
    drawTree(rootNode, rootPositionX, rootPositionY, 0, canvas, window)

    enableUI()


def onClickSearch(value):
    if not isInputValid(value):
        return

    value = int(value)

    rootPositionX = WINDOW_WIDTH/2
    rootPositionY = Y_PADDING

    disableUI()

    searchTree(rootNode, value, rootPositionX, rootPositionY, 0, canvas, window)

    sleep(1)

    canvas.delete("all")
    drawTree(rootNode, rootPositionX, rootPositionY, 0, canvas, window)
    
    enableUI()


def onClickDelete(value):
    global rootNode

    if not isInputValid(value):
        return

    value = int(value)

    rootPositionX = WINDOW_WIDTH/2
    rootPositionY = Y_PADDING

    disableUI()

    rootNode = deleteNode(rootNode, value, rootPositionX, rootPositionY, 0, canvas, window)

    sleep(1)

    canvas.delete("all")
    drawTree(rootNode, rootPositionX, rootPositionY, 0, canvas, window)
    
    enableUI()


def onClickGenerateRandomTree():
    global rootNode

    rootNode = None

    numberOfInserts = randint(100, 100)

    for x in range(numberOfInserts):
        nodeValue = randint(MIN_VALUE, MAX_VALUE)
        rootNode = insertNodeWithoutAnimation(rootNode, nodeValue, 0)
    
    rootPositionX = WINDOW_WIDTH/2
    rootPositionY = Y_PADDING

    canvas.delete("all")
    drawTree(rootNode, rootPositionX, rootPositionY, 0, canvas, window)


def disableUI():
    insertButton["state"] = DISABLED
    generateRandomTreeButton["state"] = DISABLED
    deleteButton["state"] = DISABLED
    searchButton["state"] = DISABLED
    inputField["state"] = DISABLED


def enableUI():
    insertButton["state"] = NORMAL
    generateRandomTreeButton["state"] = NORMAL
    deleteButton["state"] = NORMAL
    searchButton["state"] = NORMAL
    inputField["state"] = NORMAL

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

""""
background_image = tk.PhotoImage(file = "INF.png")
limg= Label(window, i=background_image)
limg.pack()
"""
window.mainloop()