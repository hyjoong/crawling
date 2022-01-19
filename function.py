import pyautogui

# 마우스를 특정위치로 이동시키는 함수
def move_mouse(location):
    # location 을 입력받아 이 위치로 마우스를 이동
    pyautogui.moveTo(location)

# 마우스의  현재 좌표를 구하는 함수 (마우스 현재 커서)
def get_mouse_position():
    return tuple(pyautogui.position())

# 지정된 위치로 마우스 커서를 이동하고 왼쪽 버튼을 클릭하는 함수
def click(location):
    pyautogui.click(location)

# 지정된 위치로 마우스 커서를 이동하고 오른쪽 버튼을 클릭하는 함수
def right_click(location):
    pyautogui.click(location, button='right')

# 더블클릭
def double_click(location):
    pyautogui.click(location, button='left', clicks=2, interval=0.25)

# 키를 한 번 눌렀다가 떼는 함수
def key_press_once(key):
    pyautogui.press(key)