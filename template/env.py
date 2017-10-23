# coding: utf-8
from enum import Enum

__QA_55 = "http://192.168.130.55"
__QA_83 = "http://192.168.130.83"
__QA_IDC = "http://192.168.200.22"
__RD_102 = "http://192.168.130.102"
__RD_103 = "http://192.168.130.103"

# ==================================================
# 当前测试Server环境
# ==================================================
current_root = __QA_83


# ==================================================
# 测试模块枚举
# ==================================================
class TestModuleEnum(Enum):
    PAS = ":5003/projects/"
    CONSOLE = ":5002/"


def get_current_env(module: TestModuleEnum):
    return current_root + module.value


if __name__ == "__main__":
    print(get_current_env(TestModuleEnum.PAS))
    print(get_current_env(TestModuleEnum.CONSOLE))
