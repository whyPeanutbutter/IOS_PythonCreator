#对比查找相同字段
# -*- coding: utf-8 -*-
import tkinter as tk  # 使用Tkinter前需要先导入
import re

def getOutfileArr():
	videohtmlAdressFilefp = open("outfile.txt", "r", encoding="utf-8")
	herfListTemp = []
	while True:
	    rowData = videohtmlAdressFilefp.readline()
	    rowData = rowData.strip('\n')
	    if rowData == "":
	        break
	    else :
	    	herfListTemp.append(rowData)
	videohtmlAdressFilefp.close()
	herfList = list(set(herfListTemp))
	return herfList


def lower_str():
    nameEntry.insert('end', "")
    tempstr = nameEntry.get('1.0', 'end')
    if len(tempstr) == 0 or tempstr == '\n':
        tempstr = window.clipboard_get()
    outfileArr = getOutfileArr()
    errorStr = ""
    currentString = ""
    result = re.findall('forKey:@"(.*?)"',tempstr)
    j = 0
    for astr in result:
    	currentString = currentString + " "+ astr
    	if astr not in outfileArr:
        	errorStr = errorStr + "error：" + astr +"\n"

    nameEntry.insert('end', "")
    nameEntry.delete('1.0', 'end')
    nameEntry.insert('end', currentString + "\n" + errorStr)


def stick():
	nameEntry.insert('end', "")
	nameEntry.delete('1.0', 'end')
	nameEntry.insert('end', window.clipboard_get())
	

window = tk.Tk()
window.title('WHY String Creator')
window.geometry('700x700')  # 这里的乘是小x
nameEntry = tk.Text(window)
nameEntry.place(x=0, y=0, width=700, height=400)
nameEntry.pack()

b1 = tk.Button(window, text="查找相同字段", command=lower_str)
b1.place(x=250, y=400, width=250, height=100)

b1 = tk.Button(window, text="粘贴", command=stick)
b1.place(x=0, y=400, width=250, height=100)

window.mainloop()