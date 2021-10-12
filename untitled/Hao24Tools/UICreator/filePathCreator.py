# -*- coding: utf-8 -*-
import json
import os
dict_temp = {
    "UIView": "UIViewJson.text",
    "UIButton": "UIButtonJson.txt",
    "UILabel": "UILabelJson.text",
    "UITableView": "UITableViewJson.text",
    "UITableViewCell": "UITableViewCellJson.text",
    "UIImageView": "UIImageViewJson.text",
    "UIScrollView": "UIScrollViewJson.text",
    "WHYMasConstraints": "WHYMasConstraintsJson.text",
    "UITextView": "UITextViewJson.text",
    "数据库": "FMDBDataBaseJson.text",
    "接口相关": "ServerAPIJson.text",
    "UICollectionView": "UICollectionViewJson.text",
    "NSMutableAttributedString": "NSMutableAttributedStringJson.text"
}
myFile = "UIFilePath.txt"
if os.path.exists(myFile):
    os.remove(myFile)
file = open(myFile, 'w')
file.write(json.dumps(dict_temp))
# 注意关闭文件
file.close()

file = open(myFile, 'r')
dict = json.loads(file.read())
print(dict)
print(dict["UIButton"])
# 注意关闭文件
file.close()