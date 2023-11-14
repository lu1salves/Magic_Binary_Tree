



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