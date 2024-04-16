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
	-i/--input		FASTA			Specify a fasta file. FASTA file requires headers starting with accession number. (i.e. >NZ_CP006019 
[fullname])
	
Basic Options:
--------------
	-h/--help		HELP			Shows this help text and exits the run.

