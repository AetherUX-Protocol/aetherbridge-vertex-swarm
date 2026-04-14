![AetherBridge  Sovereign Agentic Rails for P2P Swarms](https://github.com/user-attachments/assets/1808c743-37fe-41c6-84a6-3eaae5187fa8)


PLAYBOOK.md

Vertex Swarm Integration
The Aether Bridge utilizes Vertex 2.0 as its primary coordination layer. By stripping out central orchestrators, our agents use the Vertex P2P mesh to discover peers and verify transaction state in milliseconds, ensuring zero cloud dependency and maximum resilience

# AetherBridge: Sovereign Agentic Rails (Vertex Swarm)

This repository contains the leaderless settlement layer for **AetherUX**, utilizing the **Vertex/Tashi** consensus engine for resilient P2P coordination.

## 🚀 Key Features
- **x402 Intercepts:** Dynamic fee and settlement redirection at the agent level.
- **Stateful Handshake:** Real-time state replication via Tashi FoxMQ.
- **Blackout Mode:** P2P IOU persistence when primary RPCs are unavailable.

## 📂 Project Structure
- `/agents/aether_agent.py`: Core logic for the Stateful Handshake and x402 intercepts.
- `/tashi/docs`: Technical architecture and protocol specifications.
- `/contracts`: (If applicable) Soroban/Stellar settlement hooks.

## 🛠 Running the Demo
1. Install dependencies: `pip install tashi-sdk` (simulated)
2. Launch Agent A: `python agents/aether_agent.py --id Alpha`
3. Launch Agent B: `python agents/aether_agent.py --id Beta`

4. ### 🔧 Auditor's Quick-Start
The core logic for the Vertex Swarm Challenge is located in `/agents/aether_agent.py`. 
- **Stateful Handshake:** Lines 13-28
- **Blackout Mode / P2P Resilience:** Lines 33-36
- **x402 Settlement Logic:** Integrated within the agent state management.

One-Pager: https://docs.google.com/document/d/1WCPXCqH52RNEn1XyFY6DkxbVQF5P1qQZKvtuUcsdN1U/edit?usp=sharing
Demo Video: https://youtu.be/FOBf4af3o4U
