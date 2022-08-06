# from tkinter import messagebox
from tkinter import *
import pandas
from random import *

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}
try:
    data = pandas.read_csv("data/what_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict("records")
else:
    to_learn = data.to_dict("records")


def next_card():
    global current_card, sleep
    window.after_cancel(sleep)
    current_card = choice(to_learn)
    canvas.itemconfig(word_text, text=current_card["French"], fill="black")
    canvas.itemconfig(title_text, text="French", fill="black")
    canvas.itemconfig(canvas_image, image=card_front_image)
    sleep = window.after(3000, flip_card)


def is_known():
    to_learn.remove(current_card)
    df = pandas.DataFrame(to_learn)
    df.to_csv("data/what_to_learn.csv", index=False)
    next_card()


def flip_card():
    canvas.itemconfig(canvas_image, image=card_back_image)
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=current_card["English"], fill="white")


window = Tk()
window.title("Study English With My Cards")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)
sleep = window.after(3000, flip_card)
# ---------------- CANVAS

canvas = Canvas(width=800, height=526)
card_front_image = PhotoImage(file="./images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=card_front_image)
title_text = canvas.create_text(400, 100, text="", font=("Arial", 30, "italic"))
word_text = canvas.create_text(400, 253, text="", font=("Arial", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

# ---------------- BUTTONS

yes_image = PhotoImage(file="./images/right.png")
yes_button = Button(image=yes_image, highlightthickness=0, border=0, command=is_known)
yes_button.grid(row=1, column=1)

no_image = PhotoImage(file="./images/wrong.png")
no_button = Button(image=no_image, highlightthickness=0, border=0, command=next_card)
no_button.grid(row=1, column=0)


next_card()

window.mainloop()
