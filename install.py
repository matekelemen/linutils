# --- STL Imports ---
import pathlib
import argparse
import sys
import shutil

# Get source directory
thisScript = pathlib.Path(__file__).absolute()
sourceDir  = thisScript.parent

# CLI
parser     = argparse.ArgumentParser(description="Install shell scripts")
parser.add_argument(
    "install_prefix",
    type=str,
    help="destination directory for executable scripts"
)

parser.add_argument(
    "--config_prefix",
    type=str,
    default=str(pathlib.Path.home()),
    help="destination directory for configuration files (should be $HOME)"
)

parser.add_argument(
    "--overwrite",
    action="store_const",
    default=False,
    const=True,
    help="overwrite existing files during installation"
)

# Parse command line arguments
arguments = parser.parse_args(sys.argv[1:])

# Make sure destination directories exist
installDir = pathlib.Path(arguments.install_prefix).absolute()
configDir  = pathlib.Path(arguments.config_prefix).absolute()

installDir.mkdir(parents=True, exist_ok=True)
configDir.mkdir(parents=True, exist_ok=True)

# Print what actions will be taken
print("Copying scripts from {} to:".format(sourceDir))

messages = (
    (arguments.install_prefix, "(executable scripts)"),
    (arguments.config_prefix, "(configuration files)")
)

alignLength = max((len(arguments.install_prefix), len(arguments.config_prefix)))
for message in messages:
    print("  {:<{alignLength}} {:<}".format(*message, alignLength=alignLength))

# Copy scripts
for item in sourceDir.glob("*"):
    if item.is_file() and item != thisScript:

        # Config file definition:
        #   - hidden (begins with '.')
        #   - ends with 'rc'
        name = str(item.name)
        destination = pathlib.Path()
        if name.startswith('.') and name.endswith('rc'):
            destination = configDir / name
        else:
            destination = installDir / name

        if destination.is_dir():
            raise RuntimeError("{} is a directory".format(destination))

        if destination.is_file():
            print("{} exists ".format(destination), end='')

            if arguments.overwrite:
                print("(overwriting)")
                shutil.copy(str(item), str(destination))
            else:
                print("(skipping)")
        else:
            shutil.copy(str(item), str(destination))
