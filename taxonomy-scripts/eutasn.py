# Extend uniparous taxids, add scientific names
import sys
import pprint
import sqlite3

taxid_file  = sys.argv[1]
unipar_file = sys.argv[2]

if len(sys.argv) > 3:
    gettax_db_path = sys.argv[3]
else:
    gettax_db_path = '/panfs/traces01.be-md.ncbi.nlm.nih.gov/trace_software/tax_analysis/gettax.sqlite'

def get_scientific_name(taxid):
    conn = sqlite3.connect(gettax_db_path)
    cur = conn.cursor()
    cur.execute('select scientific_name from taxons where tax_id=' + str(taxid))
    for sn in cur:
        return sn[0].encode('ascii')
        Break

ct = open(taxid_file, 'r')
taxids = ct.read().splitlines()
taxids = map(int, taxids)

extended = {}

unipar = eval(open(unipar_file).read())

for taxid in taxids:
    extended[taxid] = {'name':get_scientific_name(taxid), 'autoextend':[]}

    taxidi = taxid
    while taxidi in unipar:
        extended[taxid]['autoextend'].append({unipar[taxidi]:get_scientific_name(unipar[taxidi])})
        taxidi = unipar[taxidi]

    if len(extended[taxid]['autoextend']) == 0:
        del extended[taxid]['autoextend']

ppc = pprint.PrettyPrinter(indent=4)
ppc.pprint(extended)
