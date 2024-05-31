package consensus

import (
	"math/rand"
	"strconv"
	"time"
)

// generateNewBlockWithHybrid generates a new block in the blockchain using a hybrid consensus algorithm.
func generateNewBlockWithHybrid(prevBlock Block, data string, difficulty int, validators []string, authorities []string) Block {
	timestamp := time.Now().Unix()
	newBlock := Block{
		Index:        prevBlock.Index + 1,
		Timestamp:    timestamp,
		PrevHash:     prevBlock.Hash,
		Data:         data,
		Nonce:        0,
		Difficulty:   difficulty,
	}
	// Select a random validator and authority
	rand.Seed(time.Now().UnixNano())
	validatorIndex := rand.Intn(len(validators))
	validator := validators[validatorIndex]
	authorityIndex := rand.Intn(len(authorities))
	authority := authorities[authorityIndex]
	newBlock.Hash = calculateHash(newBlock, validator, authority)
	return newBlock
}
