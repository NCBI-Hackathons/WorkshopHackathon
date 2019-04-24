#!/bin/bash
# get-blastdbs.sh: Gets BLASTDBs useful for viral content analysis
#
# Author: Christiam Camacho (camacho@ncbi.nlm.nih.gov)
# Created: Tue 23 Apr 2019 01:47:24 PM EDT

export PATH=/bin:/usr/bin
set -euo pipefail

sudo mkdir -m 755 -p /blast/db/
cd /blast/db/
sudo update_blastdb.pl --source gcp --decompress nt_v5
sudo update_blastdb.pl --source gcp --decompress ref_viroids_rep_genomes_v5 
sudo update_blastdb.pl --source gcp --decompress split-cdd 
sudo update_blastdb.pl --source gcp --decompress ref_viruses_rep_genomes_v5
sudo update_blastdb.pl --source ncbi --decompress nt

# FIXME: cannot find VIV?
#sudo update_blastdb.pl --source gcp --decompress NCBI_VIV_nucleotide_sequences_v5

# Temporary workaround (WB-3554)
#sudo gsutil -qm cp gs://blast-db/2019-04-20-05-01-28/genomic/Viruses/NCBI_VIV* .
#sudo update_blastdb.pl --source ncbi --decompress other_genomic
#sudo parallel --joblog /tmp/download-other-genomic.log --eta -t "curl -Os ftp://ftp.ncbi.nlm.nih.gov/blast/db/other_genomic.{}.tar.gz.md5" ::: $(seq -w 0 10) $(seq 11 186)
# this line doesn't work
#sudo parallel --joblog /tmp/download-other-genomic.log --eta -t "curl -s ftp://ftp.ncbi.nlm.nih.gov/blast/db/other_genomic.{}.tar.gz | tar -xzf - " ::: $(seq -w 0 10) $(seq 11 186)
#sudo parallel --joblog /tmp/download-other-genomic.log --eta -t "curl -Os ftp://ftp.ncbi.nlm.nih.gov/blast/db/other_genomic.{}.tar.gz" ::: $(seq -w 0 10) $(seq 11 186)
