package crypto

import (
	"crypto/ecdsa"
	"crypto/elliptic"
	"crypto/rand"
	"crypto/sha256"
	"errors"
	"golang.org/x/crypto/sha3"
)

func Sign(privateKey *ecdsa.PrivateKey, data []byte) ([]byte, error) {
	r, s, err := ecdsa.Sign(rand.Reader, privateKey, sha256.New224(), data)
	if err != nil {
		return nil, err
	}
	signature := make([]byte, 0, 64)
	signature = append(signature, r.Bytes()...)
	signature = append(signature, s.Bytes()...)
	return signature, nil
}

func Verify(publicKey *ecdsa.PublicKey, data []byte, signature []byte) error {
	x, y := publicKey.X, publicKey.Y
	if x == nil || y == nil {
		return errors.New("invalid public key")
	}
	r := new(big.Int).SetBytes(signature[:32])
	s := new(big.Int).SetBytes(signature[32:])
	hash := sha3.New224()
	hash.Write(data)
	return ecdsa.Verify(publicKey, hash.Sum(nil), r, s)
}
