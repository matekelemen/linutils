#!/bin/python3

# --- STL Imports ---
import pathlib
import argparse
import sys
import shutil

# Get source directory
thisScript = pathlib.Path(__file__).absolute()
sourceDir  = thisScript.parent
scriptDir  = sourceDir / "scripts"
configDir  = sourceDir / "config"

# CLI
parser = argparse.ArgumentParser(description="Install shell scripts")
parser.add_argument(
    "installPrefix",
    metavar="install_prefix",
    type=str,
    nargs='?',
    default=str(pathlib.Path.home() / "bin"),
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

# Parse command line arguments
arguments = parser.parse_args(sys.argv[1:])

# Make sure destination directories exist
scriptInstallDir = pathlib.Path(arguments.installPrefix).absolute()
configInstallDir = pathlib.Path(arguments.configPrefix).absolute()

scriptInstallDir.mkdir(parents=True, exist_ok=True)
configInstallDir.mkdir(parents=True, exist_ok=True)

def copyFile(source: pathlib.Path, destination: pathlib.Path):
    if destination.is_dir():
        raise FileExistsError("{} is a directory".format(destination))

    if destination.is_file():
        print("{} exists ".format(destination), end='')

        if arguments.overwrite:
            print("(overwriting)")
            shutil.copy(str(item), str(destination))
        else:
            print("(skipping)")
    else:
        destination.parent.mkdir(exist_ok=True, parents=True)
        shutil.copy(str(item), str(destination))

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
