import time
from src.blockchain import Block, Blockchain

def test_genesis_block():
    bc = Blockchain()
    genesis = bc.chain[0]
    assert isinstance(genesis, Block)
    assert genesis.transactions[0]["msg"] == "Genesis Block"
    assert genesis.previous_hash == "0"

def test_mine_block():
    bc = Blockchain()
    bc.add_transaction("Alice", "Bob", 50)
    mined_block = bc.mine_block()
    
    # Verify block was mined
    assert mined_block is not None
    assert mined_block.transactions[0]["sender"] == "Alice"
    assert mined_block.transactions[0]["receiver"] == "Bob"
    assert len(bc.pending_transactions) == 0  # pending transactions cleared
    assert len(bc.chain) == 2  # genesis + mined block

def test_chain_validation():
    bc = Blockchain()
    bc.add_transaction("Alice", "Bob", 50)
    bc.mine_block()
    assert bc.is_chain_valid() is True
    
    # Tamper with a block
    bc.chain[1].transactions[0]["amount"] = 1000
    assert bc.is_chain_valid() is False
