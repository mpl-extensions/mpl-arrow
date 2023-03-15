import matplotlib.patches as mpatches


def arrow(ax, dx, dy, x=0.0, y=0.0, shrinkA=0.0, shrinkB=0.0, **kwargs):
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

    Other Parameters
    ----------------
    **kwargs
    `~matplotlib.patches.FancyArrowPatch` properties.
    """
    posA = (x, y)
    posB = (x + dx, y + dy)

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
