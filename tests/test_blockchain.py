# tests/test_blockchain.py
from src.blockchain import Block, Blockchain

def test_block_creation():
    bc = Blockchain()
    bc.add_block("test data")
    assert len(bc.chain) == 2  # genesis + 1 block
    assert bc.chain[1].data == "test data"

def test_genesis_block():
    bc = Blockchain()
    assert bc.chain[0].data == "Genesis Block"
