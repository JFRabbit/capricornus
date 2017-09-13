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
        "path": "../log/myapp.log"
    }
}

if __name__ == '__main__':
    print(DRIVER["type"])
    print(LOG["fommat"])
    print(LOG["datefmt"])
    print(LOG["console"]["level"])
    print(LOG["file"]["level"])
    print(LOG["file"]["path"])