import requests
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

class BlockchainExplorer:
    def __init__(self, blockchain_api_url):
        self.blockchain_api_url = blockchain_api_url

    def get_block(self, block_height):
        response = requests.get(f'{self.blockchain_api_url}/block/{block_height}')
        return response.json()

    def get_transaction(self, transaction_hash):
        response = requests.get(f'{self.blockchain_api_url}/transaction/{transaction_hash}')
        return response.json()

    def get_address(self, address):
        response = requests.get(f'{self.blockchain_api_url}/address/{address}')
        return response.json()

@app.route('/block/<int:block_height>', methods=['GET'])
def get_block(block_height):
    explorer = BlockchainExplorer('https://api.blockchain.com')
    block = explorer.get_block(block_height)
    return jsonify(block)

@app.route('/transaction/<string:transaction_hash>', methods=['GET'])
def get_transaction(transaction_hash):
    explorer = BlockchainExplorer('https://api.blockchain.com')
    transaction = explorer.get_transaction(transaction_hash)
    return jsonify(transaction)

@app.route('/address/<string:address>', methods=['GET'])
def get_address(address):
    explorer = BlockchainExplorer('https://api.blockchain.com')
    address_info = explorer.get_address(address)
    return jsonify(address_info)

if __name__ == '__main__':
    app.run(debug=True)
