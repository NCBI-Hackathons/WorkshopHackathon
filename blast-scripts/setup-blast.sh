#!/bin/bash
# setup-blast.sh: Install the latest version of BLAST
#
# Author: Christiam Camacho (camacho@ncbi.nlm.nih.gov)
# Created: Tue 23 Apr 2019 01:54:38 PM EDT

export PATH=/bin:/usr/bin
set -euo pipefail
shopt -s nullglob

VERSION=2.9.0

curl -s ftp://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/LATEST/ncbi-blast-${VERSION}+-x64-linux.tar.gz | tar -zxf -
sudo install -m 755 ncbi-blast-${VERSION}+/bin/* /usr/bin
sudo apt-get install -y cpanminus
sudo apt-get install -y build-essential
sudo cpanm --sudo JSON
rm -fr ncbi-blast-${VERSION}+
