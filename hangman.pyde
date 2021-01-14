add_library("minim")
import pickle
import random

def setup():
    global allBoundaries, whichSquare, removeSquare, activeSquares, numSquares, board, row, col
    global gamedictionary, gdkey, file, numRow, guessWord, clues, score, temprow, letters
    global gameList, limits, clue, clueCounter, lettersTaken, mistakeCounter, addScore,logo
    global whichKey, acceptedChars, keyPressing, keysTaken, score, terminateInput,setUp, userName, userName2,charLimit
    global numMenuSquares, squareXShowMenu, squareYShowMenu, squareHeightMenu, squareWidthMenu, startSquareXMenu, startSquareYMenu, screen
    global menu, menuWidth,menuHeight,menuX,menuY
    global help, helpWidth,helpHeight,helpX,helpY
    global leaderboard,font,defaultFont
    global incrX,incrY,incrX2,incrY2,lBound,rBound,uBound,bBound,ball1
    global mylist, playerInfo, addScore2, mynewlist
    
    allBoundaries = []
    startSquareX = 42
    startSquareY = 411
    squareXShow = startSquareX
    squareYShow = startSquareY
    squareHeight = 48
    squareWidth = 45
    numSquares = 27
    removeSquare = True
    whichSquare = -1
    add_library("minim")
    minim=Minim(this)
    sound=minim.loadFile("game.mp3")
    sound.loop()
    size(500,650) 
    score = 0
    board = loadImage("board.jpg")
    row = 3
    col = 9
    guessWord = ""
    clues = ""
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "?"] 
    clueCounter = 0
    clue = 0
    lettersTaken = []
    keysTaken = ["0"]
    mistakeCounter = 0
    whichKey = " "
    acceptedChars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0?" 
    keyPressing = True
    terminateInput="0"
    setUp=True
    userName=""
    userName2=""
    charLimit=10
    addScore=True
    font = loadFont("CurlzMT-38.vlw")                       #Custom font
    defaultFont = loadFont("BookmanOldStyle-Bold-38.vlw")   #Custom font

    numMenuSquares=4
    squareXShowMenu=0
    squareYShowMenu=600
    squareHeightMenu=50
    squareWidthMenu=125
    startSquareXMenu=0
    startSquareYMenu=600
    screen=-1
    
    menu=loadImage("Menu.PNG")
    menuWidth=500
    menuHeight=50
    menuX=0
    menuY=600
    
    help=loadImage("Help.PNG")
    helpWidth=500
    helpHeight=600
    helpX=0
    helpY=0
    
    incrX=1
    incrY=3
    incrX2=4
    incrY2=2
    lBound=0
    rBound=500
    uBound=200
    bBound=600
    ball1=[50,260, 100,100]
    
    playerInfo = []
    mylist = []
    mynewlist = []
    addScore2 = True
    
    leaderboard=loadImage("Green_Leaderboard.png")
    logo = loadImage("hangmanLogo.png")

    image(menu,menuX,menuY,menuWidth,menuHeight)
    
    file = open("words.txt")                                       #Dictionary where the words that you are guessing are stored
    gameList = []   
    gamedictionary = {}
    text = file.readlines()
    gdkey = -1
    for line in text:
        line = line.strip()
        numRow = ""
        for c in line:
            numRow = numRow + c
        temprow = numRow.split( "," )
        gameList.append(temprow) 
    limits = len( gameList )
    for i in range( limits ):
        gamedictionary[i] = gameList[i] 
    gdkey = random.randint(0,7) 
    guessWord = gameList[gdkey]
    
    for i in range( row ):
        for j in range( col ):
            upperLeft =  [ squareXShow, squareYShow ]
            lowerRight = [ squareXShow + squareWidth, squareYShow + squareHeight ]
            clickBoundary = [ upperLeft, lowerRight ]
            allBoundaries.append( clickBoundary )
            squareXShow = squareXShow + squareWidth
        squareXShow = startSquareX
        squareYShow = squareYShow + squareHeight
            
    squareXShow = startSquareX
    squareYShow = startSquareY
    
    for i in range( numMenuSquares ):
        upperLeft =  [ squareXShowMenu, squareYShowMenu ]
        lowerRight = [ squareXShowMenu + squareWidthMenu, squareYShowMenu + squareHeightMenu ]
        clickBoundary = [ upperLeft, lowerRight ]
        allBoundaries.append( clickBoundary )
        squareXShowMenu = squareXShowMenu +  squareWidthMenu
        
    activeSquares = [ True for j in range( numSquares+numMenuSquares ) ]
   
   
