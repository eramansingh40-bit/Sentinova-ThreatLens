from app.threat_intel import search_indicator


def analyze_event(indicator, event_type="network"):
    result = search_indicator(indicator)

    if result:
        return {
            "detected": True,
            "indicator": indicator,
            "severity": result["severity"],
            "type": result["type"],
            "description": result["description"],
            "event_type": event_type
        }

    return {
        "detected": False,
        "indicator": indicator,
        "severity": "low",
        "type": "unknown",
        "description": "No threat intelligence match found",
        "event_type": event_type
    }
