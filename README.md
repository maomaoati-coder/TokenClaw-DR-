TokenClaw-DR (Distribution Rights)
​A Centralized Remote Token Authorization & Logic Distribution Framework 

![Security](https://img.shields.io/badge/Security-Physical--Layer--Intercept-red?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Silicon--Ready--Simulation-green?style=for-the-badge)
![License](https://img.shields.io/badge/License-Mao--Merit--1.0-orange?style=for-the-badge)

## 1. Executive Summary
​TokenClaw-DR is a specialized logic security framework designed by Independent Chip Architect Mao Guanghui. Its primary objective is to provide a robust, remote-controlled Token Authorization System for proprietary logic assets. By implementing a high-precision "Claw" intercept mechanism through the ChaKou Protocol, it ensures that logical entities remain inactive and secure until a cryptographically verified Token is validated via a real-time remote handshake.

---

## 2. Technical Architecture
The framework operates on a triple-layer security stack:
1.  **The Hub (Auth Server)**: Manages the global database of issued Distribution Rights.
2.  **The Claw (Security Gate)**: Intercepts hardware calls and performs in-memory decryption.
3.  **The Asset (Encrypted RTL)**: High-value IP (e.g., ChaKou 3nm Core) protected by AES-grade wrapping.

---

## 3. Deployment & Operation Manual

### 🛠 System Requirements
- **Environment**: Linux/Termux (Android)
- **EDA Tools**: Icarus Verilog 12.0
- **Language**: Python 3.10+ (Flask, Requests)

### Step 1: Initialize the TokenClaw Hub
Start the central verification server on your control device. This server maintains the `token_database.json`.
```bash
python mao_server.py
Confirmation: Look for Running on http://0.0.0.0:5000.

​Step 2: Grant Distribution Rights (Admin)
​Issue a unique Token for a client (e.g., Intel, OCP partners) using the management panel.
python mao_admin.py
​Enter Client Name, Asset ID, and Expiry Days.
​Copy the generated Token (Format: MAO-XXXX

​Step 3: Remote Logic Activation (Client)
​The client executes the langchain_remote_gate.py with the provided Token.
python langchain_remote_gate.py

Automated Workflow:
​Handshake: Client requests permission from the Hub.
​Unlock: Upon success, the .v.enc asset is decrypted.
​Simulation: Icarus Verilog runs the hardware logic.
​Purge: The gate executes an automatic cleanup of all plaintext files and memory traces.

4. Hardware Roadmap
​3D Logic Locking: Multi-layer intercept for stacked die security.
​Process Nodes: Validated for 3nm and 12nm tape-out pipelines.
​AI Integration: Native support for LLM-driven autonomous chip auditing.

​5. License & Attribution
​Copyright (c) 2026 Mao Guanghui. All rights reserved.
​This project is licensed under the Mao Merit-Based License 1.0 (MMBL):
​Logic over Background: Technical integrity is the sole criterion for evaluation.
​Authorization Required: No party is permitted to bypass the TokenClaw-DR gateway or use the ChaKou Protocol for commercial tape-out without a valid Token issued by the architect.
​Attribution: Any derivative works or research must credit Mao Guanghui as the original architect.
​For formal licensing inquiries, contact the architect via the OCP mailing list.
