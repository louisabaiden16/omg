from tkinter import *
from tkinter import.messagebox
import tkinter as tk
from cryptography.fernet import fernet
    

root = Tk()
root.title("Encrypt Decrypt Login")
root.geometry("925x500+300+200")
root.resizable(False, False)
root.configure(bg="#fff")

### This is Login page ####
def signin():
    username = user.get()
    password = code.get()

    if username == "test" and password == "test":
        screen = Toplevel(root)
        screen.title("Message ENcode and Decode")
        screen.geometry("500x300+300+200")
        screen.config(bg="white")
        screen.resizable(False, False)

        Label(screen, text="Encode / Decode", bg="#fff", font=("Calibri (Body)", 20, 'bold')).pack()

        screen.mainloop()
    elif username!= 'test' and password!= 'test':
        messagebox.showerror("Invalid", "Invalid username or password")
    elif password!= 'test':
        messagebox.showerror("Invalid", "Invalid password")
    elif username!= 'test':
        messagebox.showerror("Invalid", "Invalid username")


img = PhotoImage(file="C:\Users\louis\Pictures\gctu logo.png")
Label(root, image=img, bg="white").place(x=50, y=50)


frame = Frame(root, width=350, height=350, bg='white')
frame.place(x=480, y=70)

heading = Label(frame,text="ENCRYPT / DECRYPT \nLOGIN", fg="#57a1f8", bg="white", font=("Times New Romans", 23, 'bold'))
heading.place(x=30, y=1)

# Username entry function
def on_enter(e):