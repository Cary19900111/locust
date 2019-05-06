from locust import HttpLocust,TaskSet,task
import json
#locust -f test/test1.py --no-web --run-time 10s --csv ffff -c 5 -r 1

class CreditTask(TaskSet):
    @task()
    def credit(self):
        header = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36"}
        body_merchant = {"merchantID":"890211002726024","operatorMerchantID":"99671707381997705"}
        path_merchant = "/card/v1/merchants"
        r = self.client.post(url=path_merchant, data=json.dumps(body_merchant),timeout=30, headers=header)
        assert r.status_code == 201

class websitUser(HttpLocust):
    host = "http://service-card.demo.g7pay.net"
    #用户行为类
    task_set = CreditTask
    min_wait = 3000  
    max_wait = 6000 