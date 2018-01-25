import sys
import time
import json
import os

configs = json.load(open('/centralized_scheduler/config.json'))

master_id = configs['taskname_map'][os.environ['TASK']][2]
max_num_child = configs['nos_tera_slave']
task = os.environ['TASK']

all_nodes = os.environ["ALL_NODES"].split(":")
all_nodes_ips = os.environ["ALL_NODES_IPS"].split(":")
node_dict = dict(zip(all_nodes, all_nodes_ips))
print(node_dict)
fobj = open("ips.txt", 'w')

for i in range(max_num_child):
    key = "teraslave" + str(master_id) + str(i)
    if key in node_dict:
        fobj.write(node_dict[key]+'\n')
    print(key)
fobj.close()
