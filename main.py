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
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label_timer.config(text="Timer", fg=GREEN)
    label_check.config(text="")
    global reps
    reps = 0



# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    if reps % 2 == 1:
        count_down(WORK_MIN*60)
        label_timer.config(text="Work", fg=GREEN)
    elif reps > 7:
        count_down(LONG_BREAK_MIN*60)
        label_timer.config(text="Break", fg=RED)
    else:
        count_down(SHORT_BREAK_MIN*60)
        label_timer.config(text="Break", fg=PINK)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    minutes = math.floor(count / 60)
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"
    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        check_marks = ""
        works_sessions = math.floor(reps/2)
        for n in range(works_sessions):
            check_marks += "✔"
            label_check["text"] = check_marks


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

label_check = Label(fg=GREEN, bg=YELLOW, highlightthickness=0, font=(FONT_NAME, 18, "bold"))
label_check.grid(column=1, row=4)

# buttons
start_button = Button(text="Start", width=5, highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", width=5, highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)


window.mainloop()