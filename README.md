# Sites Monitoring Utility

The script receives a list of URLs from text file and checks them up for 2 points: 
1) the server responds for request by status 200
2) domain name is paid for a month or longer

# Quickstart

Example of script launch on Linux, Python 3.5:

```bash

$ python3 check_sites_health.py <filename>
```
where <filename> is the file with URLs list for testing.

Note, the script needs additional python modules to work. It would be installed by command:

```bash

$ pip3 install -r requirements.txt
```

# Output example

```
$ python3 check_sites_health.py url_list

https://pythonworld.ru:
 request HTTP 200: True,
 Domain Name paid for 1 month and more: True

https://habrahabr.ru:
 request HTTP 200: True,
 Domain Name paid for 1 month and more: True

http://naturaliste.ru:
 request HTTP 200: True,
 Domain Name paid for 1 month and more: True
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
