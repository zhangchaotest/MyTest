import json

import requests

from ofc_interface_case.ofc_base import OfcTest
from ofc_interface_case.ofc_base import exec_case

data = '{"appId":"100056","inboundPlanDetail":[{"commodityCode":"1000010787","commodityName":"新疆灰枣10kg","planQty":1.00000000,"unit":"箱"},{"commodityCode":"1000011884","commodityName":"盛源康润奥尔良鸡翅900g","planQty":1.00000000,"unit":"袋"}],"inboundPlanTime":"20190614101213","inboundType":1,"outInboundPlanCode":"3100000011","outSourceCode":"100002809","warehouseCode":"F008","warehouseName":"新希望仓"}'
interface = "YGOP.B2B.OFC.Router.InboundPlanService.Create"
ip = "192.168.2.167:8809"

OfcTest = OfcTest(ip=ip, interface=interface, data=data)





def test_blank():
    '''
    验证必填项为空的情况
    :return:
    '''
    params = OfcTest.get_params(exclude_arguments='outInboundPlanCode', test_content='121')
    exec_case(OfcTest,params)


def test_character():
    '''
    验证特殊字符
    :return:
    '''
    params = OfcTest.get_params(exclude_arguments='outInboundPlanCode', test_content='!@#$%&^')
    exec_case(OfcTest,params)


def test_succeed():
    import random
    """
    验证成功的情况
    :return: 
    """
    testdata = json.loads(data)
    testdata["outInboundPlanCode"] = str(random.randint(3100000000, 4000000000))
    exec_case(OfcTest,testdata)


if __name__ == '__main__':
    # test_character()
    # import time
    # s_time = time.time()
    # for i in range(0, 1):
    #     test_blank()
    # e_time = time.time()
    # print(e_time-s_time)
    test_succeed()

