from tkinter import*
import time
import random
from PIL import ImageTk,Image
#functions
def play():
    global startB
    global instructions
    global startImg
    #Deleting intro text and buttons
    titleScreen.place_forget()
    playB.place_forget()
    quitB.place_forget()
    #instructions
    instructions=Label(window, text="Instructions:\r You will have 30 seconds\
to hit as many targets as you can. After wards\r you will be given a score.\
 Try to beat you highscore to improve your aim!\r With consistency your aim\
 will surely improve.  ", font=("Arial Bold", 40))
    instructions.place(x=0, y=100)
    #start button
    startB=Button(window,image=startImg,command=start)
    startB.place(x=700, y=500)

def start():
    global score
    global scoreNum
    #start timer
    startTimer=timer()
    
    scoreNum=Label(window, text="SCORE:"+str(score)+"\t\t\t",font=("Arial\
 Bold",40))
    scoreNum.place(x=1550, y=0)
    score=int(score)
    score+=100
    global startB
    global instructions
    global timeR
    global target0
    #deleting start/instructions screen
    startB.place_forget()
    instructions.place_forget()
    #First target
    target0=Button (window,command=screen1,image=targetImg)
    target0.place(x=800, y=500)
def endscreen():
    global target0
    global target1
    global target2
    global target3
    global target4
    global target5
    global label2
    global scoreNum
    global score
    global highscore
    global gameOver
    global yourScore
    global highscoreT
    global playAgain
    global quitB
    global quit2Img
    global playagainImg
    global gameoverImg
    #Deleting previous target
    try:
        target4.place_forget()
    except:
        pass
    try:
        target3.place_forget()
    except:
        pass
    try:
        target2.place_forget()
    except:
        pass
    try:
        target1.place_forget()
    except:
        pass
    try:
        target5.place_forget()
    except:
        pass
    #Determining new highscore
    if (score-100)>highscore:
        highscore=score-100
    #Endscreen Text/Images and Buttons
    gameOver=Label(window, image=gameoverImg)
    gameOver.place(x=530, y=120)
    yourScore=Label(window, text="Your Score: "+str(score-100),font=("Arial Bold", 40))
    yourScore.place(x=700, y=300)
    highscoreT=Label(window, text="Highscore: "+str(highscore),font=("Arial Bold", 40))
    highscoreT.place(x=700, y=400)
    playAgain=Button(window,image=playagainImg ,command=playagain)
    playAgain.place(x=550, y=500)
    quitB=Button(window, image=quit2Img,command=window.destroy, fg="red")
    quitB.place(x=720, y=650)
def playagain():
    global timeL
    global score
    global gameOver
    global yourScore
    global highscoreT
    global playAgain
    global quitB
    playAgain.place_forget()
    highscoreT.place_forget()
    yourScore.place_forget()
    gameOver.place_forget()
    quitB.place_forget()
    #reseting variables
    score=0
    timeL=30
    #restarting game from start
    restart=start()
def timer():
    global timeL
    global label2
    if label2:
        label2.place_forget()
    label2 = Label(window, text="Time Left: " + str(timeL) + "s",font=("\
Arial Bold", 40))
    label2.place(x=0,y=0)
    timeL = timeL - 1
    #one second wait
    redo=window.after(1000, timer)
    #if timer =go to endscreen and cancel the after command
    if timeL==0:
        label2= Label(window, text="Time Left: "+str(timeL) + "s",font=("\
Arial Bold", 40))
        label2.place(x=0,y=0)
        window.after_cancel(redo)
        end=endscreen()

def screen1():
    global score
    global target0
    global target1
    global target2
    global target3
    global target4
    global target5
    #updating score
    score=str(score)
    scoreNum=Label(window, text="SCORE:"+score+"\t\t\t",font=("Arial Bold", 40))
    scoreNum.place(x=1550, y=0)  
    score=int(score)
    #adding 100 for next target
    score+=100
    #Deleting old targets
    target0.place_forget()
    try:
        target2.place_forget()
    except:
        pass
    try:
        target3.place_forget()
    except:
        pass
    try:
        target4.place_forget()
    except:
        pass
    try:
        target5.place_forget()
    except:
        pass
    #Randomize next target
    seq=[2,3,4,5]
    num=random.choice(seq)
    if num==2:
        switch=screen2
    elif num==3:
        switch=screen3
    elif num==4:
        switch=screen4
    elif num==5:
        switch=screen5
    #placing target1
    target1=Button (window,command=switch, fg="red",image=targetImg)
    target1.place(x=1300, y=450)
    
