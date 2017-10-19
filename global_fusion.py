"""
 * Copyright (c) 2017, Autonomous Networks Research Group. All rights reserved.
 *     contributors: 
 *      Pranak Sakulkar, October 2017
 *      Jiatong Wang, October 2017
 *      Aleksandra Knezevic, October 2017
 *      Bhaskar Krishnamachari, October 2017
 *     Read license file in main directory for more details  
"""

import os
import sys

def task(filelist, pathin, pathout):
 
    num = filelist[0].partition('f')[0]

    with open(os.path.join(pathout, num+'global_anomalies.log'), 'w') as outfile:
        for fname in filelist:
            with open(os.path.join(pathin,fname), 'r') as infile:
                for line in infile:
                    ano = line.split(";")
                    flow = ano[0]
                    ts = ano[1]
                    te = ano[2]
                    srcDst = flow.split()
                    srcIP, srcPort = srcDst[0].split(":")
                    dstIP, dstPort = srcDst[1].split(":")
                    ts = ts.split(".")
                    tsSec = int(ts[0])
                    tsUsec = int(ts[1])
                    te = te.split(".")
                    teSec = int(te[0])
                    teUsec = int(te[1])
                    str1 = ('{0};{1};{2}'.format(flow, tsSec, teSec))
                    #print(str1)
                    outfile.write(str1 + '\n')

if __name__ == '__main__':

    filelist = ['1fusion_center0.log', '1fusion_center1.log', '1fusion_center2.log']
    #change the corresponding path
    task(filelist, '/home/pirate/apac_scheduler/centralized_scheduler_with_profiler/securityapp', '/home/pirate/apac_scheduler/centralized_scheduler_with_profiler/securityapp')
