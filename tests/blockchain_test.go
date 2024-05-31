package tests

import (
	"testing"

	"github.com/mymodule/core/blockchain"
)

func TestBlockchain(t *testing.T) {
	// Create a new blockchain instance
	bc, err := blockchain.NewBlockchain(nil)
	if err != nil {
		t.Fatal(err)
	}

	// Test blockchain methods
	t.Run("TestGetBlock", func(t *testing.T) {
		block, err := bc.GetBlock(0)
		if err != nil {
			t.Fatal(err)
		}
		if block == nil {
			t.Errorf("Expected block to be non-nil")
		}
	})

	t.Run("TestGetTransaction", func(t *testing.T) {
		tx, err := bc.GetTransaction("0x1234567890abcdef")
		if err != nil {
			t.Fatal(err)
		}
		if tx == nil {
			t.Errorf("Expected transaction to be non-nil")
		}
	})
}
