import parameters as para
import numpy as np

__author__ = 'Gerrit'


class Query:
    def __init__(self, name):
        self.name = name
        self.sequence = None
        self.sequence_vec = None
        self.profile_vec = None
        self.structure_vec = None
        self.assignment = None
        self.scores = None
        self.probability = None
        self.accuracy = None
        self.confidence = None
        self.distances = None

    def set_input(self, blast_data):
        self.set_profile_vector(blast_data[1])
        self.set_seq_vector(blast_data[0])

    def set_profile_vector(self, profile):
        self.profile_vec = profile

    def set_assignment(self, exp_vec):
        #TODO check if scores have been set!!
        self.assignment = []
        self.distances = []
        self.confidence = np.zeros(len(self.sequence))
        self.probability = np.zeros([len(self.sequence), para.num_classes])
        for i, score_vec in enumerate(zip(*self.scores)):
            distance = [np.dot(score_vec, x) for x in exp_vec]
            self.assignment.append(para.ss_classes[distance.index(max(distance))])
            self.distances.append(distance)
            pis = [max([0, 1./para.num_classes * (1 + (para.num_classes -1) * x)]) for x in distance]
            pis = pis / np.sum(pis)
            conf = (np.max(pis) - 1./para.num_classes) * para.num_classes/(para.num_classes -1)
            self.probability[i] = pis
            self.confidence[i] = conf

    def set_structure_vector(self, scorers):
        scores = [x.get_scores() for x in scorers]
        self.structure_vec = [list(x) for x in zip(*scores)]

    def set_scores(self, scorers):
        self.scores = [x.get_scores() for x in scorers]

    def set_seq_vector(self, sequence):
        self.sequence = sequence
        self.sequence_vec = []
        for aa in sequence:
            aa_vec = [-1] * para.num_aa
            #Check for ValueError Exception!!! if aa == "X"
            aa_vec[para.aa_sorting.index(aa)] = 19
            self.sequence_vec.append(aa_vec)

    def set_confidence(self):
        self.accuracy = []
        for i, conf in enumerate(self.confidence):
            pred_cls_i = para.ss_classes.index(self.assignment[i])
            acc = np.polyval(para.fit[para.ss_classes[pred_cls_i]], conf)
            self.accuracy.append(acc)


    def __getitem__(self, i):
        ret = [i+1, self.sequence[i], self.assignment[i], self.accuracy[i], self.confidence[i],
               self.probability[i, 0], self.probability[i, 1], self.probability[i, 2]]
        return ret



if __name__ == '__main__':
    print [list(x) for x in zip([1,2,3],[1,2,3])]
    '''
    qry = Query("test", "ACFG")
    print(qry.sequence_vec)
    qry.set_seq_vector()
    print(qry.sequence_vec)
    '''
