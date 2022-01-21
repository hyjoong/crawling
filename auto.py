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

def Radio_state():
    print()

labelTitle = Label(win,text="매크로")
labelTitle.pack()

menu = Menu(win)

menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="새 매크로")
menu_file.add_command(label="매크로 저장")
menu_file.add_command(label="매크로 불러오기")

menu_start = Menu(menu, tearoff=0)
menu_start.add_command(label="실행")
menu_start.add_command(label="중지")

menu_setting = Menu(menu, tearoff=0)
menu_setting.add_command(label="키보드 설정")
menu_setting.add_command(label="마우스 설정")

menu.add_cascade(label="파일", menu=menu_file)
menu.add_cascade(label="시작", menu=menu_start)
menu.add_cascade(label="설정", menu=menu_setting)

win.config(menu=menu)

# 메뉴 프레임
frame_menu = Frame(win,relief="solid", bd=1)
frame_menu.pack(side="right", fill="both")

Button(frame_menu, text="키보드").pack()
Button(frame_menu, text="마우스").pack()
Button(frame_menu, text="시간").pack()
Button(frame_menu, text="지우기").pack()




# 반복 체크박스 (ture인 상태에서 시작을 누르면 listbox에 있는 동작들이 반복된다)
chkvar = BooleanVar()
checkBox = Checkbutton(win, text="반복", variable=chkvar)
checkBox.pack();

# 라디오 버튼
burger_var = IntVar() # 추가(0) or 삽입(1)
btn_burger1 = Radiobutton(win, text="추가", value=0, variable=burger_var)
btn_burger2 = Radiobutton(win, text="삽입", value=1, variable=burger_var)

btn_burger1.pack()
btn_burger2.pack()


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


