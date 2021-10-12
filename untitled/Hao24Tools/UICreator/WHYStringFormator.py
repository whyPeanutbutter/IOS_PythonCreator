# -*- coding: utf-8 -*-
# 将输入的字符转换成string 如换行变为 \n,输出为dict的value
import tkinter as tk  # 使用Tkinter前需要先导入


def hit_me():
    tempstr = nameEntry.get('1.0', 'end').replace('  ', '')
    tempstr = tempstr.replace('"', '\'')
    print('"' + repr(tempstr)[1:-3] + '",')
    # x = tempstr.split("_")
    # for astr in x:
    #     outStr = outStr + astr[0:1].capitalize() + astr[1:]
    # print(outStr)
    window.clipboard_clear()
    window.clipboard_append('"' + repr(tempstr)[1:-3] + '",')

window = tk.Tk()
window.title('WHY String Creator')
window.geometry('500x500')  # 这里的乘是小x
nameEntry = tk.Text(window)
nameEntry.place(x=0, y=0, width=500, height=400)

b = tk.Button(window, text="hit me", command=hit_me)
b.place(x=0, y=400, width=500, height=100)
window.mainloop()