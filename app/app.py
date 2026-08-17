from flask import Flask, render_template, request
from app.detector import analyze_event
from app.incidents import create_incident, get_incidents

app = Flask(__name__)


@app.route("/")
def dashboard():
    return render_template(
        "dashboard.html",
        incidents=get_incidents()
    )


@app.route("/analyze", methods=["POST"])
def analyze():
    indicator = request.form.get("indicator")
    event_type = request.form.get("event_type", "network")

    alert = analyze_event(indicator, event_type)

    if alert["detected"]:
        create_incident(alert)

    return render_template(
        "dashboard.html",
        alert=alert,
        incidents=get_incidents()
    )


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
