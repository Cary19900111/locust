from locust import Locust,TaskSet,task
import json
#locust -f testcc/simple.py --no-web --run-time 5s --show-task-ratio -c 1 -r 1

class ShoutTask(TaskSet):
    @task()
    def LilyShout(self):
        print("Lily Shout")
    @task()
    def CaryShout(self):
        print("Cary Shout")

class DonwTask(TaskSet):
    @task()
    def LilyDonw(self):
        print("Lily Down")
    @task()
    def CaryDonw(self):
        print("Cary Down")
class websitUser(Locust):
    host = "http://service-card.demo.g7pay.net"
    #用户行为类
    task_set = ShoutTask
    min_wait = 1000  
    max_wait = 1000 