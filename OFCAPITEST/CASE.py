import datetime
import hashlib
import json
import time

class newHopeInterface:
    def __init__(self):
        self.data_dict = {}
        self.data_dict['timestamp'] = datetime.datetime.utcnow().strftime("%Y%m%d%H%M%S")
        # self.data_dict['timestamp'] = '20190627081959'
        # self.url = 'http://api.fresh-scm.cn'
        self.url = 'http://testapi.fresh-scm.cn'

    def new_hope_encryption(self, t_data, url):
        if isinstance(t_data, str):
            data_dict = json.loads(t_data)
        if isinstance(t_data, dict):
            data_dict = t_data
        private_key = '45f07122-f036-5237-8613-c2385623b9ff'
        data_dict['pk'] = 'fccaf82e2af3a857ec6fe2bee2c21789666ad5ae'
        parameters = ''
        a = sorted(data_dict.items(), key=lambda item: item[0])
        print(a)
        for each in a:
            if each[1] == '':
                parameters = parameters + (each[0]) + '=""&'
            else:
                parameters = parameters + each[0] + "=" + str(each[1]) + "&"
        parameters = parameters.replace("'", '"')
        test = private_key + parameters + private_key
        m = hashlib.md5()
        b = test.encode(encoding='utf-8')
        m.update(b)
        str_md5 = m.hexdigest().upper()
        url = url + '?' + parameters + 'sign=' + str_md5
        return url

    def get_rk_query(self, storeCode='F007', inCodes='["YRIP201906190005"]'):
        url = self.url + '/api/qw/stock/input/query'
        self.data_dict["storeCode"] = storeCode
        self.data_dict["inCodes"] = inCodes
        return self.new_hope_encryption(self.data_dict, url)

    def get_ck_query(self, storeCode='F007', outCodes='["YCOP201906190008"]'):
        url = self.url + '/api/qw/stock/output/query'
        self.data_dict["storeCode"] = storeCode
        self.data_dict["outCodes"] = outCodes
        return self.new_hope_encryption(self.data_dict, url)

    def get_lot_query(self, store_code='F007', product_code='1000015114', quality_type='1', customer_id='1',
                      lot_no='190614190614'):
        url = self.url + '/api/qw/stock/product/lot'
        self.data_dict["storeCode"] = store_code
        self.data_dict["productCode"] = "['" + product_code + "']"
        self.data_dict["qualityType"] = quality_type
        self.data_dict["customerId"] = customer_id
        self.data_dict["lotNo"] = lot_no
        return self.new_hope_encryption(self.data_dict, url)

    def get_adjustment_query(self, store_code='F007', end_time='20190627161959', invoices_type='1', customer_id='1',
                             start_time='20190627161748'):
        url = self.url + '/api/qw/stock/adjustment/query'
        self.data_dict["storeCode"] = store_code
        self.data_dict["endTime"] = end_time
        self.data_dict["type"] = invoices_type
        self.data_dict["customerId"] = customer_id
        self.data_dict["startTime"] = start_time

        return self.new_hope_encryption(self.data_dict, url)

    def close_input_close(self, store_code='F007', in_codes=''):
        url = self.url + '/api/qw/stock/input/close'
        self.data_dict["storeCode"] = store_code
        self.data_dict["inCodes"] = in_codes
        return self.new_hope_encryption(self.data_dict, url)


if __name__ == "__main__":
    import requests

    ob = newHopeInterface()
    url = ob.get_lot_query()
    print(url)
    re = requests.get(url=url).text
    print(re)
