import torch
import numpy as np
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

def generate_keys():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
    )
    public_key = private_key.public_key()
    return private_key, public_key

def encrypt_model(model, public_key):
    encrypted_model = {}
    for k, v in model.state_dict().items():
        encrypted_v = public_key.encrypt(
            v.numpy().tobytes(),
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        encrypted_model[k] = encrypted_v
    return encrypted_model

def decrypt_model(encrypted_model, private_key):
    decrypted_model = {}
    for k, v in encrypted_model.items():
        decrypted_v = private_key.decrypt(
            v,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        decrypted_model[k] = torch.from_numpy(np.frombuffer(decrypted_v, dtype=np.float32))
    return decrypted_model

def secure_aggregation(client_models, client_weights=None):
    private_key, public_key = generate_keys()
    encrypted_client_models = [encrypt_model(model, public_key) for model in client_models]
    aggregated_model = federated_learning_aggregate(encrypted_client_models, client_weights)
    decrypted_aggregated_model = decrypt_model(aggregated_model, private_key)
    return decrypted_aggregated_model
