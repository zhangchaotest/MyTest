import datetime
import hashlib

data_dict = {}
data_dict['timestamp'] = datetime.datetime.utcnow().strftime("%Y%m%d%H%M%S")

privatekey = '45f07122-f036-5237-8613-c2385623b9ff'
data_dict['pk'] = 'fccaf82e2af3a857ec6fe2bee2c21789666ad5ae'

# data_dict["qualityType"] = '1'
# data_dict["storeCode"] = "F007"
# data_dict["customerId"] = '100056'
# data_dict["lotNo"] = '190605190620'
# data_dict["productCode"] = '1000014746'

data_dict["storeCode"] = 'F007'
data_dict["outCodes"] = '["YRIP201906140026"]'

a = sorted(data_dict.items(), key=lambda item: item[0])
parameters = ''

for each in a:
    parameters = parameters + each[0] + "=" + each[1] + "&"

# 由于MD5模块在python3中被移除
# 在python3中使用hashlib模块进行md5操作

# 待加密信息
str = privatekey + parameters + privatekey
print(str)
# 创建md5对象
m = hashlib.md5()

# Tips
# 此处必须encode
# 若写法为m.update(str)  报错为： Unicode-objects must be encoded before hashing
# 因为python3里默认的str是unicode
# 或者 b = bytes(str, encoding='utf-8')，作用相同，都是encode为bytes
b = str.encode(encoding='utf-8')
m.update(b)
str_md5 = m.hexdigest().upper()

print('MD5加密前为 ：' + str)
print('MD5加密后为 ：' + str_md5)

# 另一种写法：b‘’前缀代表的就是bytes
# str_md5 = hashlib.md5(b'this is a md5 test.').hexdigest()
# print('MD5加密后为 ：' + str_md5)
# url = 'http://api.fresh-scm.cn:80/api/qw/stock/product/lot?'+parameters+'sign=' + str_md5
url = 'http://api.fresh-scm.cn/api/qw/stock/output/query?' + parameters + 'sign=' + str_md5
import requests

print(url)
re = requests.get(url)
print(re.text)
