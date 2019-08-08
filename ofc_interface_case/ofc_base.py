import json
import random

import requests


class OfcTest:
    def __init__(self, data, ip, interface):
        if type(data) is str:
            data = json.loads(data)
        self.data = data
        self.ip = ip
        self.interface = interface

    def get_url(self, params):
        return "http://" + self.ip + "/" + self.interface + "?r=" + params

    def get_params(self, exclude_arguments, test_content):
        params = []
        get_data = self.data
        for key, value in get_data.items():
            new_data = get_data.copy()
            if key != exclude_arguments:
                new_data[exclude_arguments] = str(random.randint(3000000000, 4000000000))
                new_data[key] = test_content
                params.append(new_data)
        return params


def exec_case(OfcTest, params):
    if type(params) is not list:
        params = [params]
    for each in range(len(params)):
        print("这是第{}条请求".format(each + 1))
        param = params[each]
        print("请求信息", param)
        re = requests.get(OfcTest.get_url(json.dumps(param)))
        print("响应信息", re.text)
        print("*******************************************************" * 3)


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


if __name__ == '__main__':
    data = '{"appId":"100056","inboundPlanDetail":[{"commodityCode":"1000014746","commodityName":"多次推送云象--BCP验证002（验证3次推送）","planQty":1.00000000,"unit":"袋"}],"inboundPlanTime":"20190614101213","inboundType":2,"outInboundPlanCode":"3100000011","outSourceCode":"100002809","warehouseCode":"F008","warehouseName":"新希望仓"}'
    interface = "YGOP.B2B.OFC.Router.InboundPlanService.Create"
    ip = "192.168.2.167:8809"
    OfcTest = OfcTest(ip=ip, interface=interface, data=data)
    params = OfcTest.get_params(exclude_arguments='outInboundPlanCode', test_content='')
    for param in params:
        print(param)
        print(requests.get(OfcTest.get_url(json.dumps(param))).text)
        print("_________________________")
