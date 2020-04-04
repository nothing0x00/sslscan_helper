import subprocess
import ushlex as shlex
import os


print '''


 _____ _____ __    _____                _____     _
|   __|   __|  |  |   __|___ ___ ___   |  |  |___| |___ ___ ___
|__   |__   |  |__|__   |  _| .'|   |  |     | -_| | . | -_|  _|
|_____|_____|_____|_____|___|__,|_|_|  |__|__|___|_|  _|___|_|
                                                   |_|
'''
print "A hacky Python script to automate sslscan testing"
print "\n"
print "Make sure output directory has been created..."
print "Press Enter if directory exists and CTRL-C to exit if not"
stop = raw_input("")
print("\n")

engagement = raw_input("Name of client/target: ")
file = raw_input("Specify target file: ")

directory_create = "mkdir output/{}".format(engagement)
dir_args = shlex.split(directory_create)
subprocess.call(dir_args)
r = open(file, "r")

print "\n"
print "-" * 20
print "[*] Tests Initiated"
print "-" * 20
print "\n"

for host in r:
    print "[*] Scanning {}".format(host)
    host_name = host.replace("://", "_")
    filename = "output/{}/{}".format(engagement, host_name)
    fname = filename.strip("\n")
    #print fname
    f = open(fname, "w")
    command = "sslscan " + host
    args = shlex.split(command)
    subprocess.call(args, stdout=f)

print "\n"
print "-" * 20
print "[*] Tests Completed! Parsing Results!"
print "-" * 20
print "\n"
print "-" * 20
print "\n"
print "[*] TLS SCSV Mode Unsupported"
print "\n"
scsv_cmd = "grep 'does not' output/{}/* | grep 'SCSV'".format(engagement)
os.system(scsv_cmd)
print "\n"

print "-" * 20
print "\n"
print "[*] TLSv1.0 Enabled"
print "\n"
tls1_cmd = "grep 'TLSv1.0' output/{}/*".format(engagement)
os.system(tls1_cmd)
print "\n"

print "-" * 20
print "\n"
print "[*] 3DES CBC"
print "\n"
des_cmd = "grep 'CBC3' output/{}/*".format(engagement)
os.system(des_cmd)
print "\n"

print "-" * 20
print "\n"
print "[*] Weak Hashing Algorithms"
print "\n"
sha_cmd = "grep 'sha1WithRSAEncryption' output/{}/*".format(engagement)
os.system(sha_cmd)
print "\n"

print "-" * 20
print "\n"
print "[*] RC4"
print "\n"
rc4_cmd = "grep 'RC4' output/{}/*".format(engagement)
os.system(rc4_cmd)
print "\n"

print "-" * 20
print "\n"
print "[*]T DHE-1024/Logjam"
print "\n"
dhe_cmd = "grep '512\|1024' output/{}/* | grep 'DHE'".format(engagement)
os.system(dhe_cmd)
print "\n"

print "-" * 20
print "\n"
print "[*] SSLv2/SSLv3"
print "\n"
ssl_cmd = "grep 'SSLv2\|SSLv3' output/{}/*".format(engagement)
os.system(ssl_cmd)
print "\n"

print "-" * 20
print "\n"
print "[*] Self-Signed Certificates"
print "\n"
ssc_cmd = "grep 'Issuer' output/{}/* | grep '\[31m'".format(engagement)
os.system(ssc_cmd)
print "\n"

print "-" * 20
print "\n"
print "[*] Expired Certificates"
print "\n"
scsv_cmd = "grep 'Not valid after' output/{}/* | grep '\[31m'".format(engagement)
os.system(scsv_cmd)
print "\n"
