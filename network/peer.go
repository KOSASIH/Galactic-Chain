package network

import (
	"fmt"
	"net"
)

type Peer struct {
	Node
	ID string
}

func NewPeer(node Node, id string) *Peer {
	return &Peer{
		Node:   node,
		ID:     id,
	}
}

func (p *Peer) String() string {
	return fmt.Sprintf("%s:%d (ID: %s)", p.Address, p.Port, p.ID)
}
