# Boot2Root

## Obtaining IP address of the virtual machine, and it's open ports

First, we need to find what our `Bridged Adaptor` name is.

![VirtualBox](assets/VirtualBox.png)

Here, it's `wlp2s0`

Now we would like to know the ip address of this interface:

```sh
ip a | grep -A 2 wlp2s0:
2: wlp2s0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default qlen 1000
    link/ether 14:4f:8a:04:eb:5b brd ff:ff:ff:ff:ff:ff
    inet 192.168.1.40/24 brd 192.168.1.255 scope global dynamic noprefixroute wlp2s0
```

With this information between our hands, we will get the IP adresses behind this interface :

```sh
nmap -sn 192.168.1.40/24              
Starting Nmap 7.91 ( https://nmap.org ) at 2020-12-29 11:38 CET
...
Nmap scan report for 192.168.1.7
Host is up (0.0013s latency).
...
```

A couple of adresses show up, but only one is missing when the VM is shutdown. We will use it.

```sh
nmap 192.168.1.7                
Starting Nmap 7.91 ( https://nmap.org ) at 2020-12-29 11:40 CET
Nmap scan report for 192.168.1.7
Host is up (0.00018s latency).
Not shown: 994 closed ports
PORT    STATE SERVICE
21/tcp  open  ftp
22/tcp  open  ssh
80/tcp  open  http
143/tcp open  imap
443/tcp open  https
993/tcp open  imaps

Nmap done: 1 IP address (1 host up) scanned in 0.17 seconds
```

## Discovering the website tree structure

It exist an automated tool for `web path scanner` : [Dirsearch](https://github.com/maurosoria/dirsearch)

Let's make a search for http: (I will format output to only keep the interesting ones, aka removing responses 403)

```sh
python3 dirsearch.py -u http://192.168.1.7/

  _|. _ _  _  _  _ _|_    v0.4.1
 (_||| _) (/_(_|| (_| )

Extensions: php, asp, aspx, jsp, html, htm, js | HTTP method: GET | Threads: 30 | Wordlist size: 11793

Target: http://192.168.1.7/

[12:18:10] Starting:
[12:19:54] 301 -  310B  - /fonts  ->  http://192.168.1.7/fonts/
[12:20:02] 200 -    1KB - /index.html

Task Completed
```

Let's do the same thing for https:

```sh
python3 dirsearch.py -u https://192.168.1.7/

  _|. _ _  _  _  _ _|_    v0.4.1
 (_||| _) (/_(_|| (_| )

Extensions: php, asp, aspx, jsp, html, htm, js | HTTP method: GET | Threads: 30 | Wordlist size: 11793

Target: https://192.168.1.7/

[12:23:26] Starting:
[12:24:38] 301 -  312B  - /forum  ->  https://192.168.1.7/forum/
[12:24:38] 200 -    5KB - /forum/
[12:25:02] 301 -  317B  - /phpmyadmin  ->  https://192.168.1.7/phpmyadmin/
[12:25:03] 200 -    7KB - /phpmyadmin/
[12:25:03] 200 -    7KB - /phpmyadmin/index.php
[12:25:30] 403 -  306B  - /webmail/src/configtest.php
[12:25:30] 302 -    0B  - /webmail/  ->  src/login.php
```

## Exploring [https://192.168.1.7/forum/](https://192.168.1.7/forum/)
