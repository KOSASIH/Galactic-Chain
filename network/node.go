package network

import (
	"fmt"
	"net"
)

type Node struct {
	Address string
	Port    int
	Conn    net.Conn
}

func NewNode(address string, port int) *Node {
	return &Node{
		Address: address,
		Port:    port,
	}
}

func (n *Node) Connect() error {
	conn, err := net.Dial("tcp", fmt.Sprintf("%s:%d", n.Address, n.Port))
	if err != nil {
		return err
	}
	n.Conn = conn
	return nil
}

func (n *Node) Disconnect() {
	n.Conn.Close()
}
