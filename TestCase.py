# -*- coding: gb2312 -*-
import json

ip = "192.168.2.167:8809"
interface = "YGOP.B2B.OFC.Router.InboundPlanService.Create"

data = '{"appId":"100056","inboundPlanDetail":[{"commodityCode":"1000014746","commodityName":"�����������--BCP��֤002����֤3�����ͣ�","planQty":1.00000000,"unit":"��"}],"inboundPlanTime":"20190614101213","inboundType":2,"outInboundPlanCode":"3100000011","outSourceCode":"100002809","warehouseCode":"1","warehouseName":"��ϣ����"}'
data = json.loads(data)
params = json.dumps(data)
url = "http://" + ip + "/" + interface + "?r=" + params
print("url��" + url)
print(params)
print(type(data))
print(data.keys())
import requests

headers = {"content-type": "application/json"}
re = requests.get(url=url, headers=headers)
print(re.text)

data = '{"appId":"100056","inboundPlanDetail":[{"commodityCode":"1000014746","commodityName":"�����������--BCP��֤002����֤3�����ͣ�","planQty":1.00000000,"unit":"��"}],"inboundPlanTime":"20190614101213","inboundType":2,"outInboundPlanCode":"3100000011","outSourceCode":"100002809","warehouseCode":"1","warehouseName":"��ϣ����"}'

if type(data) is str:
    print(22,data)
    print(type(eval(data)))
    print(type(json.loads(data)))


