#!/bin/bash
# fmt-blast.sh: Interim script to format BLAST results on available BLASTDBs
#
# Author: Christiam Camacho (camacho@ncbi.nlm.nih.gov)
# Created: Tue 23 Apr 2019 09:47:53 PM EDT

export PATH=/usr/local/bin:/bin:/usr/bin
set -euo pipefail
shopt -s nullglob

export BLASTDB=/blast/db

# Format results
parallel gunzip {} ::: *.asn.gz
parallel --joblog blast-format.log blast_formatter -archive {} -out {.}.tab -outfmt '7 std qlen qcovs qcovhsp qcovus staxids sblastnames' ::: *.asn
parallel gzip {} ::: *.asn

#F=blastn-nt-SRR1449381.contigs.tab
