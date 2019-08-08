import requests

s_url = 'http://192.168.2.167:8809/YGOP.B2B.OFC.Router.InventoryAdjustmentService.Query?req={"warehouseCode":"F009","appId":"100056","startTime":"20190108160000","endTime":"20191015160000","type":1}'
if __name__ == '__main__':
    re = requests.get(s_url)
    print(re.text)