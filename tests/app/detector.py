import ipaddress
import re

MALICIOUS_IPS = {
    "185.199.110.153"
}

MALICIOUS_DOMAINS = {
    "malicious-example.test"
}

MALWARE_HASHES = {
    "44d88612fea8a8f36de82e1278abb02f"
}


def analyze_event(indicator, event_type):

    indicator = indicator.strip().lower()

    # Malware hash
    if indicator in MALWARE_HASHES:
        return {
            "detected": True,
            "severity": "critical",
            "type": "md5",
            "description": "Simulated malware hash",
            "score": 100
        }

    # Malicious IP
    if indicator in MALICIOUS_IPS:
        return {
            "detected": True,
            "severity": "high",
            "type": "ipv4",
            "description": "Simulated malicious IP for laboratory testing",
            "score": 75
        }

    # Malicious domain
    if indicator in MALICIOUS_DOMAINS:
        return {
            "detected": True,
            "severity": "high",
            "type": "domain",
            "description": "Simulated malicious domain for laboratory testing",
            "score": 85
        }

    # Clean IPv4
    try:
        ipaddress.ip_address(indicator)

        return {
            "detected": False,
            "severity": "low",
            "type": "ipv4",
            "description": "No known threat detected",
            "score": 0
        }

    except ValueError:
        pass

    # Domain
    if re.match(r"^[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", indicator):
        return {
            "detected": False,
            "severity": "low",
            "type": "domain",
            "description": "No known threat detected",
            "score": 0
        }

    return {
        "detected": False,
        "severity": "low",
        "type": "unknown",
        "description": "Indicator not recognized",
        "score": 0
    }
