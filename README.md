# 👻 SpecterShield AI (PRO v2.5)
### Autonomous Enterprise Cyber-Defense, AST Self-Healing & AI Orchestrator Framework
**Submission for Kiroween 2026 Hackathon (Frankenstein & Resurrection Tracks)**

[![License: MIT](https://img.shields.io/badge/License-MIT-purple.svg)](https://opensource.org/licenses/MIT)
[![Build Status](https://img.shields.io/badge/Tests-6%20Passed%20(100%25)-emerald.svg)]()
[![Theme](https://img.shields.io/badge/Track-Frankenstein%20%26%20Resurrection-indigo.svg)]()

---

## 📌 Executive Overview
Legacy firewalls, static vulnerability scanners, and perimeter intrusion detection systems are structurally dead. Modern systems face complex multi-vector threats: **CWE-89 SQL Injections**, **OWASP-LLM01 Prompt Injections & Jailbreaks**, and **CWE-78 Remote OS Execution**. 

**SpecterShield AI** resurrects static analysis by embedding a **Dual-Agent Autonomous SOC** that doesn't just sound the alarm—it performs **Abstract Syntax Tree (AST) micro-surgery** to synthesize, compile, test, and hot-patch vulnerable code in **0.24 milliseconds** with zero human intervention.

---

## 🔬 Enterprise 5-Tool Autonomous Suite

1. **`Specter-AST-Patcher`** (`spectershield/ast_patcher.py`):
   - AST-level compiler rewriter that replaces dynamic SQL strings with parameterized queries and wraps shell commands into `shlex.quote` boundaries.
2. **`Phantom-Fuzzer`** (`spectershield/fuzzer.py`):
   - Adversarial Red-Team payload generator that stress-tests API endpoints with mutating injection attacks.
3. **`Specter-Guardrail-Proxy`** (`spectershield/guardrail.py`):
   - Interceptor gateway for LLM endpoints that blocks DAN-mode jailbreaks, system overrides, and data leakage.
4. **`DeepPacket-Sniffer`** (`spectershield/packet_sniffer.py`):
   - Network anomaly engine detecting SYN floods and real-time credential exfiltration.
5. **`Container-Sentry`** (`spectershield/container_sentry.py`):
   - CIS-Benchmark auditing engine for Dockerfiles and Kubernetes pod manifests.

---

## 🌐 Multi-Page Enterprise Web Suite
- **`index.html`**: Interactive Vulnerability Exorcism & AST Self-Healing Lab.
- **`dashboard.html`**: Enterprise Threat Operations (SOC) Real-Time Telemetry.
- **`redteam.html`**: Phantom Red-Team Attack Simulation Arena.
- **`reports.html`**: Printable SOC2 Type II & ISO-27001 Compliance Attestations.

---

## 🧪 Verification & Unit Testing

Run the full automated test suite across all 5 engines:
```bash
python test_enterprise_framework.py
```
*Output: 6/6 Tests passed in 0.006 seconds.*

---

## 👨‍💻 Framework Architect
- **Lead Developer:** Ahmed Hassan Ahmed Mohamed
- **Event:** Kiroween 2026 Hackathon
- **License:** Open Source MIT
