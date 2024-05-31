package main

import (
	"fmt"
	"log"

	"github.com/mymodule/core/blockchain"
	"github.com/mymodule/config"
)

func main() {
	// Load configuration
	cfg, err := config.LoadConfig("config.json")
	if err!= nil {
		log.Fatal(err)
	}

	// Create a new blockchain instance
	bc, err := blockchain.NewBlockchain(cfg)
	if err!= nil {
		log.Fatal(err)
	}

	// Start the blockchain
	bc.Start()

	fmt.Println("Blockchain started successfully!")
}
