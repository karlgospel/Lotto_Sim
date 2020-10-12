#!/usr/bin/env python3
import random
import tkinter as tk
from tkinter import messagebox
from tkinter import StringVar
from tkinter import ttk
from tkinter import simpledialog

def lotto():
    """Runs the lotto simulation by randomly selecting 6 numbers and then comparing them to the user's
        chosen numbers. This is repeated for as many times as stated by the user. Each time the relevant
        amount of numbers match, the corresponding prize money is totalled up. The total prize money is
        returned and the 'updateResults' function is called to display the results to the user"""
    try:
        ballPicks = {int(pickOne.get()), pickTwo.get(), pickThree.get(), pickFour.get(), pickFive.get(), pickSix.get()}
    except:
        return
    
    if len(ballPicks) < 6:
        messagebox.showinfo("Hmmmmmmmmmm", "Please check your numbers: No duplicates")
        return
    notEmpty()
        
    #playButton.config(text="please wait...")
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
        balls = random.sample(range(1,49), 6)
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
    """Returns the six lotto numbers that have been picked by the user"""
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
    """Returns the amount of runs/weeks that has been entered by the user"""
    
    total=0
    try:
        total = int(runs.get())
    except:
        return
    return(total)

def getTicketCost():
    """Returns the ticket cost that has been entered by the user"""
    
    try:
        ticket = ticketCost.get()
    except:
        return
    return(int(ticket))

def updateResults(totalPrize, ticketPrice, threeCount,fourCount,fiveCount,fiveAndBonusCount,sixCount):
    """Returns all of the information regarding winnings and costs to the user"""
    
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
    prizeMoney.config(text = "$" + (str(totalPrize)))
    
    
def randomPick():
    """Creates a list of six random integers and adds each one to an entry box"""
    
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
    randPicks = []
    randPicks = random.sample(range(1,49), 6)
    pickOne.insert(0, randPicks[0])
    pickTwo.insert(0, randPicks[1])
    pickThree.insert(0, randPicks[2])
    pickFour.insert(0, randPicks[3])
    pickFive.insert(0, randPicks[4])
    pickSix.insert(0, randPicks[5])
    #random.sample(range(1,49))

def callback(input):
    """Validates user input to ensure it is an integer"""
    if input.isdigit():
        return True
                        
    elif input is "":
        return True

    else:
        return False
    
def notEmpty():
    if not pickOne.get() or int(pickOne.get()) > 49:
        pickOne.config(highlightbackground="black",highlightthickness=1.5)
    else:
        pickOne.config(highlightthickness=0)
        
    if not pickTwo.get() or int(pickTwo.get()) > 49:
        pickTwo.config(highlightbackground="black",highlightthickness=1.5)
    else:
        pickTwo.config(highlightthickness=0)
    
    if not pickThree.get() or int(pickThree.get()) > 49:
        pickThree.config(highlightbackground="black",highlightthickness=1.5)
    else:
        pickThree.config(highlightthickness=0)

    if not pickFour.get() or int(pickFour.get()) > 49:
        pickFour.config(highlightbackground="black",highlightthickness=1.5)
    else:
        pickFour.config(highlightthickness=0)
        
    if not pickFive.get() or int(pickFive.get()) > 49:
        pickFive.config(highlightbackground="black",highlightthickness=1.5)
    else:
        pickFive.config(highlightthickness=0)
        
    if not pickSix.get() or int(pickSix.get()) > 49:
        pickSix.config(highlightbackground="black",highlightthickness=1.5)
    else:
        pickSix.config(highlightthickness=0)
    
    if not ticketCost.get() or int(ticketCost.get()) > 49:
        ticketCost.config(highlightbackground="black", highlightthickness=1.5)
    else:
        ticketCost.config(highlightthickness=0)
        
    if not runs.get():
        runs.config(highlightbackground="black", highlightthickness=1.5)
    else:
        runs.config(highlightthickness=0)
    

#####----------GUI Code-----------######

window = tk.Tk()
window.title("Lotto")
window.state('zoomed')
#window['bg'] = '#49A'

#Register the callback function to validate user input, ensuring an integer is entered
reg=window.register(callback)

