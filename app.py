import logging
import os

logging.basicConfig(level=logging.INFO)

if os.getenv("APPLICATIONINSIGHTS_CONNECTION_STRING"):
    from azure.monitor.opentelemetry import configure_azure_monitor

    logging.info("Initializing Azure Monitor OpenTelemetry")
    configure_azure_monitor(enable_live_metrics=True)
    logging.info("Azure Monitor initialization completed")
else:
    logging.warning("Application Insights connection string is missing")

import flask

app = flask.Flask(__name__)
