# -*- coding: utf-8 -*-
import json
import os
dict_temp = {
    "init": "UIButton *WHYName = [UIButton buttonWithType:UIButtonTypeCustom];",
    "frame": "WHYName.frame = CGRectMake(<#CGFloat x#>, <#CGFloat y#>, <#CGFloat width#>, <#CGFloat height#>);",
    "cornerRadius": "WHYName.layer.cornerRadius = 4;\nWHYName.layer.masksToBounds = YES;",
    "title": "[WHYName setTitle:@\"<#content#>\" forState:UIControlStateNormal];\nWHYName.titleLabel.textAlignment = <#NSTextAlignmentCenter#>;\n[WHYName setTitleColor:<#Color_Theme#> forState:UIControlStateNormal];\nWHYName.titleLabel.font = GetMediumFont(<#16#>);",
    "image": "[WHYName setImage:[UIImage imageNamed:@\"<#content#>\"] forState:UIControlStateNormal];",
    "backgroundColor": "WHYName.backgroundColor = <#Color_FC5A1C#>;",
    "clicked": "[WHYName addTarget:self action:@selector(<#WHYNameClicked:#>) forControlEvents:UIControlEventTouchUpInside];\n- (void)WHYNameClicked:(UIButton *)button{\n\n}",
    "Border": "[WHYName.layer setBorderColor:<#Color_Theme#>.CGColor];\n[WHYName.layer setBorderWidth:<#1.0#>];",
    "addSubView": "[<#self#> addSubview:WHYName];",
    "masonry": "[WHYName mas_makeConstraints:^(MASConstraintMaker *make) {\n}];",
}

file = open("UIFilePath.txt", 'r')
dict = json.loads(file.read())
myFile = dict["UIButton"]

if os.path.exists(myFile):
    os.remove(myFile)
file = open(myFile, 'w')
file.write(json.dumps(dict_temp))
# 注意关闭文件
file.close()

file = open(myFile, 'r')
dict = json.loads(file.read())
print(dict)
print(dict["title"])
# 注意关闭文件
file.close()