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

from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify(
        message="Hello from Azure Container Apps! Deployment Added"
    )


@app.route("/health")
def health():
    return jsonify(status="healthy"), 200

@app.route("/test-error")
def test_error():
    raise RuntimeError("Demo exception for Application Insights")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
