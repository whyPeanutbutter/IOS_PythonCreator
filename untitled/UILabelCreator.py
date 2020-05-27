import json
import os
dict_temp = {
    "init": "UILabel *WHYName = [[UILabel alloc]init];",
    "frame": "WHYName.frame = CGRectMake(<#CGFloat x#>, <#CGFloat y#>, <#CGFloat width#>, <#CGFloat height#>);",
    "cornerRadius": "WHYName.layer.cornerRadius = 4;\nWHYName.layer.masksToBounds = YES;",
    "backgroundColor": "WHYName.backgroundColor = [UIColor whiteColor];",
    "title": "titleLabel.text = @\"<#反馈原因#>\";\ntitleLabel.textColor = Color_Black_Medium;\ntitleLabel.font = GetRegularFont(16);\ntitleLabel.textAlignment = NSTextAlignmentCenter;",
    "clicked": "WHYName.userInteractionEnabled = YES;\nUITapGestureRecognizer *tapGestureRecognizer = [[UITapGestureRecognizer alloc]initWithTarget:self action:@selector(WHYNameTap)];\n[WHYName addGestureRecognizer:tapGestureRecognizer];",
    "addSubView": "[<#self#> addSubview:WHYName];",
    "masonry": "[WHYName mas_makeConstraints:^(MASConstraintMaker *make) {\n<#make.left.mas_equalTo(16);#>\n<#make.right.mas_equalTo(16);#>\n<#make.top.mas_equalTo(16);#>\n<#make.bottom.mas_equalTo(0);#>\n<#make.width.mas_equalTo(16);#>\n<#make.height.mas_equalTo(16);#>\n}];",
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
print(dict["title"])
# 注意关闭文件
file.close()