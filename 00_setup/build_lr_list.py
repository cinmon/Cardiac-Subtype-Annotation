import liana as li, json

lr = li.resource.select_resource('consensus') # reference of known LR protein pairs
raw = set(lr['ligand']) | set(lr['receptor']) # combine into a single set
lr_genes = {g for s in raw for g in str(s).split('_') if g}   # split complexes

protected = sorted(lr_genes)
json.dump(protected, open('cardiac_subtype_annotation/00_setup/protected_lr_genes.json','w'))
print(len(protected), 'protected LR genes (LIANA consensus only)')
