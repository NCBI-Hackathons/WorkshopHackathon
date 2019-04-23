#!/bin/bash
# get-blastdbs.sh: Gets BLASTDBs useful for viral content analysis
#
# Author: Christiam Camacho (camacho@ncbi.nlm.nih.gov)
# Created: Tue 23 Apr 2019 01:47:24 PM EDT

export PATH=/bin:/usr/bin
set -euo pipefail
shopt -s nullglob

sudo mkdir -m 755 -p /blast/db/
cd /blast/db/
sudo update_blastdb.pl --source gcp --decompress ref_viroids_rep_genomes_v5 
sudo update_blastdb.pl --source ncbi --decompress nt cdd
