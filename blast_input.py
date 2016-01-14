import numpy as np


__author__ = 'Gerrit'

def parse_psiblast(blastfn):
    #doublecheck ueber line index
    with open(blastfn) as f:
        content = f.readlines()
        content = [x.strip('\n') for x in content]
    mtx_start = False
    profile = []
    seq = []
    for line in content:
        line_cont = line.split()
        if line_cont == []:
            mtx_start = False
            continue
        if mtx_start:
            seq.append(line_cont[1])
            profile.append(map(int, line_cont[2:22]))
        if line_cont[0] == "A":
            mtx_start = True
    ret = (seq, profile)
    return ret




if __name__ == '__main__':
    res = parse_psiblast("example\T0515-D1.out")
    print res

