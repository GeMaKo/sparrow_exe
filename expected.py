import numpy as np

__author__ = 'Gerrit'


def get_expected(numberOfClasses):
    outputs = np.zeros([numberOfClasses, numberOfClasses - 1], dtype=float)
    # set first vector to positive "highest" axis
    outputs[0][numberOfClasses-2] += 1.0
    #print outputs
    # initialize all other vectors to be zero vectors in the beginning
    # calculate other vectors by maintaining that the scalar product with the previous vectors are equal to the desired
    # scalar product and the norm of each vector is 1
    scalarProduct = -1.0 / (numberOfClasses - 1)
    for i in range(1,numberOfClasses - 1):
        outputs[i][numberOfClasses - 2] = scalarProduct # so the scalar product with the first vector matches the requirements
        if i == numberOfClasses - 2:
            outputs[i + 1][numberOfClasses - 2] = scalarProduct #so the scalar product with the first vector matches the requirements
        normSum = scalarProduct * scalarProduct #used to maintain vector length
        for k in range(i-1): # calculate all free func_parameters_ but the last
            prodSum = scalarProduct * scalarProduct #used to maintain scalar product values
            for k2 in range(k):
                prodSum += outputs[i][k2] * outputs[k + 1][k2]
            outputs[i][k] = (scalarProduct - prodSum) / outputs[k + 1][k]
            normSum += outputs[i][k] * outputs[i][k]
            if i == numberOfClasses - 2:
                outputs[i + 1][k] = outputs[i][k]
        if i < numberOfClasses - 2:
            outputs[i][i - 1] = np.sqrt(1 - normSum) #calculate the last free parameter by maintaining the vector's length
        else:
            outputs[i][i - 1] = np.sqrt(1 - normSum)
            outputs[i + 1][i - 1] = -np.sqrt(1 - normSum)
    return outputs


if __name__ == '__main__':
    print get_expected(3)