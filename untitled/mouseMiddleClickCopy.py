# -*- coding: utf-8 -*-
import pyautogui as pag
from pynput.mouse import Listener, Button

def on_click(x, y, button, pressed):
    # 监听鼠标点击
    # print('{0} at {1}'.format('Pressed' if pressed else 'Released', (x, y)))
    print(button)
    if not pressed and button == Button.middle:
        pag.hotkey('ctrl', 'c')


with Listener(on_click=on_click) as listener:
    listener.join()