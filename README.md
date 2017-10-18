# Network_Anomaly_Detection_CIRCE
Network Anomaly Detection application customized for CIRCE framework

# Network Anomaly Detection: Task Graph
The application task graph is inspired from Hashdoop [1, 2], where a MapReduce framework is used for anomaly detection. We have modified the codes from [2] to suit our purpose.

## Generating the input files
Convert the pcap file to a text file using [Ipsumdump](http://www.read.seas.harvard.edu/~kohler/ipsumdump/) as follows:

```
ipsumdump -tsSdDlpF -r botnet-capture-20110810-neris.pcap > botnet_summary.ipsum
```

## Code Structure
- `local_pro.py`: Process the Ipsum file locally and split the traffic into multiple independent streams based on the hash value of the IP adresses.
- `aggregate<SPLIT_ID>.py`: SPLIT_ID (0, 1 or 2, in our case) uniquely idenfifies the split. This script aggregates traffic for a particular traffic split from different monitoring nodes.
- `simple_detector<SPLIT_ID>.py`: A simple threshold based anomaly detector for the particular split.
- `astute_detector<SPLIT_ID>.py`: An implementation of ASTUTE anomaly detector [3] from the repository [2].
- `fusion_center<SPLIT_ID>.py`: Combine the detected anomalies by different detectors for the particular split.
- `global_fusion.py`: Collect all the anomalies from different splits and combine the detected anomalies.

# References
[1] Romain Fontugne, Johan Mazel, and Kensuke Fukuda. "Hashdoop: A mapreduce framework for network anomaly detection." Computer Communications Workshops (INFOCOM WORKSHOPS), IEEE Conference on. IEEE, 2014.

[2] [Hashdoop GitHub Repository](https://github.com/necoma/hashdoop "Hashdoop Repository")

[3] Fernando Silveira, Christophe Diot, Nina Taft, and Ramesh Govindan. "ASTUTE: Detecting a different class of traffic anomalies." ACM SIGCOMM Computer Communication Review 40.4 (2010): 267-278.

# Acknowledgement
This material is based upon work supported by Defense Advanced Research Projects Agency (DARPA) under Contract No. HR001117C0053. Any views, opinions, and/or findings expressed are those of the author(s) and should not be interpreted as representing the official views or policies of the Department of Defense or the U.S. Government.