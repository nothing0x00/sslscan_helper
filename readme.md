## SSLScan-Helper

sslscan_helper.py is a simple Python script to allow for the use of sslscan with a list of hosts as input (these can be listed in a text file either as fully formatted URLs or simply as a list if IPs and the corresponding ports).

Due to issues with ushlex in Python 3 the script is still in Python 2.7. The next upgrade will solve this issue, update to Python 3 and fix some of the parsing issues to make the output more easily readable without post-processing.

The script can be launched with the following command:

`python sslscan_helper.py`

When launched the script will prompt for a name for the output folder and the location of the list.

Once these prompts are completed the script will scan each host on the list, then parse the resulting output files and organize the output into vulnerability finding lists, grouping hosts by vulnerability, and print this to the screen for processing and reporting.

### Installation

The script requires the rbsec rewrite of sslscan (https://github.com/rbsec/sslscan), rather than the older Titania developed version.
This version is installed through apt on Ubuntu 18.04, Kali and others. Check your apt packages for the version included in the package repo.
If the older version is included in the repo then it is possible to custom compile the rbsec version of sslscan and modify the script to run with this custom compiled version.
Eventually, I will add a version of the script into this repo which will install the tools and run the script with this compiled version.  

To get the script up and running do the following:

`sudo apt install sslscan`

`pip install ushlex`

`git clone https://github.com/nothing0x00/sslscan_helper.git`

`cd sslscan_helper`

`mkdir output`

`python sslscan_helper.py`
