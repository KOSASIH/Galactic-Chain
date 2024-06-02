# galactic_chain/core/algorithms/quantum_resistant_crypto.py

import numpy as np
from scipy.linalg import qr


class NTRUCryptosystem:
    def __init__(self, n, q, p, d):
        """
        Initialize the NTRU cryptosystem.

        :param n: Dimension of the lattice
        :param q: Large modulus
        :param p: Small modulus
        :param d: Degree of the polynomial ring
        """
        self.n = n
        self.q = q
        self.p = p
        self.d = d
        self.poly_ring = PolynomialRing(n, d)

    def keygen(self):
        """
        Generate a public and private key pair.

        :return: (public_key, private_key)
        """
        f = self.poly_ring.random_element()
        g = self.poly_ring.random_element()
        F = f * g % self.q
        h = F * g ^ -1 % self.q
        public_key = h
        private_key = (f, g)
        return public_key, private_key

    def encrypt(self, message, public_key):
        """
        Encrypt a message using the public key.

        :param message: Message to encrypt
        :param public_key: Public key
        :return: Ciphertext
        """
        r = self.poly_ring.random_element()
        e = self.poly_ring.random_element()
        c = (r * public_key + e) % self.q
        return c

    def decrypt(self, ciphertext, private_key):
        """
        Decrypt a ciphertext using the private key.

        :param ciphertext: Ciphertext to decrypt
        :param private_key: Private key
        :return: Decrypted message
        """
        f, g = private_key
        a = ciphertext * f ^ -1 % self.q
        b = a * g % self.q
        return b


class PolynomialRing:
    def __init__(self, n, d):
        """
        Initialize the polynomial ring.

        :param n: Dimension of the lattice
        :param d: Degree of the polynomial ring
        """
        self.n = n
        self.d = d
        self.modulus = 2**d - 1

    def random_element(self):
        """
        Generate a random polynomial in the ring.

        :return: Random polynomial
        """
        coeffs = np.random.randint(0, self.modulus, size=self.n)
        return np.poly1d(coeffs)

    def __mul__(self, a, b):
        """
        Multiply two polynomials in the ring.

        :param a: First polynomial
        :param b: Second polynomial
        :return: Product of the two polynomials
        """
        return np.poly1d(np.convolve(a.c, b.c) % self.modulus)

    def __add__(self, a, b):
        """
        Add two polynomials in the ring.

        :param a: First polynomial
        :param b: Second polynomial
        :return: Sum of the two polynomials
        """
        return np.poly1d((a.c + b.c) % self.modulus)

    def __sub__(self, a, b):
        """
        Subtract two polynomials in the ring.

        :param a: First polynomial
        :param b: Second polynomial
        :return: Difference of the two polynomials
        """
        return np.poly1d((a.c - b.c) % self.modulus)

    def __truediv__(self, a, b):
        """
        Divide two polynomials in the ring.

        :param a: Dividend
        :param b: Divisor
        :return: Quotient of the two polynomials
        """
        q, r = qr(a.c, b.c)
        return np.poly1d(q)


def main():
    n = 512
    q = 2048
    p = 3
    d = 11

    ntru = NTRUCryptosystem(n, q, p, d)
    public_key, private_key = ntru.keygen()

    message = np.random.randint(0, 2, size=n)
    ciphertext = ntru.encrypt(message, public_key)
    decrypted_message = ntru.decrypt(ciphertext, private_key)

    print("Public Key:", public_key)
    print("Private Key:", private_key)
    print("Message:", message)
    print("Ciphertext:", ciphertext)
    print("Decrypted Message:", decrypted_message)


if __name__ == "__main__":
    main()
