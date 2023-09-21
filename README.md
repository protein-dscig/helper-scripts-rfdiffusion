# helper-scripts-rfdiffusion

Helper scripts to modify/fix residues after running RFDiffusion

This folder contains information on how to run these helper scripts with the output of RFDiffusion BEFORE running the MPNN-FR + AF2 Initial Guess protocols from Nate Bennett's paper.

## Substitute Residues after Partial Diffusion Script

After running Partial Diffusion all the residues in the chain are changed to Glycines and the sidechain information is lost.

If in your application you want to put the original sequence back and fix some of the residues before running ProteinMPNN, run the `substitute_residues.py` script.

This script receives 3 inputs: (i) the reference pdb file to copy the residues from; (ii) the folder with the input pdbs; and (iii) the folder to copy the substituted pdbs.

```
python substitute_residues.py --refpdb REF.pdb --pdbdir /dir/of/pdbs --outpdbdir /dir/of/output/pdbs
```

NOTE: This script expects the chain to be substituted to be chain 'A'.

## Add Fixed Labels for specific positions

NOTE: for most of the cases, you can use the script 'addFIXEDlabels.py' from https://github.com/nrbennet/dl_binder_design to fix your residues after running RFDiffusion.

If you want to define the residues to be fixed MANUALLY, please use the following script! For example, after running Partial Diffusion, if you want to recover the original sequence and fix some of the residues, run the following command:

```
python addFIXEDlabels_manual.py --pdbdir /dir/of/pdbs
```

*How to change the input positions*: Open `addFIXEDlabels_manual.py` and change the variable positions in line 17 for the list of positions that you want to fix. This is done manually now, but soon I will add the options to input it as contigs or individual positions as command line inputs. Wait a bit...

NOTE: the pdb files after this command are changed with REMARK lines, so it is advisable to copy the original folder to a new folder if you want to keep the original clean pdbs.

## To do

[ ] Add to accept both contigs and individual input position in add fixed label scripts as command line inputs.

## Library requirements

- biopython
- pandas
- numpy