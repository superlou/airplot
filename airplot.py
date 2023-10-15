import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import CheckButtons
from matplotlib.ticker import AutoLocator

try:
    import addcopyfighandler
except Exception:
    print("addcopyfighandler not available")


def shifty(axes, fig_range):
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
    axes.yaxis.set_label_coords(position - 0.05, np.mean([y0, y1]))


class Airplot:
    def __init__(self, df: pd.DataFrame, config):
        self.df = df
        self.config = config
    
    def show(self):
        df = self.df
        config = self.config
        fig, ax = plt.subplots()
        ax.grid(True)
        ax.set_yticks([])

        for axes_cfg in config["axes"]:
            twin = ax.twinx()
            twin.spines["left"].set_visible(True)
            twin.yaxis.set_label_position("left")
            twin.yaxis.set_ticks_position("left")
            twin.spines.left.set_position(("axes", -0.01))
            twin.set_ylim(axes_cfg["range"])

            for column in axes_cfg["columns"]:
                twin.plot(df.index, df[column])
            
            twin.set_ylabel("\n".join(axes_cfg["columns"]))
            shifty(twin, axes_cfg["position"])            

        fig.set_layout_engine("tight")

        # fig, ax = plt.subplots()
        # check_buttons = CheckButtons(
        #     ax=ax,
        #     labels=df.columns
        # )
        # check_buttons.on_clicked(self.on_check_buttons_clicked)

        plt.show()
    
    # def on_check_buttons_clicked(self, label):
    #     print(label)
