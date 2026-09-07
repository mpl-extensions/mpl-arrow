import numpy as np
from matplotlib import pyplot as plt

from mpl_arrow import arrow, arrow_absolute, vector


def test_basic_test():
    fig, ax = plt.subplots()
    arrow(1, 0, 2, 0.5, label="arrow")
    arrow_absolute(1, 0.5, 3.5, 2, label="arrow absolute")

    vector(4, 4, label="vector")
    vector(4, 4, x=0, y=2, label="vector with offset")

    assert len(ax.patches) == 4
    np.testing.assert_allclose(np.round(ax.get_xlim(), 3), (-0.203, 4.2))
    np.testing.assert_allclose(np.round(ax.get_ylim(), 3), (-0.306, 6.3))
