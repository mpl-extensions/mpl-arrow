# arrow
Arrow plot for matplotlib

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

