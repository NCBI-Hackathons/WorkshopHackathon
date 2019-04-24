#!/bin/bash
# run-jupyter-server-on-gce.sh: Assumes Jupyter server has been set up on GCE instance
#
# Author: Christiam Camacho (camacho@ncbi.nlm.nih.gov)
# Created: Wed 24 Apr 2019 11:23:32 AM EDT

export PATH=/usr/local/bin:/bin:/usr/bin
set -euo pipefail
shopt -s nullglob

jupyter notebook \
  --NotebookApp.allow_origin='https://colab.research.google.com' \
  --port=8888 \
  --NotebookApp.port_retries=0
