package crypto

import (
	"crypto/sha256"
	"encoding/hex"
)

func Hash(data []byte) []byte {
	hasher := sha256.New()
	hasher.Write(data)
	return hasher.Sum(nil)
}

func HashString(data string) string {
	hash := Hash([]byte(data))
	return hex.EncodeToString(hash)
}
