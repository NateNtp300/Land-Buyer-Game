from tkinter import *
import random
import time
from threading import Timer

window = Tk()
window.title("name")
# window.geometry("500x500")


class Player:
    def __init__(self, coins, coinsIncrement, grunts, warriors, black_knights, champions):
        self.coins = coins
        self.coinsIncrement = coinsIncrement
        self.grunts = grunts
        self.warriors = warriors
        self.black_knights = black_knights
        self.champions = champions

class Troops:
    def __init__(self, attack, defense, foodCost, ironCost, titatniumCost, crystalCost):
        self.attack = attack
        self.defense = defense
        self.foodCost = foodCost
        self.ironCost = ironCost
        self.titaniumCost = titatniumCost
        self.crystalCost = crystalCost

class MyButton(Button):
    def __init__(self, frame, text, isOwned, width, height, bg, command, **kwargs):
        rand = random.randint(1, 2)
        self.frame = frame
        self.text =text
        self.isOwned = isOwned
        self.bg = bg
        self.height=height
        self.width = width
        if rand == 1:
            self.cost = 20
        if rand == 2:
            self.cost = 50
        if self.cost ==20:
            self.coinAward = 2
        if self.cost ==50:
            self.coinAward = 3
        self.command = command
        super().__init__()
        if self.cost == 20:
            self['text']=20
        if self.cost == 50:
            self['text'] =50
        self['width']=self.width
        self['height']=self.height
        self['bg']=self.bg
        self['command'] = self.command
        
        
        


buttons = [ [0,0,0,0,0,0,0,0,0,0] ,[0,0,0,0,0,0,0,0,0,0] ,[0,0,0,0,0,0,0,0,0,0] ,[0,0,0,0,0,0,0,0,0,0] ,[0,0,0,0,0,0,0,0,0,0] ,[0,0,0,0,0,0,0,0,0,0] ,[0,0,0,0,0,0,0,0,0,0] ,[0,0,0,0,0,0,0,0,0,0] ,[0,0,0,0,0,0,0,0,0,0]  ,[0,0,0,0,0,0,0,0,0,0] ]
player = Player(20,0, 0, 0, 0, 0)


coinLabel = Label(window, text="Your Coins: "+ str(player.coins))
coinLabel.grid(row=20,column=0, columnspan=3, ipady=20)
# coinLabel.pack(side="top")

#adds the players passive income every 2 seconds and displays it
def updateCoins():
    global coinLabel
    #player coins increment according to land they own
    player.coins +=player.coinsIncrement
    coinLabel = Label(window, text="Your Coins: "+ str(player.coins))
    coinLabel.grid(row=20,column=0, columnspan=3, ipady=20)
    coinLabel.after(2000, updateCoins)
    # Timer(5,displayCoins).start()
updateCoins()

def displayCoins():
    global coinLabel
    coinLabel = Label(window, text="Your Coins: "+ str(player.coins))
    coinLabel.grid(row=20,column=0, columnspan=3, ipady=20)


def clickTurn(row, column):
    #checks if land is already bought. If it is then player cannot buy
    if buttons[row][column].isOwned == TRUE:
        print('plot already owned')
    if buttons[row][column].isOwned == FALSE:
        #if the players coins are greater than or equal to the land cost then they purchase the land
        if player.coins >= buttons[row][column].cost:
            print('You bought this plot')
            buttons[row][column]['text'] = "  "
            buttons[row][column]['bg'] = 'green'
            buttons[row][column].isOwned = TRUE
            player.coins -= buttons[row][column].cost
            #each land grants passive income and is added to the players coin increment
            player.coinsIncrement+= buttons[row][column].coinAward
            #displays player coins right after a purchase
            displayCoins()
        else:
            print('not enough coins')
    

frame1 = Frame(window)
frame1.grid()



for row in range(10):
    for column in range(10):
        buttons[row][column] = MyButton(frame1, " ", FALSE, 8, 3,"lightgrey", command=lambda row=row, column=column: clickTurn(row,column))
        buttons[row][column].grid(row=row,column=column)




window.mainloop()
