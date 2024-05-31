package tools

import (
	"fmt"
	"io/ioutil"
	"net"
	"os"

	"github.com/mymodule/network"
)

func CreatePeer(addr string) error {
	conn, err := net.Dial("tcp", addr)
	if err != nil {
		return err
	}
	defer conn.Close()

	peer := &network.Peer{
		Conn: conn,
		ID:   fmt.Sprintf("peer-%d", time.Now().Unix()),
	}

	err = peer.Handshake()
	if err != nil {
		return err
	}

	fmt.Printf("Peer %s created successfully.\n", peer.ID)
	return nil
}

func main() {
	addr := "localhost:12345"
	err := CreatePeer(addr)
	if err != nil {
	fmt.Println("Error creating peer:", err)
		os.Exit(1)
	}
}
