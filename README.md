# Sentinova ThreatLens

**PROJ-SENT-260702 · Cybersecurity**

Sentinova ThreatLens is a lightweight cybersecurity threat-intelligence and detection platform designed for a Security Operations Center (SOC) laboratory environment.

The project demonstrates how security events can be analyzed against known threat indicators such as IP addresses, domains, and malware hashes. When a match is found, ThreatLens assigns a severity level and creates an incident for investigation.

---

## Project Status

**Status:** In Progress

**Project Type:** Cybersecurity / SOC / Threat Intelligence

**Environment:** VMware Laboratory

**Operating Systems:**

* Ubuntu — ThreatLens Server
* Kali Linux — Security Event Simulator

---

## Project Objective

The objective of Sentinova ThreatLens is to demonstrate a simplified SOC workflow:

```text
Security Event
      ↓
Indicator Extraction
      ↓
Threat Intelligence Lookup
      ↓
Indicator Correlation
      ↓
Severity Assessment
      ↓
Alert Generation
      ↓
Incident Creation
      ↓
SOC Investigation
```

The project provides a foundation for a larger threat-intelligence platform that can later integrate external threat feeds, Wazuh, Suricata, MITRE ATT&CK, real-time alerts, and advanced dashboards.

---

## Lab Architecture

```text
                    VMware SOC LAB
                         |
          +--------------+--------------+
          |                             |
          |                             |
     Ubuntu VM                      Kali Linux VM
   ThreatLens Server              Event Simulator
   192.168.230.15                 192.168.230.20
          |                             |
          |                             |
          +-------------+---------------+
                        |
                        ↓
                Sentinova ThreatLens
                        |
                +-------+-------+
                |               |
          Threat Intel       Detection
          Indicators           Engine
                |               |
                +-------+-------+
                        |
                        ↓
                    Severity
                        |
                        ↓
                    Incident
                        |
                        ↓
                    Dashboard
```

---

## Technologies Used

| Technology | Purpose                     |
| ---------- | --------------------------- |
| Python     | Application development     |
| Flask      | Web application             |
| JSON       | Threat intelligence storage |
| Pytest     | Detection testing           |
| HTML       | Dashboard                   |
| Kali Linux | Security event simulation   |
| Ubuntu     | ThreatLens server           |
| VMware     | Isolated laboratory         |
| Git/GitHub | Version control             |

---

## Project Structure

```text
Sentinova-ThreatLens/
│
├── app/
│   ├── __init__.py
│   ├── app.py
│   ├── detector.py
│   ├── threat_intel.py
│   └── incidents.py
│
├── data/
│   └── indicators.json
│
├── templates/
│   └── dashboard.html
│
├── logs/
│   └── security.log
│
├── tests/
│   └── test_detection.py
│
├── screenshots/
│   ├── 01-project-structure.png
│   ├── 02-threatlens-dashboard.png
│   ├── 03-malicious-ip-detected.png
│   ├── 04-clean-ip-tested.png
│   ├── 05-incident-created.png
│   ├── 06-kali-event.png
│   └── 07-test-results.png
│
├── requirements.txt
├── README.md
└── run.py
```

---

## Detection Capabilities

The current laboratory version supports three indicator categories.

### 1. IP Address Detection

Example laboratory indicator:

```text
185.199.110.153
```

Expected result:

```text
Detected: True
Severity: High
Type: IPv4
```

### 2. Domain Detection

Example laboratory indicator:

```text
malicious-example.test
```

Expected result:

```text
Detected: True
Severity: High
Type: Domain
```

### 3. Malware Hash Detection

Example laboratory hash:

```text
44d88612fea8a8f36de82e1278abb02f
```

Expected result:

```text
Detected: True
Severity: Critical
Type: MD5
```

> The indicators used in this initial laboratory are demonstration values for testing the detection workflow. They should not be treated as a production threat-intelligence feed.

---

## Severity Model

ThreatLens currently uses a simple severity model.

| Severity | Meaning                              |
| -------- | ------------------------------------ |
| Low      | No known threat-intelligence match   |
| Medium   | Suspicious indicator                 |
| High     | Known malicious/suspicious indicator |
| Critical | High-risk malware indicator          |

---

## Installation

Clone the project:

```bash
git clone <YOUR-GITHUB-REPOSITORY-URL>
cd Sentinova-ThreatLens
```

Create a Python virtual environment:

```bash
python3 -m venv venv
```

Activate it:

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Start ThreatLens

Run:

```bash
python run.py
```

The Flask server listens on:

```text
http://127.0.0.1:5000
```

