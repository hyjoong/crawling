from tkinter import *
import pyautogui

# settings
win = Tk()
win.geometry("600x300")
win.title("Macro")
win.option_add("*Font","맑은고딕 25")


# variable & function
autoList=[]

def createNewWindow():
    global new
    new = Toplevel()

def find_location():
    place = pyautogui.position()
    print(place)

def type_input():
    inputs = ent.get()
    print(inputs)
    

labelTitle = Label(win,text="매크로")
labelTitle.pack()

ent = Entry(win)
ent.pack()

btn = Button(win, text="좌표 버튼")
btn.config(command = find_location)
btn.pack()


btn2 = Button(win, text="추가")
btn2.config(command = type_input)
btn2.pack()


  # win.Tk()를 사용해서 새로운 Tkinter 창 생성

btn3 = Button(win, text="새로운 창")
btn3.config(command = createNewWindow)
btn3.pack()

win.mainloop()


