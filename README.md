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

### 🔄 Execution Flow
```text
[ CLIENT SIDE ]                      [ TOKENCLAW HUB ]
       |                                     |
       |-- 1. Request Authorization -------->|
       |      (Encrypted Token Handshake)    |
       |                                     |
       |<-- 2. Validate & Grant DR ----------|
       |      (Status: 200 OK)               |
       |                                     |
[ UNLOCKING ASSET ]                          |
       |-- 3. In-Memory Decryption           |
       |-- 4. RTL Logic Execution            |
       |-- 5. TRACE PURGE (Safe Exit)        |
       v                                     |
[ LOGIC PROTECTED ] <------------------------|

### 🛠 System Requirements
- **Environment**: Linux/Termux (Android)
- **EDA Tools**: Icarus Verilog 12.0
- **Language**: Python 3.10+ (Flask, Requests)

## 3. Operational Walkthrough (Step-by-Step)

To ensure the security of the logic assets, follow this exact sequence to initialize the TokenClaw-DR gateway.

### Step 1: Launch the Verification Hub (Server Side)
Open your terminal (e.g., Termux or Linux Bash) and start the central authentication server. This acts as the "Brain" of the authorization network.
```bash
python mao_server.py

​What to look for: The terminal should display Running on http://0.0.0.0:5000.
​Status: Keep this window OPEN and running. Do not close it, or all authorization requests will fail.

​Step 2: Issue a Distribution Token (Admin Side)
​Open a NEW terminal session (Swipe right in Termux and click "New Session"). We will now generate a unique access credential.

python mao_admin.py

Interaction:
​Enter the client's name (e.g., Dan_Intel).
​Define the asset ID (e.g., ChaKou_Core).
​Enter validity period in days (e.g., 365).
​Result: The system will print a Token like MAO-1C97XXXXXXXX.
​Action: Long-press to COPY this token string immediately.

Step 3: Configure the Client Gate (Authorization Setup)
​Before running the client, you must "hand" the token to the security gate.

nano langchain_remote_gate.py

Edit: Find the line self.token = "...".
​Important: Paste your copied Token between the double quotes.
​Incorrect: self.token = MAO-123 (Causes SyntaxError)
​Correct: self.token = "MAO-123"
​Save: Press Ctrl+O, then Enter, then Ctrl+X to exit.

Step 4: Execute Remote Logic Simulation (Client Side)
​Now, trigger the automated verification and simulation process.

python langchain_remote_gate.py

🔍 What Happens Next? (Automated Workflow)
Once you press Enter in Step 4, the TokenClaw-DR architecture executes the following:
1.Handshake: The gate sends the Token to the Hub (started in Step 1).
2.​Audit: The Hub checks the database and returns a "Success" status code (200).
3.​Decryption: The system dynamically decrypts the chakou_logic.v.enc asset in-memory.
​4.Simulation: Icarus Verilog is automatically invoked to run the logic verification.
​5.Purge: The gate performs a Deep Cleanup, deleting all plaintext files and memory traces to prevent logic leakage.

​4. System Roadmap
​Node Compatibility: Validated for 3nm and 12nm tape-out pipelines.
​AI Protocol: Native integration for LLM-driven autonomous logic auditing.
​Cross-Device Auth: Supports remote authorization across different physical IPs.

5. License & Attribution
​Copyright (c) 2026 Mao Guanghui. All rights reserved.
​This project is licensed under the Mao Merit-Based License 1.0 (MMBL):
​Logic over Background: Technical integrity is the sole criterion for evaluation.
​Authorization Required: No party is permitted to bypass the TokenClaw-DR gateway or use the ChaKou Protocol for commercial tape-out without a valid Token issued by the architect.
​Attribution: Any derivative works or research must credit Mao Guanghui as the original architect.
​For formal licensing inquiries, contact the architect via the OCP mailing list.
