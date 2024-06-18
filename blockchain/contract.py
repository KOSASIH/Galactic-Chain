from web3 import Web3

class EthereumContract:
    def __init__(self, contract_address, abi):
        self.web3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/YOUR_PROJECT_ID'))
        self.contract_address = contract_address
        self.abi = abi

    def deploy(self, bytecode):
        tx_hash = self.web3.eth.send_transaction({'from': '0x...', 'gas': 200000, 'gasPrice': 20, 'data': bytecode})
        return tx_hash

    def call(self, function, args):
        contract = self.web3.eth.contract(address=self.contract_address, abi=self.abi)
        result = contract.functions[function](*args).call()
        return result
