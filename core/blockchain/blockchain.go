package blockchain

import (
	"encoding/json"
	"fmt"
	"log"

	"github.com/boltdb/bolt"
)

type Blockchain struct {
	tip []byte
	db  *bolt.DB
}

func NewBlockchain() *Blockchain {
	db, err := bolt.Open("blockchain.db", 0600, nil)
	if err!= nil {
		log.Panic(err)
	}
	return &Blockchain{tip: []byte{}, db: db}
}

func (bc *Blockchain) AddBlock(data []byte) {
	var lastHash []byte
	err := bc.db.Update(func(tx *bolt.Tx) error {
		b := tx.Bucket([]byte("blocks"))
		lastHash = b.Get([]byte("l"))
		block := NewBlock(data, lastHash)
		err := b.Put(block.Hash, block.Serialize())
		if err!= nil {
			return err
		}
		b.Put([]byte("l"), block.Hash)
		return nil
	})
	if err!= nil {
		log.Panic(err)
	}
}

func (bc *Blockchain) Iterator() *BlockchainIterator {
	return &BlockchainIterator{bc.tip, bc.db}
}

type BlockchainIterator struct {
	currentHash []byte
	db          *bolt.DB
}

func (i *BlockchainIterator) Next() *Block {
	var block *Block
	err := i.db.View(func(tx *bolt.Tx) error {
		b := tx.Bucket([]byte("blocks"))
		blockBytes := b.Get(i.currentHash)
		block, _ = DeserializeBlock(blockBytes)
		return nil
	})
	if err!= nil {
		log.Panic(err)
	}
	i.currentHash = block.PrevBlockHash
	return block
}
