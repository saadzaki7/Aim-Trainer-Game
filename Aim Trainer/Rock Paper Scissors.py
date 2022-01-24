
import random
from tkinter import*
from PIL import ImageTk,Image
window=Tk()
choice=1
scisTrue=False
rockTrue=False
paperTrue=False
started=False
def clicked():
    global choice
    global rockImg
    global paperImg
    global scisImg
    global rockImgU
    global paperImgU
    global scisImgU
    global titlePic
    rockText=0
    paperText=0
    scisText=0
    #deleting intro screen
    title.grid_forget()
    subtitle.grid_forget()
    titlePic.place_forget()
    #randomly choosing an option for computer
    comp=compChoice()
    #text to give user feedback
    variable=selected
    text=Label(window, text="You picked"+choice, font=("Impact",30))
    text.grid(column=0, row=0)
    npc=Label(window, text="The computer picked "+comp, font=("Impact",30))
    npc.place(y=75,x=0)
    versus=Label(window, text="VS", font=("Impact",45))
    versus.place(y=325,x=650)

#Placing images for user selection
    if choice==" Rock        ":
        rockPic=Label(image=rockImgU)
        rockPic.place(y=150,x=0)
    if choice==" Scissors":
        scisPic=Label(image=scisImgU)
        scisPic.place(y=150,x=0)
    if choice==" Paper      ":
        paperPic=Label(image=paperImgU)
        paperPic.place(y=150,x=0)
        
#Placing images for computer selection
    if comp=="rock          ":
        rockPic2=Label(image=rockImg)
        rockPic2.place(y=150,x=750)
    if comp=="scissors":
        scisPic2=Label(image=scisImg)
        scisPic2.place(y=150,x=750)
    if comp=="paper        ":
        paperPic2=Label(image=paperImg)
        paperPic2.place(y=150,x=750)

#Determing if player won and placing on screen    
    if comp=="rock          " and choice==" Paper      ":
        result=Label(window, text="You Win ", font=("Impact", 40))
        result.place(y=600,x=0)
    elif comp=="rock          " and choice==" Scissors":
        result=Label(window, text="You Lose ", font=("Impact", 40))
        result.place(y=600,x=0)
    elif comp=="rock          " and choice==" Rock        ":
        result=Label(window, text="Its a Tie  ", font=("Impact", 40))
        result.place(y=600,x=0)
    elif comp=="paper        " and choice==" Scissors":
        result=Label(window, text="You Win ", font=("Impact", 40))
        result.place(y=600,x=0)
    elif comp=="paper        " and choice==" Paper      ":
        result=Label(window, text="Its a Tie  ", font=("Impact", 40))
        result.place(y=600,x=0)
    elif comp=="paper        " and choice==" Rock        ":
        result=Label(window, text="You Lose ", font=("Impact", 40))
        result.place(y=600,x=0)
    elif comp=="scissors" and choice==" Scissors":
        result=Label(window, text="Its a Tie  ", font=("Impact", 40))
        result.place(y=600,x=0)
    elif comp=="scissors" and choice==" Paper      ":
        result=Label(window, text="You Lose", font=("Impact", 40))
        result.place(y=600,x=0)
    elif comp=="scissors" and choice==" Rock        ":
        result=Label(window, text="You Win ", font=("Impact", 40))
        result.place(y=600,x=0)
    else:
        result=Label(window, text="An error occured please try again", font=("Impact", 40))
        result.place(y=600,x=0)

#Makes choice varible = the chosen radial button.
def rock():
    global choice
    rockTrue= True
    choice=" Rock        "
def scissors():
    global choice
    scisTrue= True
    choice=" Scissors"
def paper():
    global choice
    choice=" Paper      "
    paperTrue=True
def compChoice():
    #randomly selects and option
    rps=random.randint(1,3)
    if rps==1:
        rps="rock          "
    elif rps==2:
        rps="paper        "
    elif rps==3:
        rps="scissors"
    else:
        rps="error"
    return rps
window.title("Rock Paper Scissors")
#Title page image
titleImg=ImageTk.PhotoImage(Image.open("rps.png"))
titlePic=Label(image=titleImg)
titlePic.place(y=200,x=500)
#Text
title= Label(window, text="Welcome to Saad's Rock, Paper, Scissors!", font=("Impact", 70))
title.grid(column=0, row=0)
subtitle= Label(window, text="Please pick an option.", font=("Impact", 40))
subtitle.grid(column=0, row=2)

#Button
selected=IntVar()

rock=Radiobutton(window,text='Rock', value=1, command=rock)
paper=Radiobutton(window,text='Paper', value=2, command=paper)
scis=Radiobutton(window,text='Scissors', value=3,command=scissors)

#placements
start=Button(window, text="Start", command= clicked)
rock.place(y=700,x=600)
paper.place(y=700,x=675)
scis.place(y=700,x=750)
start.place(y=700,x=890)
window.geometry('1920x1080')


#Adding images for Computer
rockImg= ImageTk.PhotoImage(Image.open("rock.png"))
scisImg= ImageTk.PhotoImage(Image.open("scis.png"))
paperImg= ImageTk.PhotoImage(Image.open("paper.png"))

#Adding flipped around images for User choice
rockImgU= ImageTk.PhotoImage(Image.open("rockU.png"))
scisImgU= ImageTk.PhotoImage(Image.open("scisU.png"))
paperImgU= ImageTk.PhotoImage(Image.open("paperU.png"))


window.mainloop()


