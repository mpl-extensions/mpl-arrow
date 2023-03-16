import numpy as np
from matplotlib import pyplot as plt
from mpl_arrow import arrow


def test_smoke_test():
    for x, y in np.random.random((10, 2)):
        arrow(x, y)
    ax = plt.gca()
    assert len(ax.patches) == 10
