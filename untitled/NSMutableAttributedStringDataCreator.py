# -*- coding: utf-8 -*-
import json
import os
dict_temp = {
    "init": "NSStering * titleString = <#content#>;\nNSMutableAttributedString *WHYName = [[NSMutableAttributedString alloc] initWithString:titleString];",
    "局部变色": "[WHYName addAttribute:NSForegroundColorAttributeName value:Color_White range:NSMakeRange(0, titleString.length)];\n[WHYName addAttribute:NSForegroundColorAttributeName value:Color_White range:NSMakeRange(0, 2)];",
    "ParagraphStyle": " NSMutableParagraphStyle *paragraphStyle = [[NSMutableParagraphStyle alloc] init];\nparagraphStyle.lineSpacing = 8;\n[WHYName addAttribute:NSParagraphStyleAttributeName value:paragraphStyle range:NSMakeRange(0, titleString.length)];",
    "font": "[WHYName addAttribute:NSFontAttributeName value:messageLbl.font range:NSMakeRange(0, [titleString length])];",
}

file = open("UIFilePath.txt", 'r')
dict = json.loads(file.read())
myFile = dict["NSMutableAttributedString"]

if os.path.exists(myFile):
    os.remove(myFile)
file = open(myFile, 'w')
file.write(json.dumps(dict_temp))
# 注意关闭文件
file.close()

file = open(myFile, 'r')
dict = json.loads(file.read())
print(dict)
print(dict["init"])
# 注意关闭文件
file.close()