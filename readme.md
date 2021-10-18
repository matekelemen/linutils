# bash

A collection of convenience (mostly shell) scripts that make life easier. Some work on their own, but most require a system that was set up with one of the scripts in ```os_setup```.


## OS Setup

Scripts in the ```os_setup``` directory automate basic stuff I do on every fresh install: they install packages I use often and create a home structure I'm used to:
```
$HOME
|    .gitcredentials.gpg (a gpg-encrypted .gitcredentials file containing your tokens to GitHub/etc.)
└─── ... (default home directory stuff)
└─── git
|    └─── bash (this repo)
|    └─── ... (oher sources cloned from GitHub/GitLab/etc.)
└─── build
|    └─── ... (built projects from $HOME/git that aren't build in source)
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

Ideally, this repo gets installed when running a script from ```os_setup```, but if you want to manually install it, run ```install.py``` and specify a directory on your PATH. Global config files get copied to ```$HOME``` by default, but you can specify a different destination with ```--config_prefix```. Existing files won't get overridden unless you set ```--overwrite```.

## Scripts

- ```brightness``` : thanks to NVidia's shitty drivers and developers avoiding them, the brightness on laptop displays can't be set on gnome (Ubuntu). This script sets the screen brightness to ```$1``` [0.0, 1.0]. (works on Ubuntu, no idea about other distros)
- ```encrypt``` : zip a file/directory and encrypt it with gpg. ```$1``` is the target file/dir, ```$2``` the output file.
- ```decrypt``` : undoes ```encrypt```. ```$1``` is the encrypted file, ```$2``` the decrypted decompressed output directory.
- ```gitcredentials``` : assuming you have ```$HOME/.gitcredentials.gpg```, this script ```cat```s its contents (decrypts the file and deletes the results after ```cat```ting)
- ```grepandreplace``` : scans all files in ```$1``` and replaces every occurence of ```$2``` with ```$3```. Fun script. Please don't use it. No warranty.
- ```install.py``` : installs other scripts in this repo to ```$1```.
- ```kdebackground``` : set the background on KDE Plasma 5 to ```$1```.
- ```loadenv.sh``` : ```source``` this script to load a virtual python environment from ```$HOME/python_venv```. ```default``` gets loaded if you don't specify an argument.
- ```scanlocalips``` : ```echo``` every active IP address in ```192.168.0.XXX```. Great for finding your raspberry or realizing that your phone's battery died.
- ```sizeof``` : ```echo``` the total size of a file/directory
- ```togif``` : ```$1``` video ==> ```$2``` gif
