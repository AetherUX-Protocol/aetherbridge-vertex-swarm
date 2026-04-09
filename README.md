PLAYBOOK.md

# aetherbridge-vertex-swarm
Leaderless Economic Settlement for the Tashi P2P Swarm.
Overview
AetherBridge provides the Financial and Identity Rails for decentralized agentic swarms. While Vertex 2.0 (Tashi) handles the P2P coordination and state sharing, AetherBridge ensures that agents can autonomously negotiate and settle technical debts (compute, data, task hand-offs) without a central orchestrator or cloud dependency.
The Stack
Coordination Layer: Tashi Network / Vertex 2.0 (Leaderless P2P Mesh).

Economic Layer: AetherBridge (Sovereign Rails for M2M payments).

Settlement Layer: Stellar / Soroban (or other L1 for finality).

Agent Logic: Python (LangChain) / Rust.
Architecture: The "Sovereign" Handshake
Discovery: Agent A and Agent B discover each other via Tashi’s gossip protocol (No central server).

Negotiation: Agents exchange "Task Intent" messages over the Vertex mesh.

AetherBridge Rail: AetherBridge validates the agent’s Sovereign Identity and locks the necessary assets on-chain.

Local Finality: Once the task is verified by the swarm consensus (Tashi), AetherBridge triggers the peer-to-peer payout.
Quick Start (Zero-Cloud Demo)
# Clone the repo
git clone https://github.com/AetherUX-Protocol/aetherbridge-vertex-swarm.git

# Launch a 3-node local swarm
docker-compose up -d

# Run the Agentic Negotiation Demo
python scripts/demo_swarm_negotiation.py
Robustness & Recovery
Blackout Mode: If the internet connection is lost, AetherBridge continues to track "Economic Credit" locally within the Tashi mesh.

Self-Healing: If a node drops during a transaction, AetherBridge uses Tashi’s state-sync to rollback or re-route the settlement to a backup agent.
Safety & Security
Leaderless Arbitration: AetherBridge uses Tashi Vertex consensus to automatically resolve disputes and prevent double-spending in offline/blackout scenarios. See PLAYBOOK.md for our arbitration standards.
