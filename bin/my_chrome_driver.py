import subprocess

chrome_driver_path = "../win/chromedriver.exe"


# 运行 chrome
def run_chrome():
    subprocess.Popen(chrome_driver_path)


# 关闭chrome
def close_chrome():
    subprocess.call('taskkill /f /im chromedriver.exe', stdout=subprocess.PIPE)
