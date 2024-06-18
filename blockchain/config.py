import os

class Config:
    def __init__(self):
        self.node_host = 'localhost'
        self.node_port = 8080
        self.wallet_filename = 'wallet.pem'
        self.blockchain_filename = 'blockchain.json'
        self.difficulty = 2
        self.mining_reward = 10

    def save_config(self, filename):
        with open(filename, 'w') as f:
            f.write(f'node_host={self.node_host}\n')
            f.write(f'node_port={self.node_port}\n')
            f.write(f'wallet_filename={self.wallet_filename}\n')
            f.write(f'blockchain_filename={self.blockchain_filename}\n')
            f.write(f'difficulty={self.difficulty}\n')
            f.write(f'mining_reward={self.mining_reward}\n')

    def load_config(self, filename):
        with open(filename, 'r') as f:
           lines = f.readlines()
            for line in lines:
                key, value = line.strip().split('=')
                if key == 'node_host':
                    self.node_host = value
                elif key == 'node_port':
                    self.node_port = int(value)
                elif key == 'wallet_filename':
                    self.wallet_filename = value
                elif key == 'blockchain_filename':
                    self.blockchain_filename = value
                elif key == 'difficulty':
                    self.difficulty = int(value)
                elif key == 'ining_reward':
                    self.mining_reward = int(value)