def sortingval(listtosort):               #Bubble sort 
    for i in range (len(listtosort)):
        for j in range (len(listtosort)):
            if listtosort[i][1]>listtosort[j][1]:
                listtosort[i],listtosort[j]=listtosort[j],listtosort[i]
    
def resetgame():
    global allBoundaries, whichSquare, removeSquare, activeSquares, numSquares, board, row, col
    global gamedictionary, gdkey, file, numRow, guessWord, clues, score, temprow, letters
    global gameList, limits, clue, clueCounter, lettersTaken, mistakeCounter , addScore,addScore2
    global whichKey, acceptedChars, keyPressing, keysTaken, score, terminateInput,setUp, userName, userName2,charLimit
    
    #resets original values for the game
    board = loadImage("board.jpg")
    row = 3
    col = 9
    guessWord = ""
    clues = ""
    clueCounter = 0
    clue = 0
    lettersTaken = []
    keysTaken = ["0"]
    mistakeCounter = 0
    whichKey = ""
    acceptedChars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0?"
    keyPressing = True
    setUp=True
    userName=""
    addScore=True
    addScore2 = True
     
    activeSquares = [ True for j in range( numSquares+numMenuSquares ) ]
    
    file = open("words.txt")
    
    gameList = []                           
    gamedictionary = {}
    text = file.readlines()
    gdkey = -1
    for line in text:
        line = line.strip()
        numRow = ""
        for c in line:
            numRow = numRow + c
        temprow = numRow.split( "," )
        gameList.append(temprow) 
    limits = len( gameList )
    for i in range( limits ):
        gamedictionary[i] = gameList[i] 
    gdkey = random.randint(0,7) 
    guessWord = gameList[gdkey]
    
def keyPressed():
    global acceptedChars, whichKey, keyPressing
    if keyPressing:
        if key ==CODED:
            whichKey=""
                                            #makes it so that if you press a coded key it changes it to a blank so the program does not crash
        else:
            if key in acceptedChars:
                whichKey = (key).lower()
   
def mouseReleased():
    global allBoundaries, whichSquare, removeSquare, activeSquares, numSquares,numMenuSquares
    
    whichSquare = - 1
    validLocation = False
    for i in range( numSquares+numMenuSquares ):        
        if activeSquares[ i ]:
            validXRange = allBoundaries[i][0][0] <= mouseX <= allBoundaries[i][1][0] 
            validYRange = allBoundaries[i][0][1]  <= mouseY <= allBoundaries[i][1][1]
            validLocation = validXRange and validYRange
            if validLocation:
                whichSquare = i
                break
    if validLocation and removeSquare:
        activeSquares[ whichSquare ] = False
    
    activeSquares[27]=True     #these are the menu squares and we do not want them being turned off after being clicked on
    activeSquares[28]=True
    activeSquares[29]=True
    activeSquares[30]=True
    
    if mistakeCounter >= 6 or len(lettersTaken) == len(guessWord[0]):
        if mouseX>=288 and mouseX<=458 and mouseY>=200 and mouseY<=250 and mouseReleased:
            resetgame()
            image(board, 0, 0, 500, 600) 
            
            
def mouseLetterCheck(guessWord,letters,whichSquare,lettersTaken):               #Function to check if a letter is in the word that you're guessing by mouse
    for i in range(len(guessWord[0])):
        if letters[whichSquare] == guessWord[0][i]:
            textFont(defaultFont,18)
            fill(0)
            text (letters[whichSquare], 168 + i*44, 385) 
            lettersTaken.append(letters[whichSquare])

