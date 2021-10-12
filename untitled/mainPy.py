# -*- coding: utf-8 -*-
import tkinter as tk  # 使用Tkinter前需要先导入
import json
import os


def print_selection():
    global varDict
    global tempDict
    global nameEntry
    global needAppendString
    global currentDisplayStr

    textView.delete('1.0', 'end')
    textView.insert('end', tempDict["init"])
    textView.insert('end', '\n')
    for key1, values1 in varDict.items():
        if varDict[key1].get() == 1:
            textView.insert('end', tempDict[key1])
            textView.insert('end', '\n')
    currentDisplayStr = str(textView.get('1.0', 'end')).replace('WHYName', nameEntry.get())
    textView.delete('1.0', 'end')
    textView.insert('end', currentDisplayStr)
    window.clipboard_clear()
    window.clipboard_append(needAppendString + currentDisplayStr)


def stop_append_string():
    global needAppendString
    global isAppendString
    needAppendString = ""
    isAppendString = False
    button.configure(text="点击合并代码")
    window.clipboard_clear()
    window.clipboard_append(needAppendString + currentDisplayStr)


def append_string():
    global needAppendString
    global isAppendString
    if isAppendString:
        stop_append_string()
    else:
        isAppendString = True
        button.configure(text="点击清除合并代码")


def creatSelection():
    global tempDict
    global varDict
    global nameEntry
    global needAppendString

    needAppendString = currentDisplayStr + needAppendString
    myFile = pathDict[varUIName.get()]
    for widget in frame.winfo_children():
        widget.destroy()
    file = open(myFile, 'r')
    tempDict = json.loads(file.read())
    file.close()
    varDict = dict()
    namelabel = tk.Label(frame, text='name', font=('Arial', 14))
    namelabel.place(x=0, y=0, width=50, height=40)
    nameEntry = tk.Entry(frame, show=None, font=('Arial', 14))
    nameEntry.place(x=50, y=0, width=200, height=40)
    i = 0
    for key, values in tempDict.items():
        i = i + 1
        if key == 'init':
            i = i - 1
            continue
        var1 = tk.IntVar()
        c1 = tk.Checkbutton(frame, text=key, variable=var1, onvalue=1, offvalue=0, command=print_selection)
        c1.place(x=0, y=i * 20 + 25)
        varDict[key] = var1


varDict = dict()
tempDict = dict()
needAppendString = ""
isAppendString = False
currentDisplayStr = ""

os.system("python filePathCreator.py")
os.system("python UIbuttonDataCreator.py")
os.system("python UILabelCreator.py")
os.system("python UITableViewDataCreator.py")
os.system("python UITableViewCellDataCreator.py")
os.system("python UIImageViewDataCreator.py")
os.system("python NSMutableAttributedStringDataCreator.py")
os.system("python UITextViewDataCreator.py")
os.system("python UICollectionViewDataCreator.py")
os.system("python UIScrollViewDataCreator.py")
os.system("python WHYMasConstraintsCreator.py")
os.system("python FMDBCreator.py")
os.system("python ServerApiCreator.py")
os.system("python UIViewCreator.py")

window = tk.Tk()
window.title('WHY IOS Creator')
# 设定窗口的大小(长 * 宽)
window.geometry('500x500')  # 这里的乘是小x
textView = tk.Text(window)
textView.place(x=0, y=0, height=70)

pathfile = open("UIFilePath.txt", 'r')
pathDict = json.loads(pathfile.read())
varUIName = tk.StringVar()
pathDicti = 0
for key, values in pathDict.items():
    r1 = tk.Radiobutton(window, text=key, variable=varUIName, value=key, command=creatSelection)
    r1.place(x=20, y=90 + pathDicti * 30)
    pathDicti = pathDicti + 1

frame = tk.Frame(window)
frame.place(x=150, y=90, width=300, height=800)
nameEntry = tk.Entry()

button = tk.Button(window, text="点击补充代码", command=append_string)
button.place(x=350, y=400, width=150, height=100)

window.mainloop()