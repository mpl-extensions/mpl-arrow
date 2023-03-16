import matplotlib.patches as mpatches

__all__ = [
    "arrow",
    "arrow_absolute",
    "vector",
]


def vector(dx, dy, x=0, y=0, ax=None, **kwargs):
    """
    Plot an arrow indicating a vector.

    Parameters
    ----------
    dx : float
        The x-component of the vector
    dy : float
        The y-component of the vector
    x : float (optional)
        The x-coordinate of the vector's base if nonzero.
    y : float (optional)
        The y-coordinate of the vector's base if nonzero.
    ax : `~matplotlib.axes.axis`, optional
        If *None* get the current axis from pyplot
    **kwargs
        `~matplotlib.patches.FancyArrowPatch` properties.

    Returns
    -------
        `~matplotlib.patches.FancyArrowPatch`
    """
    return arrow(x, y, dx, dy, ax, **kwargs)


def arrow_absolute(x, y, x2, y2, ax=None, **kwargs):
    """
    Plot an arrow between two points in data space.

    Parameters
    ----------
    x : float
        The x-coordinate of the arrows's base.
    y : float
        The y-coordinate of the arrows's base.
    x2 : float
        The x-coordinate of the arrows's tip.
    y2 : float
        The y-coordinate of the arrows's tip.
    ax : `~matplotlib.axes.axis`, optional
        If *None* get the current axis from pyplot
    **kwargs
        `~matplotlib.patches.FancyArrowPatch` properties.

    Returns
    -------
        `~matplotlib.patches.FancyArrowPatch`
    """
    return arrow(x, y, x2 - x, y2 - y, ax, **kwargs)


def arrow(x, y, dx, dy, ax=None, **kwargs):
    """
    Plot an arrow with a base and offset defined in data space.

    Parameters
    ----------
    x : float
        The x-coordinate of the arrow's base.
    y : float
        The y-coordinate of the arrow's base.
    dx : float
        The x component from the base to tip.
    dy : float
        The x component from the base to tip.
    ax : `~matplotlib.axes.axis`, optional
        If *None* get the current axis from pyplot
    **kwargs
        `~matplotlib.patches.FancyArrowPatch` properties.

    Returns
    -------
        `~matplotlib.patches.FancyArrowPatch`
    """
    if ax is None:
        from matplotlib.pyplot import gca

        ax = gca()
    posA = (x, y)
    posB = (x + dx, y + dy)

    shrinkA = kwargs.pop("shrinkA", 0.0)
    shrinkB = kwargs.pop("shrinkB", 0.0)

    stylekw = {
        "head_length": kwargs.pop("head_length", 12),
        "head_width": kwargs.pop("head_width", 12),
        "tail_width": kwargs.pop("tail_width", 4),
    }
    color = kwargs.pop("color", None)
    if color is None:
        color = ax._get_lines.get_next_color()

    vect = mpatches.FancyArrowPatch(
        posA, posB, color=color, shrinkA=shrinkA, shrinkB=shrinkB, **kwargs
    )
    ms = vect._mutation_scale

    for k in ["head_length", "tail_width", "head_width"]:
        stylekw[k] /= ms
    vect.set_arrowstyle(kwargs.get("arrowstyle", "simple"), **stylekw)
    ax.add_patch(vect)
    ax.update_datalim([posA, posB])
    ax._request_autoscale_view()
    return vect
