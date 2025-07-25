import tkinter as tk;
from tkinter import *

def click_button(value):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, current + value)

def calculate(value):
    current = display.get()
    result = str(eval(current))
    display.delete(0, tk.END)
    display.insert(0, result)

container = tk.Tk()
container.title("CALCULATOR")
container.geometry("500x500")
container.configure(bg = "#F6ED9C")
frame = tk.Frame(container, width=400, height= 600, relief="groove",borderwidth=10, bg="#8AF7FF")
frame.place(x=450, y=50)
screen = tk.Frame(frame, width=360, height= 80, relief="groove",borderwidth=7, bg="#000000")
screen.place(x=10, y=10)
display = tk.Entry(screen, font=("Courier", 22), bd=0, relief="flat", bg="#000000", fg="#00FF00", justify="right")
display.pack(fill="both", expand=True, padx=5, pady=5)
but1 = tk.Button(frame, text="1", font=("",20,"bold"), width=4, height=1,relief="groove",borderwidth=7, fg="#EC5A5A", bg="#7FF88F",command=lambda: click_button("1"))
but1.place(x=10, y=130)
but2 = tk.Button(frame, text="2", font=("",20,"bold"), width=4, height=1,relief="groove",borderwidth=7, fg="#EC5A5A", bg="#7FF88F",command=lambda: click_button("2"))
but2.place(x=145, y=130)
but3 = tk.Button(frame, text="3", font=("",20,"bold"), width=4, height=1,relief="groove",borderwidth=7, fg="#EC5A5A", bg="#7FF88F",command=lambda: click_button("3"))
but3.place(x=280, y=130)
but4 = tk.Button(frame, text="4", font=("",20,"bold"), width=4, height=1,relief="groove",borderwidth=7, fg="#EC5A5A", bg="#7FF88F",command=lambda: click_button("4"))
but4.place(x=10, y=220)
but5 = tk.Button(frame, text="5", font=("",20,"bold"), width=4, height=1,relief="groove",borderwidth=7, fg="#EC5A5A", bg="#7FF88F",command=lambda: click_button("5"))
but5.place(x=145, y=220)
but6 = tk.Button(frame, text="6", font=("",20,"bold"), width=4, height=1,relief="groove",borderwidth=7, fg="#EC5A5A", bg="#7FF88F",command=lambda: click_button("6"))
but6.place(x=280, y=220)
but7 = tk.Button(frame, text="7", font=("",20,"bold"), width=4, height=1,relief="groove",borderwidth=7, fg="#EC5A5A", bg="#7FF88F",command=lambda: click_button("7"))
but7.place(x=10, y=310)
but8 = tk.Button(frame, text="8", font=("",20,"bold"), width=4, height=1,relief="groove",borderwidth=7, fg="#EC5A5A", bg="#7FF88F",command=lambda: click_button("8"))
but8.place(x=145, y=310)
but9 = tk.Button(frame, text="9", font=("",20,"bold"), width=4, height=1,relief="groove",borderwidth=7, fg="#EC5A5A", bg="#7FF88F",command=lambda: click_button("9"))
but9.place(x=280, y=310)
but0 = tk.Button(frame, text="0", font=("",20,"bold"), width=4, height=1,relief="groove",borderwidth=7, fg="#EC5A5A", bg="#7FF88F",command=lambda: click_button("0"))
but0.place(x=10, y=400)
butEq = tk.Button(frame, text="=", font=("",20,"bold"), width=4, height=1,relief="groove",borderwidth=7, fg="#000000", bg="#C1C1C1",command=lambda: calculate("="))
butEq.place(x=280, y=400)
but_Add = tk.Button(frame, text="+", font=("",20,"bold"), width=3, height=1,relief="groove",borderwidth=5, fg="#000000", bg="#C1C1C1",command=lambda: click_button("+"))
but_Add.place(x=10, y=480)
but_Sub = tk.Button(frame, text="-", font=("",20,"bold"), width=3, height=1,relief="groove",borderwidth=5, fg="#000000", bg="#C1C1C1",command=lambda: click_button("-"))
but_Sub.place(x=80, y=480)
but_Mul = tk.Button(frame, text="*", font=("",20,"bold"), width=3, height=1,relief="groove",borderwidth=5, fg="#000000", bg="#C1C1C1",command=lambda: click_button("*"))
but_Mul.place(x=150, y=480)
but_Div = tk.Button(frame, text="/", font=("",20,"bold"), width=3, height=1,relief="groove",borderwidth=5, fg="#000000", bg="#C1C1C1",command=lambda: click_button("/"))
but_Div.place(x=220, y=480)
but_clear = tk.Button(frame, text="C", font=("", 20, "bold"), width=3, height=1,relief="groove", borderwidth=5, fg="#000000", bg="#FF8888",command=lambda: display.delete(0, tk.END))
but_clear.place(x=300, y=480)
container.mainloop()
