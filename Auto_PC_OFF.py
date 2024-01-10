from tkinter import *
from tkinter import ttk
import os
import time
import threading

def Clock_PC_OFF():
    entry1 = int(godzina.get())
    entry2 = int(minuta.get())
    entry3 = int(sekunda.get())
    target_time = entry1 * 3600 + entry2 * 60 + entry3
    Label(window, text=f"Komputer się wyłączy o {entry1}:{entry2}:{entry3}").place(relx=0.5,rely=1,anchor="s")

    def check_shutdown():
        current_time = time.localtime()
        current_seconds = current_time.tm_hour * 3600 + current_time.tm_min * 60 + current_time.tm_sec
        if current_seconds >= target_time:
            os.system("shutdown /s /t 0")
        else:
            window.after(1000, check_shutdown)

    window.after(1000, check_shutdown)
def Timer_PC_OFF():
    global timer1
    global timer2
    godzina = int(timer1.get())
    minuta = int(timer2.get())
    try:
        if not godzina:
            raise ValueError
    except ValueError:
        godzina == 0
    off = (godzina * 3600) + (minuta * 60)
    os.system(f"shutdown /s /t {off}")

window = Tk()
window.title("Auto PC Off")
window.geometry("250x200")
notebook = ttk.Notebook(window)
tab1 = Frame(notebook)
tab2 = Frame(notebook)
notebook.add(tab1, text="Clock")
notebook.add(tab2, text="Timer")
notebook.pack(expand=True,fill="both")

Label(tab1, text="Hour:").place(relx=0, rely=0, anchor="nw")
Label(tab1, text="Minute:").place(relx=0.5, rely=0, anchor="n")
Label(tab1, text="Second:").place(relx=1, rely=0, anchor="ne")


godzina = Entry(tab1, width="5", justify="center")
godzina.place(relx=0.01, rely=0.1, anchor="nw")

minuta = Entry(tab1, width="5", justify="center")
minuta.place(relx=0.49, rely=0.1, anchor="n")

sekunda = Entry(tab1, width="5", justify="center")
sekunda.place(relx=0.97, rely=0.1, anchor="ne")

Button(tab1, text="OK", command=Clock_PC_OFF).place(rely=0.25, relx=0.45)
Label(tab2, text="Hour:").place(relx=0.3, rely=0)
Label(tab2, text="Minute:").place(relx=0.6,rely=0)

timer1 = Entry(tab2, width=5, justify="center")
timer1.place(relx= 0.3,rely=0.1)

timer2 = Entry(tab2, width=5, justify="center")
timer2.place(relx=0.63,rely=0.1)

Button(tab2,text="OK",command=Timer_PC_OFF).place(rely=0.25, relx=0.45)

window.mainloop()
