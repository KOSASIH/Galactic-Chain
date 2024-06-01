class GalacticChainModel:
    def __init__(self):
        self.blockchain = []
        self.smart_contracts = []

    def add_block(self, block):
        self.blockchain.append(block)

    def add_smart_contract(self, smart_contract):
        self.smart_contracts.append(smart_contract)
