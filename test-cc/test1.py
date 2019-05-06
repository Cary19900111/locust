from locust import HttpLocust, TaskSet, task

#http://service-cif.demo.g7pay.net

class test_126(TaskSet):
    @task()
    def test_password(self):
        header = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36"}
        r = self.client.get("/cif/v0/account/1022681076096614402/password/PAY", timeout=30, headers=header)
        print(r)
        assert r.status_code == 200


class websitUser(HttpLocust):
    host = "http://172.16.1.111"
    # 指向一个上面定义的用户行为类
    task_set = test_126
    # 执行事物之间用户等待时间的下界，单位毫秒，相当于lr中的think time
    min_wait = 1000
    max_wait = 1000

def test():
    from faker import Faker
    f=Faker(locale='zh_CN')
    g = f.ssn()
    print(g)
if __name__=="__main__":
    test()