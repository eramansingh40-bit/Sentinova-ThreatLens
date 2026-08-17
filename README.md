# Sentinova ThreatLens

## Cyber Threat Intelligence and SOC Detection Platform

**Project ID:** PROJ-SENT-260702  
**Category:** Cybersecurity  
**Project Status:** In Progress

---

## 1. Project Overview

Sentinova ThreatLens is a lightweight Cyber Threat Intelligence (CTI) and Security Operations Center (SOC) detection platform.

The project demonstrates how security events can be correlated with known threat intelligence indicators such as:

- Malicious IP addresses
- Malicious domains
- Malware hashes

When a security event matches a known threat indicator, ThreatLens generates an alert, calculates a risk score, and allows the SOC analyst to create an incident.

The project was designed as a simple practical cybersecurity lab that can be deployed on a VMware Ubuntu virtual machine and accessed through a web browser.

---

# 2. Project Objective

The main objective of Sentinova ThreatLens is to demonstrate a simplified SOC threat-detection workflow.

The platform performs the following operations:

1. Stores threat intelligence indicators.
2. Receives simulated security events.
3. Compares events against threat intelligence.
4. Detects matching indicators.
5. Assigns threat severity.
6. Calculates a risk score.
7. Displays alerts on a dashboard.
8. Creates incidents for detected threats.
9. Allows a SOC analyst to investigate the detected event.

---

# 3. Key Features

## Threat Intelligence

ThreatLens currently supports three indicator types:

- IP addresses
- Domains
- File hashes

Example:

```text
192.0.2.10
malicious-example.test
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
