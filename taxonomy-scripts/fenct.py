# Flatten, extend, clean, name taxids
import sys
import os

contax_file = sys.argv[1]
etaxid_file = sys.argv[2]

cxf = open(contax_file, 'r')
contaxes = cxf.read().splitlines()
contaxes = [contax.split('\t') for contax in contaxes]

contax_dict = {}
for contax in contaxes:
    tax_dict = {}
    for tax in contax[1:]:
        kv = tax.split('x')
        if len(kv) > 1:
            tax_dict[int(kv[0])] = int(kv[1])
        else:
            tax_dict[int(kv[0])] = 1
    contax_dict[contax[0].split(':')[0]] = tax_dict

etaxids = eval(open(etaxid_file).read())

print 'name\ttaxid\thits\tscientific_name'

for contax in contax_dict:
    for taxid in contax_dict[contax]:
        outline = contax + '\t' + str(taxid) + '\t' + str(contax_dict[contax][taxid]) + '\t'
        if taxid in etaxids:
            if 'name' in etaxids[taxid] and etaxids[taxid]['name']:
                outline = outline + etaxids[taxid]['name']
            if 'autoextend' in etaxids[taxid]:
                for entry in etaxids[taxid]['autoextend']:
                    for key in entry:
                        outline = outline + '\n' + contax + '\t' + str(key) + '\t' + str(contax_dict[contax][taxid]) + '\t' + str(entry[key])
        print outline
