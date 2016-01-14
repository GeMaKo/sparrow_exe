# sparrow_exe
This project is an executable for the protein secondary structure prediction method *SPARROW+.
The prediction is based on a vector-valued linear regression function
To make a prediction a PSI-BLAST pssm file in ASCII format has to be supplied as seen in the examples folder.
For the training of *SPARROW+ the pssm files were generated from a UniRef50 Blast database filtered with the program pfilt (default configuration)
pfilt can be obtained from:
http://www.mybiosoftware.com/pfilt-sequence-filtering-low-complexity-coiled-coil-biased-amino-acid-regions.html
http://bioinfadmin.cs.ucl.ac.uk/downloads/pfilt/


INSTALLATION
============

The software requires Python 2.7.6 as an interpreter and the numpy package
has to be installed

You must also install the PSI-BLAST and Impala software from the
NCBI toolkit, and also install appropriate sequence data banks.

The NCBI toolkit can be obtained from URL ftp://ftp.ncbi.nih.gov

PSI-BLAST executables can be obtained from ftp://ftp.ncbi.nih.gov/blast

UniRef50 BLAST database can be obtained from
ftp://ftp.uniprot.org/pub/databases/uniprot/uniref/uniref50/


EXAMPLE USAGE
=============

*SPARROW+ can be started from a linux or windows command line.
In this example the target sequence is called "example.fasta":

python star_sparrow_plus.py example.pssm

The output is returned to stdout, so it should normally be printed to
the shell



SEQUENCE DATA BANK
==================

It is important to ensure than the sequence data bank used with PSI-BLAST
has been filtered to remove low-complexity regions, transmembrane regions,
and coiled-coil segments. If this is not done, then it is essential that
the PSI-BLAST output for the target sequence is checked by-eye to ensure
that no spurious sequences have been included in the PSI-BLAST alignment.
A program called "pfilt" is included which will filter FASTA files before
using the formatdb command to generate the encoded BLAST data bank files.
Currently the program can be obtained from:
http://www.mybiosoftware.com/pfilt-sequence-filtering-low-complexity-coiled-coil-biased-amino-acid-regions.html
http://bioinfadmin.cs.ucl.ac.uk/downloads/pfilt/

Usage:

 pfilt nr.fasta > uniref50filt

 formatdb -t uniref50filt -i uniref50filt

For BLAST+ the formatdb command must be replaced by

 makeblastdb -dbtype prot -in uniref50filt -out uniref50filt

(note that the above command assumes you have already set the BLASTDB
environment variable to the directory where you usually keep your
BLAST data banks)
