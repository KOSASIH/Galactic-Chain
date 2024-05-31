package blockchain

import (
	"encoding/json"
)

type Tx struct {
	From  string `json:"from"`
	To    string `json:"to"`
	Value uint   `json:"value"`
	Data  string `json:"data"`
}

func (t Tx) IsReward() bool {
	return t.Data == "reward"
}

func (t Tx) Serialize() ([]byte, error) {
	return json.Marshal(t)
}

func DeserializeTx(d []byte) (*Tx, error) {
	var tx Tx
	err := json.Unmarshal(d, &tx)
	return &tx, err
}
