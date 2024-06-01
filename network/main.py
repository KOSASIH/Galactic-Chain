from blockchain.blockchain import Blockchain
from blockchain.blockchain_storage import BlockchainStorage

if __name__ == "__main__":
    # Initialize the blockchain with a storage layer
    blockchain_storage = BlockchainStorage()
    blockchain = Blockchain(blockchain_storage)

    # Add blocks to the blockchain
    block1 = Block(1, [], "0x0000000000000000000000000000000000000000000000000000000000000000")
    block2 = Block(2, [], "0x0000000000000000000000000000000000000000000000000000000000000001")
    blockchain.add_block(block1)
    blockchain.add_block(block2)

    # Print the blockchain
    print("Blockchain:")
    for block in blockchain.blocks:
        print(block)

    # Get the latest block
    latest_block = blockchain.get_latest_block()
    print("Latest block:", latest_block)
