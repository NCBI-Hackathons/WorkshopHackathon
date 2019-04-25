#!/bin/bash
# run-blast.sh: Interim script to run BLAST on available BLASTDBs
#
# Author: Christiam Camacho (camacho@ncbi.nlm.nih.gov)
# Created: Tue 23 Apr 2019 09:47:53 PM EDT

export PATH=/usr/local/bin:/bin:/usr/bin
set -euo pipefail
shopt -s nullglob

export BLASTDB=/blast/db
for db in ref_viruses_rep_genomes_v5 ref_viroids_rep_genomes_v5 nt ; do
    vmtouch -tqm 5G $BLASTDB/$db.*
    parallel --joblog blastn-$db.log -t blastn -db $BLASTDB/$db -query {} -outfmt 11 -out blastn-$db-{/.}.asn ::: /blast/queries/contigs/*
done

# Format results
parallel -q --joblog blast-format.log blast_formatter -archive {} -out {.}.tab -outfmt '7 std qlen qcovs qcovhsp qcovus staxids sblastnames' ::: *.asn
parallel gzip {} ::: *.asn
