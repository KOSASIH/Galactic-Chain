class Block:
    def __init__(self, block_id, transactions, previous_hash):
        self.block_id = block_id
        self.transactions = transactions
        self.previous_hash = previous_hash

    def __repr__(self):
        return f"Block({self.block_id}, {self.transactions}, {self.previous_hash})"
