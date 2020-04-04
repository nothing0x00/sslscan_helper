## SSLScan-Helper

sslscan_helper.py is a simple Python script to allow for the use of sslscan with a list of hosts as input (these can be listed in a text file either as fully formatted URLs or simply as a list if IPs and the corresponding ports).

Due to issues with ushlex in Python 3 the script is still in Python 2.7. The next upgrade will solve this issue, update to Python 3 and fix some of the parsing issues to make the output more easily readable without post-processing.

The script can be launched with the following command:

`python sslscan_helper.py`

When launched the script will prompt for a name for the output folder and the location of the list.

Once these prompts are completed the script will scan each host on the list, then parse the resulting output files and organize the output into vulnerability finding lists, grouping hosts by vulnerability, and print this to the screen for processing and reporting.

### Installation

To get the script up and running do the following:

`sudo apt install sslscan`

`pip install ushlex`

`git clone https://github.com/nothing0x00/sslscan_helper.git`

`cd sslscan_helper`

`mkdir output`

`python sslscan_helper.py`
