import json
import os
dict_temp = {
    "init": "UITableViewDataSource,UITableViewDelegate\nUITableView *WHYName = [[UITableView alloc]initWithFrame:CGRectZero style:UITableViewStyleGrouped]; \ntableView.dataSource = self;\ntableView.delegate = self;\nWHYName.separatorStyle = UITableViewCellSeparatorStyleNone;\nWHYName.showsVerticalScrollIndicator = NO;",
    "frame": "WHYName.frame = CGRectMake(<#CGFloat x#>, <#CGFloat y#>, <#CGFloat width#>, <#CGFloat height#>);",
    "estimatedRowHeight": "WHYName.estimatedRowHeight = <#65#>;\ntableView.rowHeight = UITableViewAutomaticDimension;",
    "backgroundColor": "WHYName.backgroundColor = UIColor.whiteColor;",
    "registerClass": "static NSString* const CellIdentifier = @\"CellIdentifier\";\n[WHYName registerClass:[<#ELInteractiveListTableViewCell#> class] forCellReuseIdentifier:CellIdentifier];",
    "addSubView": "[<#self#> addSubview:WHYName];",
    "masonry": "[WHYName mas_makeConstraints:^(MASConstraintMaker *make) {\n}];",
    "sectionNum": "- (NSInteger)numberOfSectionsInTableView:(UITableView *)tableView{\nreturn 1;\n}\n",
    "rowNum": "- (NSInteger)tableView:(UITableView *)tableView numberOfRowsInSection:(NSInteger)section{\nreturn interactionList.data.count;\n}\n",
    "rowHeight": "- (CGFloat)tableView:(UITableView *)tableView heightForRowAtIndexPath:(NSIndexPath *)indexPath{\nreturn 103;\n}\n",
    "cellView": "- (UITableViewCell *)tableView:(UITableView *)tableView cellForRowAtIndexPath:(NSIndexPath *)indexPath{\nELInteractiveListTableViewCell *cell = [tableView dequeueReusableCellWithIdentifier:CellIdentifier];\nreturn cell;\n}\n",
    "headerView": "- (UIView *)tableView:(UITableView *)tableView viewForHeaderInSection:(NSInteger)section{\nreturn [[UIView alloc]init];\n}\n\n- (CGFloat)tableView:(UITableView *)tableView heightForHeaderInSection:(NSInteger)section\n{\nreturn 0.0001f;\n}\n",
    "footerView": "- (UIView *)tableView:(UITableView *)tableView viewForFooterInSection:(NSInteger)section{\nUIView *view = [[UIView alloc] init];\nreturn view;\n}\n\n- (CGFloat)tableView:(UITableView *)tableView heightForFooterInSection:(NSInteger)section{\nreturn 4.0;\n}\n",
    "selectCell": "- (void)tableView:(UITableView *)tableView didSelectRowAtIndexPath:(NSIndexPath *)indexPath {\n[tableView deselectRowAtIndexPath:indexPath animated:NO];\n}\n",
}

file = open("UIFilePath.txt", 'r')
dict = json.loads(file.read())
myFile = dict["UITableView"]

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