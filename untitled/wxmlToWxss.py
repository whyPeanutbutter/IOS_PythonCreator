import tkinter as tk  # 使用Tkinter前需要先导入
import re

def autoCR():
    nameEntry.insert('end', "")
    tempstr = window.clipboard_get()
    # print(repr(window.clipboard_get()))
    nameEntry.delete('1.0', 'end')
    errorStr(r'[0-9]+px', tempstr, 'px单位错误:\n')
    errorStr(r'console(.*)\n', tempstr, '包含输出错误:\n')
    errorStr(r'}+px', tempstr, '可能的px单位错误:\n')
    errorStr(r'[a-z]+-[A-Z][a-z]+', tempstr, '命名错误:\n')
    errorStr(r'. ?[a-z]+[A-Z]+[a-z]+ ?{', tempstr, '命名错误:\n')
    errorStr(r'[a-z]+[A-Z][a-z]+.png', tempstr, '命名错误:\n')
    errorStr(r'[a-z]+_[A-Z]?[a-z]+ {', tempstr, '可能的命名错误:\n')
    errorStr(r'Number.MAX_VALUE', tempstr, '可能的参数错误:\n')
    errorStr(r'opacity', tempstr, '可能的UI错误:\n')


def errorStr(patternStr, orginStr, errMessage):
    pattern = re.compile(patternStr)
    results = pattern.findall(orginStr)
    if len(results) > 0:
        nameEntry.insert('end', errMessage)
        for item in results:
            nameEntry.insert('end', item)
            nameEntry.insert('end', '\n')



def replacepx():
    nameEntry.insert('end', "")
    tempstr = nameEntry.get('1.0', 'end')
    if len(tempstr) == 0 or tempstr == '\n':
        tempstr = window.clipboard_get()
    tempstr = tempstr.replace('rpx','px').replace('px','rpx')
    nameEntry.insert('end', "")
    window.clipboard_clear()
    window.clipboard_append(tempstr)



def lower_str():
    nameEntry.insert('end', "")
    tempstr = nameEntry.get('1.0', 'end')
    if len(tempstr) == 0 or tempstr == '\n':
        tempstr = window.clipboard_get()
    arr = tempstr.split("\n")
    outStr = ""
    # 重新排列前面带有Block的控件的位置
    blockIdx = 0
    for astr in arr:
        blockIdx = blockIdx + 1
        blockObj = re.search(r'( *?)<block', astr, re.M | re.I)
        if blockObj:
            needEnd = False
            for inBlockInx in range(blockIdx, len(arr)):
                if not needEnd:
                    blockEndObj = re.search(r'</block', arr[inBlockInx], re.M | re.I)
                    if blockEndObj:
                        needEnd = True
                    else:
                        arr[inBlockInx] = arr[inBlockInx][4:len(arr[inBlockInx])]

    j = 0
    tmpLenArr = [9999] * len(arr)
    tmpStrArr = [''] * len(arr)
    for astr in arr:
        nameEntry.insert('end', "")
        j = j + 1
        needJump = False
        searchObj = re.search(r' class ?= ?"(.*?)" ?', astr, re.M | re.I)
        if searchObj:
            tmpStrArr[j - 1] = searchObj.group(1)
        else:
            needJump = True

        if not needJump:
            searchObj2 = re.search(r'( *?)<', astr)
            if searchObj2:
                tmpLenArr[j - 1] = len(searchObj2.group(1))
                tmpStr = '.' + tmpStrArr[j - 1]
                needBreak = False
                lastLength = 999
                for index in range(j):
                    whiteLen = tmpLenArr[j - 1 - index]

                    if not needBreak:
                        if len(searchObj2.group(1)) > whiteLen and whiteLen < lastLength:
                            tmpStr = '.' + tmpStrArr[j - 1 - index] + ' ' + tmpStr
                    if whiteLen == 0:
                        needBreak = True
                    if whiteLen < lastLength:
                        lastLength = whiteLen
                outStr = outStr + tmpStr + ' {\n\n}\n\n'
            else:
                outStr = outStr + '.' + searchObj.group(1) + ' {\n\n}\n\n'
        if j == len(arr):
            nameEntry.insert('end', "")
            window.clipboard_clear()
            window.clipboard_append(outStr)
            return


window = tk.Tk()
window.title('WHY wxss Creator')
window.geometry('700x700')  # 这里的乘是小x
nameEntry = tk.Text(window)
nameEntry.place(x=0, y=0, width=700, height=400)
nameEntry.pack()

b1 = tk.Button(window, text="提取wxml class", command=lower_str)
b1.place(x=300, y=400, width=250, height=100)

b2 = tk.Button(window, text="替换px为rpx", command=replacepx)
b2.place(x=50, y=400, width=250, height=100)

b3 = tk.Button(window, text="autoCR", command=autoCR)
b3.place(x=50, y=500, width=250, height=100)

window.mainloop()
