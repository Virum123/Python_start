

# 기본 제공 GUI 라이브러리 ==> tkinter
import tkinter as tk

def IncreseFuc():
    numcnt.set( numcnt.get() + 1)
    print("증가")

def DecreseFuc():
    numcnt.set( numcnt.get() - 1)
    print("감소")

mywind = tk.Tk() # main 윈도우 객체 생성
mywind.title("계산기")
mywind.geometry("600x600+500+200") # 윈도우 사이즈 조절 및 출력 위치 조절


numcnt = tk.IntVar() # 제어변수 : 내부 프로그램 메모리 값과 GUI 표시 데이터의 연동 변수
numcnt.set(0)

lb1 = tk.Label(text="numbering", textvariable=numcnt)
lb1.pack()

# 버튼 자식 윈도우 생성
b1 = tk.Button(text="Increse" , padx=50, pady=50, font=20, background="#888888",
               command=IncreseFuc, repeatdelay=1, repeatinterval=5) # 버튼의 크기
# 자식윈도우를 부모 윈도우에 배치 ( gird, pack, place )
b1.pack(padx=10, pady=10) # 버튼의 위치

b1 = tk.Button(text="Increse" , padx=50, pady=50, font=20, background="#DD9908",
               command=DecreseFuc, repeatdelay=1, repeatinterval=5) # 버튼의 크기
# 자식윈도우를 부모 윈도우에 배치 ( gird, pack, place )
b1.pack(padx=10, pady=10) # 버튼의 위치

mywind.mainloop() # 윈도우 객체를 화면에 계속 갱신해서 출력
