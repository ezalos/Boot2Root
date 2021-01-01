# Finding vulnerabilities

For finding vulnberabilities in this project, 2 tools have been of great use, here are there link:

 1. [Lynis](https://github.com/CISOfy/lynis)

```sh
git clone https://github.com/CISOfy/lynis
 cd lynis; ./lynis audit system
```

The `git clone` need to be done outside the VM (git is not installed in it) and then imported with `scp`.

 2. [linux-exploit-suggester](https://github.com/mzet-/linux-exploit-suggester)

```sh
wget https://raw.githubusercontent.com/mzet-/linux-exploit-suggester/master/linux-exploit-suggester.sh -O les.sh
bash les.sh
```
