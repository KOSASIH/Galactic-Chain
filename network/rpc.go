package network

import (
	"context"
	"errors"
	"net"
	"net/rpc"
)

type RPCClient struct {
	client *rpc.Client
}

func NewRPCClient(conn net.Conn) *RPCClient {
	client := rpc.NewClient(conn)
	return &RPCClient{
		client: client,
	}
}

func (c *RPCClient) Call(serviceMethod string, args interface{}, reply interface{}) error {
	err := c.client.Call(serviceMethod, args, reply)
	if err != nil {
		return err
	}
	return nil
}

func (c *RPCClient) Close() {
	c.client.Close()
}

type RPCServer struct {
	server *rpc.Server
}

func NewRPCServer() *RPCServer {
	server := rpc.NewServer()
	return &RPCServer{
		server: server,
	}
}

func (s *RPCServer) Register(service interface{}) error {
	return s.server.Register(service)
}

func (s *RPCServer) ServeConn(conn net.Conn) {
	s.server.ServeConn(conn)
}

func (s *RPCServer) Close() {
	s.server.Close()
}
