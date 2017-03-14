import csv
import os
import subprocess


strIPv6="IPv6"
with open('/usr/local/bin/dnscrypt-resolvers.csv', 'rb') as csvfile:
    #spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    spamreader = csv.reader(csvfile, dialect='excel')
    for row in spamreader:
        e6=row[1].find(strIPv6)
        if e6 is not -1:
            dns_ip_all = row[10]
            dns_name = row[0]
            dns_ip_start = dns_ip_all.index('[')
            dns_ip_end = dns_ip_all.index(']')
            dns_ip = dns_ip_all[dns_ip_start+1:dns_ip_end]

            cmd = r"ping6 -c 3 -W 1 " + dns_ip +r"  | grep loss | awk '{print $6}' "
            ps = subprocess.Popen(cmd, shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
            str_rsys = ps.communicate()[0]
            str_rsys = str_rsys[0:len(str_rsys)-1]
            
            if str_rsys == "0%":
                print "connect success "
                print dns_name
                os.popen("dnscrypt-proxy --daemonize --resolver-name=" + dns_name)
                break
            else:
                print dns_name , 'faled loss ',str_rsys
