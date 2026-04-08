import time
import random
import uuid

class AetherBridgeRail:
    """Simulates the Sovereign Agentic Rail for Stellar/Soroban settlement."""
    def __init__(self, agent_name):
        self.agent_name = agent_name
        self.is_online = True

    def lock_funds(self, amount, recipient):
        print(f"  [RAIL] {self.agent_name}: Requesting Soroban lock for {amount} USDC to {recipient}...")
        time.sleep(1)  # Simulate blockchain latency
        tx_hash = uuid.uuid4().hex
        print(f"  [RAIL] Success! Settlement locked. Tx: {tx_hash[:12]}...")
        return tx_hash

class SwarmAgent:
    def __init__(self, name):
        self.name = name
        self.rail = AetherBridgeRail(name)
        self.peers = []

    def discover_peers(self):
        """Simulates Tashi P2P gossip discovery."""
        print(f"[{self.name}] Scanning Tashi P2P mesh for active peers...")
        time.sleep(1.5)
        return ["Agent-Alpha", "Agent-Beta"]

    def negotiate_task(self, peer):
        print(f"[{self.name}] Found {peer}. Negotiating Task: 'Compute-Vector-Optimization'...")
        price = random.randint(5, 20)
        print(f"[{self.name}] {peer} quoted {price} USDC. Initializing AetherBridge Rail...")
        
        # Trigger the Sovereign Rail
        receipt = self.rail.lock_funds(price, peer)
        print(f"[{self.name}] Task Hand-off Complete. Payment secured for {peer}. \n")

def run_demo():
    print("--- STARTING AETHERBRIDGE SWARM DEMO ---")
    print("Scenario: Leaderless Economic Settlement (Blackout Resilient)\n")
    
    # Initialize Main Agent
    my_agent = SwarmAgent("Aether-Node-01")
    
    # 1. P2P Discovery Phase (Tashi)
    discovered = my_agent.discover_peers()
    target_peer = discovered[0]
    
    # 2. Negotiation & Settlement Phase (AetherBridge)
    my_agent.negotiate_task(target_peer)
    
    print("--- DEMO COMPLETE ---")
    print("Status: Sovereign Rails Verified. No Cloud Centralization Detected.")

if __name__ == "__main__":
    run_demo()
