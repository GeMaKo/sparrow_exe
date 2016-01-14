__author__ = 'Gerrit'

window_size = 17
aa_sorting = ["A", "R", "N", "D", "C",
              "Q", "E", "G", "H", "I",
              "L", "K", "M", "F", "P",
              "S", "T", "W", "Y", "V"]
num_aa = len(aa_sorting)
ss_classes = ["H", "E", "C"]
num_classes = len(ss_classes)
features_types = ["sequence", "profile", "structure"]
default_values = {"sequence": 0, "profile": -1, "structure": -1}
feature_dimensions = {"sequence": 20, "profile": 20, "structure": 2}

#confidence fit
fit = {"Total":  [  28.29208857,  -54.00240479,  -33.27722022,  121.35702162,   35.72017738],
        "H":  [  73.95490542, -182.71330166,   93.51729204,   72.36579521,   42.0372141 ],
        "E": [ -38.49299277,   86.40363177,  -91.90923997,  105.13293685,   34.61311213],
        "C": [ -15.51348696,   83.62267893, -191.3420046,  188.60098719,   31.8880759 ]}

#weigths
lvl1_coef = ["paras\proseq_17w_0.prm", "paras\proseq_17w_1.prm"]

lvl2_coef = ["paras\strucpro_17w_0.prm", "paras\strucpro_17w_1.prm"]