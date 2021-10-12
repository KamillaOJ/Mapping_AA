import sys


def find_template(filename_pdb, filename_txt):
    """Get the AA sequence from a PDB file and save it in a text file"""
    with open(filename_pdb, "r") as pdb_file, open(filename_txt, "a") as temp_file:
        temp_file.write(f">{filename_pdb[15:22]}  _P_ {filename_pdb[15:20]}\n")

for file in sys.argv[2:]:
        find_template(file, sys.argv[1])

### Example of what to write in the command line
# python PH_templist_motifs.py PH_motif_temp.txt motif_pdbs_raw/*.pdb
