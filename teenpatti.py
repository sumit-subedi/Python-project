import random,itertools
import time
import conse
import draw
from tkinter import *
root=Tk()
msg1=StringVar()
msg2=StringVar()
root.geometry("1200x800")
usercoin=100
comcoin=100
i=0
j=0
k=0
f=Frame(root,bg="#00CED1")
f.place(relx=0.05,rely=0.05,relwidth=0.9,relheight=0.9)
root.update()
class patti:

    def __init__(self):
        num=[range(2,14)]
        color=['Hearts','Diamond','Spade','Club']

    def inival(self,deck,n):
        self.num=deck[n][0]
        self.color=deck[n][1]



    def show(self):
        global i
        if (self.color=="Diamond"):
            img=PhotoImage(file="images/diamond.gif")
        elif (self.color=="Spade"):
            img=PhotoImage(file="images/spade.gif")
        elif (self.color=="Hearts"):
            img=PhotoImage(file="images/heart.gif")
        else:
            img=PhotoImage(file="images/club.gif")

        if(self.num==11):
            no="J"
        elif(self.num==12):
            no="Q"
        elif(self.num==13):
            no="K"
        elif(self.num==14):
            no="A"
        else:
            no=self.num

        f1 = Frame(f,bg="white")
        f1.place(relx=0.05 + i, rely=0.2, relheight=0.3, relwidth=0.12)
        card = Label(f1, text=str(no), font=("", 20),bg="white")
        card.place(relx=0.05, rely=0.054, relheight=0.25)
        card1 = Label(f1, text=str(no), font=("", 20),bg="white")
        card1.place(relx=0.7, rely=0.75, relheight=0.25)


        l6 = Label(f1, image=img)
        l6.image = img
        l6.place(relx=0.15,rely=0.28, relwidth=0.7, relheight=0.5)

        i=i+0.15

    def comshow(self):
        global k
        if (self.color=="images/Diamond"):
            img=PhotoImage(file="images/diamond.gif")
        elif (self.color=="Spade"):
            img=PhotoImage(file="images/spade.gif")
        elif (self.color=="Hearts"):
            img=PhotoImage(file="images/heart.gif")
        else:
            img=PhotoImage(file="images/club.gif")

        if(self.num==11):
            no="J"
        elif(self.num==12):
            no="Q"
        elif(self.num==13):
            no="K"
        elif(self.num==14):
            no="A"
        else:
            no=self.num

        f1 = Frame(f,bg="white")
        f1.place(relx=0.55 + k, rely=0.2, relheight=0.3, relwidth=0.12)
        card = Label(f1, text=str(no), font=("", 20),bg="white")
        card.place(relx=0.05, rely=0.054, relheight=0.25)
        card1 = Label(f1, text=str(no), font=("", 20),bg="white")
        card1.place(relx=0.7, rely=0.75, relheight=0.25)


        l6 = Label(f1, image=img)
        l6.image = img
        l6.place(relx=0.15,rely=0.28, relwidth=0.7, relheight=0.5)

        k=k+0.15


    def cshow(self):
        global j
        f1 = Frame(f, bg="white")
        f1.place(relx=0.55 + j, rely=0.2, relheight=0.3, relwidth=0.12)

        photo=PhotoImage(file="images/card.gif")
        l5=Label(f1,image=photo)
        l5.image=photo
        l5.place(relwidth=1,relheight=1)
        j=j+0.15



    def checkstat(self,card1,card2,card3):
        if(card1.num==card2.num==card3.num):
            return 10
        elif(card1.color==card2.color==card3.color):
            if (conse.conse(card1.num,card2.num,card3.num)):
                return 8
            else:
                return 4
        elif(conse.conse(card1.num,card2.num,card3.num)==True):
            return 6
        elif((card1.num==card2.num or card1.num==card3.num) or (card2.num==card1.num or card2.num==card3.num)):
            return 2
        else:
            return 1

def pg():

    _list =f.winfo_children()


    for item in _list:
        item.destroy()
    pgm()

def butnpress(stat1,stat2,card1,card2,card3,card01,card02,card03):
    time.sleep(1)
    card01.comshow()
    card02.comshow()
    card03.comshow()
    if (stat1 == stat2):
        s = draw.checkstati(stat1, stat2, card1, card2, card3, card01, card02, card03)
        if (s == 1):
            stat1 += 1
        else:
            stat2 += 1
        if (stat1 > stat2):
            l5=Label(f,text="Hurray!! you won the game",font=("",25),bg="green")
            l5.place(relx=0.05,rely=0.7,relwidth=0.9,relheight=0.15)
        else:
            l5 = Label(f, text="Sorry! Computer won the game.", font=("", 25),bg="black",fg="white")
            l5.place(relx=0.05, rely=0.7, relwidth=0.9, relheight=0.15)

    elif (stat1 > stat2):
        l5 = Label(f, text="Hurray!! you won the game", font=("", 25),bg="green")
        l5.place(relx=0.05, rely=0.7, relwidth=0.9, relheight=0.15)
    else:
        l5 = Label(f, text="Sorry! Computer won the game.", font=("", 25),bg="black",fg="white")
        l5.place(relx=0.05, rely=0.7, relwidth=0.9, relheight=0.15)

    b2 = Button(f, text="Play Again", bg="yellow", fg="brown", font=("", 15),command=lambda:pg())
    b2.place(relx=0.45, rely=0.9, relwidth=0.2, relheight=0.1)




def pgm():
    global i
    global j,k
    global usercoin
    i=j=k=0
    while(1):
        deck = list(itertools.product(range(2, 15), ['Hearts', 'Diamond', 'Spade', 'Club']))
        random.shuffle(deck)
        user=patti()
        card1=patti()
        card1.inival(deck,0)
        card2=patti()
        card2.inival(deck,1)
        card3=patti()
        card3.inival(deck,2)
        card01=patti()
        card01.inival(deck,3)
        card02=patti()
        card02.inival(deck,4)
        card03=patti()
        card03.inival(deck,5)

        msg1.set("Yourcoin="+str(usercoin))
        l1=Label(f,textvariable=msg1,bg="lightgreen",font=("",15),fg="brown")
        l1.place(relx=0,rely=0,relwidth=0.22,relheight=0.05)

        msg2.set("Computer's coin= "+str(comcoin))
        label=Label(f,textvariable=msg2,bg="silver",font=("",15))
        label.place(relx=0.75,rely=0,relwidth=0.25,relheight=0.05)

        l3=Label(f,bg="brown")
        l3.place(relx=0.5,rely=0,relheight=0.7,relwidth=0.01)


        l2=Label(f,text="Your cards are:".ljust(10,"\n"),anchor=NE,bg="gray",font=("",25),fg="white")
        l2.place(relx=0.05,rely=0.1,relheight=0.08)
        card1.show()
        card2.show()
        card3.show()

        l4=Label(f,text="Computer's cards are:".ljust(10,"\n"),anchor=NE,bg="gray",font=("",25),fg="white")
        l4.place(relx=0.6,rely=0.1,relheight=0.08)
        card01.cshow()
        card02.cshow()
        card03.cshow()

        usercoin=usercoin-20
        msg1.set("Your coin's = "+str(usercoin))
        root.update()

        user=patti()
        com=patti()

        stat1=user.checkstat(card1,card2,card3)
        stat2=com.checkstat(card01,card02,card03)
        b1=Button(f,text="Check result",command=lambda : butnpress(stat1,stat2,card1,card2,card3,card01,card02,card03))
        b1.place(relx=0.25,rely=0.6,relheight=0.08)
        root.mainloop()

pgm()