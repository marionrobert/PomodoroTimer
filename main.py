from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    count_down(25*60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    minutes = math.floor(count / 60)
    seconds = count % 60
    if seconds == 0:
        seconds = "00"
    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0 :
        window.after(1000, count_down, count-1)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 24, "bold"))
canvas.grid(column=1, row=1)


# labels
label_timer = Label(text="Timer", fg=GREEN, bg=YELLOW, highlightthickness=0, font=(FONT_NAME, 40, "bold"))
label_timer.grid(column=1, row=0)

label_check = Label(text="🗸", fg=GREEN, bg=YELLOW, highlightthickness=0, font=(FONT_NAME, 24, "bold"))
label_check.grid(column=1, row=4)

# buttons
start_button = Button(text="Start", width=5, highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", width=5, highlightthickness=0)
reset_button.grid(column=2, row=2)


window.mainloop()