from optparse import OptionParser,OptionGroup
import assignment

__author__ = 'Gerrit'


def main():
    usage = "usage: %prog  profile_fn [options]"
    parser = OptionParser(usage=usage, description="Make secondary structure prediction from a PSI-BLAST profile")

    parser.add_option("-o", "--outfile",action = "store", dest="outfile", type="string",
                      help="outputfile, if not specfied output is stdout")

    parser.add_option("-v", "--verbose",
                      action="store_true", dest="verbose")

    (options, args) = parser.parse_args()

    if len(args) != 1:
            parser.error("incorrect number of arguments, expected 1")

    profile_fn = args[0]
    if options.outfile:
        outfile = options.outfile
        voutfn = options.outfile
    else:
        outfile = None
        voutfn = 'stdout'

    if options.verbose:
        print "outfile: %s"%(str(voutfn))

    assignment.assign(profile_fn, outfile)

if __name__ == "__main__":
    main()