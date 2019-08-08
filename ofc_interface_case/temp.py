import hashlib

text ='45f07122-f036-5237-8613-c2385623b9ffoutCodes=["YRIP201906140026"]&pk=fccaf82e2af3a857ec6fe2bee2c21789666ad5ae&storeCode=F007&timestamp=20190621074215&45f07122-f036-5237-8613-c2385623b9ff'
# m = hashlib.md5()
# b = test.encode(encoding='utf-8')
# m.update(b)
# str_md5 = m.hexdigest().upper()
# print(str_md5)

m = hashlib.md5()
b = text.encode(encoding='utf-8')
m.update(b)
str_md5 = m.hexdigest().upper()

print('MD5加密前为 ：' + text)
print('MD5加密后为 ：' + str_md5)

