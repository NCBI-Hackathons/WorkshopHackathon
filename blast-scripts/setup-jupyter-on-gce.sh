#!/bin/bash
# setup-jupyter-on-gce.sh: Install jupyter notebook in GCE instance
#
# Author: Christiam Camacho (camacho@ncbi.nlm.nih.gov)
# Created: Tue 23 Apr 2019 02:59:47 PM EDT

export PATH=/bin:/usr/bin
set -euo pipefail
shopt -s nullglob
echo "Do this only once!"
sudo apt-get install -y python3-pip
sudo python3 -m pip install --upgrade pip
sudo python3 -m pip install jupyter
sudo pip install jupyter_http_over_ws
jupyter serverextension enable --py jupyter_http_over_ws
sudo pip install pandas # Bonus
