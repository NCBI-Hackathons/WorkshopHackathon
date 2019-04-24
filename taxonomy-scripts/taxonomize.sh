#!/bin/bash
fasta=$1
taxlist=$2

/opt/taxonomy/aligns_to -dbss /opt/taxonomy/tree_filter.dbss -tax_list $taxlist $fasta > $fasta.taxids.tsv

echo $taxlist - decoding scientific names
python /opt/taxonomy/eutasn.py $taxlist /opt/taxonomy/tax.uniparous /opt/taxonomy/gettax.sqlite > $taxlist.ten.dict

echo $fasta - flatten, extend, clean, name taxids for contigs
python /opt/taxonomy/fenct.py $fasta.taxids.tsv $taxlist.ten.dict > $fasta.taxonomy.tsv

rm -rf $fasta.taxids.tsv
rm -rf $taxlist.ten.dict
