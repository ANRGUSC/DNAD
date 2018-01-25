"""
 * Copyright (c) 2017, Autonomous Networks Research Group. All rights reserved.
 *     contributors:
 *      Pradipta Ghosh, January 2018
 *      Pranav Sakulkar, October 2017
 *      Jiatong Wang, October 2017
 *      Aleksandra Knezevic, October 2017
 *      Bhaskar Krishnamachari, October 2017
 *     Read license file in main directory for more details  
"""


import os
import time
import json

all_nodes = os.environ["ALL_NODES"].split(":")
all_nodes_ips = os.environ["ALL_NODES_IPS"].split(":")
node_dict = dict(zip(all_nodes, all_nodes_ips))
# print(node_dict)
configs = json.load(open('/centralized_scheduler/config.json'))
tera_idx = configs['taskname_map'][os.environ['TASK']][2] 
ssh_port = configs['ssh_port']


def task(filename, pathin, pathout):
    num = filename.partition('m')[0]

    realMasterIP = node_dict['teramaster' + str(tera_idx)] #"10.244.9.145"

    # send the input file to the real master
    print("Send file")
    os.system("sshpass -p 'anrgapac' scp -o StrictHostKeyChecking=no "
              + "-P " + ssh_port + " " + 
              pathin + "/"+ filename + " root@" +
              realMasterIP + ":/root/TeraSort/Input/data.txt")

    time.sleep(10)
    # Execute uncoded TeraSort
    # For coded TeraSort, replace "uncoded" below by "coded"
    print("Run code")
    os.system("sshpass -p 'anrgapac' ssh -p" + ssh_port + " " +
      realMasterIP + " '/root/TeraSort/Master-Detection.sh uncoded'")

    # Download the results
    # For coded TeraSort, replace "result.txt" below by "result-C.txt"
    print("Download the result")
    while True:
        try:
            print("Downlao file")
            os.system("sshpass -p 'anrgapac' scp -o" +
                      " StrictHostKeyChecking=no " + "-P " + ssh_port 
                      + " root@" + realMasterIP +
                      ":/root/TeraSort/Output/result.txt " +
                      pathout + "/" + str(num) + "anomalies_tera" + str(tera_idx) + ".out")
            break
        except Exception as e:
            print("waiting for output")
            time.sleep(1)

    # Remove the results from real master
    # For coded TeraSort, replace "result.txt" below by "result-C.txt"
    print("Delete rermote files")
    os.system("sshpass -p 'anrgapac' ssh -p" + ssh_port + " -o StrictHostKeyChecking=no " + realMasterIP +
              " 'rm /root/TeraSort/Output/result.txt'")
    print("Finished")


if __name__ == '__main__':
    oneName = 'data.txt'
    pathin = './'
    pathout = './'
    task(oneName, pathin, pathout)
