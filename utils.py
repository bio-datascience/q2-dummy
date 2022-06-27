import numpy as np

def normalize(X):
    """
    transforms to the simplex
    X should be of a pd.DataFrame of form (p,N)
    """
    return X / X.sum(axis=0)

def geometric_mean(x, positive=False):
    """
    calculates the geometric mean of a vector
    """
    assert not np.all(x == 0)

    if positive:
        x = x[x > 0]
    a = np.log(x)
    g = np.exp(a.sum() / len(a))
    return g

def log_transform(X, transformation=str, eps=0.1):
    """
    log transform, scaled with geometric mean
    X should be a pd.DataFrame of form (p,N)
    """
    if transformation == "clr":
        assert not np.any(X.values == 0), "Add pseudo count before using clr"
        g = X.apply(geometric_mean)
        Z = np.log(X / g)
    return Z
