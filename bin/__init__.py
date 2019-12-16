import threading
from queue import Queue

from bin import ssr_properties, my_speed_test, parse_url, ssr_crawler, my_chrome_driver, subscribe_crawler
from bin.retest_configs import retest_configs


def fun1(num):
    for ssr_url in to_test_list:
        try:
            config = parse_url.ssr2json(ssr_url)
            have_this = 0
            result = my_speed_test.test_ssr(config, num)
            if result:
                for x in configs:
                    if x['server'] == config['server']:
                        have_this = 1
                if have_this == 0:
                    configs.append(config)
        except Exception as e:
            print(e)
            print(ssr_url)
            continue


class ThreadCrawl(threading.Thread):
    def __init__(self, thread_name, idQueue):
        # 继承父类的方法
        super(ThreadCrawl, self).__init__()
        self.threadName = thread_name  # 线程名字

    def run(self):
        print('启动' + str(self.threadName))
        while not idQueue.empty():
            try:
                url = idQueue.get(False)  # False 如果队列为空，抛出异常
                self.get_con(url)

            except Exception as e:
                print('队列为空。。。。。', e)
                pass
            print('#' * 300)

    def get_con(self, ssr_url):  # 自己封装的请求自定义
        try:
            config = parse_url.ssr2json(ssr_url)
            have_this = 0
            result = my_speed_test.test_ssr(config, self.threadName)
            if result:
                for x in configs:
                    if x['server'] == config['server']:
                        have_this = 1
                if have_this == 0:
                    configs.append(config)
        except Exception as e:
            print(e)
            print(ssr_url)


if __name__ == '__main__':
    my_chrome_driver.run_chrome()
    to_test_list = []
    to_test_list.extend(subscribe_crawler.get_from_subscribe())
    # to_test_list.extend(ssr_crawler.get_from_ssr_share())
    # to_test_list.extend(ssr_crawler.get_from_lncn())
    # to_test_list.extend(ssr_crawler.get_from_SSRSUB())
    # to_test_list.extend(ssr_crawler.get_from_youneed1())
    # to_test_list.extend(ssr_crawler.get_from_youneed2())
    print('to_test_urls=', to_test_list)
    my_chrome_driver.close_chrome()

    properties = ssr_properties.get_properties()
    configs = properties['configs']

    while True:
        crawlList = [1, 2, 3, 4]
        # id的队列
        idQueue = Queue(20)
        if idQueue.empty() and to_test_list.__len__() > 0:
            for i in crawlList:
                idQueue.put(to_test_list[-1])
                to_test_list.pop()

        # 　采集线程的数量

        # 存储采集线程的列表集合
        thread_crawl = []
        for threadName in crawlList:
            thread = ThreadCrawl(threadName, idQueue)
            thread.start()
            thread_crawl.append(thread)

        for thread in thread_crawl:
            thread.join()
        if to_test_list.__len__() <= 0:
            break

    properties['configs'] = configs
    print(configs)
    ssr_properties.save_properties(properties)

    # retest_configs()
