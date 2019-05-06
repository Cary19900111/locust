from locust import HttpLocust,TaskSet,task
from faker import Faker
import json
#locust -f test/test1.py --no-web --run-time 10s --csv ffff -c 5 -r 1

class CreditTask(TaskSet):
    @task()
    def credit(self):
        f = Faker(locale='zh_CN')
        merchantID = "11111111"#f.numerify('#'*18)
        operatorMerchantID ="22222222"  #f.numerify('#'*18)
        comment = "".join(f.random_letters(length=10))
        creditAmount = f.random_int(min=100,max = 999)
        extID = "fffffffffffffff"#f.numerify('#'*18)
        header = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36"}
        body_merchant = {"merchantID":merchantID,"operatorMerchantID":operatorMerchantID}
        path_merchant = "/card/v1/merchants"
        r = self.client.post(url=path_merchant, name="创建商户",data=json.dumps(body_merchant),timeout=30, headers=header)
        path_account = "/card/v1/accounts"
        body_account = {"merchantID":merchantID,"subAccountList":[{"accountID":"28591572842163000","accountUniqueIdentifier":"505012201103153000","allowPay":False,"operatorMerchantID":operatorMerchantID,"subAccountType":"CREDIT"}]}
        r_account = self.client.post(url=path_account, name="创建账户",data=json.dumps(body_account),timeout=30, headers=header)
        assert r_account.status_code == 201,self.locust.share_data[0]#self.assert1()#json.dumps(body_account)
        datas = json.loads(r_account.text)
        # print(datas)
        for data in datas['data']:
            if data["subAccountType"] == "CREDIT":
                subAccountID_cash = data["subAccountID"]
        path_credit = "/card/v1/credits"
        body_credit = {"comment":comment,"creditAmount":creditAmount,"extID":extID,"merchantID":merchantID,"subAccountID":subAccountID_cash}
        resp_credit = self.client.post(url=path_credit, name="账户授信",data=json.dumps(body_credit),timeout=30, headers=header)
        assert resp_credit.status_code == 201
        # print(r_account.text)
        # account_cash = 
        # print(r_account)
    def assert1(self):
        with open("file.txt",'a') as f:
            f.write("This is test")
        return "This is test"

class websitUser(HttpLocust):
    host = "http://service-card.demo.g7pay.net"
    #每个hatch公用
    share_data = ['url1', 'url2', 'url3', 'url4', 'url5']
    #用户行为类
    task_set = CreditTask
    min_wait = 500  
    max_wait = 500 