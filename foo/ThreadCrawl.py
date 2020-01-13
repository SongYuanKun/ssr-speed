import json
import threading
from queue import Queue

from foo import my_speed_test


class ThreadCrawl(threading.Thread):
    configs = []
    idQueue = Queue(20)

    def __init__(self, thread_name):
        # 继承父类的方法
        super(ThreadCrawl, self).__init__()
        self.threadName = thread_name  # 线程名字

    def run(self):
        print('启动' + str(self.threadName))
        while not self.idQueue.empty():
            try:
                config = self.idQueue.get(False)  # False 如果队列为空，抛出异常
                result = my_speed_test.test_ssr(json.loads(config), self.threadName)
                if result:
                    self.configs.append(json.loads(config))

            except Exception as e:
                print(e)
                pass
            print('#' * 200)
