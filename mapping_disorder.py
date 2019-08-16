import pandas as pd
import numpy as np
import re
import time
import argparse

def getArgs():
    parser = argparse.ArgumentParser('python')
    parser.add_argument('-input',required=True,help='SNPs input file')
    parser.add_argument('-out',required=True,help='output of disorder')
    return parser.parse_args()
    
def crystal_structure(filename):
    SNP_dataset = pd.read_csv(SNPs_file, delim_whitespace=True, names=['PROTEIN_ID', 'SNP_ID', 'Position', 'wild_type', 'Mutant', 'wt-codon', 'mu-codon'], dtype=object)
    structures = pd.read_csv(proteins_file, delim_whitespace=True, header=None, names=['PROTEIN_ID'])
    New = df.merge(d, on='PROTEIN_ID')
    return(New)
    
def disorder(New, output):
    myfile = open(output, 'w')
    for protein, position, wildtype, mutant, snp, wt, mu in zip(New['PROTEIN_ID'], New['Position'], New['wild_type'], New['Mutant'], New['SNP_ID'], New['wt-codon'], New['mu-codon']):
        with open('%s.diso' %(protein), 'r') as f:
            for line in f:
                a7a = list(line.split())
                if str(position) == a7a[0]:
                    myfile.write(protein + '\t' + snp + '\t' + wt + '\t' + mu + '\t' + wildtype + '\t' + mutant + '\t' + str(position) + '\t' + a7a[2] + '\t' + a7a[3] + '\n')
    myfile.close()
if __name__ == "__main__":
    args = getArgs()
    filename = crystal_structure(args.input)
    output = args.out
    start = time.time()
    end = time.time()
    print ('time elapsed:' + str(end - start))
    
    