def screen2():
    global score
    global target0
    global target1
    global target2
    global target3
    global target4
    global target5
    score=str(score)
    #updating scoreboard
    scoreNum=Label(window, text="SCORE:"+score+"\t\t\t",font=("Arial Bold", 40))
    scoreNum.place(x=1550, y=0)
    score=int(score)
    #adding 100 for next target
    score+=100

    #Deleting old targets
    try:
        target0.place_forget()
    except:
        pass
    try:
        target1.place_forget()
    except:
        pass
    try:
        target3.place_forget()
    except:
        pass
    try:
        target4.place_forget()
    except:
        pass
    try:
        target5.place_forget()
    except:
        pass
    #Randomize next target
    seq=[1,3,4,5]
    num=random.choice(seq)
    if num==1:
        switch=screen1
    elif num==3:
        switch=screen3
    elif num==4:
        switch=screen4
    elif num==5:
        switch=screen5
    #placing target 2
    target2=Button (window,command=switch,image=targetImg)
    target2.place(x=152, y=153)
    
def screen3():
    global score
    global target0
    global target1
    global target2
    global target3
    global target4
    global target5
    #updating score
    score=str(score)
    scoreNum=Label(window, text="SCORE:"+score+"\t\t\t",font=("Arial Bold", 40))
    scoreNum.place(x=1550, y=0)
    score=int(score)
    #adding 100 for next target
    score+=100
    #Deleting old targets
    try:
        target4.place_forget()
    except:
        pass
    try:
        target0.place_forget()
    except:
        pass
    try:
        target1.place_forget()
    except:
        pass
    try:
        target2.place_forget()
    except:
        pass
    try:
        target5.place_forget()
    except:
        pass        
    #Randomize next target
    seq=[1,2,4,5]
    num=random.choice(seq)
    if num==1:
        switch=screen1
    elif num==2:
        switch=screen2
    elif num==4:
        switch=screen4
    elif num==5:
        switch=screen5
    #placing target 3
    target3=Button (window, command=switch, fg="red",image=targetImg)
    target3.place(x=789, y=120)

def screen4():
    global score
    global target0
    global target1
    global target2
    global target3
    global target4
    global target5
    #updating score
    score=str(score)
    scoreNum=Label(window, text="SCORE:"+score+"\t\t\t",font=("Arial Bold", 40))
    scoreNum.place(x=1550, y=0)
    score=int(score)
    #adding 100 for next target
    score+=100
    #Deleting old targets
    try:
        target0.place_forget()
    except:
        pass
    try:
        target1.place_forget()
    except:
        pass
    try:
        target2.place_forget()
    except:
        pass
    try:
        target3.place_forget()
    except:
        pass
    try:
        target5.place_forget()
    except:
        pass
    #Randomize next target
    seq=[1,2,3,5]
    num=random.choice(seq)
    if num==1:
        switch=screen1
    elif num==2:
        switch=screen2
    elif num==3:
        switch=screen3
    elif num==5:
        switch=screen5
                
    #placing target 4
    target4=Button (window,command=switch,image=targetImg)
    target4.place(x=153, y=881)

def screen5():
    global score
    global target0
    global target1
    global target2
    global target3
    global target4
    global target5
    #updating score
    score=str(score)
    scoreNum=Label(window, text="SCORE:"+score+"\t\t\t",font=("Arial Bold", 40))
    scoreNum.place(x=1550, y=0)
    score=int(score)
    #adding 100 for next target
    score+=100
    #Deleting old targets
    try:
        target0.place_forget()
    except:
        pass
    try:
        target1.place_forget()
    except:
        pass
    try:
        target2.place_forget()
    except:
        pass
    try:
        target3.place_forget()
    except:
        pass
    try:
        target4.place_forget()
    except:
        pass
    #Randomize next target
    seq=[1,2,3,4]
    num=random.choice(seq)
    if num==1:
        switch=screen1
    elif num==2:
        switch=screen2
    elif num==3:
        switch=screen3
    elif num==4:
        switch=screen4
    #placing target 5
    target5=Button (window,command=switch, fg="red",image=targetImg)
    target5.place(x=1500, y=881)

    
window=Tk()
window.title("Aim Trainer")
#initailizing variables
score=0
timeL = 30
highscore=0
label2 = None
#Background image:
backgroundImg= ImageTk.PhotoImage(Image.open("Neon.png"))
background=Label(image=backgroundImg)
background.place(x=0,y=0)
#Game Title
neonImg= ImageTk.PhotoImage(Image.open("coolText.png"))
titleScreen=Label(window, image=neonImg)
titleScreen.place(x=550, y=100)
#Play Button
playImg=ImageTk.PhotoImage(Image.open("play.png"))
playB=Button (window,image=playImg,command=play)
playB.place(x=750, y=300)
#Quit Button
quitImg=ImageTk.PhotoImage(Image.open("quit.png"))
quitB=Button(window, image=quitImg,command=window.destroy)
quitB.place(x=760, y=500)

#Adding images for functions
targetImg= ImageTk.PhotoImage(Image.open("Target.png"))
startImg=ImageTk.PhotoImage(Image.open("start.png"))
playagainImg=ImageTk.PhotoImage(Image.open("play again.png"))
gameoverImg=ImageTk.PhotoImage(Image.open("game over.png"))
quit2Img=ImageTk.PhotoImage(Image.open("quit2.png"))
window.geometry('1920x1080')

window.mainloop()

