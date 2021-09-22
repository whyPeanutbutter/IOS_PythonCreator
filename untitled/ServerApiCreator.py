import json
import os
dict_temp = {
    "init": "",
    "数据结构.h": "#import 'ELBaseResponse.h'\n#import 'ELBaseRequest.h'\n\nNS_ASSUME_NONNULL_BEGIN\n@interface WHYNAME : NSObject\n@property (nonatomic, assign) BOOL hasTrial;\n@property (nonatomic, copy) NSString *name;\n@property (nonatomic, copy) NSString *coverImage;\n@property (nonatomic, assign) NSInteger beginTime;\n@property (nonatomic, assign) NSInteger endTime;\n\n@end\n\n@interface WHYNAMEs : ELBaseResponse\n@property (nonatomic, strong) NSArray<WHYNAME *> *data;\n@end\n\n@interface ELWHYNAMERequest : ELBaseRequest\n\n@property (strong, nonatomic) NSNumber *organizationId;\n@property (strong, nonatomic) NSArray *categoryClassIds;\n@property (strong, nonatomic) NSNumber *trainingType;\n@property (strong, nonatomic) NSNumber *offset;\n@property (strong, nonatomic) NSNumber *limit;\n@property (nonatomic, copy) NSString *name;\n\n@end\nNS_ASSUME_NONNULL_END",
    "数据结构.m": "@implementation WHYNAME\n+ (NSDictionary *)keyMapper\n{\nreturn @{@'id':@'classId'};\n}\n\n@end\n\n@implementation ELCategoryClassSearchDetails\n+ (Class)classForObjectsInArray:(NSString *)propertyName {\nClass class = [super classForObjectsInArray:propertyName];\nif ([propertyName isEqualToString:@'data']) {\nclass = [WHYNAME class];\n}\n\nreturn class;\n}\n@end\n\n@implementation ELWHYNAMERequest\n\n-(NSDictionary *)keyMapper{\nreturn @{@'description': @'requestDescription'};\n}\n\n- (void)setLimit:(NSNumber *)limit {\nif (limit && [limit intValue] < 0) {\n_limit = nil;\n_offset = nil;\nreturn;\n}\n\n_limit = limit;\nif (!_offset) {\n_offset = @(0);\n}\n}\n\n- (void)setUserClassId:(NSNumber *)userClassId {\n_userClassId = [userClassId intValue] <= 0 ? nil :userClassId;\n}\n\n\n@end",
    "manger.h": "#import 'ELDiscoveryCloudClassDetail.h'\n\nNS_ASSUME_NONNULL_BEGIN\n\n@interface WHYNAME : NSObject\n\n+ (void)getByRequest:(ELRequest *)request callback:(void (^)(ELDetails *response))callback;\n\n\n+ (void)getById:(NSInteger)Id Id:(NSInteger)Id callBack:(void (^)(ELInfos *response))callback;\n\n@end\n\nNS_ASSUME_NONNULL_END",
    "manger.m": "#import 'ELBaseRequestDataManager.h'\n#import 'ELHttpHelper.h'\n#import 'Utility.h'\n\n@implementation ELDiscoveryCloudClassManger\n\n+ (void)getByRequest:(ELRequest *)request callback:(void (^)(ELhDetails *response))callback {\nNSDictionary *parameters = [request requestDictioaryWithPropertiesOfObject];\n[ELBaseRequestDataManager simpleRequestDataFromServerWithMethod:<#Get#> url:[ELHttpHelper urlForGetTeacherInfo] parameters:parameters targetClassName:@'ELDetails' callBack:^(id target, NSString *responseDataString) {\ncallback(target);\n}];\n}\n\n+ (void)getById:(NSInteger)Id Id:(NSInteger)Id callBack:(void (^)(ELInfos *response))callback {\nNSDictionary *parameters = @{\n@'Id': @(Id),\n@'pageIndex': @(pageIndex),\n@'pageSize': @(pageSize)\n};\n<#\nNSMutableDictionary *parameters = @{\n@'classId' : [Utility excludeNullValue:classId],\n@'schoolId' : @(schoolId)\n} ;\nif (!isEmptyStr(courseId)) {\nparameters[@'courseId'] = courseId;\n}\n#>\n\n[ELBaseRequestDataManager simpleRequestDataFromServerWithMethod:Get url:[ELHttpHelper urlForGetTeacherInfo] parameters:parameters targetClassName:@'ELInfos' callBack:^(id target, NSString *responseDataString) {\ncallback(target);\n}];\n}\n\n@end\n",
    "ELHttpHelper.h": "+ (NSString *)urlForWHYName;",
    "ELHttpHelper.m": "+ (NSString *)urlForWHYName\n{\nreturn [[[ELBuildConfig singleBuildConfigInfo] elementValueForKey:@'url_qsxt'] stringByAppendingString:GetWHYNameUrlExtension];\n}\nstatic NSString *const GetWHYNameExtension = @'/yxk/contact';\n",
}

file = open("UIFilePath.txt", 'r')
dict = json.loads(file.read())
myFile = dict["接口相关"]

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