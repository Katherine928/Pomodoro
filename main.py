from tkinter import *
import math
import winsound
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
timer = 0
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    timer_label.config(text = "Timer")
    canvas.itemconfig(timer_text, text = "00:00")
    check_label.config(text = "")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text = "Break", fg = RED)
        winsound.Beep(1000, 500)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Break", fg=PINK)
        winsound.Beep(1000, 500)
    else:
        count_down(work_sec)
        timer_label.config(text="Work", fg=GREEN)
        winsound.Beep(1000, 500)




# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global timer
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text = f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            mark += "✓"
        check_label.config(text = mark)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx = 100, pady = 50, bg = YELLOW)



canvas = Canvas(width = 200, height = 224, bg = YELLOW, highlightthickness = 0)
tomato_img = PhotoImage(file = "tomato.png")
canvas.create_image(100, 112, image = tomato_img)
timer_text = canvas.create_text(100, 130, text = "00:00", fill = "white", font = (FONT_NAME, 35, "bold"))
canvas.grid(column = 1, row = 1)



timer_label = Label(text = "Timer", bg = YELLOW, fg = GREEN, font = (FONT_NAME, 40, "bold"))
timer_label.grid(column = 1, row = 0)

start_button = Button(text = "Start", highlightthickness = 0,command = start_timer)
start_button.grid(column = 0, row = 2)

reset_button = Button(text = "Reset", highlightthickness = 0, command = reset_timer)
reset_button.grid(column = 2, row = 2)

check_label = Label(bg = YELLOW, fg = GREEN)
check_label.grid(column = 1, row = 3)

window.mainloop()