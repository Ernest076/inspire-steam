from tkinter import *

def hello():
    print("Hello from Ernest")


root = Tk()
root.geometry("400x400")

frame_one = Frame(root)
frame_one.pack()

button_one = Button(frame_one,text="Say Hello",command= hello)
button_one.pack()

root.mainloop()
