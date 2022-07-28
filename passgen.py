from logging import root
from tkinter import Button, Entry, Frame, Label, LabelFrame, Tk, font
import string
from secrets import choice
from tkinter.constants import END
from tkinter import *
import tkinter as tk

from matplotlib.pyplot import text

UPPERCASE = list(string.ascii_uppercase)
LOWERCASE = list(string.ascii_lowercase)
NUMBER = list(string.digits)
SYMBOLS = ['@', '#', '$', '%', '&', '_', '<', '>', '!', '^', '~', '`']

class PasswordGenerator:
    def __init__(self):

        self.window = Tk()
        self.window.title("PassGen")
        self.window.geometry("450x300")
        self.window.resizable(False,False)
        p1 = PhotoImage(file="/home/sh1vv/Documents/c0d3/Passgen/padlock.png")
        self.window.iconphoto(False, p1)


        # Label Frame
        self.label_frame = LabelFrame(
            self.window, text="< The length of password >", font=("terminal", 12, "normal"))
        self.label_frame.pack(pady=20)
    
    
        # Entry box for number of characters
        self.length_entry_box = Entry(self.label_frame, width=20)
        self.length_entry_box.pack(padx=20, pady=20)
        
        # Declaring feedback if no length is found
        self.feedback = Label(self.window)
        # Entry box for password
        self.password_entry_box = Entry(
            self.window, text="", width=50)
        self.password_entry_box.pack(pady=20)
        
        # Frame for buttons
        self.button_frame = Frame(self.window)
        self.button_frame.pack(pady=20)
        
        # Generate Password Button
        generate_btn = Button(
            self.button_frame, text="Generate", font="terminal", command=self.generate_random_password)
        generate_btn.grid(row=0, column=0, padx=10)
        
        # Copy Password Button
        copy_btn = Button(self.button_frame,
                          text="Copy", font="terminal", command=self.copy_password)
        copy_btn.grid(row=0, column=1, padx=10)
    def generate_random_password(self):
        self.password_entry_box.delete(0, END)
        try:
            password_length = int(self.length_entry_box.get())
            self.feedback.destroy()  # Destroy feedback if length is there
            data = UPPERCASE+LOWERCASE+NUMBER + SYMBOLS
            password = ''.join(choice(data) for _ in range(password_length))
            self.password_entry_box.insert(0, password)
        except ValueError:
            self.feedback = Label(self.window, font=("terminal",9), fg="red",
                                  text="Please enter length of password")
            self.feedback.place(x=113, y=100)

    def copy_password(self):
        self.window.clipboard_clear()
        self.window.clipboard_append(self.password_entry_box.get())

    

if __name__ == '__main__':
    PasswordGenerator().window.mainloop()