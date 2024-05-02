from tkinter import *

canvas_width = 500
canvas_height = 150

def paint( event ):
   colo= "#000000"
   x1, y1 = ( event.x - 1 ), ( event.y - 1 )
   x2, y2 = ( event.x + 1 ), ( event.y + 1 )
   w.create_oval( x1, y1, x2, y2, fill = colo )

root = Tk()
root.title( "Painting using Ovals" )
w = Canvas(root, 
           width=canvas_width, 
           height=canvas_height)
w.pack(expand = YES, fill = BOTH)
w.bind("<B1-Motion>", paint )

message = Label( root, text = "Press and Drag the mouse to draw" )
message.pack( side = BOTTOM )
    
mainloop()