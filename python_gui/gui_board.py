from tkinter import *

root = Tk()
root.title('Ship Tracker')
root.geometry("1024x768")

my_canvas = Canvas(root, width=800, height=600, bg="white")
my_canvas.pack(side = LEFT)         # 캔버스 배치

# Create Line
# my_canvas.create_line(x1, y1, x2, y2, fill="color")

# Draw rows
x1, x2, y1, y2 = 0, 800, 75, 75
for n in range(7):
    my_canvas.create_line(x1, y1, x2, y2, fill = "black")
    y1 += 75
    y2 += 75

# Draw columns
x1, x2, y1, y2 = 100, 100, 0, 600
for n in range(7):
    my_canvas.create_line(x1, y1, x2, y2, fill = "black")
    x1 += 100
    x2 += 100    

root.mainloop()