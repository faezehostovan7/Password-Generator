from tkinter import *
import string
import random
import pyperclip

def callback():

    small_alphabets = string.ascii_lowercase
    #abcdefghijklmnopqrstuvwxyz
    
    capital_alphabets = string.ascii_uppercase
    #ABCDEFGHIJKLMNOPQRSTUVWXYZ
    
    numbers = string.digits
    #0123456789
    
    special_charecters = string.punctuation
    #!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~
    
    all = small_alphabets + capital_alphabets + numbers + special_charecters
    
    password_length = int(spinlength.get())

    if choice.get() == 1:
        passwordField.insert(0, random.sample(small_alphabets, password_length))
    if choice.get() == 2:
        passwordField.insert(0, random.sample(small_alphabets+capital_alphabets, password_length))
    if choice.get() == 3:
        passwordField.insert(0, random.sample(all, password_length))
    #password = random.sample(all, password_length)
    #passwordFile.insert(0, password)

def copy():
    random_password = passwordField.get()
    pyperclip.copy(random_password)


Win = Tk()
Win.title("Password Generator")
Win.geometry("370x330")
Win.resizable(0, 0)

label_title = Label(Win, text = "Choose the Strength of your password", fg = 'white', bg = 'purple', font = ('Helvtica', 14))
label_title.pack(pady = 15)

choice = IntVar()
rb1 = Radiobutton(Win, text = "Poor Password", variable = choice, value = 1)
rb1.pack(pady = 5)
rb2 = Radiobutton(Win, text = "Average Password", variable = choice, value = 2)
rb2.pack(pady = 5)
rb3 = Radiobutton(Win, text = "Strong Password", variable = choice, value = 3)
rb3.pack(pady = 5)

label_password = Label(Win, text = "Choose the strength of your password")
label_password.pack()

spinlength = Spinbox(Win, from_=8, to_=30, width = 15)
spinlength.pack()


button_submit = Button(Win, text = "Generate Password", command = callback)
button_submit.pack(pady = 15)

passwordField = Entry(Win, width = 25, font = ('Helvtica', 14))
passwordField.pack()

copyButton = Button(Win, text = 'Copy', font = ('Helvtica', 14), command = copy)
copyButton.pack(pady = 5)


Win.mainloop()
