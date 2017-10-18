# LOCAL_CHROME
from selenium import webdriver

__chrome = webdriver.Chrome
__firefox = webdriver.Firefox

DRIVER = {
    "type": __firefox
}

LOG = {
    "fommat": '%(asctime)s %(levelname)-8s %(filename)s[line:%(lineno)d] - %(message)s',
    "datefmt": '%Y-%m-%d %H:%M:%S',
    "console": {
        "level": "INFO"
    },
    "file": {
        "level": "DEBUG",
        "path": r"D:\project\code\capricornus\log\myapp.log"
    }
}

GECKO_DRIVER_LOG_PATH = r"D:\project\code\capricornus\log\geckodriver.log"

DEFAULT_FIND_ELEMENT_TIMEOUT = 3  # 默认查找元素超时时间
DEFAULT_PAGE_LOAD_TIMEOUT = 10  # 默认加载页面超时时间

if __name__ == '__main__':
    print(DRIVER["type"])
    print(LOG["fommat"])
    print(LOG["datefmt"])
    print(LOG["console"]["level"])
    print(LOG["file"]["level"])
    print(LOG["file"]["path"])