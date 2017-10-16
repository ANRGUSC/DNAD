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
import time

def task(onefile, pathin, pathout):

    time.sleep(10)

    filelist=[]
    filelist.append(onefile)
    num=filelist[0].partition('s')[0]

    with open(os.path.join(pathout, num+'merged_file1.ipsum'),'w') as outfile:
        for filename in filelist:
            with open(os.path.join(pathin, filename), 'r') as infile:
                for line in infile:
                    outfile.write(line)


if __name__ == '__main__':

    filelist = '1split_1'
    #change the corresponding path
    task(filelist, '/home/pirate/apac_scheduler/centralized_scheduler_with_profiler/securityapp', '/home/pirate/apac_scheduler/centralized_scheduler_with_profiler/securityapp')
