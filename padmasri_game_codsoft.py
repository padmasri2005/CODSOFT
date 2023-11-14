from tkinter import *
import random

root = Tk()

root.geometry("550x500")

root.title("Rock Paper Scissor Game")

computer_value = {
    "0": "Rock",
    "1": "Paper",
    "2": "Scissor"
}

# To Reset The Game 

def reset_game():
    b1["state"] = "active"
    b2["state"] = "active"
    b3["state"] = "active"
    l1.config(text="User              ")
    l3.config(text="Computer")
    l4.config(text="")


# Disable the Button


def button_disable():
    b1["state"] = "disable"
    b2["state"] = "disable"
    b3["state"] = "disable"


# If user selected rock as option

def isrock():
    c_v = computer_value[str(random.randint(0, 2))]
    if c_v == "Rock":
        match_result = "Match Draw"
    elif c_v == "Scissor":
        match_result = "User Win"
    else:
        match_result = "Computer Win"
    l4.config(text=match_result)
    l1.config(text="Rock            ")
    l3.config(text=c_v)
    button_disable()


# If user selected paper as option


def ispaper():
    c_v = computer_value[str(random.randint(0, 2))]
    if c_v == "Paper":
        match_result = "Match Draw"
    elif c_v == "Scissor":
        match_result = "Computer Win"
    else:
        match_result = "User Win"
    l4.config(text=match_result)
    l1.config(text="Paper           ")
    l3.config(text=c_v)
    button_disable()


# If player selected scissor as option


def isscissor():
    c_v = computer_value[str(random.randint(0, 2))]
    if c_v == "Rock":
        match_result = "Computer Win"
    elif c_v == "Scissor":
        match_result = "Match Draw"
    else:
        match_result = "User Win"
    l4.config(text=match_result)
    l1.config(text="Scissor         ")
    l3.config(text=c_v)
    button_disable()


#  To Add Labels, Frames and Button
Label(root,
      text="Rock Paper Scissor Game",
      font="normal 20 bold",
      fg="blue").pack(pady=20)

frame = Frame(root)
frame.pack()

l1 = Label(frame,
           text="User              ",
           font=10)

l2 = Label(frame,
           text="VS             ",
           font="normal 10 bold")

l3 = Label(frame, text="Computer", font=10)

l1.pack(side=LEFT)
l2.pack(side=LEFT)
l3.pack()

l4 = Label(root,
           text="",
           font="normal 20 bold",
           bg="white",
           width=15,
           borderwidth=2,
           relief="solid")
l4.pack(pady=20)

frame1 = Frame(root)
frame1.pack()

b1 = Button(frame1, text="Rock",
            font=10, width=7,
            command=isrock)

b2 = Button(frame1, text="Paper ",
            font=10, width=7,
            command=ispaper)

b3 = Button(frame1, text="Scissor",
            font=10, width=7,
            command=isscissor)

b1.pack(side=LEFT, padx=10)
b2.pack(side=LEFT, padx=10)
b3.pack(padx=10)

Button(root, text="Play Again",
       font=10, fg="red",
       bg="black", command=reset_game).pack(pady=20)

Label(root,
      text="Press Rock or Paper Or  Scissor Button",
      font="normal 20 bold",
      fg="green").pack(side=LEFT)

frame = Frame(root)

root.mainloop()

