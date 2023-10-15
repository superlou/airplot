from datetime import datetime, timedelta
import pandas as pd
import numpy as np
from airplot import Airplot


def make_dummy_df():
    start = datetime.now()
    index = pd.date_range(start, start + timedelta(seconds=120), freq="S")
    df = pd.DataFrame(index=index)
    df["flaps_left"] = 25
    df["flaps_right"] = 24
    df["pitch"] = np.sin(0.1 * df.index.second) + 3
    return df


def main():
    df = make_dummy_df()
    print(df)

    airplot = Airplot(df, {
        "axes": [
            {
                "range": [0, 50],
                "position": [0.6, 0.9],
                "columns": ["flaps_left", "flaps_right"],
            },
            {
                "range": [-10, 20],
                "position": [0.1, 0.5],
                "columns": ["pitch"]
            }
        ]
    })
    airplot.show()


if __name__ == "__main__":
    main()