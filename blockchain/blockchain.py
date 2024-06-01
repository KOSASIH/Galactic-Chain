import hashlib
import time
from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///blockchain.db"
db = SQLAlchemy(app)

class Block(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    index = db.Column(db.Integer)
    timestamp = db.Column(db.Float)
    data = db.Column(db.String(100))
    previous_hash = db.Column(db.String(100))
    hash = db.Column(db.String(100))

class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.create_block(proof=1, previous_hash="0")

    def create_block(self, proof, previous_hash):
        block = {
            "index": len(self.chain) + 1,
            "timestamp": time.time(),
            "data": "",
            "previous_hash": previous_hash,
            "hash": "",
        }

        block["hash"] = self.calculate_hash(block)
        self.chain.append(block)

        return block

    def calculate_hash(self, block):
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def is_valid_chain(self, chain):
        for i in range(1, len(chain)):
            current_block = chain[i]
            previous_block = chain[i - 1]

            if current_block["previous_hash"]!= self.calculate_hash(previous_block):
                return False

            if current_block["hash"]!= self.calculate_hash(current_block):
                return False

        return True

    def replace_chain(self, chain):
        if self.is_valid_chain(chain) and len(chain) > len(self.chain):
            self.chain = chain

@app.before_first_request
def setup_blockchain():
    blockchain = Blockchain()
    db.create_all()
    db.session.add(blockchain)
    db.session.commit()

class BlockchainAPI(Resource):
    def get(self):
        return jsonify({"chain": self.blockchain.chain})

    def post(self):
        data = request.get_json()
        new_block = self.blockchain.create_block(data["proof"], data["previous_hash"])
        db.session.add(new_block)
        db.session.commit()
        return jsonify({"message": "New block added to the chain"})

api.add_resource(BlockchainAPI, "/blockchain")

if __name__ == "__main__":
    app.run(debug=True)
