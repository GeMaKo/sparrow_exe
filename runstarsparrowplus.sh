#!/bin/tcsh

# This is a simple script which will carry out all of the basic steps
# required to make a *SPARROW+ prediction using BLAST+. Note that it
# assumes that the following programs are in the appropriate directories:
# psiblast - PSIBLAST executable (from NCBI BLAST+)
# psipred - *SPARROW+ program


# NOTE: Experimental PSIPRED script with BLAST+ compatability (DTJ May 2010)

# The name of the BLAST+ data bank
set dbname = uniref90filt

# Where the NCBI BLAST+ programs have been installed
set ncbidir = /usr/local/bin

# Where the *SPARROW+ programs have been installed
set execdir = .

set basename = $1:r
set rootname = $basename:t

# Generate a "unique" temporary filename root
set hostid = `hostid`
set tmproot = sparrowtmp$$$hostid

\cp -f $1 $tmproot.fasta

echo "Running *SPARROW+ with sequence" $1 "..."

$ncbidir/psiblast -db $dbname -query $tmproot.fasta -inclusion_ethresh 0.001 -out_ascii_pssm $tmproot.mtx -num_iterations 3 -num_alignments 0 >& $tmproot.blast

if ($status != 0) then
    tail $tmproot.blast
    echo "FATAL: Error whilst running psiblast - script terminated!"
    exit $status
endif

echo "Predicting secondary structure..."

python $execdir/star_sparrow_plus.py $tmproot.mtx > $rootname.ss

if ($status != 0) then
    echo "FATAL: Error whilst running *SPARROW+ - script terminated!"
    exit $status
endif

# Remove temporary files

echo Cleaning up ...
\rm -f $tmproot.* error.log

echo "Final output files:" $rootname.ss
echo "Finished."
