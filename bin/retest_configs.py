from bin import ssr_properties, my_speed_test


def retest_configs():
    properties = ssr_properties.get_properties()
    configs = properties['configs']
    for config in configs:
        if my_speed_test.test_ssr(config) != 'Success':
            configs.remove(config)
    print(my_speed_test.table)
    ssr_properties.save_properties(properties)
