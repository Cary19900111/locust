from locust import HttpLocust,TaskSet,task
from faker import Faker
import json
#locust -f test/test1.py --no-web --run-time 10s --csv ffff -c 5 -r 1

class CreditTask(TaskSet):
    @task()
    def credit(self):
        f = Faker(locale='zh_CN')
        merchantID = f.numerify('#'*18)
        operatorMerchantID =  f.numerify('#'*18)
        header = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36"}
        body_merchant = {"merchantID":merchantID,"operatorMerchantID":operatorMerchantID}
        path_merchant = "/card/v1/merchants"
        r = self.client.post(url=path_merchant, name="创建商户",data=json.dumps(body_merchant),timeout=30, headers=header)
        path_account = "/card/v1/accounts"
        body_account = {"merchantID":merchantID,"subAccountList":[{"accountID":"28591572842163000","accountUniqueIdentifier":"505012201103153000","allowPay":False,"operatorMerchantID":operatorMerchantID,"subAccountType":"CREDIT"}]}
        r_account = self.client.post(url=path_account, name="创建账户",data=json.dumps(body_account),timeout=30, headers=header)
        assert r_account.status_code == 201
        datas = json.loads(r_account.text)
        print(datas)
        for data in datas['data']:
            if data["subAccountType"] == "CREDIT":
                print(data["subAccountID"])
        # print(r_account.text)
        # account_cash = 
        # print(r_account)


class websitUser(HttpLocust):
    host = "http://service-card.demo.g7pay.net"
    #用户行为类
    task_set = CreditTask
    min_wait = 3000  
    max_wait = 6000 