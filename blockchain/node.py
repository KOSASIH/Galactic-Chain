import socket
import threading
import time
from blockchain import Blockchain
from pow import ProofOfWork
from transaction import Transaction
from wallet import Wallet

class Node:
    def __init__(self, host, port, blockchain, wallet):
        self.host = host
        self.port = port
        self.blockchain = blockchain
        self.wallet = wallet
        self.pow = ProofOfWork(self.blockchain)
        self.peers = []
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((self.host, self.port))
        self.socket.listen(5)

    def start(self):
        print(f'Node started on {self.host}:{self.port}')
        self.listen_for_peers()

    def listen_for_peers(self):
        while True:
            client_socket, address = self.socket.accept()
            print(f'Connected to {address}')
            client_thread = threading.Thread(target=self.handle_client, args=(client_socket,))
            client_thread.start()

    def handle_client(self, client_socket):
        while True:
            message = client_socket.recv(1024).decode()
            if message == 'get_blockchain':
                self.send_blockchain(client_socket)
            elif message == 'get_pending_transactions':
                self.send_pending_transactions(client_socket)
            elif message.startswith('transaction'):
                self.handle_transaction(message, client_socket)
            elif message.startswith('block'):
                self.handle_block(message, client_socket)

    def send_blockchain(self, client_socket):
        blockchain_json = self.blockchain.to_json()
        client_socket.sendall(blockchain_json.encode())

    def send_pending_transactions(self, client_socket):
        pending_transactions_json = [tx.to_json() for tx in self.blockchain.pending_transactions]
        client_socket.sendall(json.dumps(pending_transactions_json).encode())

    def handle_transaction(self, message, client_socket):
        transaction_json = message.split(':')[1]
        transaction = Transaction.from_json(transaction_json)
        self.blockchain.add_transaction(transaction)
        client_socket.sendall('Transaction added to pending transactions'.encode())

    def handle_block(self, message, client_socket):
        block_json = message.split(':')[1]
        block = Block.from_json(block_json)
        self.blockchain.add_block(block)
        client_socket.sendall('Block added to blockchain'.encode())

    def mine_block(self):
        while True:
            if len(self.blockchain.pending_transactions) > 0:
                new_block = self.pow.mine_block(self.wallet)
                self.blockchain.add_block(new_block)
                print(f'Mined block {new_block.index} with {len(new_block.transactions)} transactions')
            time.sleep(10)

    def start_mining(self):
        mining_thread = threading.Thread(target=self.mine_block)
        mining_thread.start()

    def connect_to_peer(self, host, port):
        peer_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        peer_socket.connect((host, port))
        self.peers.append(peer_socket)

    def broadcast_transaction(self, transaction):
        for peer in self.peers:
            peer.sendall(f'transaction:{transaction.to_json()}'.encode())

    def broadcast_block(self, block):
        for peer in self.peers:
            peer.sendall(f'block:{block.to_json()}'.encode())
