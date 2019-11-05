from bin import ss_crawler, ssr_properties, my_speed_test, parse_url, ssr_crawler, subscribe_crawler, my_chrome_driver
from bin.retest_configs import retest_configs

if __name__ == '__main__':
    my_chrome_driver.run_chrome()
    to_test_list = []
    # to_test_list.extend(subscribe_crawler.get_from_subscribe())
    to_test_list.extend(ssr_crawler.get_from_ssr_share())
    # to_test_list.extend(ssr_crawler.get_from_SSRSUB())
    to_test_list.extend(ssr_crawler.get_from_youneed1())
    to_test_list.extend(ssr_crawler.get_from_youneed2())
    print('to_test_urls=', to_test_list)
    my_chrome_driver.close_chrome()

    properties = ssr_properties.get_properties()
    configs = properties['configs']
    for ssr_url in to_test_list:
        try:
            config = parse_url.ssr2json(ssr_url)
        except ImportError:
            continue
        have_this = 0
        for x in configs:
            if x['server'] == config['server']:
                have_this = 1
        if have_this == 0 and my_speed_test.test_ssr(config):
            configs.append(config)
    print(my_speed_test.table.str())
    ssr_properties.save_properties(properties)

    retest_configs()
