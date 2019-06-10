from locust import HttpLocust,TaskSet,task
#locust -f testcc/g7.py --no-web --run-time 10s --csv result -c 5 -r 1
from locust import events
import datetime 


'''写的钩子函数'''
# from locust import Locust, TaskSet, events, task

# mars_event = events.EventHook()

# def mars_special_event(verb = '', content = ''):
#     print("mars {} {}".format(verb,content))

# mars_event += mars_special_event

# class UserTask(TaskSet):
#     def on_stop(self):
#         print("stop the Usertask!")
#     @task(1)
#     def job1(self):
#         mars_event.fire(verb = 'love', content = 'locust')

#     @task(3)
#     def job2(self):
#         print("In job2")

# class User(Locust):
#     task_set = UserTask
#     min_wait = 1000
#     max_wait = 3000
#     stop_timeout = 10000
'''设置集合点Semaphore'''
# from gevent._semaphore import Semaphore
# all_locusts_spawned = Semaphore()
# all_locusts_spawned.acquire()
# all_locusts_spawned.wait()#放在要集合的地方

# def on_hatch_complete(**kwargs):
#     all_locusts_spawned.release()


# def request_success_hook(request_type, name, response_time, response_length):
#     with open ("result.txt",'a+') as f:
#         now_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
#         msg = "{}  {}  {}  {}  {}  {}\n".format(now_time,"SUCCESS",request_type,name,response_time,response_length)
#         f.write(msg)
# def request_failure_hook(request_type, name, response_time, exception):
#     with open ("result.txt",'a+') as f:
#         now_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
#         msg = "{}  {}  {}  {}  {}  {}\n".format(now_time,"FAIL",request_type,name,response_time,exception)
#         f.write(msg)
# events.request_success+=request_success_hook
# events.request_failure+=request_failure_hook
class TestPerform(TaskSet):
    @task
    def smoke(self):
        response = self.client.get(url="/perform",name="测试",catch_response=True)
        # if response.status_code=="200":
        response.failure('!=201')
class WebUser(HttpLocust):
    # task_set = [ShoutTask,DonwTask]
    host = "http://127.0.0.1:8000"
    task_set = TestPerform
    # stop_timeout=60