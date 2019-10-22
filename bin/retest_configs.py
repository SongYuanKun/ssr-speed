from bin import get_ssr_properties, my_speed_test


def retest_configs():
    properties = get_ssr_properties.get_properties()
    configs = properties['configs']
    for config in configs:
        if my_speed_test.test_ssr(config):
            configs.remove(config)

    get_ssr_properties.save_properties(properties)
