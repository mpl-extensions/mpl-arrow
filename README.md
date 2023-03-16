[![License](https://img.shields.io/pypi/l/mpl-arrow.svg?color=green)](https://github.com/mpl-extensions/mpl-arrow/raw/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/mpl-arrow.svg?color=green)](https://pypi.org/project/mpl-arrow)
[![Python Version](https://img.shields.io/pypi/pyversions/mpl-arrow.svg?color=green)](https://python.org)
[![CI](https://github.com/mpl-extensions/mpl-arrow/actions/workflows/ci.yml/badge.svg)](https://github.com/mpl-extensions/mpl-arrow/actions/workflows/ci.yml)
[![codecov](https://codecov.io/gh/mpl-extensions/mpl-arrow/branch/main/graph/badge.svg)](https://codecov.io/gh/mpl-extensions/mpl-arrow)
[![Documentation Status](https://readthedocs.org/projects/mpl-arrow/badge/?version=stable)](https://mpl-arrow.readthedocs.io/en/stable/)

# mpl-arrow
A simpler way to draw nice arrows in matplotlib

## Installation
`pip install mpl-arrow`

## Example usage:
```python
import matplotlib.pyplot as plt

from mpl_arrow import arrow, arrow_absolute, vector

fig, ax = plt.subplots()

#     x, y, dx, dy
arrow(1, 0, 2, 0.5, label="arrow")

#              x,  y,  x2,  y2
arrow_absolute(1, 0.5, 3.5, 2, label="arrow absolute")

#     dx, dy
vector(4, 4, label="vector")

#     dx, dy, x,    y
vector(4, 4, x=0, y=2, label="vector with offset")

plt.legend()
plt.show()
```

![arrows](img/readme_img.png)
