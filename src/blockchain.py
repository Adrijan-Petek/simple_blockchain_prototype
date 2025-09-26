import hashlib
import json
import time
from typing import List

class Block:
    def __init__(self, index: int, transactions: List[dict], previous_hash: str, difficulty: int = 2):
        self.index = index
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.difficulty = difficulty
        self.nonce = 0
        self.timestamp = time.time()
        self.hash = self.compute_hash()

    def compute_hash(self) -> str:
        """
        Compute the SHA-256 hash of the block's contents (excluding the hash itself).
        """
        block_dict = self.__dict__.copy()
        block_dict.pop("hash", None)  # Exclude existing hash
        return hashlib.sha256(json.dumps(block_dict, sort_keys=True, default=str).encode()).hexdigest()


class Blockchain:
    def __init__(self, difficulty: int = 2):
        self.chain: List[Block] = []
        self.pending_transactions: List[dict] = []
        self.difficulty = difficulty
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis_block = Block(0, [{"msg": "Genesis Block"}], "0", self.difficulty)
        self.chain.append(genesis_block)

    def get_last_block(self) -> Block:
        return self.chain[-1]

    def add_transaction(self, sender: str, receiver: str, amount: float):
        self.pending_transactions.append({
            "sender": sender,
            "receiver": receiver,
            "amount": amount,
            "timestamp": time.time()
        })

    def mine_block(self):
        if not self.pending_transactions:
            return None
        new_block = Block(
            index=len(self.chain),
            transactions=self.pending_transactions,
            previous_hash=self.get_last_block().hash,
            difficulty=self.difficulty
        )
        self.chain.append(new_block)
        self.pending_transactions = []
        return new_block

    def is_chain_valid(self) -> bool:
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            prev = self.chain[i - 1]

            # Recompute hash excluding 'hash' field
            block_dict = current.__dict__.copy()
            block_dict.pop("hash", None)
            recomputed_hash = hashlib.sha256(
                json.dumps(block_dict, sort_keys=True, default=str).encode()
            ).hexdigest()

            if recomputed_hash != current.hash or current.previous_hash != prev.hash:
                return False
        return True
