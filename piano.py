from tkinter import *
import time
import pygame
import datetime

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

root.mainloop()