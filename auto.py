from tkinter import *
import pyautogui

# settings

win = Tk()
win.geometry("600x600")
win.title("Macro")
win.option_add("*Font","맑은고딕 25")


# variable & function
def createNewWindow():
    global new
    new = Toplevel()

def find_location():
    place = pyautogui.position()
    print(place)

def type_input():
    inputs = ent.get()
    print(inputs)

def delete_list():
    listbox.delete(listbox.curselection()) # 선택한 항목 삭제



labelTitle = Label(win,text="매크로")
labelTitle.pack()


listbox = Listbox(win, selectmode ="extended",height=0)
listbox.insert(0,"시작")
listbox.insert(END,"동작1")
listbox.insert(END,"동작2")
listbox.pack()

ent = Entry(win)
ent.pack()

def add_list():
    temp = ent.get()
    print(ent.get())
    listbox.insert(END,temp)

deleteBtn = Button(win, text="삭제", command=delete_list)
deleteBtn.pack()


btn = Button(win, text="좌표 버튼")
btn.config(command = find_location)
btn.pack()


btn2 = Button(win, text="추가")
btn2.config(command = add_list)
btn2.pack()


  # win.Tk()를 사용해서 새로운 Tkinter 창 생성

# 클릭 시 키보드 키 입력하는 창 생성
keyboardBtn = Button(win, text="키보드")
keyboardBtn.config(command = createNewWindow)
keyboardBtn.pack()

win.mainloop()


