import tkinter as tk  # 使用Tkinter前需要先导入


# 检验首字母中文字符或数字
def is_first_chinese_or_number(strs):
    # for _char in strs:
    if '\u4e00' <= strs[0:1] <= '\u9fa5' or '0' <= strs[0:1] <= '9':
        return True
    return False


def hit_me():
    tempstr = nameEntry.get('1.0', 'end')
    if len(tempstr) == 0 or tempstr == '\n':
        tempstr = window.clipboard_get()
    tempstr = tempstr.replace('  ', '')
    arr = tempstr.split("\n")
    print(arr)
    outStr = ""
    for astr in arr:
        outStr = outStr + '\n_' + astr + ' = ' + astr + ';'
    # print('"' + repr(tempstr)[1:-3] + '",')
    # x = tempstr.split("_")
    # for astr in x:
    #     outStr = outStr + astr[0:1].capitalize() + astr[1:]
    outStr = outStr.replace('_ ', '_')
    print(outStr)
    window.clipboard_clear()
    window.clipboard_append(outStr)


def lower_str():
    tempstr = nameEntry.get('1.0', 'end')
    if len(tempstr) == 0 or tempstr == '\n':
        tempstr = window.clipboard_get()
    tempstr = tempstr.replace('\t\n', '\n').replace('\t', ' ')
    arr = tempstr.split("\n")
    print(arr)
    outStr = ""
    notInferString = "以下是程序无法推断的属性或是不需要的注释:"
    for astr in arr:
        arrTemp = astr.split(" ")
        arrTemp = list(filter(lambda a: a != '', arrTemp))
        needJump = False
        if len(arrTemp) == 0:
            needJump = True
        if needJump == False and is_first_chinese_or_number(arrTemp[0]):
            outStr = outStr + '//' + astr
            needJump = True
        if not needJump:
            strTemp = arrTemp[0][0:1].lower() + arrTemp[0][1:]
            for i in range(len(arrTemp)):
                arrTemp[i] = arrTemp[i].lower()
            print(arrTemp)
            if len(arrTemp) > 1:
                if "string" in arrTemp:
                    outStr = outStr + '\n' + "private String " + strTemp + ';'
                elif ("int" in arrTemp) or ("long" in arrTemp) or ("datetime" in arrTemp) or ("number" in arrTemp) or (
                        "integer" in arrTemp) or ("date" in arrTemp):
                    outStr = outStr + '\n' + "private Integer " + strTemp + ';'
                elif ("bool" in arrTemp) or ("boolean" in arrTemp):
                    outStr = outStr + '\n' + "private Boolean " + strTemp + ';'
                elif ("double" in arrTemp) or ("float" in arrTemp):
                    outStr = outStr + '\n' + "private Float " + strTemp + ';'
                elif ("object" in arrTemp):
                    outStr = outStr + '\n' + "private EL" + strTemp[0:1].capitalize() + strTemp[
                                                                                                              1:] + ' *' + strTemp + ';(这是推测类型)'
                elif ("object[]" in arrTemp):
                    outStr = outStr + '\n' + "private List<EL" + strTemp[
                                                                                          0:1].capitalize() + strTemp[
                                                                                                              1:] + ' *' + "> *" + strTemp + ';(这是推测类型)'
                elif ("string[]" in arrTemp):
                    outStr = outStr + '\n' + "private List<String> " + strTemp + ';'
                else:
                    notInferString = notInferString + '\n' + '//' + astr
            else:
                if arrTemp[0] == 'success':
                    continue
                elif len(outStr) == 0:
                    outStr = "public class EL" + strTemp + ' { (这是推测类型)'
                else:
                    outStr = outStr + "\n}\n" + '\n\n' + "public class EL" + strTemp[0:1].capitalize() + strTemp[
                                                                                                          1:] + ' { (这是推测类型)'
    if notInferString != "以下是程序无法推断的属性或是不需要的注释:":
        outStr = outStr + "\n" + notInferString
    print(outStr)
    # nameEntry.insert('end', outStr)
    window.clipboard_clear()
    window.clipboard_append(outStr)


def get_firist():
    tempstr = nameEntry.get('1.0', 'end')
    if len(tempstr) == 0 or tempstr == '\n':
        tempstr = window.clipboard_get()
    tempstr = tempstr.replace('\t', ' ')
    arr = tempstr.split("\n")
    print(arr)
    outStr = ""
    for astr in arr:
        arrTemp = astr.split(" ")
        arrTemp = list(filter(lambda a: a != '', arrTemp))
        if len(arrTemp) == 0:
            continue
        print(arrTemp)
        strTemp = arrTemp[0][0:1].lower() + arrTemp[0][1:]
        outStr = outStr + '\n' + strTemp
    print(outStr)
    window.clipboard_clear()
    window.clipboard_append(outStr)


window = tk.Tk()
window.title('WHY String Creator')
window.geometry('700x700')  # 这里的乘是小x
nameEntry = tk.Text(window)
nameEntry.place(x=0, y=0, width=700, height=400)
# nameEntry.pack()

b = tk.Button(window, text="string 变为 _string = string;\n(可多行输入)", command=hit_me)
b.place(x=0, y=400, width=250, height=100)

b1 = tk.Button(window, text="将文档转换为属性", command=lower_str)
b1.place(x=250, y=400, width=250, height=100)

b2 = tk.Button(window, text="保留每行第一个（小写首字母）", command=get_firist)
b2.place(x=250, y=500, width=250, height=100)
window.mainloop()
