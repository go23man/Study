from tkinter import*
from datetime import datetime

win = Tk()                              # 창 생성

win.geometry('600x100')                # 창의 크기 설정
win.title('What\'s the time?')        # 창의 제목 설정
win.option_add('*Font', '궁서 25')     # 폰트 설정

def what_time():
    dnow = datetime.now()
    btn.config(text = dnow)

btn = Button(win)                       # 버튼 생성
btn.config(text = '현재 시각')          # 버튼 텍스트 설정
btn.config(width = 30)
btn.config(command = what_time)

btn.pack()                              # 버튼 배치

win.mainloop()                          # 창 실행