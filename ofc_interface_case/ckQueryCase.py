import MySQLdb
import requests


def get_outbound_code(sql):
    db = MySQLdb.connect("qa-winchain.mysql.rds.aliyuncs.com", "ygtest", "ygtest", "ygop_b2b_ofc_wcs", charset='utf8')
    cursor = db.cursor()
    cursor.execute(sql)
    data = cursor.fetchall()
    db.close()
    outInboundCodeList = ''
    data_list = []
    for each in data:
        if outInboundCodeList == "":
            outInboundCodeList = each[0]
        else:
            outInboundCodeList = outInboundCodeList + '","' + each[0]
        data_list.append(each[0])
    return outInboundCodeList, data_list


def get_url(outInboundCodeList):
    data = '{"appId":"100056","outOutboundCodeList":["' + outInboundCodeList + '"],"warehouseCode":"F007"}'
    interface = "YGOP.B2B.OFC.Router.OutboundService.Query"
    ip = "192.168.2.167:8809"

    url = "http://" + ip + "/" + interface + "?r=" + data
    return url


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


def test_blank(test_content):
    data = '{"appId":"100056","outOutboundCodeList":["YCOP201906190008"],"warehouseCode":"F007"}'
    interface = "YGOP.B2B.OFC.Router.OutboundService.Query"
    ip = "192.168.2.167:8809"
    params = []
    new_data = json.loads(data).copy()
    for each in new_data:
        new_data = json.loads(data).copy()
        new_data[each] = test_content
        url = "http://" + ip + "/" + interface + "?r=" + json.dumps(new_data)
        params.append(url)
    return params


if __name__ == "__main__":
    import json
    #
    # sql = "SELECT b.out_outbound_code FROM outbound_detail a LEFT JOIN outbound b on a.outbound_code = b.outbound_code where b.warehouse_code = 'F007'GROUP BY (a.outbound_code) ORDER BY (a.create_time) DESC  LIMIT 10;"
    # data = get_outbound_code(sql)
    #
    # url = get_url(data[0])
    # text_data = requests.get(url=url)
    # re_list = list(set(get_value("outOutboundCode", json.loads(text_data.text))))
    # data_list = list(set(data[1]))
    # re_list.sort()
    # data_list.sort()
    # if re_list == data_list:
    #     print("suscces")
    for x in test_blank(''):
        print(x)
        print(requests.get(url=x).text)
