# galactic_chain/network/p2p/libp2p.py

import asyncio
import json
import hashlib
import base64
from libp2p import Libp2p
from libp2p.crypto import Crypto
from libp2p.network import Network
from libp2p.peer import Peer
from libp2p.protocol import Protocol
from libp2p.stream import Stream
from libp2p.multiformats import CID
from libp2p.dht import DHT
from libp2p.kad import Kademlia
from libp2p.routing import Routing

class GalacticChainPeer(Peer):
    def __init__(self, node_id, private_key, public_key):
        super().__init__(node_id, private_key, public_key)
        self.chain = []  # Store the blockchain data
        self.peers = {}  # Store connected peers
        self.blocks_to_send = asyncio.Queue()  # Queue for sending blocks
        self.dht = DHT(self)  # Distributed Hash Table
        self.kad = Kademlia(self)  # Kademlia routing
        self.routing = Routing(self)  # Routing table

    async def handle_stream(self, stream: Stream):
        async for message in stream:
            if message.type == "block":
                block = json.loads(message.data.decode())
                self.chain.append(block)
                print(f"Received block {block['index']} from {stream.remote_peer}")
                # Verify block and update chain
                self.verify_block(block)
                # Broadcast block to other peers
                await self.broadcast_block(block)
            elif message.type == "get_chain":
                print(f"Received get_chain request from {stream.remote_peer}")
                await stream.write(json.dumps(self.chain).encode())
            elif message.type == "peer_info":
                peer_info = json.loads(message.data.decode())
                self.peers[peer_info["id"]] = peer_info["address"]
                print(f"Received peer info from {stream.remote_peer}")
            elif message.type == "dht_query":
                query = json.loads(message.data.decode())
                result = await self.dht.query(query)
                await stream.write(json.dumps(result).encode())
            elif message.type == "kad_query":
                query = json.loads(message.data.decode())
                result = await self.kad.query(query)
                await stream.write(json.dumps(result).encode())
            elif message.type == "routing_update":
                update = json.loads(message.data.decode())
                self.routing.update(update)
                print(f"Received routing update from {stream.remote_peer}")

    async def broadcast_block(self, block):
        for peer_id, peer_address in self.peers.items():
            if peer_id!= self.id:
                try:
                    stream = await self.connect(peer_address)
                    await stream.write(json.dumps(block).encode(), "block")
                    print(f"Sent block {block['index']} to {peer_id}")
                except Exception as e:
                    print(f"Error sending block to {peer_id}: {e}")

    def verify_block(self, block):
        # Verify block hash and signature
        block_hash = hashlib.sha256(json.dumps(block).encode()).hexdigest()
        if block_hash!= block["hash"]:
            raise ValueError("Invalid block hash")
        # Verify block signature
        signature = base64.b64decode(block["signature"])
        if not Crypto.verify_signature(self.public_key, block_hash.encode(), signature):
            raise ValueError("Invalid block signature")
        # Update chain
        self.chain.append(block)

class GalacticChainProtocol(Protocol):
    def __init__(self, peer: GalacticChainPeer):
        super().__init__(peer)
        self.peer = peer

    async def handle_message(self, message: bytes):
        if message.startswith(b"block:"):
            block = json.loads(message[6:].decode())
            self.peer.chain.append(block)
            print(f"Received block {block['index']} from {self.peer.id}")
            # Verify block and update chain
            self.peer.verify_block(block)
            # Broadcast block to other peers
            await self.peer.broadcast_block(block)
        elif message.startswith(b"get_chain:"):
            print(f"Received get_chain request from {self.peer.id}")
            await self.peer.stream.write(json.dumps(self.peer.chain).encode())
        elif message.startswith(b"peer_info:"):
            peer_info = json.loads(message[9:].decode())
            self.peer.peers[peer_info["id"]] = peer_info["address"]
            print(f"Received peer info from {self.peer.id}")
        elif message.startswith(b"dht_query:"):
            query = json.loads(message[10:].decode())
            result = await self.peer.dht.query(query)
            await self.peer.stream.write(json.dumps(result).encode())
        elif message.startswith(b"kad_query:"):
query = json.loads(message[7:].decode())
            result = await self.peer.kad.query(query)
            await self.peer.stream.write(json.dumps(result).encode())
        elif message.startswith(b"routing_update:"):
            update = json.loads(message[14:].decode())
            self.peer.routing.update(update)
            print(f"Received routing update from {self.peer.id}")

async def main():
    # Create a libp2p node
    node = Libp2p()

    # Generate a key pair
    private_key, public_key = Crypto.generate_key_pair()

    # Create a peer
    peer = GalacticChainPeer(node.id, private_key, public_key)

    # Create a protocol
    protocol = GalacticChainProtocol(peer)

    # Add the protocol to the node
    node.add_protocol(protocol)

    # Start the node
    await node.start()

    # Connect to other peers
    await node.connect("QmHashOfOtherPeer")

    # Send a block to another peer
    block = {"index": 1, "transactions": [], "hash": "0x123456", "signature": "0xabcdef"}
    await node.send("QmHashOfOtherPeer", json.dumps(block).encode(), "block")

    # Get the chain from another peer
    await node.send("QmHashOfOtherPeer", "get_chain".encode(), "get_chain")

    # Query the DHT
    query = {"key": "value"}
    await node.send("QmHashOfOtherPeer", json.dumps(query).encode(), "dht_query")

    # Query Kademlia
    query = {"key": "value"}
    await node.send("QmHashOfOtherPeer", json.dumps(query).encode(), "kad_query")

    # Update the routing table
    update = {"key": "value"}
    await node.send("QmHashOfOtherPeer", json.dumps(update).encode(), "routing_update")
