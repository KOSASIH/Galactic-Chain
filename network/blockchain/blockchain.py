from .blockchain_storage import BlockchainStorage


class Blockchain:
    def __init__(self, blockchain_storage):
        self.blockchain_storage = blockchain_storage

    def add_block(self, block):
        # Call blockchain_storage to add block
        pass
