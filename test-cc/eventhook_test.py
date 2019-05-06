from locust import Locust, TaskSet, events, task

mars_event = events.EventHook()

def mars_special_event(verb = '', content = ''):
    print("mars {} {}".format(verb,content))

mars_event += mars_special_event

class UserTask(TaskSet):
    def on_stop(self):
        print("stop the Usertask!")
    @task(1)
    def job1(self):
        mars_event.fire(verb = 'love', content = 'locust')

    @task(3)
    def job2(self):
        print("In job2")

class User(Locust):
    task_set = UserTask
    min_wait = 1000
    max_wait = 3000
    stop_timeout = 10000

