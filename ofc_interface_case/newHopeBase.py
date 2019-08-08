import datetime
import hashlib
import json


class newHopeInterface:
    def __init__(self):
        self.data_dict = {}
        self.data_dict['timestamp'] = datetime.datetime.utcnow().strftime("%Y%m%d%H%M%S")

    def test_encryption(self, t_data, url):
        if isinstance(t_data, str):
            data_dict = json.loads(t_data)
        if isinstance(t_data, dict):
            data_dict = t_data
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
        m = hashlib.md5()
        b = test.encode(encoding='utf-8')
        m.update(b)
        str_md5 = m.hexdigest().upper()
        url = url + '?' + parameters + 'sign=' + str_md5
        return url

    def get_rk_query(self, storeCode='F007', inCodes='["YRIP201906190005"]'):
        url = 'http://api.fresh-scm.cn/api/qw/stock/input/query'
        self.data_dict["storeCode"] = storeCode
        self.data_dict["inCodes"] = inCodes
        return self.test_encryption(self.data_dict, url)

    def get_ck_query(self, storeCode='F007', outCodes='["YCOP201906190008"]'):
        url = 'http://api.fresh-scm.cn/api/qw/stock/output/query'
        self.data_dict["storeCode"] = storeCode
        self.data_dict["outCodes"] = outCodes
        return self.test_encryption(self.data_dict, url)

    def get_lot_query(self, store_code='F007', product_code='1000015114', quality_type='1', customer_id='100056',
                      lot_no='190614190614'):
        url = 'http://api.fresh-scm.cn/api/qw/stock/product/lot'
        self.data_dict["storeCode"] = store_code
        self.data_dict["productCode"] = product_code
        self.data_dict["qualityType"] = quality_type
        self.data_dict["customerId"] = customer_id
        self.data_dict["lotNo"] = lot_no
        return self.test_encryption(self.data_dict, url)

    def get_lot_query(self, store_code='F007', end_time='1000015114', invoices_type='', customer_id='100056',
                      start_time='190614190614'):
        url = 'http://api.fresh-scm.cn/api/qw/stock/adjustment/query'
        self.data_dict["storeCode"] = store_code
        self.data_dict["EndTime"] = end_time
        self.data_dict["type"] = invoices_type
        self.data_dict["customerId"] = customer_id
        self.data_dict["StartTime"] = start_time
        return self.test_encryption(self.data_dict, url)

    # def insert_stock_input(self, store_code='F007', product_code='1000015114', quality_type='1', customer_id='100056',
    #                  lot_no='190614190614'):
    #     url = 'http://api.fresh-scm.cn/api/qw/stock/product/lot'
    #     self.data_dict["storeCode"] = store_code
    #     self.data_dict["list"] ='[[productCode:商品编码,productName:商品编码,productCount:入库数量,unit:单位]...]'
    #     self.data_dict["storeCode"] = store_code
    #     self.data_dict["productCode"] = product_code
    #     self.data_dict["qualityType"] = quality_type
    #     self.data_dict["customerId"] = customer_id
    #     self.data_dict["lotNo"] = lot_no
    #     return self.test_encryption(self.data_dict, url)

    def close_input_planned(self, store_code='F007', in_codes=''):
        url = 'http://api.fresh-scm.cn/api/qw/stock/input/close'
        self.data_dict["storeCode"] = store_code
        self.data_dict["inCodes"] = in_codes
        return self.test_encryption(self.data_dict, url)


ob = newHopeInterface()
print(ob.get_lot_query())
