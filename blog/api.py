import os
import time

def apply(data):
	res = {}

	if data:
		os.system("bash /root/MRongM/tools.sh s")
		time.sleep(1)
		os.system("ps -ef|grep python3")
		os.system("bash /root/MRongM/tools.sh r")
		time.sleep(1)
		os.system("ps -ef|grep python3")
		res["msg"]="ok"		
	return res
