#!/bin/bash
# setup-aux-tools.sh: Set up auxiliary tools for running BLAST
#
# Author: Christiam Camacho (camacho@ncbi.nlm.nih.gov)
# Created: Tue 23 Apr 2019 09:48:39 PM EDT

export PATH=/bin:/usr/bin
set -euo pipefail
shopt -s nullglob

sudo apt-get install -y parallel
echo 'will cite' | parallel --citation
git clone https://github.com/hoytech/vmtouch.git
cd vmtouch
make 
sudo make install
cd - && rm -fr vmtouch
