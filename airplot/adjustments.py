import numpy as np
from matplotlib.ticker import AutoLocator
from matplotlib.axes import Axes


def restrict_axes_y(axes: Axes, fig_range):
    d0, d1 = axes.get_ylim()
    y0, y1 = fig_range
    m = (d1 - d0) / (y1 - y0)
    b = d0 - m * y0

    y_min = m * 0 + b
    y_max = m * 1 + b
    axes.set_ylim(y_min, y_max)
    axes.spines["left"].set_bounds(d0, d1)

    ticker = AutoLocator()
    axes.set_yticks(ticker.tick_values(d0, d1))

    position_type, position = axes.spines["left"].get_position()

    # Set the yaxis label position without margin changing as
    # the window resizes    
    x = axes.yaxis.label.get_position()[0]
    y = np.mean([y0, y1])
    axes.yaxis.label.set_position((x, y))