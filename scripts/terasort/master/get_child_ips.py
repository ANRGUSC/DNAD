"""
 * Copyright (c) 2018, Autonomous Networks Research Group. All rights reserved.
 * Developed by:
 * Autonomous Networks Research Group (ANRG)
 * University of Southern California
 * http://anrg.usc.edu/
 *
 * Contributors:
 * Pranav Sakulkar, 
 * Pradipta Ghosh, 
 * Aleksandra Knezevic, 
 * Jiatong Wang, 
 * Quynh Nguyen, 
 * Jason Tran, 
 * H.V. Krishna Giri Narra, 
 * Zhifeng Lin, 
 * Songze Li, 
 * Ming Yu, 
 * Bhaskar Krishnamachari, 
 * Salman Avestimehr, 
 * Murali Annavaram
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy 
 * of this software and associated documentation files (the "Software"), to deal
 * with the Software without restriction, including without limitation the 
 * rights to use, copy, modify, merge, publish, distribute, sublicense, and/or 
 * sell copies of the Software, and to permit persons to whom the Software is 
 * furnished to do so, subject to the following conditions:
 * - Redistributions of source code must retain the above copyright notice, this
 *     list of conditions and the following disclaimers.
 * - Redistributions in binary form must reproduce the above copyright notice, 
 *     this list of conditions and the following disclaimers in the 
 *     documentation and/or other materials provided with the distribution.
 * - Neither the names of Autonomous Networks Research Group, nor University of 
 *     Southern California, nor the names of its contributors may be used to 
 *     endorse or promote products derived from this Software without specific 
 *     prior written permission.
 * - A citation to the Autonomous Networks Research Group must be included in 
 *     any publications benefiting from the use of the Software.
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR 
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE 
 * CONTRIBUTORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER 
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS WITH 
 * THE SOFTWARE.
 """

 import sys
import time
import json
import os

configs = json.load(open('/centralized_scheduler/dft_config/config.json'))

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
