[![License](https://img.shields.io/pypi/l/mpl-arrow.svg?color=green)](https://github.com/mpl-extensions/mpl-arrow/raw/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/mpl-arrow.svg?color=green)](https://pypi.org/project/mpl-arrow)
[![Python Version](https://img.shields.io/pypi/pyversions/mpl-arrow.svg?color=green)](https://python.org)
[![CI](https://github.com/mpl-extensions/mpl-arrow/actions/workflows/ci.yml/badge.svg)](https://github.com/mpl-extensions/mpl-arrow/actions/workflows/ci.yml)
[![codecov](https://codecov.io/gh/mpl-extensions/mpl-arrow/branch/main/graph/badge.svg)](https://codecov.io/gh/mpl-extensions/mpl-arrow)

# mpl-arrow
A simpler way to draw nice arrows in matplotlib

## Installation
`pip install mpl-arrow`

## Example usage:
```python
from matplotlib import pyplot as plt
import numpy as np
from easy_arrow import arrow

ax = plt.gca()
for x,y in np.random.random((10, 2)):
        arrow(ax, x, y)
plt.show()
```

![arrows](img/arrow.png)
