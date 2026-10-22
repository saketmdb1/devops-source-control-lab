from azure.monitor.opentelemetry import configure_azure_monitor
#Initialize Application Insights before importing Flask
configure_azure_monitor(
    enable_live_metrics=True
)

from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify(message="Hello from Azure Container Apps!Deployment Added")


@app.route("/health")
def health():
    return jsonify(status="healthy"), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
