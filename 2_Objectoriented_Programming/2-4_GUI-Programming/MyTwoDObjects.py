from dataclasses import dataclass
@dataclass

class MyTwoDObjects:
    cv: tk.Canvas
    x : float = 0
    y:  float = 0
    index : int = field(dafault = 0, init = False)  # Dieses Attribut hat Stdndartwert 0 
                                                    # wird vom Konstruktor aber nicht gesetzt.
    
    def move(self, xchange: float = 0, ychange: float = 0):
        self.x += xchange
        self.y += ychange
        if self.cv and self.index:
            self.cv.move(self.index, xchange, ychange)