# -*- coding: utf-8 -*-
import json
import os
dict_temp = {
    "init": "UITextView *WHYName = [[UITextView alloc] init];",
    "frame": "WHYName.frame = CGRectMake(<#CGFloat x#>, <#CGFloat y#>, <#CGFloat width#>, <#CGFloat height#>);",
    "ScrollEnabled": "[WHYName setScrollEnabled:NO];",
    "editable": "WHYName.editable = NO;",
    "backgroundColor": "WHYName.backgroundColor = [UIColor whiteColor];",
    "text": "WHYName.text = @\"<#反馈原因#>\";\nWHYName.textColor = Color_Black_Medium;\nWHYName.font = GetRegularFont(16);\nWHYName.textAlignment = NSTextAlignmentLeft;",
    "textContainerInset": "WHYName.textContainerInset = UIEdgeInsetsMake(0, 0, 0, 0);",
"returnKeyType": "WHYName.returnKeyType = UIReturnKeySearch;",
"keyboardType": "WHYName.keyboardType = UIKeyboardTypeNamePhonePad;",
    "addSubView": "[<#self#> addSubview:WHYName];",
    "masonry": "[WHYName mas_makeConstraints:^(MASConstraintMaker *make) {\n}];",
}

file = open("UIFilePath.txt", 'r')
dict = json.loads(file.read())
myFile = dict["UITextView"]

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