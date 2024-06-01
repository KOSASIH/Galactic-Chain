class NodeStorage:
    def __init__(self):
        self.transactions = []
        self.blocks = []

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def add_block(self, block):
        self.blocks.append(block)
