from dataclasses import dataclass, field
from tkinter import *
@dataclass

class MyTwoDObjects:
    cv: Canvas
    x : float = 0
    y:  float = 0
    index : int = field(default = 0, init = False)  # Dieses Attribut hat Stdndartwert 0 
                                                    # wird vom Konstruktor aber nicht gesetzt.
    
    def move(self, xchange: float = 0, ychange: float = 0):
        self.x += xchange
        self.y += ychange
        if self.cv and self.index:
            self.cv.move(self.index, xchange, ychange)
            
    
@dataclass
class MyCircle(MyTwoDObjects):
    radius : float = 1
    def __post_init__(self):
        self.index = self.cv.create_oval(self.x-self.radius,
                                         self.y-self.radius,
                                         self.x+self.radius,
                                         self.y+self.radius)
        
def setup_canvas(height : int = 600, width : int = 600):
    root = Tk()
    cv = Canvas(root, height= height, width = width)
    cv.pack()
    return cv
    

def my_geo() -> int:
    cv = setup_canvas()
    return MyCircle(cv,  200, 300, radius = 50)

my_geo()
mainloop()



