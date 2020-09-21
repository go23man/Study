from tkinter import *
import cv2
from PIL import Image, ImageTk

root = Tk()
root.title('Ship Tracker')
root.geometry("1200x768")
root.bind('<Escape>', lambda e: root.quit())

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 200)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 150)

my_canvas = Canvas(root, width=800, height=600, bg="white")
my_canvas.pack(side = LEFT)         # 캔버스 배치
lmain = Label(root, bg="grey")
lmain.pack(side = TOP, anchor = NE)

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

def show_frame():
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    lmain.after(10, show_frame)

show_frame()
root.mainloop()