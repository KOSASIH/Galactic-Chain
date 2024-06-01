import cryptography

class Encryption:
    def __init__(self):
        self.key = cryptography.generate_key()

    def encrypt_data(self, data):
        # Encrypt data using the generated key
        pass

    def decrypt_data(self, encrypted_data):
        # Decrypt data using the generated key
        pass
