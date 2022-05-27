from rdkit import Chem

painslist=[]

with open('PAINS.txt') as file:
    while (line := file.readline().rstrip()):
        painslist.append(line)

suppl = Chem.SDMolSupplier('LDC_Top_SPECS.sdf')
for mol in suppl:
    print(Chem.MolToSmiles(mol))
    for pain in painslist:
        #print(pain)
        patt = Chem.MolFromSmarts(pain)
        if mol.HasSubstructMatch(patt) == True:
            print("PAIN " + str(pain) + " Found in " + str(Chem.MolToSmiles(mol)))