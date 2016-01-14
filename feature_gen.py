import numpy as np
import query
import parameters as para
import copy

__author__ = 'Gerrit'


class Feature:
    def __init__(self, ftype):
        self.ftype = ftype
        self.dimension = para.feature_dimensions[ftype]
        self.data = None

    def set_data(self, query):
        qdata = getattr(query, self.ftype + "_vec")
        assert qdata is not None,  "%s vector not generated" %self.ftype
        window_side = (para.window_size - 1) / 2
        self.data = []
        self.data += [[para.default_values[self.ftype]] * self.dimension] * window_side
        self.data += qdata
        self.data += [[para.default_values[self.ftype]] * self.dimension] * window_side

    def sliding_window(self, step=1):
        """Returns a generator that will iterate through
        the defined chunks of input sequence.  Input sequence
        must be iterable."""

        # Verify the inputs
        try: it = iter(self.data)
        except TypeError:
            raise Exception("**ERROR** sequence must be iterable.")
        if not ((type(para.window_size) == type(0)) and (type(step) == type(0))):
            raise Exception("**ERROR** type(winSize) and type(step) must be int.")
        if step > para.window_size:
            raise Exception("**ERROR** step must not be larger than winSize.")
        if para.window_size > len(self.data):
            raise Exception("**ERROR** winSize must not be larger than sequence length.")

        # Pre-compute number of chunks to emit
        numOfChunks = ((len(self.data) - para.window_size) / step)+1

        # Do the work
        for i in range(0, numOfChunks*step, step):
            yield np.array([item for sublist in self.data[i:i+para.window_size] for item in sublist])


class ScorerInput:
    def __init__(self, ftypes):
        self.ftypes = ftypes
        self.features = []
        for ftype in ftypes:
            self.features.append(Feature(ftype))

    def set_data(self, query):
        for i in range(len(self.features)):
            self.features[i].set_data(query)


if __name__ == '__main__':
    qry = query.Query("test", "ACF")
    qry.set_seq_vector()
    feat = Feature("sequence")
    feat.set_data(qry)
    for w in feat.sliding_window():
        print w, len(w)
    input = ScorerInput(["sequence", "sequence"])
    input.set_data(qry)
    #for i, ftype in enumerate(input.get_input_vector()):
    #    for k, window in enumerate(ftype):
    #        print i, k, window

