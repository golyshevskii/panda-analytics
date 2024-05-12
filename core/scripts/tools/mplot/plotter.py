import matplotlib.pyplot as plt
from config import PATH
from matplotlib.axes import Axes
from matplotlib.font_manager import FontProperties
from matplotlib.patches import FancyBboxPatch
from scripts.objects.logger import logger
from scripts.objects.plotter import Plotter


class MetricPhotoPlotter(Plotter):
    """Class for plotting metrics in PNG format"""

    FONT = f"{PATH}media/fonts/montserrat/static/Montserrat-Regular.ttf"

    def __init__(self, metrics: dict):
        self.metrics = metrics
        self.font = FontProperties(fname=self.FONT)

    def _save(self, file: str) -> None:
        """
        Saves metrics to PNG

        Params:
            file: Path of the PNG file where metrics will be saved
        """
        plt.savefig(f"{PATH}{file}", dpi=300, bbox_inches="tight")
        logger.info(f"Metrics has been saved to the {file}")

        plt.close()

    def _rx(self, ax: Axes, value) -> float:
        """Returns the right edge of the given axes object"""
        ax.figure.canvas.draw()
        bbox = value.get_window_extent().transformed(ax.transAxes.inverted())
        return bbox.x1

    def _set_ax(self, ax: Axes):
        """
        Sets the axis layout

        Params:
            ax: Axes object
        """
        ax.set_facecolor("white")
        ax.set_box_aspect(1 / 2)  # TODO: dynamic box aspect
        ax.axis("off")

        bbox = FancyBboxPatch(
            (0, 0),
            1,
            1,
            boxstyle="round,pad=0.1,rounding_size=0.1",
            edgecolor="white",
            facecolor="white",
            linewidth=0.1,
            transform=ax.transAxes,
            clip_on=False,
        )
        ax.add_patch(bbox)

    def plot(self, file: str, metrics_prow: int = 2) -> None:
        """
        Plots metrics

        Params:
            - file: Path of the PNG file where metrics will be saved
            - metrics_prow: Number of metrics per row
        """
        nmetrics = len(self.metrics["metrics"])
        nrows = (nmetrics + metrics_prow - 1) // metrics_prow
        logger.info(f"Plotting {nmetrics} metrics in {nrows} rows...")

        fig, axs = plt.subplots(
            nrows, metrics_prow, figsize=(metrics_prow * 4, nrows * 2)
        )

        fig.set_facecolor("#f0f0f0")
        fig.text(
            x=0,
            y=0.87,
            ha="left",
            va="bottom",
            fontproperties=self.font,
            **self.metrics["date"],
        )
        plt.subplots_adjust(
            left=0, right=0.4, bottom=0.4, top=0.85, wspace=0.33, hspace=0.33
        )

        axs = axs.flatten() if metrics_prow > 1 else axs

        logger.info("Plotting metrics...")
        for ax, metric in zip(axs, self.metrics["metrics"]):
            self._set_ax(ax)

            ax.text(
                x=0.01,
                y=0.7,
                ha="left",
                va="bottom",
                fontproperties=self.font,
                **metric["metric"],
            )
            ax.text(
                x=0.01,
                y=0.2,
                ha="left",
                va="bottom",
                fontproperties=self.font,
                **metric["value"],
            )
            ax.text(
                x=0.95,
                y=0.305,
                ha="right",
                va="bottom",
                fontproperties=self.font,
                **metric["change"],
            )

        # Turn off unused axes
        for ax in axs[nmetrics:]:
            ax.axis("off")

        self._save(file)
