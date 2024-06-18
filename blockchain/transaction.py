import hashlib
import time
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend

class Transaction:
    def __init__(self, sender, recipient, amount, timestamp=None):
        self.sender = sender
        self.recipient = recipient
        self.amount = amount
        self.timestamp = timestamp or int(time.time())
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        data_string = self.sender + self.recipient + str(self.amount) + str(self.timestamp)
        return hashlib.sha256(data_string.encode()).hexdigest()

    def sign_transaction(self, private_key):
        signer = serialization.load_pem_private_key(private_key.encode(), password=None, backend=default_backend())
        signature = signer.sign(self.hash.encode(), padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH), hashes.SHA256())
        return signature

    def verify_signature(self, public_key, signature):
        verifier = serialization.load_pem_public_key(public_key.encode(), backend=default_backend())
        verifier.verify(signature, self.hash.encode(), padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH), hashes.SHA256())

    def to_json(self):
        return {
            'ender': self.sender,
            'ecipient': self.recipient,
            'amount': self.amount,
            'timestamp': self.timestamp,
            'hash': self.hash
        }

    @classmethod
    def from_json(cls, json_data):
        return cls(json_data['sender'], json_data['recipient'], json_data['amount'], json_data['timestamp'])

    def __str__(self):
        return f'Transaction from {self.sender} to {self.recipient} for {self.amount} at {self.timestamp}'

    def __repr__(self):
        return self.__str__()
