#!/usr/bin/python3

import subprocess
import sys
import time

runtime  = int(sys.argv[1])
interval = int(sys.argv[2])
div = "--------------------"
print("Getrl")
print(div)

dp_cpu_stats = open("dp_cpu_stats.txt", "a")
dp_mem_stats = open("dp_mem_stats.txt", "a")
physical_port_stats = open("physical_port_stats", "a")
tunnel_port_stats = open("tunnel_port_stats", "a")

while runtime != 0:
    time.localtime()
    get_dp_cpu_stats=['su', 'admin', '-c', 'get dataplane cpu stats']
    get_mem_stats=['su', 'admin', '-c', 'get dataplane memory stats']
    subprocess.run(get_dp_cpu_stats, stdout=dp_cpu_stats)
    subprocess.run(get_mem_stats, stdout=dp_mem_stats)
    runtime -=  1
    print(div)
    time.sleep(interval)