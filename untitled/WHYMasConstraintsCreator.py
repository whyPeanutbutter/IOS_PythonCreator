import json
import os
dict_temp = {
    "init":"",
    "left": "make.left.equalTo(@16);",
"right": "make.left.equalTo(@-16);",
"top": "make.top.equalTo(@16);",
"bottom": "make.bottom.equalTo(@0);",
"width": "make.width.equalTo(@0);",
"height": "make.height.equalTo(@0);",
"edges": "make.edges.equalTo(@0);",
"size": "make.size.mas_equalTo(CGSizeMake(0, 0));",
"centerX": "make.centerX.equalTo(@0);",
"centerY": "make.centerY.equalTo(@0);",
}

file = open("UIFilePath.txt", 'r')
dict = json.loads(file.read())
myFile = dict["WHYMasConstraints"]

if os.path.exists(myFile):
    os.remove(myFile)
file = open(myFile, 'w')
file.write(json.dumps(dict_temp))
# 注意关闭文件
file.close()

file = open(myFile, 'r')
dict = json.loads(file.read())
print(dict["left"])
# 注意关闭文件
file.close()