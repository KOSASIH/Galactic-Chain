package consensus

import (
	"math/rand"
	"strconv"
	"time"
)

// generateNewBlockWithPoA generates a new block in the blockchain using Proof of Authority.
func generateNewBlockWithPoA(prevBlock Block, data string, difficulty int, authorities []string) Block {
	timestamp := time.Now().Unix()
	newBlock := Block{
		Index:        prevBlock.Index + 1,
		Timestamp:    timestamp,
		PrevHash:     prevBlock.Hash,
		Data:         data,
		Nonce:        0,
		Difficulty:   difficulty,
	}
	// Select a random authority
	rand.Seed(time.Now().UnixNano())
	authorityIndex := rand.Intn(len(authorities))
	authority := authorities[authorityIndex]
	newBlock.Hash = calculateHash(newBlock, authority)
	return newBlock
}
