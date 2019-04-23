#!/bin/bash
# get-queries.sh: Retrieves sample query sequences (contigs)
#
# Author: Christiam Camacho (camacho@ncbi.nlm.nih.gov)
# Created: Tue 23 Apr 2019 02:39:17 PM EDT

export PATH=/bin:/usr/bin
set -euo pipefail
shopt -s nullglob

sudo mkdir -m 755 -p /blast/queries
sudo gsutil -qm cp -r gs://nola-workshop-jupyter-test/test/contigs/ /blast/queries/
