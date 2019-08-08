import json

from ofc_interface_case.ofc_base import OfcTest
from ofc_interface_case.ofc_base import exec_case

data = '{"appId":"100056","outOutboundPlanCode":"6600000018","outSourceCode":"200022161","outboundPlanDetailList":[{"commodityCode":"1000014746","commodityName":"多次推送云象--BCP验证002（验证3次推送）","destinationName":"测试门店1","planQty":2.0000,"stockUnit":"袋"}],"outboundPlanTime":"20190617120000","outboundType":1,"warehouseCode":"F007","warehouseName":"新希望仓"}'
interface = "YGOP.B2B.OFC.Router.OutboundPlanService.Create"

ip = "192.168.2.167:8809"
OfcTest = OfcTest(ip=ip, interface=interface, data=data)


def test_blank():
    '''
    验证必填项为空的情况
    :return:
    '''
    params = OfcTest.get_params(exclude_arguments='outOutboundPlanCode', test_content='')
    exec_case(OfcTest, params)


def test_character():
    '''
    验证特殊字符
    :return:
    '''
    params = OfcTest.get_params(exclude_arguments='outOutboundPlanCode', test_content='!@#$%&^')
    exec_case(OfcTest, params)


def test_succeed():
    import random
    """
    验证成功的情况
    :return: 
    """
    testdata = json.loads(data)
    testdata["outOutboundPlanCode"] = str(random.randint(3000000000, 4000000000))
    exec_case(OfcTest, testdata)


if __name__ == '__main__':
    import time
    s_time = time.time()
    for i in range(0, 1):
        test_blank()
    e_time = time.time()
    print(e_time-s_time)
    test_blank()