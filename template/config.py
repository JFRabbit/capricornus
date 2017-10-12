# LOCAL_CHROME  REMOTE_CHROME LOCAL_FIREFOX

DRIVER = {
    "type": "LOCAL_CHROME"
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

DEFAULT_FIND_ELEMENT_TIMEOUT = 3  # 默认查找元素超时时间
DEFAULT_PAGE_LOAD_TIMEOUT = 10  # 默认加载页面超时时间

if __name__ == '__main__':
    print(DRIVER["type"])
    print(LOG["fommat"])
    print(LOG["datefmt"])
    print(LOG["console"]["level"])
    print(LOG["file"]["level"])
    print(LOG["file"]["path"])