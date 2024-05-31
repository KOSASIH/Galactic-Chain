package consensus

import (
	"math/rand"
	"strconv"
	"time"
)

// generateNewBlockWithPoS generates a new block in the blockchain using Proof of Stake.
func generateNewBlockWithPoS(prevBlock Block, data string, difficulty int, validators []string) Block {
	timestamp := time.Now().Unix()
	newBlock := Block{
		Index:        prevBlock.Index + 1,
		Timestamp:    timestamp,
		PrevHash:     prevBlock.Hash,
		Data:         data,
		Nonce:        0,
		Difficulty:   difficulty,
	}
	// Select a random validator
	rand.Seed(time.Now().UnixNano())
	validatorIndex := rand.Intn(len(validators))
	validator := validators[validatorIndex]
	newBlock.Hash = calculateHash(newBlock, validator)
	return newBlock
}
