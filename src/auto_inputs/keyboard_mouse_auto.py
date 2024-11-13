import pyautogui
import os


def start():
    current_directory = os.getcwd()
    print(current_directory)

    x,y = pyautogui.size()
    print(x, y)
    img_loc = pyautogui.locateOnScreen('src/auto_inputs/edge_icon.png', confidence=0.9)
    pyautogui.PAUSE = 2.5

    pyautogui.moveTo(img_loc[0], img_loc[1], 1)
    # pyautogui.click(x * 0.6, y * 0.97)
    # pyautogui.click(820, 400)
    # pyautogui.typewrite("Dog")
    # pyautogui.typewrite(["enter"])