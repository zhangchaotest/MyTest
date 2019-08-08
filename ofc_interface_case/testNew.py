import hashlib
import json
import datetime

# data = '{"appId":"100056","outOutboundCodeList":["YCOP201906190008"],"warehouseCode":"F007"}'
# interface = "YGOP.B2B.OFC.Router.OutboundService.Query"
# ip = "192.168.2.167:8809"
#
# re_data = '{"appId":"100056","outOutboundCodeList":["YCOP201906190008"],"warehouseCode":"F007"}'


def test_blank(re_data, test_content):
    params = []
    new_data = json.loads(re_data).copy()
    for each in new_data:
        new_data = json.loads(data).copy()
        new_data[each] = test_content
        params.append(json.dumps(new_data))
    return params


def test_encryption(t_data, url):
    if isinstance(t_data, str):
        data_dict = json.loads(t_data)
    if isinstance(t_data, dict):
        data_dict = t_data
    data_dict['timestamp'] = datetime.datetime.utcnow().strftime("%Y%m%d%H%M%S")
    privatekey = '45f07122-f036-5237-8613-c2385623b9ff'
    data_dict['pk'] = 'fccaf82e2af3a857ec6fe2bee2c21789666ad5ae'
    parameters = ''
    a = sorted(data_dict.items(), key=lambda item: item[0])
    for each in a:
        if each[1] == '':
            parameters = parameters + (each[0]) + '=""&'
        else:
            parameters = parameters + each[0] + "=" + str(each[1]) + "&"
    parameters = parameters.replace("'", '"')
    test = privatekey + parameters + privatekey

    print(test)
    m = hashlib.md5()
    b = test.encode(encoding='utf-8')
    m.update(b)
    str_md5 = m.hexdigest().upper()

    print(str_md5)

    url = url + '?' + parameters + 'sign=' + str_md5
    print(url)
    return url


if __name__ == '__main__':
    import requests


    test_url = 'http://api.fresh-scm.cn/api/qw/stock/input/query'
    data = '{"storeCode":"F007","inCodes":["YRIP201906190005"]}'

    # test_url = 'http://api.fresh-scm.cn/api/qw/stock/output/query'
    # data = '{"storeCode":"F007","outCodes":["YRIP201906140026"]}'
    # test = encryption('{"appId": "", "outOutboundCodeList": ["YCOP201906190008"], "warehouseCode": "F007"}', test_url)
    params = test_blank(data, "1")
    # t_data = {"appId": "", "outOutboundCodeList": ["YCOP201906190008"], "warehouseCode": "F007"}
    # for each in params:
    #     test = test_encryption(t_data=each, url=test_url)
    #     print(requests.get(test).text)
    test = test_encryption(t_data=data, url=test_url)
    print(test)
    print(requests.get(url=test).text)
    # print(requests.get(test).text)
    # test = test_encryption(t_data=t_data, url=test_url)
    # print(test)
