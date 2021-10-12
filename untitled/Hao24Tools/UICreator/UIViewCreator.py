# -*- coding: utf-8 -*-
import os
import json
dict_temp = {
    "init": "UIView *WHYName = [[UIView alloc] init];",
    "frame": "WHYName.frame = CGRectMake(<#CGFloat x#>, <#CGFloat y#>, <#CGFloat width#>, <#CGFloat height#>);",
    "border": "WHYName.layer.borderColor = Color_Black_Light.CGColor;\nWHYName.layer.borderWidth = 0.5;",
    "cornerRadius": "WHYName.layer.cornerRadius = 4;\nWHYName.layer.masksToBounds = YES;",
    "backgroundColor": "WHYName.backgroundColor = [UIColor whiteColor];",
    "clicked": "WHYName.userInteractionEnabled = YES;\nUITapGestureRecognizer *tapGestureRecognizer = [[UITapGestureRecognizer alloc]initWithTarget:self action:@selector(WHYNameTap)];\n[WHYName addGestureRecognizer:tapGestureRecognizer];",
    "addSubView": "[<#self#> addSubview:WHYName];",
    "masonry": "[WHYName mas_makeConstraints:^(MASConstraintMaker *make) {\n}];",
}

file = open("UIFilePath.txt", 'r')
dict = json.loads(file.read())
myFile = dict["UIView"]

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