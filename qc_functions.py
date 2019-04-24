#!/usr/bin/env python3

import csv
import re
import pandas as pd
from collections import defaultdict


def parse_sra_accs(sra_accs):
    sra_acc_pattern = re.compile('[SED]RR\d+')
    sra_accs = sra_accs.replace(',', ' ')
    sra_accs = sra_accs.upper().split()
    for acc in sra_accs:
        if not sra_acc_pattern.fullmatch(acc):
            print('ERROR! {} does not look like a valid SRA run accession.' .format(acc))
            return
    sra_accs = ' '.join(sra_accs)
    return sra_accs


def parse_summary_qc(fastqc_summary, qc_level='fail'):
    qc_level = qc_level.strip().upper()
    if qc_level not in ['WARN', 'FAIL']:
        return print('ERROR! QC level can only be `WARN` or `FAIL`')
        
    qc_dict = {'PASS': 0, 'WARN': 1, 'FAIL': 2}
    qc_level = qc_dict[qc_level]
    qc_results = defaultdict(list)
    with open(fastqc_summary, 'rt') as f:
        tbl = csv.reader(f, delimiter = '\t')
        for line in tbl: 
            if qc_dict[line[0]] >= qc_level:
                qc_results[line[0]].append(line[1])
    return qc_results


def parse_fastqc_data(fastqc_data):
    with open(fastqc_data, 'rt') as f:
        basic_stats = {}
        per_seq_quals = {}
        for line in f:
            if line.startswith('>>Basic Statistics'):
                while not line.startswith('>>END_MODULE'):
                    line = line.strip('\n').split('\t')
                    basic_stats[line[0]] = line[1]
                    line = next(f)
            if line.startswith('>>Per sequence quality scores'):
                while not line.startswith('>>END_MODULE'):
                    line = line.strip('\n').split('\t')
                    per_seq_quals[line[0]] = line[1]
                    line = next(f)
    return basic_stats, per_seq_quals


def process_per_seq_quals(per_seq_quals, threshold=27):
    try:
        threshold = int(threshold)
    except:
        return print('ERROR! Min. Qual. score can only be a number')
        
    if threshold > 40:
        print('Aiming too high?!')
        return
    
    total = 0
    seqs_over_thr = 0

    for k, v in per_seq_quals.items():
        if not k.startswith('#') and not k.startswith('>>'):
            k = int(k)
            v = int(float(v))
            total += v
            if v >= threshold:
                seqs_over_thr += v
    pct_seqs_over_thr = (seqs_over_thr/total)*100
    return pct_seqs_over_thr


def generate_results_table_md(sra_accs, qc_level, threshold):
    passing_accs = []
    header = ['SRA Acc.',
              'No. of reads',
              'Read length', 
              'Percent GC',
              'Poor qual reads',
              'Failed metrics',
              'Pct reads over threshold qual',
              'FastQC Report']
    tbl_str = '|' + '|'.join(header) + '|\n'
    tbl_str += '|----|----|----|----|----|----|----|----|\n'
    for acc in sra_accs.split():
        fastqc_summary = acc + '_fastqc/summary.txt'
        fastqc_data = acc + '_fastqc/fastqc_data.txt'
        fastqc_report = acc + '_fastqc.html'
        qc_results = parse_summary_qc(fastqc_summary, qc_level)
        failed_metrics = '<br>'.join(qc_results.get('FAIL', ['None']))
        warn_metrics = '<br>'.join(qc_results.get('WARN', ['None']))
        basic_stats, per_seq_quals = parse_fastqc_data(fastqc_data)
        pct_seqs_over_thr = process_per_seq_quals(per_seq_quals)
        
        if pct_seqs_over_thr >= 90:
            passing_accs.append(acc)

        tbl_str += '|' + acc + '|'
        for k in ['Total Sequences',
                  'Sequence length',
                  '%GC',
                  'Sequences flagged as poor quality']:
            tbl_str += basic_stats[k] + '|'
        tbl_str += failed_metrics + '|'    
        tbl_str += '{0:5.2f}|'.format(pct_seqs_over_thr)
    #     tbl_str += '[Report](./' + fastqc_report + ')|\n' # not opening in new tab
        tbl_str += '<a href="./' + fastqc_report + '" target="_blank">Report</a> |\n'
        
    print("At least 90% of the reads have quality scores over the threshold in the following accessions: {}" .format(', '.join(passing_accs)))
    return tbl_str


def generate_results_table(sra_accs, qc_level, threshold):
    passing_accs = []
    results_table = defaultdict(list)
    for acc in sra_accs.split():
        fastqc_summary = acc + '_fastqc/summary.txt'
        fastqc_data = acc + '_fastqc/fastqc_data.txt'
        fastqc_report = acc + '_fastqc.html'
        qc_results = parse_summary_qc(fastqc_summary, qc_level)
        failed_metrics = ', '.join(qc_results.get('FAIL', ['None']))
        warn_metrics = ', '.join(qc_results.get('WARN', ['None']))
        basic_stats, per_seq_quals = parse_fastqc_data(fastqc_data)
        pct_seqs_over_thr = process_per_seq_quals(per_seq_quals)
        
        if pct_seqs_over_thr >= 90:
            passing_accs.append(acc)

        results_table['SRA Acc'].append(acc)
        for k in ['Total Sequences',
                  'Sequence length',
                  '%GC',
                  'Sequences flagged as poor quality']:
            results_table[k].append(basic_stats[k])
        results_table['Failed metrics'].append(failed_metrics)    
        results_table['Pct reads over threshold qual'].append('{0:5.2f}|'.format(pct_seqs_over_thr))
        
    print("At least 90% of the reads have quality scores over the threshold in the following accessions: {}" .format(', '.join(passing_accs)))
    return results_table