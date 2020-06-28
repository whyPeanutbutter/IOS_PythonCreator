import json
import os
dict_temp = {
    "UIButton": "UIButtonJson.txt",
    "UILabel": "UILabelJson.text",
    "UITableView": "UITableViewJson.text",
    "UITableViewCell": "UITableViewCellJson.text",
    "UIImageView": "UIImageViewJson.text",
    "UIScrollView": "UIScrollViewJson.text",
    "NSMutableAttributedString": "NSMutableAttributedStringJson.text",
    "UITextView": "UITextViewJson.text",
    "UICollectionView": "UICollectionViewJson.text",
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