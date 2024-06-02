import hashlib
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.backends import default_backend

class EllipticCurve:
    def __init__(self):
        self.curve = ec.SECP256K1()
        self.backend = default_backend()

    def generate_key_pair(self):
        private_key = ec.generate_private_key(self.curve, self.backend)
        public_key = private_key.public_key()
        return private_key, public_key

    def sign(self, private_key, message):
        signer = private_key.signer(padding=ec.ECDSA(max_size=32).padding, algorithm=ec.ECDSA(hash_func=hashlib.sha256))
        signature = signer.sign(message.encode())
        return signature

    def verify(self, public_key, message, signature):
        verifier = public_key.verifier(signature, padding=ec.ECDSA(max_size=32).padding, algorithm=ec.ECDSA(hash_func=hashlib.sha256))
        try:
            verifier.verify(message.encode())
            return True
        except InvalidSignature:
            return False
