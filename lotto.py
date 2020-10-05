#!/usr/bin/env python3
import random
import tkinter as tk
from tkinter import messagebox
from tkinter import StringVar
from tkinter import ttk

def lotto():
    playButton.config(text="please wait...")
    totalRuns=0
    totalPrize = 0
    threeCount = 0
    fourCount = 0
    fiveCount = 0
    fiveAndBonusCount = 0
    sixCount = 0
    choices = getPicks()
    #print(choices)
    try:
        runs = int(getRuns())
        ticketPrice = runs * int(getTicketCost())
    except:
        return
    #choices = {a,b,c,d,e,f}
    if len(choices) < 6:
        tk.messagebox.askretrycancel('Missing Entry','You missed something')
        return
    #print(choices)
    while totalRuns <= int(runs):
        prize = 0
        correct = []
        bonusWin = False
        balls = random.sample(range(1,49), 7)
        bonusBall = balls.pop(5)
        balls.sort()
        #print(balls)
        #print(bonusBall)
        for i in choices:
            if i in balls:
                correct.append(i)
        #print(correct)
        if bonusBall in balls:
            bonusWin == True
        if len(correct) == 3:
            prize += 30
            threeCount += 1
        if len(correct) == 4:
            prize+= 140
            fourCount+= 1
        if len(correct) == 5:
            prize+= 1750
            fiveCount+=1
        if len(correct) == 6:
            prize+= 5000000
            sixCount+=1
        if len(correct) == 5 and bonusWin == True:
            prize += 1000000
            fiveAndBonusCount+=1
        #print("prize")
        #print(prize)
        totalRuns += 1
        totalPrize = totalPrize + prize
    #print("Total prize")
    updateResults(totalPrize, ticketPrice, threeCount,fourCount,fiveCount,fiveAndBonusCount,sixCount)
    playButton.config(text="PLAY")

    return(totalPrize)    
        
    
    
def getPicks():
    try:
        ballOne = int(pickOne.get())
        ballTwo = int(pickTwo.get())
        ballThree = int(pickThree.get())
        ballFour = int(pickFour.get())
        ballFive = int(pickFive.get())
        ballSix = int(pickSix.get())
    except:
        return
    return(ballOne,ballTwo,ballThree,ballFour,ballFive,ballSix)

def getRuns():
    total=0
    try:
        total = int(runs.get())
    except:
        return
    return(total)

def getTicketCost():
    try:
        ticket = ticketCost.get()
    except:
        return
    return(int(ticket))

def updateResults(totalPrize, ticketPrice, threeCount,fourCount,fiveCount,fiveAndBonusCount,sixCount):
    totalWinnings = totalPrize - ticketPrice
    if totalWinnings <= 0:
        winningsLabel.config(text="You Lost",bg="red")
    elif totalWinnings >0 and sixCount == 0:
        winningsLabel.config(text="You Won",bg="green")
    elif sixCount >0:
        winningsLabel.config(text="$$$$$$ CONGRATULATIONS, YOU WON THE JACKPOT!!! $$$$$$$", bg="yellow")

    winningsTotal.config(text = "$" + str((abs(totalWinnings))))
    ticketsTotal.config(text= "$" + (str(ticketPrice)))
    threeCorrectCount.config(text = (str(threeCount) + " ($" + str((threeCount)*30) + ")"))
    fourCorrectCount.config(text = (str(fourCount) + " ($" + str((fourCount)*140) + ")"))
    fiveCorrectCount.config(text = (str(fiveCount) + " ($" + str((fiveCount)*1750) + ")"))
    fiveAndBonusCorrectCount.config(text = (str(fiveAndBonusCount) + " ($" + str((fiveAndBonusCount)*1000000) + ")"))
    sixCorrectCount.config(text = (str(sixCount) + " ($" + str((sixCount)*5000000) + ")"))
    
def randomPick():
    try:
        pickOne.delete(0, tk.END)
    except:
        pass
    try:
        pickTwo.delete(0, tk.END)
    except:
        pass
    try:
        pickThree.delete(0, tk.END)

    except:
        pass
    try:
        pickFour.delete(0, tk.END)
    except:
        pass
    try:
        pickFive.delete(0, tk.END)
    except:
        pass
    try:
        pickSix.delete(0, tk.END)
    except:
        pass
    pickOne.insert(0, random.randint(1,49))
    pickTwo.insert(0, random.randint(1,49))
    pickThree.insert(0, random.randint(1,49))
    pickFour.insert(0, random.randint(1,49))
    pickFive.insert(0, random.randint(1,49))
    pickSix.insert(0, random.randint(1,49))
    #random.sample(range(1,49))

#####----------GUI Code-----------######

window = tk.Tk()
window.title("Lotto")
window.state('zoomed')

#Main Heading
heading = tk.Label(window, text= "Lotto Simulator", font = ("Comic Sans MS Bold", 16))
heading.grid(column=3, row =0)

#Six boxes for user to pick their Lotto numbers
pickLabel = tk.Label(window, text= "Pick your numbers (1-49):", font = ("Comic Sans MS", 12))
pickLabel.grid(column=0, row =2, columnspan=2)

pickOne = tk.Entry(window,width=2, font = ("Comic Sans MS", 40))
pickOne.grid(column=0, row=3, pady=10, ipady=8, padx = 10)

