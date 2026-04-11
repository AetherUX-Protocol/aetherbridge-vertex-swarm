Swarm Failure Mode
In the event of a total network partition (The Blackout), AetherBridge initiates Mesh-Local State Sync. All IOUs are stored in a distributed ledger across all active peers. Upon reconnection, the first node to see a Stellar Validator acts as the State Relay for the entire swarm.
Arbiter" Role
Dispute Resolution: In Tier 3 transactions, the Tashi Vertex consensus serves as the final arbiter. If an agent attempts to double-spend a P2P IOU, the mesh rejects the state sync, protecting the integrity of the Sovereign Rail.

### **The "Arbiter" Role: Peer-to-Peer Dispute Resolution**

In a decentralized mesh, disagreements are handled via consensus rather than a central authority. 

> **Dispute Resolution:** In Tier 3 transactions, the **Tashi Vertex consensus** serves as the final arbiter. If an agent attempts to double-spend a P2P IOU or submits a fraudulent claim, the mesh rejects the state sync across all peers. This consensus-driven rejection protects the integrity of the **Sovereign Rail** and triggers an automatic reduction in the offending agent's local reputation score.

---

1. Multi-Agent Conflict Serialization
Instead of a "Master Node" deciding transaction order, AetherBridge utilizes the Tashi DAG (Directed Acyclic Graph) logic to timestamp IOU events.

Logical Clocking: Every x402 intercept is hashed with a Lamport timestamp.

Order Consensus: If Agent A and Agent B record an IOU simultaneously, the swarm uses the Vertex Gossip Protocol to agree on the sequence based on network-wide propagation time, preventing race conditions without a leader.

2. The "Blackout" State Recovery (Anti-Entropy)
To ensure the swarm doesn't diverge during a total network partition:

Version Vectors: Each node maintains a Version Vector of the total IOU ledger.

Gossip Reconciliation: Upon reconnection, nodes exchange "State Deltas" rather than the full ledger. The Tashi consensus identifies the most "economically heavy" chain (the one with the most signed peer-proofs) and synchronizes the swarm to that truth.

3. Dynamic Reputation & Soft-Slashing
Reputation Matrix: Every agent maintains a local reputation table for its peers.

Punishment: If an agent proposes a block that violates the x402 Settlement Rule, its "Trust Weight" is reduced.

Isolation: When a Reputation Score falls below 0.4, the swarm automatically ignores that node’s messages until a "Re-calibration Handshake" is performed with at least 3 high-reputation peers.
