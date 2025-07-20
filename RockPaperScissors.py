import tkinter as tk
import random
from tkinter import *

def play ():
    r = int(rounds.get())
    def rule():
        move = user.get()
        print(move)
        turns = ["rock", "paper", "scissors"] 
        bot = random.choice(turns)
        bot_1 = tk.Label(frame, text=("BOT'S MOVE: ",bot),font=("Helvetica", 10, "bold"), fg = "#000000", bg="#8AF7FF")
        bot_1.place(x=350,y=300)
        if move == bot:
            print("it is a tie..")
        elif move == "scissors" and bot == "rock":
            str = "i win.."
            b+=1
        elif move == "scissors" and bot == "paper":
            str = "u win.."            
            u+=1
        elif move == "rock" and bot == "scissors":
            str = "u win.."
            u+=1
        elif move == "rock" and bot == "paper":
            str = "i win.."
            b+=1
        elif move == "paper" and bot == "scissors":
            str = "i win.."
            b+=1
        elif move == "paper" and bot == "rock":
            str = "u win.."
            u+=1
        else:
            str = "wrong input (no one wins)"
        res = tk.Label(frame, text= str, font=("Kristen ITC", 10, "bold"),bg="#FCFCFC", fg="#000000" )
        res.place(x=500,y=350)
    for i in range (r):
        i+=1
        user = tk.Entry(frame, text="", font=("Kristen ITC", 10, "bold"), bg="#FCFCFC", fg="#000000")
        user.place(x=400, y=200)
        submit = tk.Button(frame, text="GO..!", font=("Helvetica",9,"bold"), fg="#FCFCFA", bg="#FFAEAE", command=rule)
        submit.place(x=450, y=250)




container = tk.Tk()
container.title("Rock Paper Scissors:-")
container.geometry("500x500")
container.configure(bg = "#F6ED9C")
frame = tk.Frame(container, width=1100, height= 600, relief="groove",borderwidth=10, bg="#8AF7FF")
frame.place(x=100, y=50)
heading = tk.Label(frame, text="Rock Paper Scissors",font=("Helvetica", 30, "bold underline"), fg = "#FF8585", bg="#8AF7FF")
heading.place(x=350,y=20)
heading = tk.Label(frame, text="ENTER THE NUMBER OF ROUNDS",font=("Helvetica", 8, "bold"), fg = "#000000", bg="#8AF7FF")
heading.place(x=450,y=100)
rounds = tk.Entry(frame, text="", font=("Kristen ITC", 20, "bold"),width=2, bg="#FCFCFC", fg="#000000")
rounds.place(x=400, y=120)
submit = tk.Button(frame, text="SUBMIT", font=("Helvetica",9,"bold"),  height=1, fg="#FCFCFA", bg="#FFAEAE", command= play)
submit.place(x=520, y=160)

container.mainloop()