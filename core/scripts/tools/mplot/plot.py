from config import PADWH_CONN
from scripts.objects.configurator import Configurator
from scripts.objects.logger import logger
from scripts.tools.mplot.plotter import MetricPhotoPlotter
from scripts.tools.psql.client import PSQLClient


def plot_daily_metrics(config_path: str):
    """
    Plots daily metrics

    Params:
        config_path: Path to the yaml config file. See configs folder
    """
    logger.info("BEGIN")

    # Get config
    config = Configurator(config_path=config_path).get()

    # Import metrics
    psql = PSQLClient(conn_str=PADWH_CONN)
    metrics = psql.select(sql=config["metrics"])

    # Plot metrics
    plotter = MetricPhotoPlotter(metrics=metrics.to_dict(orient="records")[0])
    plotter.plot(file=config["photo"], metrics_prow=3)

    logger.info("END")