#Main Heading
heading = tk.Label(window, text= "Lotto Simulator", font = ("Times New Roman", 22))
heading.grid(column=2, row =0, sticky='nsew', columnspan=3, pady=25)

#Six boxes for user to pick their Lotto numbers
pickLabel = tk.Label(window, text= "1. Pick your numbers (1-49):", font = ("Times New Roman", 14))
pickLabel.grid(column=0, row =2, columnspan=3, sticky='w',padx=20)

pickOne = tk.Entry(window,width=3, font = ("Times New Roman", 40),bg="red", fg="yellow", justify=tk.CENTER)
pickOne.grid(column=0, row=3, pady=2, ipady=8, padx = (20,0), sticky='w')
pickOne.config(validate="key", validatecommand=(reg, '%P'), relief=tk.RIDGE)

pickTwo = tk.Entry(window,width=3, font = ("Times New Roman", 40),bg="green", fg="red", justify=tk.CENTER)
pickTwo.grid(column=1, row=3, pady=2, ipady=8, padx = (20,0), sticky='w')
pickTwo.config(validate="key", validatecommand=(reg, '%P'), relief=tk.RIDGE)

pickThree = tk.Entry(window,width=3, font = ("Times New Roman", 40),bg="yellow", fg="orange", justify=tk.CENTER)
pickThree.grid(column=2, row=3, pady=2, ipady=8, padx = (20,0), sticky='w')
pickThree.config(validate="key", validatecommand=(reg, '%P'), relief=tk.RIDGE)

pickFour = tk.Entry(window,width=3, font = ("Times New Roman", 40),bg="blue", fg="pink", justify=tk.CENTER)
pickFour.grid(column=3, row=3, pady=2, ipady=8, padx = (20,0), sticky='w')
pickFour.config(validate="key", validatecommand=(reg, '%P'), relief=tk.RIDGE)

pickFive = tk.Entry(window,width=3, font = ("Times New Roman", 40),bg="pink", fg="blue", justify=tk.CENTER)
pickFive.grid(column=4, row=3, pady=2, ipady=8, padx = (20,0), sticky='w')
pickFive.config(validate="key", validatecommand=(reg, '%P'), relief=tk.RIDGE)

pickSix = tk.Entry(window,width=3, font = ("Times New Roman", 40),bg="orange", fg="red", justify=tk.CENTER)
pickSix.grid(column=5, row=3, pady=2, ipady=8, padx = (20,0), sticky='w')
pickSix.config(validate="key", validatecommand=(reg, '%P'), relief=tk.RIDGE)

#Button to randomise user's Lotto balls pick
randomButton = tk.Button(window, text= "Lucky Dip", font = ("Times New Roman", 14),command=randomPick)
randomButton.grid(column=2, row=4, pady=10, ipady=1, padx = (20,0), columnspan=3, sticky='nsew', rowspan=2)

#Choose the cost of a Lotto ticket
ticketCostLabel = tk.Label(window, text= "2. Cost per ticket:", font = ("Times New Roman", 14))
ticketCostLabel.grid(column=0, row =7, columnspan=2, sticky='w',padx=20)
ticketCost = tk.Entry(window,width=4, font = ("Times New Roman", 20))
ticketCost.grid(column=4, row=7, pady=10, ipady=4, padx = 10, sticky='nsew', columnspan=2,rowspan=1)
ticketCost.config(validate="key", validatecommand=(reg, '%P'))

#Choose how many times to run simulation
runsLabel = tk.Label(window, text= "3. How many runs/weeks would you like to play?", font = ("Times New Roman", 14))
runsLabel.grid(column=0, row =9, columnspan=4, sticky='w',padx=20)
runs = tk.Entry(window,width=4, font = ("Times New Roman", 20))
runs.grid(column=4, row=9, pady=10, ipady=4, padx = 10, sticky='nsew', columnspan=2,rowspan=1)
runs.config(validate="key", validatecommand=(reg, '%P'))

#Enter choices - run sim
playButton = tk.Button(window, text= "PLAY", font = ("Times New Roman", 30), width =10, command=lotto)
playButton.grid(column=2, row=10, pady=10, ipady=4, padx = 10, columnspan=3, sticky='nsew',rowspan=3)

