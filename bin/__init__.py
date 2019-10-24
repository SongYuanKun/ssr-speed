from bin import ss_crawler, ssr_properties, my_speed_test, parse_url, ssr_crawler, subscribe_crawler

if __name__ == '__main__':
    to_test_list = []
    # to_test_list.extend(subscribe_crawler.get_from_subscribe())
    to_test_list.extend(ssr_crawler.get_from_ssr_share())
    # to_test_list.extend(ss_crawler.query_from_free_ss())
    to_test_list.extend(ssr_crawler.get_from_youneed1())
    to_test_list.extend(ssr_crawler.get_from_youneed2())
    print('to_test_urls=', to_test_list)

    properties = ssr_properties.get_properties()
    configs = properties['configs']
    for ssr_url in to_test_list:
        config = parse_url.ssr2json(ssr_url)
        have_this = 0
        for x in configs:
            if x['server'] == config['server']:
                have_this = 1
        if have_this == 0 and my_speed_test.test_ssr(config):
            configs.append(config)
    print(my_speed_test.table.str())
    ssr_properties.save_properties(properties)

    # retest_configs()
