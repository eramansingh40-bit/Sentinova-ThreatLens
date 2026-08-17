from app.detector import analyze_event


def test_malicious_ip_detection():
    result = analyze_event(
        "185.199.110.153",
        "network"
    )

    assert result["detected"] is True
    assert result["severity"] == "high"
    assert result["type"] == "ipv4"


def test_clean_ip():
    result = analyze_event(
        "8.8.8.8",
        "network"
    )

    assert result["detected"] is False
    assert result["severity"] == "low"


def test_malicious_domain_detection():
    result = analyze_event(
        "malicious-example.test",
        "network"
    )

    assert result["detected"] is True
    assert result["severity"] == "high"
    assert result["type"] == "domain"


def test_malware_hash_detection():
    result = analyze_event(
        "44d88612fea8a8f36de82e1278abb02f",
        "malware"
    )

    assert result["detected"] is True
    assert result["severity"] == "critical"
    assert result["type"] == "md5"
