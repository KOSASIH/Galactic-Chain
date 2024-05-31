package tests

import (
	"testing"

	"github.com/mymodule/consensus"
)

func TestConsensus(t *testing.T) {
	// Create a new consensus instance
	cs, err := consensus.NewConsensus(nil)
	if err != nil {
		t.Fatal(err)
	}

	// Test consensus methods
	t.Run("TestValidateBlock", func(t *testing.T) {
		block := &blockchain.Block{}
		err := cs.ValidateBlock(block)
		if err != nil {
			t.Fatal(err)
		}
	})

	t.Run("TestGetValidators", func(t *testing.T) {
		validators, err := cs.GetValidators()
		if err != nil {
			t.Fatal(err)
		}
		if len(validators) == 0 {
			t.Errorf("Expected validators to be non-empty")
		}
	})
}
