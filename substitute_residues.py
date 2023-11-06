import os
import argparse
from Bio import PDB


# Function to substitute residue names
def substitute_residue_names(pdb_file1, pdb_file2, output_file):
    # Parse both PDB files
    parser = PDB.PDBParser(QUIET=True)
    structure1 = parser.get_structure('structure1', pdb_file1)
    structure2 = parser.get_structure('structure2', pdb_file2)

    # Get chain 'A' from both structures
    chain1 = structure1[0]['A']
    chain2 = structure2[0]['A']

    # Check if the number of residues match
    if len(chain1) != len(chain2):
        raise ValueError("Both PDB files must have the same number of residues in chain 'A'.")

    # # Iterate through residues in chain 'A'
    for residue1, residue2 in zip(chain1.get_residues(), chain2.get_residues()):
        # Substitute residue name
        residue2.resname = residue1.resname

    # Save the modified structure to a new PDB file
    io = PDB.PDBIO()
    io.set_structure(structure2)
    io.save(output_file)

# Function to exclude TER and END records from a PDB file
def exclude_ter_and_end(input_pdb, output_pdb):
    with open(input_pdb, "r") as input_file, open(output_pdb, "w") as output_file:
        for line in input_file:
            # Check if the line contains "TER" or "END" and exclude those lines
            if not line.startswith("TER") and not line.startswith("END"):
                output_file.write(line)

if __name__ == "__main__":

    # Parse Arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--refpdb", type=str, required=True)
    parser.add_argument("--pdbdir", type=str, required=True)
    parser.add_argument("--outpdbdir", type=str, required=True)
    args = parser.parse_args()

    pdb_file1 = args.refpdb
    pdb_list = os.listdir(args.pdbdir)

    i=1
    for pdb in pdb_list:
        print(i)

        if not pdb.endswith(".pdb"):
            print(f"Skipping {pdb} as it is not a PDB file")
            continue

        substitute_residue_names(pdb_file1, os.path.join(args.pdbdir, pdb), 'tmp.pdb')
        exclude_ter_and_end('tmp.pdb', os.path.join(args.outpdbdir, pdb))
        i += 1