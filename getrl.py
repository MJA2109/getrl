#!/usr/bin/python3

import subprocess
import sys
import time

sec  = int(sys.argv[1])
div = "--------------------"
print("Getrl")
print(div)

while sec != 0:
    time.localtime()
    subprocess.run(['su', 'admin', '-c', 'get dataplane cpu stats'])
    sec -=  1
    print(div)
    time.sleep(1)