#Prize breakdown info - how many times user won each prize
prizeBreakdownLabel = tk.Label(window, text= "Prize Breakdown:", font = ("Times New Roman", 22))
prizeBreakdownLabel.grid(column=6, row =0, columnspan=4, sticky='nsew', pady=25)

threeCorrectLabel = tk.Label(window, text= "3 Balls ($30) - ", font = ("Times New Roman", 12))
threeCorrectLabel.grid(column=7, row =4, columnspan=1, sticky='nsew')
threeCorrectCount = tk.Label(window, text="", font = ("Times New Roman", 12))
threeCorrectCount.grid(column=8, row=4, columnspan =3, padx=0, pady=0, sticky='nsew')

fourCorrectLabel = tk.Label(window, text= "4 Balls ($140) - ", font = ("Times New Roman", 12))
fourCorrectLabel.grid(column=7, row =5, columnspan=1)
fourCorrectCount = tk.Label(window, text="", font = ("Times New Roman", 12))
fourCorrectCount.grid(column=8, row=5, columnspan =3, padx=5, pady=5, sticky='nsew')

fiveCorrectLabel = tk.Label(window, text= "5 Balls ($1750) - ", font = ("Times New Roman", 12))
fiveCorrectLabel.grid(column=7, row =6, columnspan=1, sticky='nsew')
fiveCorrectCount = tk.Label(window, text="", font = ("Times New Roman", 12))
fiveCorrectCount.grid(column=8, row=6, columnspan =3, padx=5, pady=5, sticky='nsew')

fiveAndBonusCorrectLabel = tk.Label(window, text= "5 Balls + Bonus ($1,000,000) - ", font = ("Times New Roman", 12))
fiveAndBonusCorrectLabel.grid(column=7, row =7, columnspan=1, sticky='nsew')
fiveAndBonusCorrectCount = tk.Label(window, text="", font = ("Times New Roman", 12))
fiveAndBonusCorrectCount.grid(column=8, row=7, columnspan =3, padx=5, pady=5, sticky='nsew')

sixCorrectLabel = tk.Label(window, text= "6 Balls - JACKPOT - ($5,000,000) - ", font = ("Times New Roman", 12))
sixCorrectLabel.grid(column=7, row =8, columnspan=1, sticky='nsew')
sixCorrectCount = tk.Label(window, text="", font = ("Times New Roman", 12))
sixCorrectCount.grid(column=8, row=8, columnspan =3, padx=5, pady=5, sticky='nsew')

prizeMoneyLabel = tk.Label(window, text= "Total Prize Money - ", font = ("Times New Roman", 12))
prizeMoneyLabel.grid(column=7, row =9, columnspan=1, sticky='nsew')
prizeMoney = tk.Label(window, text="", font = ("Times New Roman", 12))
prizeMoney.grid(column=8, row=9, columnspan =3, padx=5, pady=5, sticky='nsew')

winningsLabel = tk.Label(window, text= "", font = ("Times New Roman", 20))
winningsLabel.grid(column=7, row =11, columnspan=3, sticky='nsew')
winningsTotal = tk.Label(window, text="", font = ("Times New Roman", 40))
winningsTotal.grid(column=7, row=12, columnspan =3, padx=15, pady=5, sticky='nsew')

ticketsLabel = tk.Label(window, text= "Total ticket cost - ", font = ("Times New Roman", 12))
ticketsLabel.grid(column=7, row =10, columnspan=1, sticky='nsew')
ticketsTotal = tk.Label(window, text="", font = ("Times New Roman", 12))
ticketsTotal.grid(column=8, row=10, columnspan =3, padx=5, pady=5, sticky='nsew')

##Line to seperate results
tk.ttk.Separator(window, orient=tk.VERTICAL).grid(column=6, row=0, rowspan=20, sticky='ns',padx=(0,20))
#tk.ttk.Separator(window, orient=tk.HORIZONTAL).grid(column=0, row=1,columnspan=20, sticky='ew')

window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
window.columnconfigure(2, weight=1)
window.columnconfigure(3, weight=1)
window.columnconfigure(4, weight=1)
window.columnconfigure(5, weight=1)
window.columnconfigure(6, weight=1)
window.columnconfigure(7, weight=1)
window.columnconfigure(8, weight=1)
window.columnconfigure(9, weight=1)
window.columnconfigure(10, weight=1)

window.mainloop()