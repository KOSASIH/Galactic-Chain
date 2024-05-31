package tools

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"os"

	"github.com/mymodule/core/config"
)

func CreateGenesis(filename string, cfg *config.Config) error {
	genesis := &config.Genesis{
		Timestamp: time.Now().Unix(),
		Balances: map[string]uint64{
			"account1": 1000,
			"account2": 2000,
		},
	}

	data, err := json.MarshalIndent(genesis, "", "  ")
	if err != nil {
		return err
	}

	err = ioutil.WriteFile(filename, data, 0644)
	if err != nil {
		return err
	}

	fmt.Printf("Genesis file %s created successfully.\n", filename)
	return nil
}

func main() {
	cfg := config.NewConfig()
	err := CreateGenesis("genesis.json", cfg)
	if err != nil {
		fmt.Println("Error creating genesis file:", err)
		os.Exit(1)
	}
}
