Latency: How fast does the "Economic Handshake" happen? (Tashi aims for sub-100ms).

Scalability: How does AetherBridge handle a swarm growing from 3 to 50 agents?

Security: How do you prevent a "Malicious Agent" from draining the swarm's treasury? (Mention Soroban's auth or Multi-sig).
Local State Reconciliation

Blackout Mode: Local Economic Resilience
AetherBridge is designed with a "Partition-Tolerant" architecture. When a swarm loses its connection to the global internet (the Blackout), the protocol shifts from Real-Time Settlement to Local State Reconciliation.

1. The Disconnection Trigger
AetherBridge monitors the Tashi Arc layer for connectivity. If the heartbeat to the public settlement layer (e.g., Stellar/Soroban) is lost, the local nodes trigger "Blackout Mode."

State Freeze: The last known on-chain balance for each agent is "snapshotted" into the Tashi P2P mesh.

Local Identity: Agents continue to verify each other using Self-Sovereign Identity (SSI) keys stored locally on-device.

2. P2P Credit & IOUs (Offline Negotiation)
During a blackout, agents can still "hire" each other for swarm tasks.

Economic Gossip: Transactions are recorded as signed "IOUs" (cryptographic promises) shared across the Tashi gossip protocol.

Virtual Ledger: Every node in the local mesh maintains a copy of these offline transactions. The swarm uses Tashi Vertex consensus to ensure that an agent doesn't "double-spend" its local credit.

3. Reconnection & Global Settlement (The "Flush")
When any single node in the swarm (the "Gateway Node") regains internet access, the local offline ledger is "flushed" to the main chain.

Atomic Batching: All offline IOUs are batched into a single Soroban transaction.

Conflict Resolution: If an agent overspent its global balance while offline, AetherBridge triggers a Reputation Slash—lowering that agent's trust score within the swarm for future tasks.

4. Failure Scenarios handled
5. Scenario,Blackout Response
Node Dropout,Tashi's leaderless state-sync ensures the offline transaction history is mirrored on all other active nodes.
Total Mesh Partition,"The swarm splits into ""Sub-Swarms."" Each maintains its own local credit ledger until they re-merge."
Malicious IOU,Agents verify the digital signature of every offline credit request before providing service.
How to Test Blackout Mode

Technical Implementation: See /scripts/test_blackout_reconciliation.py for the P2P IOU gossip logic
In our docker-compose environment, you can simulate a blackout by dropping the bridge network to the external web while keeping the internal P2P network alive:
# Block external traffic to simulate Blackout
docker exec -it aetherbridge-node-1 iptables -A OUTPUT -d 0.0.0.0/0 -j DROP

# Observe agents continuing to negotiate via Tashi local mesh
tail -f logs/agent_negotiation.log
