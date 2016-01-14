# sparrow_exe
This project is an executable for the protein secondary structure prediction method *SPARROW+.
The prediction is based on a vector-valued linear regression function
To make a prediction a PSI-BLAST pssm file in ASCII format has to be supplied as seen in the examples folder.
For the training of *SPARROW+ the pssm files were generated from a UniRef50 Blast database filtered with the program pfilt (default configuration)
pfilt can be obtained from:
http://www.mybiosoftware.com/pfilt-sequence-filtering-low-complexity-coiled-coil-biased-amino-acid-regions.html
http://bioinfadmin.cs.ucl.ac.uk/downloads/pfilt/
