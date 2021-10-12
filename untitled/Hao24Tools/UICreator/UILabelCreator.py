# -*- coding: utf-8 -*-
import json
import os
dict_temp = {
    "init": "UILabel *WHYName = [[UILabel alloc]init];",
    "frame": "WHYName.frame = CGRectMake(<#CGFloat x#>, <#CGFloat y#>, <#CGFloat width#>, <#CGFloat height#>);",
    "border": "WHYName.layer.borderColor = Color_Black_Light.CGColor;\nWHYName.layer.borderWidth = 0.5;",
    "cornerRadius": "WHYName.layer.cornerRadius = 4;\nWHYName.layer.masksToBounds = YES;",
    "backgroundColor": "WHYName.backgroundColor = [UIColor whiteColor];",
    "numberOfLines": "WHYName.numberOfLines = 0;",
    "text": "WHYName.text = @\"<#反馈原因#>\";\nWHYName.textColor = Color_Black_Medium;\nWHYName.font = GetRegularFont(16);\nWHYName.textAlignment = NSTextAlignmentLeft;",
    "clicked": "WHYName.userInteractionEnabled = YES;\nUITapGestureRecognizer *tapGestureRecognizer = [[UITapGestureRecognizer alloc]initWithTarget:self action:@selector(WHYNameTap)];\n[WHYName addGestureRecognizer:tapGestureRecognizer];",
    "addSubView": "[<#self#> addSubview:WHYName];",
    "masonry": "[WHYName mas_makeConstraints:^(MASConstraintMaker *make) {\n}];",
}

file = open("UIFilePath.txt", 'r')
dict = json.loads(file.read())
myFile = dict["UILabel"]

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