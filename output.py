import sys

__author__ = 'Gerrit'


def output(data, outfile=None):
    if outfile is None:
        out = sys.stdout
    else:
        out = open(outfile, 'w')
    try:
        out.write('#Index\tResidue\tAssignment\tAccuracy[%]\tConfidence\tHelix_Prob\tStrand_Prob\tCoil_Prob\n')
        for entry in data:
        #outfile.write("%i\t%s\t%s\t%f.1\t%f.2\t%f.2\t%f.2" %tuple([i]+entry))
            out.write("%i\t%s\t%s\t%.2f\t%.2f\t%.2f\t%.2f\t%.2f\n" %tuple(entry))
    finally:
        if outfile is not None:
            out.close()



