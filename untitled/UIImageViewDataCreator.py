import json
import os
dict_temp = {
    "init": "UIImageView *WHYName = [[UIImageView alloc] initWithImage: [UIImage imageNamed:@\"<#qs_video_background#>\"]];",
    "frame": "WHYName.frame = CGRectMake(<#CGFloat x#>, <#CGFloat y#>, <#CGFloat width#>, <#CGFloat height#>);",
    "imageUrl": "#import \"UIImageView+WebCache.h\" [WHYName sd_setImageWithURL:[NSURL URLWithString:[Utility urlEncode:imageUrl]] placeholderImage:@\"wuhytodo\"];",
    "cornerRadius": "WHYName.layer.cornerRadius = 4;\nWHYName.layer.masksToBounds = YES;",
    "contentMode": "WHYName.contentMode = UIViewContentModeScaleToFill;",
    "clicked": "[WHYName addTarget:self action:@selector(<#WHYNameClicked:#>) forControlEvents:UIControlEventTouchUpInside];\nWHYName.userInteractionEnabled = YES;",
    "addSubView": "[<#self#> addSubview:WHYName];",
    "masonry": "[WHYName mas_makeConstraints:^(MASConstraintMaker *make) {\n}];",
}

file = open("UIFilePath.txt", 'r')
dict = json.loads(file.read())
myFile = dict["UIImageView"]

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