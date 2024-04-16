import argparse
import sys
import os
import subprocess
import textwrap

try:
    from Bio import SeqIO
except:
    print("SeqIO module is not installed! Please install SeqIO and try again.")
    sys.exit()

try:
    import tqdm
except:
    print("tqdm module is not installed! Please install tqdm and try again.")
    sys.exit()

parser = argparse.ArgumentParser(prog='python seq_fetch.py',
      formatter_class=argparse.RawDescriptionHelpFormatter,
      epilog=textwrap.dedent('''\

# remove_empty_fasta

Author: Murat Buyukyoruk

        remove_empty_fasta help:

This script is developed to remove empty sequences from a multi/fasta file (i.e., after Trimal run) 

SeqIO package from Bio is required to fetch sequences. Additionally, tqdm is required to provide a progress bar since some multifasta files can contain long and many sequences.
        
Syntax:

        remove_empty_fasta seq_fetch.py -i demo.fasta

remove_empty_fasta dependencies:

Bio module and SeqIO available in this package      refer to https://biopython.org/wiki/Download

tqdm                                                refer to https://pypi.org/project/tqdm/
	
Input Paramaters (REQUIRED):
----------------------------
	-i/--input		FASTA			Specify a fasta file. FASTA file requires headers starting with accession number. (i.e. >NZ_CP006019 [fullname])
	
Basic Options:
--------------
	-h/--help		HELP			Shows this help text and exits the run.

      	'''))
parser.add_argument('-i', '--input', required=True, type=str, dest='filename',
                    help='Specify a alinged fasta file.\n')

results = parser.parse_args()
filename = results.filename

out = filename.split('.')[0] + "_removed_empty." + filename.split('.')[1]

os.system('> ' + out)

proc = subprocess.Popen("grep -c '>' " + filename, shell=True, stdout=subprocess.PIPE, text=True)
length = int(proc.communicate()[0].split('\n')[0])

with tqdm.tqdm(range(length), desc='Reading...') as pbar:
    for record in SeqIO.parse(filename, "fasta"):
        pbar.update()
        f = open(out, 'a')
        sys.stdout = f
        if len(record.seq)!=0:
            print(record.format("fasta"))
