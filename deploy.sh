#! /usr/bin/bash

ERR="ERR "
LOG="LOG "
WARN="WARN"

function log () {
    printf "[$(date +'%Y-%m-%d %T')]  [$1] \t$2 \n"
}


#####
#   Meta Info
#####

CWD="$(pwd)"
PIP_INSTALL_DIR="$CWD/pip"




#####
#   MAIN
#####

if [ ! -d "$PIP_INSTALL_DIR" ]; then
    log $LOG "Creating install dir [$PIP_INSTALL_DIR]"
    mkdir -p $PIP_INSTALL_DIR
fi



log $LOG "installing flask"
pip3 install --target=$PIP_INSTALL_DIR flask




#####
#   CLosing
#####

log $LOG "Adding new pip location to PYTHONPATH"
export PYTHONPATH=$PYTHONPATH:$PIP_INSTALL_DIR
export FLASK_ENV=development
python3 ./app.py


