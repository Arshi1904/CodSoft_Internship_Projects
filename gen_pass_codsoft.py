import tkinter as tk
import string
import random

def pass_gen ():
    
    dialog = tk.Toplevel()
    dialog.title("PASSWORD")
    dialog.configure(bg = "#FFFEB4")
    dialog.geometry("400x500")
    tk.Label(dialog, text="The Genrated Password", font=("MV Boli", 20, "bold"), fg="#FA6868", bg = "#9CFFAF").pack()
    l = int(len.get())
    s = ""
    symbols = "!@#$%^&*()_+-=[]:;'<>,.?/"
    U_letters = string.ascii_uppercase
    L_letters = string.ascii_lowercase
    digits = string.digits
    randoms = random.choice(U_letters)+random.choice(L_letters)
    s = s + random.choice(randoms)
    for i in range(l-1):
        randoms1 =  random.choice(symbols)+random.choice(U_letters)+random.choice(L_letters)+random.choice(digits)
        s = s + random.choice(randoms1)

    tk.Label(dialog, text=s, font=("MV Boli",40,"bold"), fg="#FF0000", bg="#FFFF98").pack(pady=80)
    

container = tk.Tk()
container.title("Password Generator")
container.geometry("500x500")
container.configure(bg = "#F6ED9C")
frame = tk.Frame(container, width=1050, height= 500, relief="groove",borderwidth=10, bg="#8AF7FF")
frame.place(x=90, y=100)
heading = tk.Label(frame, text="PASSWORD GENERATOR", font=("MV Boli", 20, "bold"), bg="#C2F8A0", fg="#FD6565")
heading.place(x=350, y=20)
length = tk.Label(frame, text="ENTER THE LENGTH OF THE PASSWORD: ", font=("Kristen ITC", 10, "bold"), bg="#FCFCFC", fg="#000000")
length.place(x=20, y=90)
len = tk.Entry(frame, text="", font=("Kristen ITC", 10, "bold"), bg="#FCFCFC", fg="#000000")
len.place(x=300, y=90)
password = tk.Button(frame, text="Generate", font=("Kristen ITC", 10, "bold"), bg="#FF0000", fg="#F89B9B", command= pass_gen)
password.place(x= 500, y=85)

container.mainloop()
