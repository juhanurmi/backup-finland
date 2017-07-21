Suomen varmuuskopio
===================

Suomen IP-avaruus ja Suomessa olevat domainit.

Download files
--------------

```sh
$ wget http://www.ipdeny.com/ipblocks/data/countries/fi.zone
$ wget https://scans.io/data/rapid7/sonar.fdns_v2/20170714-fdns.json.gz
$ sha1sum 20170714-fdns.json.gz
```

Simplify, simplify, simplify
----------------------------

```sh
$ time zcat 20170714-fdns.json.gz | cut -d'"' -f 8,16 | sed 's/\"/ /g' > 20170714_dns.txt
$ python3 print_every_ip.py > 2017-07-18_fi_every_ip.txt
$ cat fi.zone | cut -d"." -f1,2 | sed 's/\.//g' > short_ip_filter.txt
# Run 2 times:
$ python3 split_dns_file.py
$ python3 split_dns_file.py
```

Use masscan script to scan port 80/TCP in Finland
-------------------------------------------------

- Install https://github.com/robertdavidgraham/masscan

```sh
$ sudo scan_80_finland.sh > results.log
$ tail results.log | cut -d" " -f 6 > 80_results_ip_only.log
$ bash get_only_fi.sh > 80_fi_domains_ips.log
```
