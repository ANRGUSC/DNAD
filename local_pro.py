"""
 * Copyright (c) 2017, Autonomous Networks Research Group. All rights reserved.
 *     contributors: 
 *      Pranak Sakulkar, October 2017
 *      Jiatong Wang, October 2017
 *      Aleksandra Knezevic, October 2017
 *      Bhaskar Krishnamachari, October 2017
 *     Read license file in main directory for more details  
"""


import zlib
import os
import time
import sys

def task(onefile, pathin, pathout):

    filelist=[]
    filelist.append(onefile)
    num = filelist[0].partition('b')[0]

    time.sleep(10)
    num_agg_points = 3
    hash_seed = 14635
    files_dict = dict()
    for idx in range(num_agg_points):
        files_dict[idx] = []

    for filename in filelist:
        with open(os.path.join(pathin, filename), 'r') as f:
            # input comes from STDIN (standard input)
            for line in f:
                # ignore header
                if line.startswith('!'):
                    continue

                # get each fields of the tuple
                part = line.partition(" ")
                ts = part[0]
                pkt = part[2]
                fields = pkt.split()

                # Sketch once using IP src and once using IP dst
                for pass_number, field_index in enumerate([0, 2]):
                    ip = fields[field_index]
                    #hash_value = zlib.crc32(ip, hash_seed)
                    hash_value = zlib.crc32(ip.encode('utf-8'), hash_seed)
                    sketch_index = hash_value % num_agg_points
                    assert sketch_index <= num_agg_points

                    line = ts + '\t' + pkt
                    files_dict[sketch_index].append(line)


    for idx in range(num_agg_points):
        with open(os.path.join(pathout,num+'split_' + str(idx)), 'w') as f:
            for item in files_dict[idx]:
                f.write("%s" % item)

if __name__ == '__main__':

    filelist= '1botnet.ipsum'
    #change the corresponding path
    task(filelist, '/home/pirate/apac_scheduler/centralized_scheduler_with_profiler/securityapp', '/home/pirate/apac_scheduler/centralized_scheduler_with_profiler/securityapp')

