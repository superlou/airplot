import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.widgets import CheckButtons
from .adjustments import restrict_axes_y
from matplotlib.axes import Axes
from matplotlib.figure import Figure
from matplotlib.backend_bases import MouseEvent

try:
    import addcopyfighandler
except Exception:
    print("addcopyfighandler not available")


class Airplot:
    def __init__(self, df: pd.DataFrame, axes_cfgs):
        self.df = df
        self.axes_cfgs = axes_cfgs

    def show(self):
        df = self.df
        fig: Figure
        ax: Axes
        fig, ax = plt.subplots()
        ax.grid(True)
        ax.set_yticks([])

        self.data_axes = []

        for axes_cfg in self.axes_cfgs:
            twin: Axes = ax.twinx()
            twin.spines["left"].set_visible(True)
            twin.yaxis.set_label_position("left")
            twin.yaxis.set_ticks_position("left")
            twin.spines.left.set_position(("axes", -0.01))
            twin.set_ylim(axes_cfg["range"])

            for column in axes_cfg["columns"]:
                twin.plot(df.index, df[column])
            
            twin.set_ylabel("\n".join(axes_cfg["columns"]))
            restrict_axes_y(twin, axes_cfg["position"])
            self.data_axes.append(twin)

        fig.set_layout_engine("tight")
        fig.align_labels()
        fig.canvas.mpl_connect("button_press_event", lambda evt: self.on_click(evt))

        # fig, ax = plt.subplots()
        # check_buttons = CheckButtons(
        #     ax=ax,
        #     labels=df.columns
        # )
        # check_buttons.on_clicked(self.on_check_buttons_clicked)

        plt.show()
    
    # def on_check_buttons_clicked(self, label):
    #     print(label)

    def on_click(self, evt: MouseEvent):
        # Check if clicked a y-axis
        axes = [axes for axes in self.data_axes
                if axes.yaxis.get_tightbbox().contains(evt.x, evt.y)]

        if len(axes) > 0:
            self.edit_axes(axes[0])

    
    def edit_axes(self, axes: Axes):
        print(axes.yaxis.label)