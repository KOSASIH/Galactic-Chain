import hashlib
import time
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend

class Block:
    def __init__(self, index, previous_hash, transactions, timestamp=None):
        self.index = index
        self.previous_hash = previous_hash
        self.transactions = transactions
        self.timestamp = timestamp or int(time.time())
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        data_string = str(self.index) + self.previous_hash + str(self.transactions) + str(self.timestamp) + str(self.nonce)
        return hashlib.sha256(data_string.encode()).hexdigest()

    def mine_block(self, difficulty):
        while self.hash[:difficulty] != '0' * difficulty:
            self.nonce += 1
            self.hash = self.calculate_hash()

    def sign_block(self, private_key):
        signer = serialization.load_pem_private_key(private_key.encode(), password=None, backend=default_backend())
        signature = signer.sign(self.hash.encode(), padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH), hashes.SHA256())
        return signature

    def verify_signature(self, public_key, signature):
        verifier = serialization.load_pem_public_key(public_key.encode(), backend=default_backend())
        verifier.verify(signature, self.hash.encode(), padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH), hashes.SHA256())

    def __str__(self):
        return f'Block {self.index} - Hash: {self.hash} - Previous Hash: {self.previous_hash} - Transactions: {self.transactions} - Timestamp: {self.timestamp} - Nonce: {self.nonce}'

    def __repr__(self):
        return self.__str__()
