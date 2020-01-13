import json

from bin import parse_url

from foo import ssr_properties, my_chrome_driver, subscribe_crawler, ssr_crawler, ss_crawler
from foo.ThreadCrawl import ThreadCrawl

if __name__ == '__main__':
    properties = ssr_properties.get_properties()
    configs = properties['configs']

    my_chrome_driver.run_chrome()
    to_test_list = []
    to_test_list.extend(subscribe_crawler.get_from_subscribe())
    to_test_list.extend(ssr_crawler.get_from_ssr_share())
    to_test_list.extend(ssr_crawler.get_from_lncn())
    to_test_list.extend(ssr_crawler.get_from_SSRSUB())
    to_test_list.extend(ss_crawler.query_from_free_ss())
    print('to_test_urls=', to_test_list)
    my_chrome_driver.close_chrome()

    while True:
        crawlList = [1, 2, 3, 4]
        # id的队列
        if ThreadCrawl.idQueue.empty():
            for i in crawlList:
                if to_test_list.__len__() > 0:
                    ThreadCrawl.idQueue.put(json.dumps(parse_url.ssr2json(to_test_list[-1])))
                    to_test_list.pop()
                elif configs.__len__() > 0:
                    ThreadCrawl.idQueue.put(json.dumps(configs[-1]))
                    configs.pop()

        # 　采集线程的数量

        # 存储采集线程的列表集合
        thread_crawl = []
        for threadName in crawlList:
            thread = ThreadCrawl(threadName)
            thread.start()
            thread_crawl.append(thread)

        for thread in thread_crawl:
            thread.join()
        if to_test_list.__len__() <= 0:
            break

    properties['configs'] = ThreadCrawl.configs
    print(ThreadCrawl.configs)
    ssr_properties.save_properties(properties)
