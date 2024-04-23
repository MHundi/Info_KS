import tkinter as tk

root = tk.Tk()


cv = tk.Canvas(root, height = 600, width = 400)
cv.pack()

r = cv.create_rectangle(100,100,200,150, fill = "green")
o = cv.create_oval(100,200,500,500, fill="red", width = 3)
root.mainloop()
