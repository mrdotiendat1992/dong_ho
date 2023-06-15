from tkinter import Tk, Frame, Button, Label
from time import sleep
import datetime

class Clock:
    def __init__(self):
        self.app = Tk()
        self.frame = Frame(self.app)
        self.frame.pack()
        self.label = Label(self.frame, 
                           text="", 
                           borderwidth=1, 
                           background="red", 
                           foreground="white",
                           font=('Helvet',50,'bold'))       
        self.label.pack()
        self.set_time()

    def run(self):
        self.app.mainloop()

    def set_time(self):
        self.label.config(text=datetime.datetime.now().strftime("%H:%M:%S"))
        self.label.after(1000,self.set_time)
        

if __name__ == "__main__":
    clock = Clock()
    clock.run()