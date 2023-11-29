#!/usr/bin/python3

import subprocess
import sys
import time

runtime  = int(sys.argv[1])
interval = int(sys.argv[2])
div = "--------------------"
delimit="---"

dp_stats=[]
dp_core_stats=[]
dp_core_stat={}

dp_cpu_stats = open("dp_cpu_stats.txt", "a")
get_dp_cpu_stats=['su', 'admin', '-c', 'get dataplane cpu stats']
append_delimit=['echo', delimit]
print("Getrl")
print(div)

while runtime != 0:
    time.localtime()
    print("Dumping DP CPU usage stats...")
    subprocess.run(get_dp_cpu_stats, stdout=dp_cpu_stats)
    subprocess.run(append_delimit, stdout=dp_cpu_stats)
    runtime -=  1
    print(div)
    time.sleep(interval)

with open('dp_cpu_stats.txt') as dp_cpu_stats:
    for line in dp_cpu_stats:
        if 'CPU Usage' not in line:
            if line.strip() and delimit not in line:
                key, val  = line.strip().split(':')
                dp_core_stat[key.strip()] = val.strip()
            elif not line.strip():
                dp_core_stats.append(dp_core_stat.copy())
                dp_core_stat.clear()

            if delimit in line:
                dp_stats.append(dp_core_stats.copy())
                dp_core_stats.clear()
    print(dp_stats)
    print('No. of entries,', len(dp_stats))
