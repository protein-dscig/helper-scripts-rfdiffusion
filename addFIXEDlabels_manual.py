#!/usr/bin/env python

import numpy as np
import os
import argparse
import pandas as pd

# Parse Arguments
parser = argparse.ArgumentParser()
parser.add_argument("--pdbdir", type=str, required=True)
parser.add_argument("--verbose", action="store_true", default=True)
args = parser.parse_args()

pdb_list = os.listdir(args.pdbdir)

# fc dimer information
positions = [28,29,30,31,
            86,87,88,89,90,
            205,206,207,208,209,210]

for pdb in pdb_list:
    
    if not pdb.endswith(".pdb"):
        if args.verbose:
            print(f"Skipping {pdb} as it is not a PDB file")
        continue

    pdb_path = os.path.join(args.pdbdir, pdb)

    if args.verbose:
        print(f"Adding FIXED labels to {pdb}")
    
    # loop through the wild type length and add FIXED labels to all the ids except the ones in positions
    remarks = []
    for id_ in positions:
        position = id_
        remark = f"REMARK PDBinfo-LABEL:{position: >5} FIXED"
        # remark = f"REMARK PDBinfo-LABEL:{position+1: >5} FIXED"
        remarks.append(remark)

    # Uncomment below to add hotspots
    remarks_str = '\n'.join(remarks)
    with open(pdb_path, 'a') as f:
        f.write('\n')
        f.write(remarks_str)