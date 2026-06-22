import matplotlib.pyplot as plt


class LiveChart:

    def __init__(self):

        plt.ion()

        self.fig, self.ax = plt.subplots(
            figsize=(10, 5)
        )

    def update(self, df):

        self.ax.clear()

        # BAR GRAPH instead of line graph
        self.ax.bar(
            df["Month"],
            df["Sales"],
            color="skyblue",
            edgecolor="black"
        )

        self.ax.set_title("Live Sales Graph")
        self.ax.set_xlabel("Month")
        self.ax.set_ylabel("Sales")

        self.ax.grid(True, axis="y", linestyle="--", alpha=0.6)

        self.fig.canvas.draw()
        self.fig.canvas.flush_events()