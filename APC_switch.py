from tkinter import *

window = Tk()
window.title("Welcome to APC Switch")
window.geometry('350x170')

lbl = Label(window, text="Hello")
lbl.pack(side="top", fill='both', expand=False, padx=4, pady=4)

btn = Button(window, text="Immediate - ON", bg="orange", fg="green", height=2, width=5)
btn.pack(side="top", fill='both', expand=False, padx=4, pady=4)

btn2 = Button(window, text="Immediate - OFF", bg="orange", fg="red", height=2, width=5)
btn2.pack(side="top", fill='both', expand=False, padx=4, pady=4)

btn3 = Button(window, text="Reset", bg="orange", fg="blue", height=2, width=5)
btn3.pack(side="top", fill='both', expand=False, padx=4, pady=4)

window.mainloop()