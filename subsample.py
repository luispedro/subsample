import numpy as np

def subsample(counts, N, copy_data=True, stepsize=131072):
    '''
    Subsample counts data

    Parameters
    ----------
    counts: ndarray
        Input histogram
    N: int
        Number of elements to sample
    copy_data : boolean,optional
        If True (default), then the algorithm will copy the ``counts`` data to
        a new array to work on it. Otherwise, it will potentially destroy the
        information in it.
    stepsize : int, optional
        Number of elements to sample at each iteration.

    Returns
    -------
    sampled : ndarray
        Histogram of same size as input ``counts`` array.
    '''
    if copy_data:
        counts = counts.copy()
    if N > counts.sum():
        raise ValueError("Trying to subsample {} from an array with {} elements.".format(N, counts.sum()))
    new = np.zeros_like(counts)

    while N > 0:
        step = min(stepsize, N)
        N -= step
        sampled = np.random.randint(0, counts.sum(), size=step)
        sampled.sort()
        acc = 0
        nexts = 0
        for i,di in enumerate(counts):
            acc += di
            while sampled[nexts] <= acc:
                nexts += 1
                new[i] += 1
                counts[i] -= 1
                if nexts == len(sampled):
                    break
            if nexts == len(sampled):
                break
    return new
