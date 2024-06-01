class BlockchainStorage:
    def __init__(self):
        self.blocks = []

    def add_block(self, block):
        self.blocks.append(block)
