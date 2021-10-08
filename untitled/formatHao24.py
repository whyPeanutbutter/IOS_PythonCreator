# -*- coding: utf-8 -*-
import tkinter as tk  # 使用Tkinter前需要先导入


#检验首字母中文字符或数字
def is_first_chinese_or_number(strs):
    if '\u4e00' <= strs[0:1] <= '\u9fa5' or '0' <= strs[0:1] <= '9':
        return True
    return False


def lower_str():
    nameEntry.insert('end', "")
    tempstr = nameEntry.get('1.0', 'end')
    if len(tempstr) == 0 or tempstr == '\n':
        tempstr = window.clipboard_get()
    tempstr = tempstr.replace('\t\n', '\n').replace('\t', ' ')
    arr = tempstr.split("\n")
    outStr = ""
    notInferString = "以下是程序无法推断的属性或是不需要的注释:"
    j = 0
    for astr in arr:
        nameEntry.insert('end', "")
        j = j + 1
        arrTemp = astr.split(" ")
        arrTemp = list(filter(lambda a: a != '可选', arrTemp))
        arrTemp = list(filter(lambda a: a != '必选', arrTemp))
        arrTemp = list(filter(lambda a: a != '', arrTemp))
        needJump = False
        if len(arrTemp) == 0 or arrTemp[0] == '参数':
            needJump = True
        if not needJump:
            strTemp = arrTemp[0][0:1].lower() + arrTemp[0][1:]
            for i in range(len(arrTemp)):
                arrTemp[i] = arrTemp[i].lower()
            if len(arrTemp) > 1:
                if "string" in arrTemp:
                    outStr = outStr + '\n' + "@property (nonatomic, strong) NSString *" + strTemp + ';'
                elif ("int" in arrTemp) or ("long" in arrTemp) or ("datetime" in arrTemp) or ("number" in arrTemp) or (
                        "integer" in arrTemp) or ("date" in arrTemp):
                    outStr = outStr + '\n' + "@property (nonatomic, strong) NSString *" + strTemp + ';'
                elif ("bool" in arrTemp) or ("boolean" in arrTemp):
                    outStr = outStr + '\n' + "@property (nonatomic, assign) BOOL " + strTemp + ';'
                elif ("double" in arrTemp) or ("float" in arrTemp):
                    outStr = outStr + '\n' + "@property (nonatomic, strong) NSString *" + strTemp + ';'
                elif arrTemp[1].startswith('List<'):
                    outStr = outStr + '\n' + "@property (nonatomic, strong) NSArray<" + strTemp[4:5].capitalize() + strTemp[5:-1] + ' *' + "> *" + strTemp + ';(这是推测类型)'
                else:
                    outStr = outStr + '\n' + "@property (nonatomic, strong) " + strTemp[0:1].capitalize() + strTemp[1:] + ' *' + strTemp + ';(这是推测类型)'
            else:
                print(outStr)
                print(arrTemp)
                if len(outStr) == 0:
                    outStr = "@interface " + strTemp[0:1].capitalize() + strTemp[1:] + ' : ELBaseResponse (这是推测类型)'
                else:
                    outStr = outStr + "\n@end\n" + '\n\n' + "@interface " + strTemp[0:1].capitalize() + strTemp[1:] + ' : NSObject (这是推测类型)'
        if needJump == False and len(arrTemp) > 2 and is_first_chinese_or_number(arrTemp[2]):
            outStr = outStr + '//' + arrTemp[2]
        if j == len(arr):
            if notInferString != "以下是程序无法推断的属性或是不需要的注释:":
                outStr = outStr + "\n" + notInferString
            nameEntry.insert('end', "")
            nameEntry.delete('1.0', 'end')
            nameEntry.insert('end', outStr)
            window.clipboard_clear()
            window.clipboard_append(outStr)
            return


window = tk.Tk()
window.title('WHY String Creator')
window.geometry('700x700')  # 这里的乘是小x
nameEntry = tk.Text(window)
nameEntry.place(x=0, y=0, width=700, height=400)
nameEntry.pack()

b1 = tk.Button(window, text="将文档转换为属性", command=lower_str)
b1.place(x=250, y=400, width=250, height=100)

window.mainloop()
