# linutils

A collection of convenience (mostly shell) scripts that make life easier. Some work on their own, but most require a system that was set up using scripts in ```scripts/setup```.


## OS Setup

Scripts in the ```scripts/setup``` directory automate basic stuff I do on every fresh install: they install packages I use often and create a home structure I'm used to:
```
$HOME
|    .gitcredentials.gpg (a gpg-encrypted .gitcredentials file containing your tokens to GitHub/etc.)
└─── ... (default home directory stuff)
└─── git
|    └─── linutils (this repo)
|    └─── ... (oher sources cloned from GitHub/GitLab/etc.)
└─── build
|    └─── ... (built projects from $HOME/git that aren't built in-source)
└─── bin (added to PATH)
|    |    (scripts installed from this repo)
|    |    ... (other custom executables/scripts you might want here)
└─── python_venv (contains virtual environments for python)
|    └─── default (venv with python packages that get used often)
|    └─── ...
```

OS setup scripts created for:
- Manjaro (21.1.6)

## Installation

Ideally, this repo gets installed when running an OS setup script from ```scripts/setup```, but if you want to manually install it, run ```install.py``` and specify a directory on your PATH. Global config files get copied to ```$HOME``` by default, but you can specify a different destination with ```-c``` (```--config-prefix```). Existing files won't get overridden unless you set ```-y```.

## Scripts

- [```grepandreplace```](https://github.com/matekelemen/linutils/blob/master/grepandreplace) : scans all files in ```$1``` and replaces every occurence of ```$2``` with ```$3```. Fun script. Please don't use it. No warranty.
- [```brightness```](https://github.com/matekelemen/linutils/blob/master/brightness) : thanks to NVidia's shitty drivers and developers avoiding them, the brightness on laptop displays can't be set on gnome (Ubuntu). This script sets the screen brightness to ```$1``` [0.0, 1.0]. (works on the Ubuntu + my laptop combo, no idea about other distros and machines)
- [```encrypt```](https://github.com/matekelemen/linutils/blob/master/encrypt) : zip a file/directory and encrypt it with gpg. ```$1``` is the target file/dir, ```$2``` the output file.
- [```decrypt```](https://github.com/matekelemen/linutils/blob/master/decrypt) : undoes ```encrypt```. ```$1``` is the encrypted file, ```$2``` the decrypted decompressed output directory.
- [```gitcredentials```](https://github.com/matekelemen/linutils/blob/master/gitcredentials) : assuming you have ```$HOME/.gitcredentials.gpg```, this script ```cat```s its contents (decrypts the file and deletes the results after ```cat```ting)
- [```install.py```](https://github.com/matekelemen/linutils/blob/master/install.py) : installs other scripts in this repo to ```$1```.
- [```kdebackground```](https://github.com/matekelemen/linutils/blob/master/kdebackground) : set the background on KDE Plasma 5 to ```$1```.
- [```loadenv.sh```](https://github.com/matekelemen/linutils/blob/master/loadenv.sh) : ```source``` this script to load a virtual python environment from ```$HOME/python_venv```. ```default``` gets loaded if you don't specify an argument.
- [```scanips```](https://github.com/matekelemen/linutils/blob/master/scanlocalips) : ```echo``` every active IP address in ```192.168.0.XXX```. Great for finding your raspberry or realizing that your phone's battery died. Alternatively, you can pass ranges to scan.
- [```sizeof```](https://github.com/matekelemen/linutils/blob/master/sizeof) : ```echo``` the total size of a file/directory
- [```togif```](https://github.com/matekelemen/linutils/blob/master/togif) : ```$1``` video ==> ```$2``` gif

## Utilities

- ```upscale```: upscale images (setup with ```scripts/setup/opencv_setup```)