import os
import time

def apply(data):
    res = {}
    if data:
        os.system("bash /root/MRongM/update.sh")
        res["msg"]="ok"
    return res