If the Ubuntu VM has the lab IP:

```text
http://192.168.230.15:5000
```

Kali can access the application through the Ubuntu VM's lab IP.

---

## Kali Linux Test

From Kali Linux:

```bash
curl -X POST http://192.168.230.15:5000/analyze \
-d "indicator=185.199.110.153" \
-d "event_type=network"
```

This simulates a network security event.

The workflow is:

```text
Kali
  ↓
Security Event
  ↓
ThreatLens
  ↓
IOC Lookup
  ↓
Threat Match
  ↓
High Severity
  ↓
Incident
```

---

## Clean Indicator Test

Test an indicator that is not present in the laboratory database:

```bash
curl -X POST http://192.168.230.15:5000/analyze \
-d "indicator=8.8.8.8" \
-d "event_type=network"
```

Expected result:

```text
Detected: False
Severity: Low
```

This demonstrates that ThreatLens can distinguish between a known test indicator and an indicator with no match.

---

## Domain Test

From Kali:

```bash
curl -X POST http://192.168.230.15:5000/analyze \
-d "indicator=malicious-example.test" \
-d "event_type=network"
```

Expected:

```text
Detected: True
Severity: High
Type: Domain
```

---

## Malware Hash Test

```bash
curl -X POST http://192.168.230.15:5000/analyze \
-d "indicator=44d88612fea8a8f36de82e1278abb02f" \
-d "event_type=malware"
```

Expected:

```text
Detected: True
Severity: Critical
Type: MD5
```

---

## Unit Testing

Run:

```bash
pytest -v
```

The project tests:

* Malicious IP detection
* Clean IP detection
* Malicious domain detection
* Malware hash detection

Expected result:

```text
4 passed
```

---

## Screenshots

### Project Structure

![Project Structure](screenshots/01-project-structure.png)

Shows the complete Sentinova ThreatLens project structure.

### ThreatLens Dashboard

![ThreatLens Dashboard](screenshots/02-threatlens-dashboard.png)

Shows the ThreatLens web dashboard running on Ubuntu.

### Malicious IP Detection

![Malicious IP Detection](screenshots/03-malicious-ip-detected.png)

Shows a simulated malicious IP being detected and assigned a high severity.

### Clean IP Test

![Clean IP Test](screenshots/04-clean-ip-tested.png)

Shows an indicator that does not match the laboratory threat-intelligence database.

### Incident Creation

![Incident Created](screenshots/05-incident-created.png)

Shows an automatically generated incident after a threat match.

### Kali Event Simulation

![Kali Event](screenshots/06-kali-event.png)

Shows Kali Linux sending a simulated security event to the ThreatLens server.

### Automated Tests

![Test Results](screenshots/07-test-results.png)

Shows the pytest detection tests passing successfully.

---

## SOC Investigation Workflow

A SOC analyst can use the platform using the following workflow:

```text
1. Receive Security Event
        ↓
2. Extract Indicator
        ↓
3. Search Threat Intelligence
        ↓
4. Determine Match
        ↓
5. Assign Severity
        ↓
6. Generate Alert
        ↓
7. Create Incident
        ↓
8. Investigate
        ↓
9. Respond
        ↓
10. Close Incident
```

---

## Future Enhancements

The current implementation is intentionally simple and designed as a foundation.

Planned enhancements include:

* Real-time threat-intelligence feeds
* Wazuh integration
* Suricata integration
* MISP integration
* Abuse.ch integration
* VirusTotal integration
* MITRE ATT&CK mapping
* Real-time alerting
* User authentication
* Role-based access control
* Global threat map
* Incident lifecycle management
* Risk scoring
* Threat-intelligence API integration
* Database backend
* SOC analyst dashboard
* Automated response playbooks

---

## Security Considerations

This project is designed for an isolated cybersecurity laboratory.

The sample indicators are used for detection testing only.

The recommended environment is:

```text
VMware
   ↓
Host-only Network
   ↓
Ubuntu + Kali
```

Do not use the sample test indicators as a production threat feed.

---

## Learning Outcomes

This project demonstrates practical experience with:

* Threat intelligence
* IOC analysis
* Security event correlation
* Detection engineering
* Severity classification
* Alert generation
* Incident management
* Flask application development
* Python testing
* Kali Linux
* Ubuntu administration
* VMware laboratory networking
* Git/GitHub project management
* SOC investigation workflow

---

## Author

**Amandeep Singh**

Cybersecurity / SOC Analyst Project

**Project ID:** `PROJ-SENT-260702`

**Project:** `Sentinova ThreatLens`

