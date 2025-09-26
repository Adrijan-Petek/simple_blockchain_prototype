from src.blockchain import Block, Blockchain

def test_block_creation():
    bc = Blockchain()
    # If your blockchain uses 'add_block', adjust here
    new_block = Block(index=1, previous_hash=bc.chain[-1].hash, transactions=["test data"])
    bc.add_block(new_block)
    assert len(bc.chain) == 2
    assert bc.chain[1].transactions[0] == "test data"

def test_genesis_block():
    bc = Blockchain()
    genesis = bc.chain[0]
    # Adjust according to your Block fields
    assert isinstance(genesis, Block)
    assert len(genesis.transactions) == 0  # or whatever your genesis block contains
