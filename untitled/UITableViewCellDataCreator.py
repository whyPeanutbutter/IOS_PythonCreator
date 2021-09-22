import json
import os
dict_temp = {
    "init": "WHYName",
    "interface": "@interface WHYName : UITableViewCell\n@end",
    "delegate": "@protocol WHYNameDelegate<NSObject>\n@optional\n- (void)WHYNameClicked;\n@end\n\n@property (weak, nonatomic) id<WHYNameDelegate> delegate;",
    "initWithStyle": "@interface WHYName(){\n\n}@end\n@implementation WHYName\n - (instancetype)initWithStyle:(UITableViewCellStyle)style reuseIdentifier:(NSString *)reuseIdentifier{\nif (self = [super initWithStyle:style reuseIdentifier:reuseIdentifier]) {\nself.selectionStyle = UITableViewCellSelectionStyleNone;\n[self setupUI];\n}\nreturn self;\n}\n\n- (void)setupUI {\n<#content#>\n}\n@end",
}

file = open("UIFilePath.txt", 'r')
dict = json.loads(file.read())
myFile = dict["UITableViewCell"]

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