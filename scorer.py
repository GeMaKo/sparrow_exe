import parameters as para
import feature_gen as fg
import numpy as np
import query
from itertools import izip


__author__ = 'Gerrit'


class Scorer:
    def __init__(self, coeffn, sc_in):
        self.sc_input = sc_in
        self.window_size = para.window_size
        self.num_feat = len(para.features_types)
        self.func_parameters_ = np.fromfile(coeffn, dtype=np.dtype("d"))
        self.constant = self.func_parameters_[-1]

        self.dimensions_ = [x.dimension * self.window_size for x in sc_in.features]
        self.primary_dim_ = self.dimensions_[0]
        self.sec_dim_ = self.dimensions_[-1]

        self.numOfQuadraticParam = (self.primary_dim_ * (self.primary_dim_ + 1)) / 2

        self.indices_lin = np.zeros(self.numOfQuadraticParam, dtype=int)
        self.indices_quad = np.zeros(self.numOfQuadraticParam, dtype=int)
        x = 0
        y = 0
        for i in range(self.numOfQuadraticParam):
            self.indices_lin[i] = x
            self.indices_quad[i] = y
            x += 1
            if x > y:
              y += 1
              x = 0


    def scoring(self, input_vector):
        #TODO change function to only consider one feature type, needs then info about lin or quad
        score = 0
        #try:
        dim_index = self.primary_dim_ + (self.primary_dim_ * (self.primary_dim_ + 1)) / 2
        #for i in range(self.dimensions_[feature_i]):
        #    score += self.func_parameters_[i] * input_vector[feature_i][i]
        score += np.dot(self.func_parameters_[:self.primary_dim_], input_vector[0])
        #for i in range(self.num_func_parameters_ - self.tot_linear_parameters):
        #print len(self.func_parameters_[self.primary_dim_:-self.sec_dim_-1]), len(input_vector[0][self.indices_lin]), len(input_vector[0][self.indices_quad])
        #    score += self.func_parameters_[i + self.primary_dim_] * input_vector[feature_i][self.indices_lin[i]] * input_vector[feature_i][self.indices_quad[i]]
        score += np.sum(self.func_parameters_[self.primary_dim_:-self.sec_dim_-1] * input_vector[0][self.indices_lin] * input_vector[0][self.indices_quad])
        #except Exception as e:


        if len(input_vector) > 1:
            #for i in range(self.dimensions_[feature_i]):
            #    score += self.func_parameters_[dim_index + i] * input_vector[feature_i][i]
            score += np.dot(self.func_parameters_[dim_index:(dim_index+self.sec_dim_)], input_vector[1])
        score += self.constant
        return score

    def get_scores(self):
        scores = []
        for iswins in zip(*[x.sliding_window() for x in self.sc_input.features]):
            tot_feat_vec = [x for x in iswins]
            #print tot_feat_vec
            #print len(tot_feat_vec)
            #print "shape: ", tot_feat_vec.shape
            scores.append(self.scoring(tot_feat_vec))
        return scores


if __name__ == '__main__':
    qry = query.Query("test")
    qry.set_seq_vector("ACFFFGHILQALVVRGTG")
    sc_input = fg.ScorerInput(["sequence", "sequence"])
    sc_input.set_data(qry)
    scorer = Scorer(para.lvl1_coef[0], sc_input)
    print scorer.get_scores()





