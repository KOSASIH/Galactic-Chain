import os
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend

class Wallet:
    def __init__(self):
        self.private_key, self.public_key = self.generate_keys()

    def generate_keys(self):
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
            backend=default_backend()
        )
        public_key = private_key.public_key()
        return private_key, public_key

    def save_keys(self, filename):
        private_pem = self.private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        )
        public_pem = self.public_key.public_bytes(
            encoding=serialization.Encoding.OpenSSH,
            format=serialization.PublicFormat.OpenSSH
        )
        with open(filename, 'wb') as f:
            f.write(private_pem)
            f.write(public_pem)

    def load_keys(self, filename):
        with open(filename, 'rb') as f:
            private_pem = f.read()
            public_pem = f.read()
        self.private_key = serialization.load_pem_private_key(private_pem, password=None, backend=default_backend())
        self.public_key = serialization.load_ssh_public_key(public_pem, backend=default_backend())

    def get_private_key(self):
        return self.private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        ).decode()

    def get_public_key(self):
        return self.public_key.public_bytes(
            encoding=serialization.Encoding.OpenSSH,
            format=serialization.PublicFormat.OpenSSH
        ).decode()
