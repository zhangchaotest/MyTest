import MySQLdb
import requests

db = MySQLdb.connect("qa-winchain.mysql.rds.aliyuncs.com", "ygtest", "ygtest", "ygop_b2b_ofc_wcs", charset='utf8')
cursor = db.cursor()
cursor.execute('''
SELECT b.out_inbound_code FROM inbound_detail a
LEFT JOIN inbound b
on a.inbound_code = b.inbound_code
where b.warehouse_code = 'F007'
GROUP BY (a.inbound_code)
''')
data = cursor.fetchall()
db.close()
print(list(data))
outInboundCodeList = ''
data_list = []
for each in data:
    if outInboundCodeList == "":
        outInboundCodeList = each[0]
    outInboundCodeList = outInboundCodeList + '","' + each[0]
    data_list.append(each[0])

data = '{"appId":"100056","outInboundCodeList":["' + outInboundCodeList + '"],"warehouseCode":"F007"}'
interface = "YGOP.B2B.OFC.Router.InboundService.Query"
ip = "192.168.2.167:8809"
url = "http://" + ip + "/" + interface + "?r=" + data


def get_value(key: str, data: dict) -> object:
    val = []
    if isinstance(data, dict):
        for k, v in data.items():
            if k == key:
                val.append(v)
            else:
                if isinstance(v, dict):
                    val += get_value(key, v)
                elif isinstance(v, list):
                    for each in v:
                        if isinstance(each, dict):
                            val += get_value(key, each)
    return val


if __name__ == "__main__":
    import json

    text_data = requests.get(url=url)
    print(text_data.text)
    re_list = get_value("outInboundCode", json.loads(text_data.text))

    re_list.sort()
    data_list.sort()
    if re_list == data_list:
        print("suscces")
