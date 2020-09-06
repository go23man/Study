from tkinter import *
import requests
from bs4 import BeautifulSoup

win = Tk()
win.geometry("300x100")
win.option_add("*Font", "맑은고딕 20")

ent = Entry(win)    # 입력창 생성
ent.pack()          # 입력창 배치

# 웹크롤링 파트
def lotto_p():
    n = ent.get()   # 회차를 입력창에서 받아옴
    url = "https://dhlottery.co.kr/gameResult.do?method=byWin&drwNo={}".format(n)
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")                        # req.text를 html.parser라는 방식으로 틀을 꾸밈
    txt = soup.find("div", attrs = {"class","win_result"}).get_text()    # attrs의 속성을 가지고 있는 div를 탐색한 뒤에 텍스트만 추출
    num_list = txt.split("\n")[7:13]     # 라인피드를 기준으로 텍스트에 대해서 인덱싱
    bonus = txt.split("\n")[-4]

    print("당첨번호")
    print(num_list)
    print("보너스번호")
    print(bonus)

btn = Button(win)
btn.config(text = "로또 당첨 번호 확인")
btn.config(command = lotto_p)
btn.pack()
win.mainloop()