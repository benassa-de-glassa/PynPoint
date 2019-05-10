import numpy as np

def resampling_estimator(data, n, estimator, axis=0, method="jackknife"):
    """
    Grabs n samples out of the data and calculated the estimator on top

    Parameters
    ----------

    data : numpy.array
        data on which the estimator should be applied
    n : int
        Size of the subsample on which the jackknife estimator is calculated.\
            Must be smaller or equal than data.shape[axis]
    estimator : method
        Function which calculates the estimated value
    axis : int


    Returns
    -------
    est : numpy.array
        Estimated numpy.array with one less dimension along the selected axis compared to data
    variance : numpy.array
        Variance of the jackknife estimator
    """

    #choose n values at random from the underlying distribution
    indices = np.random.choice(a=data.shape[axis], size=n, replace=False)
    data = data.take(indices, axis=axis)
    theta = estimator(data, axis=axis)
    theta_i = np.zeros(n)
    for i in range(n):
        # remove ith entry for indices
        no_i_indices = list(indices)
        del no_i_indices[i]
        theta_i[i] = np.sum(estimator(data.take(no_i_indices, axis=axis), axis=axis), axis=axis)
    theta_i /= n-1
    theta_dot = np.sum(theta_i, axis=axis)

    bias = (n-1) * (theta_dot - theta)
    variance = (n-1) / n * np.sum([(theta_i[i] - theta_dot)**2 for i in range(n)], axis=axis)
    return theta - bias, variance
