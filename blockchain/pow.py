import hashlib
import time

class ProofOfWork:
    def __init__(self, blockchain):
        self.blockchain = blockchain
        self.difficulty = 2

    def mine_block(self, wallet):
        new_block = Block(len(self.blockchain.chain), self.blockchain.get_latest_block().hash, self.blockchain.pending_transactions)
        new_block.mine_block(self.difficulty)
        self.blockchain.chain.append(new_block)
        self.blockchain.pending_transactions = [Transaction(None, wallet.public_key, 10)]
        return new_block

    def calculate_hash(self, block):
        data_string = str(block.index) + block.previous_hash + str(block.transactions) + str(block.timestamp) + str(block.nonce)
        return hashlib.sha256(data_string.encode()).hexdigest()

    def validate_proof(self, block):
        return block.hash[:self.difficulty] == '0' * self.difficulty

    def mine(self, block):
        while not self.validate_proof(block):
            block.nonce += 1
            block.hash = self.calculate_hash(block)
        return block
