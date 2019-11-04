# 导入locust类，成员

from locust import HttpLocust, TaskSet, task


# 任务类，必须继承TaskSet
class TestIndex(TaskSet):
    @task
    def getIndex(self):
        self.client.get("")


class WebSite(HttpLocust):
    task_set = TaskSet
    min_wait = 1000
    max_wait = 2000

