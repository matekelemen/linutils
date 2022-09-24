#!/bin/python

# --- STL Imports ---
import pathlib
import argparse
import sys
import shutil
import os

# Get source directories
thisScript = pathlib.Path(__file__).absolute()
sourceDir  = thisScript.parent
scriptDir  = sourceDir / "scripts"
configDir  = sourceDir / "config"

# CLI
parser = argparse.ArgumentParser(description="Install shell scripts and config files")
parser.add_argument(
    "installPrefix",
    metavar="install_prefix",
    type=str,
    nargs='?',
    default=str(pathlib.Path.home() / ".local" / "bin"),
    help="destination directory for executable scripts"
)

parser.add_argument(
    "-c",
    "--config-prefix",
    dest="configPrefix",
    type=str,
    default=str(pathlib.Path.home()),
    help="destination directory for configuration files ($HOME by default)"
)

parser.add_argument(
    "-y",
    "--overwrite",
    action="store_const",
    default=False,
    const=True,
    help="overwrite existing files during installation"
)

parser.add_argument(
    "-s",
    "--install-symlinks",
    dest = "installSymlinks",
    action = "store_const",
    default = False,
    const = True,
    help = "Create symlinks instead of copying files at install"
)

# Parse command line arguments
arguments = parser.parse_args(sys.argv[1:])

# Make sure destination directories exist
scriptInstallDir = pathlib.Path(arguments.installPrefix).absolute()
configInstallDir = pathlib.Path(arguments.configPrefix).absolute()

scriptInstallDir.mkdir(parents=True, exist_ok=True)
configInstallDir.mkdir(parents=True, exist_ok=True)

installFunctor = lambda source, destination: os.symlink(str(source), str(destination)) if arguments.installSymlinks else shutil.copy(str(source), str(destination))

def copyFile(source: pathlib.Path, destination: pathlib.Path):
    if destination.is_dir():
        raise FileExistsError("{} is a directory".format(destination))

    if destination.is_file():
        print("{} exists ".format(destination), end='')

        if arguments.overwrite:
            print("(overwriting)")
            os.remove(str(destination))
            installFunctor(item, destination)
        else:
            print("(skipping)")
    else:
        destination.parent.mkdir(exist_ok=True, parents=True)
        installFunctor(item, destination)

# Copy scripts
for item in scriptDir.glob("*"):
    if item.is_file():
        name = str(item.name)
        destination = scriptInstallDir / name
        copyFile(item, destination)

# Copy config files
configProperties = {
    "vscode_settings.json" : {
        "destinationDirectory" : pathlib.Path.home() / ".config" / "Code" / "User",
        "name" : "settings.json"
    },
    "default" : {
        "destinationDirectory" : configInstallDir,
        "name" : ""
    }
}

for item in configDir.glob("*"):
    if item.is_file():
        name = str(item.name)
        if name in configProperties:
            properties = configProperties[name]
        else:
            properties = configProperties["default"]
            properties["name"] = name

        destination = properties["destinationDirectory"] / properties["name"]
        copyFile(item, destination)
