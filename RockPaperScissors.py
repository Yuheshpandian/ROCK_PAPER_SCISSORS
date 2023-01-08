from tkinter import *
import random

root = Tk()
root.geometry('500x500')
root.title('ROCK-PAPER-SCISSORS')
root.config(bg='sky blue')


dict = ["rock",'paper','scissor']

def play(player):
    

    text = ''
    computer = random.choice(dict)

    lbl1 = Label(root, text = "YOU CHOOSED:" +player.upper()+'      ', font = ('Arial', 25))
    lbl1.config(bg = 'sky blue')
    lbl1.place(relx = 0.15, rely = 0.2)

    lbl2 = Label(root, text = "COMPUTER CHOOSED:" +computer.upper()+'     ', font = ('Arial', 20))
    lbl2.config(bg = 'sky blue')
    lbl2.place(relx = 0.12, rely = 0.4)


    if computer=='rock' and player == 'scissor' or computer == 'paper' and player == 'rock' or computer == 'scissor' and player == 'paper':
        text = 'computer won'
    elif player=='rock' and computer == 'scissor' or player == 'paper' and computer == 'rock' or player == 'scissor' and computer == 'paper':
        text = 'you won !       '
    else:
        text = 'its a draw      '

    lbl = Label(root, text = text,font = ('Arial', 15))
    lbl.config(bg = 'sky blue')
    lbl.place(relx = 0.43,rely = 0.9)

chooselbl = Label(root, text = 'CHOOSE')
chooselbl.config(bg = 'sky blue')
chooselbl.place(relx = 0.45, rely = 0.6)


rockbtn = Button(root, text = 'ROCK',padx = 10,pady = 20,command=lambda : play('rock'))
rockbtn.place(relx=0.2, rely= 0.7, anchor = NW)


paperbtn = Button(root, text = 'PAPER',padx = 10,pady = 20,command=lambda : play('paper'))
paperbtn.place(relx=0.45, rely= 0.7, anchor = NW)


scissorbtn = Button(root, text = 'SCISSOR',padx = 7,pady = 20,command=lambda : play('scissor'))
scissorbtn.place(relx=0.7, rely= 0.7, anchor = NW)



root.mainloop()
