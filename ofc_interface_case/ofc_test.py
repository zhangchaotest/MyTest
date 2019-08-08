from random import randint
data = {"appId":"100056","inboundPlanDetail":[{"commodityCode":"1000014746","commodityName":"多次推送云象--BCP验证002（验证3次推送）","planQty":1.00000000,"unit":"袋"}],"inboundPlanTime":"20190614101213","inboundType":2,"outInboundPlanCode":"3100000011","outSourceCode":"100002809","warehouseCode":"1","warehouseName":"新希望仓"}
params=[]
for key, value in data.items():
    new_dict = data.copy()
    if key != "outInboundPlanCode":
        new_dict[key] = ""
        new_dict["outInboundPlanCode"] = str(randint(3100000011, 4100000011))
        params.append(new_dict)

print(params)