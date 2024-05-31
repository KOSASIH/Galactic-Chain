package utils

import (
	"crypto/ecdsa"
	"crypto/elliptic"
	"crypto/rand"
	"crypto/sha256"
	"encoding/hex"
	"fmt"
	"math/big"
)

func VerifySignature(publicKey, message, signature string) bool {
	curve := elliptic.P256()
	x, y := curve.ScalarBaseMult(fromHex(publicKey))
	publicKey := ecdsa.PublicKey{Curve: curve, X: x, Y: y}

	signatureBytes, err := hex.DecodeString(signature)
	if err != nil {
		fmt.Println(err)
		return false
	}

	r := big.Int{}
	s := big.Int{}
	_, err = fmt.Sscanf(string(signatureBytes), "0x%x 0x%x", &r, &s)
	if err != nil {
		fmt.Println(err)
		return false
	}

	hashed := sha256.Sum256([]byte(message))
	valid := ecdsa.Verify(&publicKey, hashed[:], &r, &s)

	return valid
}

func fromHex(input string) *big.Int {
	output, err := new(big.Int).SetString(input, 16)
	if err != nil {
		fmt.Println(err)
		return nil
	}
	return output
}
