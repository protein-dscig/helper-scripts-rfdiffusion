#!/usr/bin/env python

import numpy as np
import os
import argparse
import pandas as pd
from Bio import PDB

# Parse Arguments
parser = argparse.ArgumentParser()
parser.add_argument("--pdbdir", type=str, required=True)
parser.add_argument("--verbose", action="store_true", default=True)
args = parser.parse_args()

pdb_list = os.listdir(args.pdbdir)

# positions designed by RFDiffusion
positions = [134,135,136,
             137,138,139]

for pdb in pdb_list:
    
    if not pdb.endswith(".pdb"):
        if args.verbose:
            print(f"Skipping {pdb} as it is not a PDB file")
        continue

    pdb_path = os.path.join(args.pdbdir, pdb)

    if args.verbose:
        print(f"Adding FIXED labels to {pdb}")

    # get length of chain A for pdt_path using Biopython
    parser = PDB.PDBParser(QUIET=True)
    structure = parser.get_structure('structure', pdb_path)
    chain = structure[0]['A']
    chain_length = len(chain)
    
    # loop through the wild type length and add FIXED labels to all the ids except the ones in positions
    remarks = []
    for id_ in range(1, chain_length+1):
        if id_ not in positions:
            position = id_
            remark = f"REMARK PDBinfo-LABEL:{position: >5} FIXED"
            # remark = f"REMARK PDBinfo-LABEL:{position+1: >5} FIXED"
            remarks.append(remark)

    # Uncomment below to add hotspots
    remarks_str = '\n'.join(remarks)
    with open(pdb_path, 'a') as f:
        f.write('\n')
        f.write(remarks_str)