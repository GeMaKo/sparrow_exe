import expected
import scorer
import query
import parameters as para
import feature_gen as fg
import blast_input as bi
import output as out

__author__ = 'Gerrit'


def assign(profile_fn, outfile=None):
    blast_data = bi.parse_psiblast(profile_fn)
    qry = query.Query("test")
    qry.set_input(blast_data)

    sc1_input = fg.ScorerInput(["profile", "sequence"])
    sc1_input.set_data(qry)
    scorers1 = []
    for i in range(para.num_classes - 1):
        scorers1.append(scorer.Scorer(para.lvl1_coef[i], sc1_input))
    qry.set_structure_vector(scorers1)
    #print "#Lvl 1 complete"
    #print qry.profile_vec
    #print qry.structure_vec
    #sc2_input = fg.ScorerInput(["sequence", "profile"])
    sc2_input = fg.ScorerInput(["structure", "profile"])
    sc2_input.set_data(qry)
    scorers2 = []

    for i in range(para.num_classes - 1):
        scorers2.append(scorer.Scorer(para.lvl2_coef[i], sc2_input))
    qry.set_scores(scorers2)
    qry.set_assignment(expected.get_expected(para.num_classes))
    qry.set_confidence()
    #print "Lvl 2 complete"
    out.output(qry, outfile)
    return qry


if __name__ == '__main__':
    profile_fn = "example\T0515-D1.out"
    ret = assign(profile_fn)

