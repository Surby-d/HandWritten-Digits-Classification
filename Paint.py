from tkinter import *
import tkcap
import random

class Draw:
    def __init__(self):
        self.current_x, self.current_y = 0, 0
        self.color = 'white'


    def locate_xy(self, event):
        self.current_x, self.current_y = event.x, event.y

    def addLine(self, event):
        self.canvas.create_line((self.current_x, self.current_y, event.x, event.y),fill = self.color, width=10)
        self.current_x, self.current_y = event.x, event.y

    def screenShot(self):
        name = random.randint(1111, 77777)
        cap = tkcap.CAP(self.window)
        self.filename = "C:\\Users\\SURYA S\\OneDrive\\Pictures\\"+str(name)+".jpg"
        cap.capture(self.filename)
        self.window.destroy()
        
    
        
    def setting(self):
        self.window = Tk()
        self.window.title('Paint')
        self.window.minsize(300, 300)
        self.window.maxsize(300, 300)
        self.window.rowconfigure(0, weight=1)
        self.window.columnconfigure(0, weight=1)
        self.canvas= Canvas(self.window,background='black') 
        self.canvas.grid()
        self.canvas.bind('<Button-1>', self.locate_xy)
        self.canvas.bind('<B1-Motion>', self.addLine)
            
        button1 = Button(self.window, text='Shot', background="#aa7bb1", foreground="white", command=self.screenShot)
        button1.grid(row=0, column=1)
        
        self.window.mainloop()
        return self.filename

