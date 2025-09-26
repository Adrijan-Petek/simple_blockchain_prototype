import time, json, random, matplotlib.pyplot as plt
from pathlib import Path
from blockchain import Blockchain

# Use relative paths inside repo
OUT = Path("outputs")
CHARTS = Path("charts")

# Create directories (including any missing parents)
OUT.mkdir(parents=True, exist_ok=True)
CHARTS.mkdir(parents=True, exist_ok=True)

bc = Blockchain(difficulty=3)

# Sample transactions
addresses = ["Alice", "Bob", "Charlie", "Dave"]
block_times = []
tx_per_block = []

for i in range(5):
    num_tx = random.randint(1, 4)
    for _ in range(num_tx):
        sender = random.choice(addresses)
        receiver = random.choice(addresses)
        bc.add_transaction(sender, receiver, random.randint(1, 10))
    start = time.perf_counter()
    bc.mine_block()
    end = time.perf_counter()
    block_times.append(end - start)
    tx_per_block.append(num_tx)

# Save outputs
with open(OUT / "blocks.json", "w") as f:
    json.dump([b.__dict__ for b in bc.chain], f, indent=2)

# Plot charts
plt.figure()
plt.bar(range(len(block_times)), block_times)
plt.xlabel("Block Index")
plt.ylabel("Mining Time (s)")
plt.title("Block Mining Times")
plt.tight_layout()
plt.savefig(CHARTS / "mining_times.png")
plt.close()

plt.figure()
plt.bar(range(len(tx_per_block)), tx_per_block)
plt.xlabel("Block Index")
plt.ylabel("Transactions")
plt.title("Transactions per Block")
plt.tight_layout()
plt.savefig(CHARTS / "transactions_per_block.png")
plt.close()

print("Demo complete. Blockchain valid:", bc.is_chain_valid())
print("Outputs in:", OUT.resolve())
print("Charts in:", CHARTS.resolve())