def keyboardLetterCheck(guessWord,whichKey,lettersTaken):                       #Function to check if a letter is in the word that you're guessing by keyboard
    for i in range(len(guessWord[0])):
        if whichKey == guessWord[0][i]:
            whichKey = (str(whichKey)).lower()  
            lettersTaken.append(whichKey)
            textFont(defaultFont,18)
            fill(0)
            text (whichKey, 168 + i*44, 385)

def gettingClues(clues,clueCounter,activeSquares):                              #Function to get a clue if you press the question mark (clickable up to 3 times)
    if clueCounter <= 2:
        clues = guessWord[clue]
        if clueCounter <= 2:
            activeSquares[ 26 ] = True
    else:
        for i in range(numSquares):
            activeSquares[26] = False
            
def draw(): 
    global allBoundaries, whichSquare, removeSquare, activeSquares, numSquares
    global gamedictionary, gdkey, file, numRow, guessWord, clues, score, temprow, letters, clue, letter, clueCounter
    global mistakeCounter, mode, whichKey, keyPressing, keysTaken, score,terminateInput,setUp, userName, userName2,charLimit, addScore
    global numMenuSquares, squareXShowMenu, squareYShowMenu, squareHeightMenu, squareWidthMenu, startSquareXMenu, startSquareYMenu, screen
    global menu, menuWidth,menuHeight,menuX,menuY
    global help, helpWidth,helpHeight,helpX,helpY
    global font,defaultFont,file, lboardHeightDiff
    global incrX,incrY,incrX2,incrY2,lBound,rBound,uBound,bBound,ball1
    global mylist, playerInfo, addScore2, mynewlist
    
    if whichSquare==27:
        if userName2 == "":
            screen=0
            whichSquare=-1
            whichKey=""
            keyPressing=True
        else:
            screen=1
            image(board, 0, 0, 500, 600) 
            
    if whichSquare==28:
        screen=2
        whichSquare=-1
    
    if whichSquare==29:
        screen=3
        whichSquare=-1
    
    if whichSquare==30:
        screen=-1
        whichSquare=-1
        userName2=""
        score=0
        resetgame()    
        
    if screen==-1:
        fill(200)
        rect(0,0,500,600)
        imageMode(CORNER)
        image(logo,0,0)
        fill(255,0,0)
        textFont(font,50)
        text("By:",235,200)
        ellipse(ball1[0],ball1[1],ball1[2],ball1[3])
        fill(0)
        textFont(font,40)
        textAlign(CENTER,CENTER)
        text("Hasan",ball1[0],ball1[1])
        textAlign(LEFT)
        
        if ball1[0]<lBound +(ball1[3]/2) :               #Hasan's ball
            incrX=abs(incrX)
            ball1[0]=lBound+(ball1[2]/2)
        if ball1[0]>rBound-(ball1[3]/2):
            incrX=-(abs(incrX))
            ball1[0]=rBound-(ball1[2]/2)
        if ball1[1]>bBound-(ball1[2]/2)-1:
            incrY=-(abs(incrY))
            ball1[1]=bBound-(ball1[2]/2)-1
        if ball1[1]<uBound+(ball1[2]/2)+1:
            incrY=(abs(incrY))
            ball1[1]=uBound+(ball1[2]/2)+1
            
        ball1[0]+=incrX
        ball1[1]+=incrY
    
    if screen==2:
        image(help, helpX, helpY, helpWidth ,helpHeight)
    
    if screen==3:
        lboardHeightDiff=110
        image(leaderboard,0,0,500,600)
        with open("highscore.pkl", "rb") as f:
            mynewlist = pickle.load(f) 
            f.close()
        fill(0)
        textFont(font,30) 
        sortingval(mynewlist)        
        displayscores=len(mynewlist)
        if displayscores >10:
            displayscores=10
        for i in range (displayscores):
            text(mynewlist[i][0],50,lboardHeightDiff)
            text(mynewlist[i][1],400,lboardHeightDiff)
            lboardHeightDiff+=53

    if screen==0:
        fill(255)
        rect(0,0,500,600)
        textFont(font,40)
        fill(0)
        text ("Enter Your Name" ,130,150)
        text( userName, 190,300 )
        if setUp and whichKey != "":
            if ( len( userName ) == charLimit ) or (  whichKey==terminateInput ):
                if userName!="":
                    setUp = False
                    screen=1
                    userName2=userName
                    userName=""
                    resetgame()
                    image(board, 0, 0, 500, 600) 
            
            else:
                userName = ( userName + whichKey ).upper()
                textFont(defaultFont,20)
                fill ( 0 )
                whichKey = ""
                    
    if screen==1:
        for j in lettersTaken:
            for i in range (len(guessWord[0])):
                if j==guessWord[0][i]:
                    fill(0)
                    textFont(defaultFont,18)
                    text (j, 168 + i*44, 385) 
                                     
        activeSquares[27]=False
        textFont(defaultFont,28)
        fill(34,139,34)
        text("?", 427, 547) 
        textSize(50)
        fill(255)
        rect(360,20,100,20)
        fill(0) 
        text("_ " * len(guessWord[0]), 165, 385)
        textFont(defaultFont,16)
        text(userName2, 370,20)
        text(score, 400,37)
      
        if 26>whichSquare:
            if whichSquare != -1 or whichKey != " ":
                if letters[whichSquare] in guessWord[0]:
                    mouseLetterCheck(guessWord,letters,whichSquare,lettersTaken)
            if letters[whichSquare] not in guessWord[0] and letters[whichSquare] != "?":
                mistakeCounter += 1                    
                            
        if whichKey in guessWord[0]:
            if whichKey not in lettersTaken:
                keyboardLetterCheck(guessWord,whichKey,lettersTaken)
    
        if whichSquare == 26 or whichKey == "?":
            if clueCounter <= 2:
                gettingClues(clues,clueCounter,activeSquares)
                clueCounter += 1
                clue += 1
                whichKey = ""
                
        whichSquare=-1
            
        if keyPressed:
            if whichKey not in guessWord[0] and whichKey != "?" :
                if whichKey not in keysTaken:
                    mistakeCounter += 1
                    whichKey = (str(whichKey)) .lower()
                    keysTaken.append(whichKey)
        
        if mistakeCounter >= 1:                  #Draws the man every time you make a mistake
            fill(255)
            ellipse(215,170,60,60)
        if mistakeCounter >= 2:
            line(215,200,215,275) 
        if mistakeCounter >= 3:
            line(215,200,155,245)
        if mistakeCounter >= 4:
            line(215,200,275,245)
        if mistakeCounter >= 5: 
            line(215,275,180,315) 
        if mistakeCounter >= 6:
            line(215,275,250,315) 
                    
            whichSquare = -1
            whichKey = ""
        
        for i in range (clueCounter):
            fill(0)
            textFont(defaultFont,16)
            text(guessWord[i+1], 195*(i), 590)   
                
        if mistakeCounter >= 6:
            textFont(font,50)
            fill(0,0,255)
            text("You Lost", 288, 180)
            fill(255)
            rect(288, 200, 170, 50) 
            fill(0)
            textFont(font,35)
            text("Play Again", 310, 240)
            playerInfo=[userName2,score]

            with open("highscore.pkl", "rb") as f:           #Opens the highscore.pkl file, reads and loads the names/scores into a list, and closes it
                mylist = pickle.load(f) 
                f.close()            
            if addScore2:
                mylist.append(playerInfo)
                addScore2 = False
            with open("highscore.pkl", "wb") as f:         #Opens the highscore.pkl file, writes and dumps the names/scores into a new list, and closes it
                pickle.dump(mylist,f) 
                f.close()
            
            score=0
            for i in range(numSquares):
                activeSquares[i] = False  
            keyPressing = False
        
        if len(lettersTaken) == len(guessWord[0]):
            textFont(font,50)
            fill(0,255,0)
            text("You Won", 288, 180)
            fill(255)
            rect(288, 200, 170, 50) 
            fill(0)
            textFont(font,35)
            text("Play Again", 310, 240)
            if addScore:
                score += len(guessWord[0])
                addScore=False
            for i in range(numSquares):
                activeSquares[i] = False 
            keyPressing = False 
            
        
 
