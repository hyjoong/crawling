from tkinter import *
import pyautogui

# settings
from function import get_mouse_position

win = Tk()
win.geometry("600x600")
win.title("Macro")
win.option_add("*Font","맑은고딕 25")



# variable & function
def createTimeWindow():
    global new
    new = Toplevel()

    def time_value():
        temp = ent2.get()
        listbox.insert(END,temp)

    lb = Label(new, text="시간(초)를 입력하세요")
    lb2 = Label(new, text="범위: 0.01 ~ 100초" )
    ent2 = Entry(new,width=10)
    success_btn = Button(new, text="완료", width=5)
    success_btn.config(command=time_value)
    lb.pack()
    lb2.pack()
    ent2.pack()
    success_btn.pack()

def createKeyWindow():
    global new
    new = Toplevel()

    def key_value():
        temp = ent2.get()
        listbox.insert(END,temp)

    lb = Label(new, text="추가할 키를 입력하세요")
    ent2 = Entry(new,width=7)
    lb.pack()
    success_btn = Button(new, text="완료", width=5)
    success_btn.config(command=key_value)
    ent2.pack()
    success_btn.pack()

def createMouseWindow():
    global new
    new = Toplevel()
    position = get_mouse_position();
    lb = Label(new, text=position)
    lb.pack()

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


keyboard_frame_btn = Button(frame_menu, text="키보드")
keyboard_frame_btn.config(command = createKeyWindow)
keyboard_frame_btn.pack()
mouse_frame_btn = Button(frame_menu, text="마우스")
mouse_frame_btn.config(command = createMouseWindow)
mouse_frame_btn.pack()
time_frame_btn = Button(frame_menu, text="시간")
time_frame_btn.config(command = createTimeWindow)
time_frame_btn.pack()
Button(frame_menu, text="지우기",command=delete_list).pack()


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

def delete_list():
    select = listbox.curselection()
    print(select)

win.mainloop()


