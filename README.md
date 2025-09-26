```
# Simple Blockchain Prototype

A minimal Python blockchain implementation with:

- Genesis and mined blocks  
- Transactions  
- Chain validation  
- Demo with mining times and transaction charts  

This project is designed as a **learning tool** for understanding blockchain basics.

---

## Features

- Add transactions and mine blocks  
- Track mining time and transactions per block  
- Simple proof-of-work with configurable difficulty  
- Automatic validation of the blockchain integrity  
- Demo generates JSON outputs and charts  

---

## Directory Structure

```

.
├── src/
│   ├── blockchain.py        # Blockchain and Block classes
│   └── demo_blockchain.py   # Demo script with charts
├── tests/
│   └── test_blockchain.py   # Unit tests
├── outputs/                 # Generated JSON data
├── charts/                  # Generated chart images
├── requirements.txt         # Python dependencies
├── run_demo.sh              # Script to run demo
└── .github/workflows/
└── ci.yml               # GitHub Actions CI workflow

````

---

## Setup

1. Clone the repository:

```bash
git clone https://github.com/Adrijan-Petek/simple_blockchain_prototype.git
cd simple_blockchain_prototype
````

2. Install dependencies:

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

> The workflow uses Python 3.11.

---

## Running Tests

Run unit tests with `pytest`:

```bash
export PYTHONPATH=$PYTHONPATH:$(pwd)/src
pytest -v
```

Expected output:

```
tests/test_blockchain.py::test_genesis_block PASSED
tests/test_blockchain.py::test_mine_block PASSED
tests/test_blockchain.py::test_chain_validation PASSED
```

All tests should pass.

---

## Running the Demo

Run the demo script to generate blocks, transactions, and charts:

```bash
bash run_demo.sh
```

This will create:

* `outputs/blocks.json` → JSON representation of the blockchain
* `charts/mining_times.png` → Block mining times
* `charts/transactions_per_block.png` → Transactions per block

Example output:

```
Demo complete. Blockchain valid: True
Outputs in: /full/path/to/outputs
Charts in: /full/path/to/charts
```

---

## Updated `run_demo.sh` (CI-ready)

```bash
#!/bin/bash
set -e
set -x

echo "Starting Simple Blockchain demo..."

# The demo script now handles directory creation itself
python src/demo_blockchain.py

echo "Demo finished successfully."
```

---

## GitHub Actions CI

The workflow automatically:

1. Installs Python dependencies
2. Runs `flake8` for linting
3. Runs `pytest` for tests
4. Runs the demo script
5. Uploads `outputs/` and `charts/` as artifacts

Artifacts can be downloaded from the workflow run in GitHub Actions.

---

## Notes

* Uses **relative paths** for outputs (`outputs/` and `charts/`) — works in CI and locally

* `Blockchain` class includes:

  * `add_transaction(sender, receiver, amount)`
  * `mine_block()`
  * `is_chain_valid()`

* Demo script randomly generates transactions and blocks for visualization.

---

## Example Usage

```python
from blockchain import Blockchain

bc = Blockchain(difficulty=3)
bc.add_transaction("Alice", "Bob", 10)
block = bc.mine_block()
print("Blockchain valid:", bc.is_chain_valid())
```

---

## License

MIT License – free to use, modify, and distribute.

```

