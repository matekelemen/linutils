#!/bin/bash

environmentName="default"

if [ $# -ne 0 ]
    then
        environmentName=$1
fi

source $HOME/python_venv/$environmentName/bin/activate
