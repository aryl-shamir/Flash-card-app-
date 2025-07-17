import pandas as pd 
from tkinter import *
import random 
from PIL import Image, ImageTk
import time 

#--- constance --- 
BACKGROUND_COLOR = "#00BFC6"
FRENCH_FONT = ("Ariel", 40, "italic")
ENGLISH_FONT = ("Ariel", 40, "bold")
SCORE_FONT = ("Ariel", 25, "bold")

# -- importing the data----

try:
    to_learn_data = pd.read_csv("./data/words_to_learn.csv")
except (FileNotFoundError, pd.errors.EmptyDataError):
    original_data = pd.read_csv("./data/french_words.csv")
    word_list = original_data.to_dict(orient="records")   
else:
    word_list = to_learn_data.to_dict(orient="records")

#----- Importing the score data------
try:
    with open("./data/score_data.txt", "r") as score_data:
        score = int(score_data.read())
except FileNotFoundError:
    score = 0

#----- function ------
def next_card():
    
    global word, flip_timer
    
    # Once the user has marked all words as known, the card will become static.
    # Indicating that there are no more words to learn. 
    
    if not word_list:
        canvas.itemconfig(card_word, text="You're done!", fill="black")
        canvas.itemconfig(card_title, text="Tu as terminé", fill="black")
        canvas.itemconfig(score_title, text=f"Final_Score:{score}", fill="black")
        canvas.itemconfig(canvas_image, image=card_front_photo)
        return
    
    window.after_cancel(flip_timer)
    word = random.choice(word_list )
    french = word['French']
    
    # if the user knows a word, it should be remove from the word_list
    canvas.itemconfig(card_word, text=french, fill="black")
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(score_title, text=f"Score:{score}", fill="green")
    canvas.itemconfig(canvas_image, image=card_front_photo)
    
    
    flip_timer = window.after(3000, flip_card)
    
def is_known():
    
    try:
        word_list.remove(word)
    except ValueError:
        pass  # already removed
    
    new_data = pd.DataFrame(word_list)
    new_data.to_csv("./data/words_to_learn.csv", index=False)
    
    increase_score()
    next_card()
    
def increase_score():
    global score
    score += 1 
    with open("./data/score_data.txt", "w") as score_file:
        score_file.write(str(score))
    
    
def flip_card():
    
    English_card = word['English']
    
    canvas.itemconfig(card_word, text=English_card, fill="white")
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(canvas_image, image=card_back_photo)

#------ UI---------
window = Tk()
window.title("Flash card app")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, flip_card)

#flash card image 
card_front_image = Image.open("./assets/card_front.png")
card_front_photo = ImageTk.PhotoImage(card_front_image)

card_back_image = Image.open("./assets/card_back.png")
card_back_photo = ImageTk.PhotoImage(card_back_image)

#---creating canvas ----
canvas = Canvas(window, width=800, height=526)
canvas.grid(column=0, row=0, columnspan=2)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_image = canvas.create_image( 0, 0,anchor = "nw", image=card_front_photo)

#creat text 
card_title = canvas.create_text(350, 90, text="Title", font=FRENCH_FONT, fill="black")
card_word = canvas.create_text(350, 180, text="Translate", font=ENGLISH_FONT, fill="black")
score_title = canvas.create_text(350, 300, text="", font=SCORE_FONT, fill="green")

# --- button widget image ---

right_image = PhotoImage(file="./assets/right.png")
known_button = Button(window, image=right_image, highlightthickness=0, command=is_known)
known_button.grid(column=1, row=1)

#----- creating the false widgets
wrong_image = PhotoImage(file="./assets/wrong.png")
unknown_button = Button(window, image=wrong_image, highlightthickness=0, command=next_card)
unknown_button.grid(column=0, row=1)

next_card()

window.mainloop()
