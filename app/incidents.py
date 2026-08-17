import datetime


incidents = []


def create_incident(alert):
    incident = {
        "id": f"INC-{len(incidents) + 1:03d}",
        "timestamp": datetime.datetime.now().isoformat(),
        "indicator": alert["indicator"],
        "severity": alert["severity"],
        "event_type": alert["event_type"],
        "description": alert["description"],
        "status": "Open"
    }

    incidents.append(incident)

    return incident


def get_incidents():
    return incidents
