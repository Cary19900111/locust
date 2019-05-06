from locust import HttpLocust, TaskSet, task
import hashlib



    

class rechargeRevoke(TaskSet):
    @task()
    def test_revoke(self):
        header = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36"}
        bodyString = "{\"orgcode\":\"12332123321\",\"merchantID\":\"1100751513682288643\",\"SubAccountList\":[{\"subAccountType\":\"CASH\",\"accountNameRelatedID\":\"1100751515313876994\"}]}"
        signString = signString(bodyString)
        path = "/cashdesk-truck-broker/v0/subAccounts?sign="+signString+"&randString=aaaaaa"
        r = self.client.get(path, timeout=30, headers=header)
        assert r.status_code == 200
    
    def signString(bodyString):
        md = hashlib.md5()
        md.update(bodyString.encode())
        signString = "randString=aaaaaa&body="+md.hexdigest()+"&secret=0631539c-d98e-4515-bfd7-4945abd7d06d-2bf62478-8d3f-4cd0-908d-7dc404317209"
        md_sign = hashlib.md5()
        md_sign.update(signString.encode())
        return md_sign.hexdigest()


class websiteUser(HttpLocust):
    task_set = rechargeRevoke
