import json
import os
dict_temp = {
    "init": "UIScrollView *WHYName = [[UIScrollView alloc]init];\nWHYName.showsVerticalScrollIndicator = NO;\nWHYName.showsHorizontalScrollIndicator = NO;",
    "frame": "WHYName.frame = CGRectMake(<#CGFloat x#>, <#CGFloat y#>, <#CGFloat width#>, <#CGFloat height#>);",
    "backgroundColor": "WHYName.backgroundColor = UIColor.whiteColor;",
    "addSubView": "[<#self#> addSubview:WHYName];",
    "masonry": "[WHYName mas_makeConstraints:^(MASConstraintMaker *make) {\n}];",
    "@available(iOS 11.0, *)": "if (@available(iOS 11.0, *)) {\nscrollView.insetsLayoutMarginsFromSafeArea = NO;\nscrollView.contentInsetAdjustmentBehavior = UIScrollViewContentInsetAdjustmentNever;\n} else {\n self.automaticallyAdjustsScrollViewInsets = NO;\n}",
}

file = open("UIFilePath.txt", 'r')
dict = json.loads(file.read())
myFile = dict["UIScrollView"]

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