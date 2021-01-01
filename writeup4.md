# Squasfs

https://linuxize.com/post/how-to-mount-iso-file-on-linux/

1. Mounting ISO

```sh
sudo mkdir /media/boot2root
sudo mount ~/Downloads/BornToSecHackMe-v1.1.iso /media/boot2root -o loop
```

```sh
ls -la /media/boot2root
total 18
dr-xr-xr-x 7 root root 2048 juin  17  2017 .
drwxr-xr-x 4 root root 4096 janv.  1 12:30 ..
dr-xr-xr-x 2 root root 2048 juin  17  2017 casper
dr-xr-xr-x 2 root root 2048 juin  17  2017 .disk
dr-xr-xr-x 2 root root 2048 juin  16  2017 install
dr-xr-xr-x 2 root root 2048 juin  17  2017 isolinux
-r--r--r-- 1 root root  844 juin  17  2017 md5sum.txt
dr-xr-xr-x 2 root root 2048 juin  16  2017 preseed
-r--r--r-- 1 root root  201 juin  17  2017 README.diskdefines
-r--r--r-- 1 root root    0 juin  17  2017 ubuntu
```

```sh
ls -la /media/boot2root/casper
total 416385
dr-xr-xr-x 2 root root      2048 juin  17  2017 .
dr-xr-xr-x 7 root root      2048 juin  17  2017 ..
-r--r--r-- 1 root root     15188 juin  17  2017 filesystem.manifest
-r--r--r-- 1 root root     15154 juin  17  2017 filesystem.manifest-desktop
-r--r--r-- 1 root root        11 juin  17  2017 filesystem.size
-r--r--r-- 1 root root 404209664 juin  17  2017 filesystem.squashfs
-r--r--r-- 1 root root  17086307 juin  17  2017 initrd.gz
-r--r--r-- 1 root root       201 juin  17  2017 README.diskdefines
-r--r--r-- 1 root root   5045536 juin  17  2017 vmlinuz
```

2. Unsquashing `filesystem.squashfs`

https://askubuntu.com/questions/437880/extract-a-squashfs-to-an-existing-directory

```sh
sudo unsquashfs -f -d /media/location1 /media/boot2root/casper/filesystem.squashfs
```

 3. Getting lmezard password

```sh
sudo cat /media/location1/home/LOOKATME/password
lmezard:G!@M6f4Eatau{sF"
```

 4. Cleaning up

```sh
sudo rm -rf /media/location1
sudo umount /media/boot2root
```

 5. Following along with writeup1
