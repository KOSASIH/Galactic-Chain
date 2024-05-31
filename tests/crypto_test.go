package tests

import (
	"testing"

	"github.com/mymodule/crypto"
)

func TestCrypto(t *testing.T) {
	// Test hash function
	t.Run("TestHash", func(t *testing.T) {
		hash := crypto.Hash([]byte("hello world"))
		if len(hash) != 32 {
			t.Errorf("Expected hash to be 32 bytes")
		}
	})

	// Test signature function
	t.Run("TestSign", func(t *testing.T) {
		privKey, err := crypto.GeneratePrivateKey()
		if err != nil {
			t.Fatal(err)
		}
		sig, err := crypto.Sign(privKey, []byte("hello world"))
		if err != nil {
			t.Fatal(err)
		}
		if len(sig) == 0 {
			t.Errorf("Expected signature to be non-empty")
		}
	})
}
