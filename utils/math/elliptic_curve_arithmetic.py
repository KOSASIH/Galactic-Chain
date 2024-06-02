import hashlib
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.backends import default_backend

class EllipticCurveArithmetic:
    def __init__(self):
        self.curve = ec.SECP256K1()
        self.backend = default_backend()

    def generate_key_pair(self):
        private_key = ec.generate_private_key(self.curve, self.backend)
        public_key = private_key.public_key()
        return private_key, public_key

    def perform_operation(self, operation, params):
        if operation == "add":
            point1 = self.decode_point(params["point1"])
            point2 = self.decode_point(params["point2"])
            result = point1 + point2
            return self.encode_point(result)
        elif operation == "multiply":
            point = self.decode_point(params["point"])
            scalar = int(params["scalar"])
            result = point * scalar
            return self.encode_point(result)
        elif operation == "hash":
            message = params["message"]
            hash = hashlib.sha256(message.encode()).digest()
            return hash.hex()
        else:
            raise ValueError("Invalid operation")

    def decode_point(self, point):
        x, y = point.split(",")
        x = int(x, 16)
        y = int(y, 16)
        return self.curve.point(x, y)

    def encode_point(self, point):
        x = format(point.x, "x")
        y = format(point.y, "x")
        return f"{x},{y}"

ecc = EllipticCurveArithmetic()