pickTwo = tk.Entry(window,width=2, font = ("Comic Sans MS", 40))
pickTwo.grid(column=1, row=3, pady=10, ipady=8, padx = 10)

pickThree = tk.Entry(window,width=2, font = ("Comic Sans MS", 40))
pickThree.grid(column=2, row=3, pady=10, ipady=8, padx = 10)

pickFour = tk.Entry(window,width=2, font = ("Comic Sans MS", 40))
pickFour.grid(column=3, row=3, pady=10, ipady=8, padx = 10)

pickFive = tk.Entry(window,width=2, font = ("Comic Sans MS", 40))
pickFive.grid(column=4, row=3, pady=10, ipady=8, padx = 10)

pickSix = tk.Entry(window,width=2, font = ("Comic Sans MS", 40))
pickSix.grid(column=5, row=3, pady=10, ipady=8, padx = 10)

#Button to randomise user's Lotto balls pick
randomButton = tk.Button(window, text= "Pick Random", font = ("Comic Sans MS ", 12),command=randomPick)
randomButton.grid(column=2, row=4, pady=10, ipady=10, padx = 10, columnspan=2)

#Choose the cost of a Lotto ticket
ticketCostLabel = tk.Label(window, text= "Cost per ticket:", font = ("Comic Sans MS ", 12))
ticketCostLabel.grid(column=0, row =5, columnspan=2)
ticketCost = tk.Entry(window,width=10, font = ("Comic Sans MS", 12))
ticketCost.grid(column=0, row=6, pady=10, ipady=4, padx = 10)

#Choose how many times to run simulation
runsLabel = tk.Label(window, text= "How many runs/weeks would you like to play?")
runsLabel.grid(column=0, row =7, columnspan=3)
runs = tk.Entry(window,width=10, font = ("Comic Sans MS", 20))
runs.grid(column=0, row=8, pady=10, ipady=4, padx = 10)

#Enter choices - run sim
playButton = tk.Button(window, text= "PLAY", font = ("Comic Sans MS ", 12), width =10, command=lotto)
playButton.grid(column=2, row=9, pady=10, ipady=10, padx = 10, columnspan=2)

#Prize breakdown info - how many times user won each prize
prizeBreakdownLabel = tk.Label(window, text= "Prize Breakdown:", font = ("Comic Sans MS ", 12))
prizeBreakdownLabel.grid(column=7, row =3, columnspan=3)

threeCorrectLabel = tk.Label(window, text= "3 Balls ($30)- ", font = ("Comic Sans MS ", 8))
threeCorrectLabel.grid(column=7, row =4, columnspan=3)
threeCorrectCount = tk.Label(window, text="", font = ("Comic Sans MS", 8))
threeCorrectCount.grid(column=8, row=4, columnspan =3, padx=5, pady=5)

fourCorrectLabel = tk.Label(window, text= "4 Balls ($140)- ", font = ("Comic Sans MS", 8))
fourCorrectLabel.grid(column=7, row =5, columnspan=3)
fourCorrectCount = tk.Label(window, text="", font = ("Comic Sans MS", 8))
fourCorrectCount.grid(column=8, row=5, columnspan =3, padx=5, pady=5)

fiveCorrectLabel = tk.Label(window, text= "5 Balls ($1750)- ", font = ("Comic Sans MS", 8))
fiveCorrectLabel.grid(column=7, row =6, columnspan=3)
fiveCorrectCount = tk.Label(window, text="", font = ("Comic Sans MS", 8))
fiveCorrectCount.grid(column=8, row=6, columnspan =3, padx=5, pady=5)

fiveAndBonusCorrectLabel = tk.Label(window, text= "5 Balls + Bonus ($1,000,000)- ", font = ("Comic Sans MS", 8))
fiveAndBonusCorrectLabel.grid(column=7, row =7, columnspan=3)
fiveAndBonusCorrectCount = tk.Label(window, text="", font = ("Comic Sans MS", 8))
fiveAndBonusCorrectCount.grid(column=8, row=7, columnspan =3, padx=5, pady=5)

sixCorrectLabel = tk.Label(window, text= "6 Balls - JACKPOT - ($5,000,000)- ", font = ("Comic Sans MS", 8))
sixCorrectLabel.grid(column=7, row =8, columnspan=3)
sixCorrectCount = tk.Label(window, text="", font = ("Comic Sans MS", 8))
sixCorrectCount.grid(column=8, row=8, columnspan =3, padx=5, pady=5)

winningsLabel = tk.Label(window, text= "", font = ("Comic Sans MS", 8))
winningsLabel.grid(column=7, row =10, columnspan=3)
winningsTotal = tk.Label(window, text="", font = ("Comic Sans MS", 8))
winningsTotal.grid(column=8, row=11, columnspan =3, padx=5, pady=5)

ticketsLabel = tk.Label(window, text= "Total ticket cost - ", font = ("Comic Sans MS", 8))
ticketsLabel.grid(column=7, row =9, columnspan=3)
ticketsTotal = tk.Label(window, text="", font = ("Comic Sans MS", 8))
ticketsTotal.grid(column=8, row=9, columnspan =3, padx=5, pady=5)

##Line to seperate results
tk.ttk.Separator(window, orient=tk.VERTICAL).grid(column=6, row=0, rowspan=20, sticky='ns',padx=(0,20))
#tk.ttk.Separator(window, orient=tk.HORIZONTAL).grid(column=0, row=1,columnspan=20, sticky='ew')

window.mainloop()

    

