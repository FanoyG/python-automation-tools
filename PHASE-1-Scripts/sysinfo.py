import os
import platform
import getpass
import sys

def get_system_info():
    info = {
        "OS": platform.system(),
        "OS Version": platform.version(),
        "Hostname": platform.node(),
        "Processor": platform.processor(),
        "Python Version": sys.version,
        "Current User": getpass.getuser(),
        "Working Directory": os.getcwd(),
    }
    return info

if __name__ == "__main__":
    info = get_system_info()
    for key, value in info.items():
        print(key, ":", value)
