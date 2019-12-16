from tkinter import *
import time
import pygame
import datetime

def show_time():
    cur = time.strftime("%H:%M:%S")
    txt2["text"] = cur
    root.after(100, show_time)

def value(value):
    str1.set(value)
    file = "Notes\\" + value + ".wav"
    sound = pygame.mixer.Sound(file)
    sound.play()

pygame.init()
root = Tk()
root.title("Piano")
root.geometry("1000x700+10+10")
root.iconbitmap("Photo\\keyboard.ico")

ABC = Frame(root, bg="powder blue", bd=5)
ABC.place(relx=0.05, rely=0.05, relheight=0.9, relwidth=0.9)

ABC1 = Frame(ABC, bg="powder blue", bd=5)
ABC1.place(relx=0.05, rely=0.05, relheight=0.2, relwidth=0.9)

ABC2 = Frame(ABC, bg="powder blue", bd=5)
ABC2.place(relx=0.05, rely=0.25, relheight=0.25, relwidth=0.9)

ABC3 = Frame(ABC, bg="powder blue", bd=5)
ABC3.place(relx=0.05, rely=0.55, relheight=0.4, relwidth=0.9)

str1=StringVar()
str1.set("Notes")
date1=StringVar()
date1.set(time.strftime("%d/%m/%Y"))

# =================================ABC1===============================================
# TEXT for date
txt1 = Label(ABC1, textvariable=date1, font=20, justify=CENTER)
txt1.place(relx=0, rely=0.3, relwidth=0.2, relheight=0.4)

# LABEL
lbl = Label(ABC1, textvariable=str1, font=("arial", 25, "bold"), bg="blue", bd=20, fg="white", justify=CENTER)
lbl.place(relx=0.25, rely=0.2, relwidth=0.5, relheight=0.6)

# TEXT for time
txt2 = Label(ABC1, font=20, justify=CENTER)
txt2.place(relx=0.8, rely=0.3, relwidth=0.2, relheight=0.4)
show_time()


# ==============================ABC2==================================================

btnCs=Button(ABC2, text="C#", bg="black", font=("bold"), fg="white", bd=5, command=lambda: value("C#"))
btnCs.place(relx=0.16, relwidth=0.08, relheight=1)
btnDs=Button(ABC2, text="D#", bg="black", font=("bold"), fg="white", bd=5, command=lambda: value("D#"))
btnDs.place(relx=0.25, relwidth=0.08, relheight=1)

btnFs=Button(ABC2, text="F#", bg="black", font=("bold"), fg="white", bd=5, command=lambda: value("F#"))
btnFs.place(relx=0.36, relwidth=0.08, relheight=1)
btnGs=Button(ABC2, text="G#", bg="black", font=("bold"), fg="white", bd=5, command=lambda: value("G#"))
btnGs.place(relx=0.45, relwidth=0.08, relheight=1)
btnBb=Button(ABC2, text="Bb", bg="black", font=("bold"), fg="white", bd=5, command=lambda: value("Bb"))
btnBb.place(relx=0.54, relwidth=0.08, relheight=1)

btnCs1=Button(ABC2, text="C#1", bg="black", font=("bold"), fg="white", bd=5, command=lambda: value("C#1"))
btnCs1.place(relx=0.65, relwidth=0.08, relheight=1)
btnDs2=Button(ABC2, text="D#1", bg="black", font=("bold"), fg="white", bd=5, command=lambda: value("D#1"))
btnDs2.place(relx=0.74, relwidth=0.08, relheight=1)


# ================================================================================
btnC=Button(ABC3, text="C", width=5, height=15, bg="white", font=("bold"), padx=5, fg="black", bd=1,
            command=lambda: value("C"))
btnC.place(relx=0, relwidth=0.08, relheight=0.9)
btnD=Button(ABC3, text="D", width=5, height=15, bg="white", font=("bold"), padx=5, fg="black", bd=1,
            command=lambda: value("D"))
btnD.place(relx=0.09, relwidth=0.08, relheight=0.9)
btnE=Button(ABC3, text="E", width=5, height=15, bg="white", font=("bold"), padx=5, fg="black", bd=1,
            command=lambda: value("E"))
btnE.place(relx=0.18, relwidth=0.08, relheight=0.9)
btnF=Button(ABC3, text="F", width=5, height=15, bg="white", font=("bold"), padx=5, fg="black", bd=1,
            command=lambda: value("F"))
btnF.place(relx=0.27, relwidth=0.08, relheight=0.9)
btnG=Button(ABC3, text="G", width=5, height=15, bg="white", font=("bold"), padx=5, fg="black", bd=1,
            command=lambda: value("G"))
btnG.place(relx=0.36, relwidth=0.08, relheight=0.9)
btnA=Button(ABC3, text="A", width=5, height=15, bg="white", font=("bold"), padx=5, fg="black", bd=1,
            command=lambda: value("A"))
btnA.place(relx=0.45, relwidth=0.08, relheight=0.9)
btnB=Button(ABC3, text="B", width=5, height=15, bg="white", font=("bold"), padx=5, fg="black", bd=1,
            command=lambda: value("B"))
btnB.place(relx=0.54, relwidth=0.08, relheight=0.9)
btnC1=Button(ABC3, text="C1", width=5, height=15, bg="white", font=("bold"), padx=5, fg="black", bd=1,
             command=lambda: value("C1"))
btnC1.place(relx=0.63, relwidth=0.08, relheight=0.9)
btnD1=Button(ABC3, text="D1", width=5, height=15, bg="white", font=("bold"), padx=5, fg="black", bd=1,
             command=lambda: value("D1"))
btnD1.place(relx=0.72, relwidth=0.08, relheight=0.9)
btnE1=Button(ABC3, text="E1", width=5, height=15, bg="white", font=("bold"), padx=5, fg="black", bd=1,
             command=lambda: value("E1"))
btnE1.place(relx=0.81, relwidth=0.08, relheight=0.9)
btnF1=Button(ABC3, text="F1", width=5, height=15, bg="white", font=("bold"), padx=5, fg="black", bd=1,
             command=lambda: value("F1"))
btnF1.place(relx=0.9, relwidth=0.08, relheight=0.9)
# ================================================================================
# ================================================================================
# ================================================================================

root.mainloop()