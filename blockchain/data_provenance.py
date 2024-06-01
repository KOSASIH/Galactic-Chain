import hashlib
from blockchain import Blockchain

class DataProvenance(object):
    def __init__(self, blockchain):
        self.blockchain = blockchain

    def add_data(self, data):
        data_hash = hashlib.sha256(data.encode()).hexdigest()
        new_block = self.blockchain.create_block(1, self.blockchain.chain[-1]["hash"])
        new_block["data"] = data_hash
        self.blockchain.chain.append(new_block)
        return new_block

    def get_data_provenance(self, data_hash):
        for block in self.blockchain.chain:
            if block["data"] == data_hash:
                return block
        return None
