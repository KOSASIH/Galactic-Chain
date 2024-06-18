import argparse
import json
import os
import sys
from getpass import getpass
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend

from wallet import Wallet
from explorer import BlockchainExplorer

class CLI:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description='Blockchain CLI')
        self.subparsers = self.parser.add_subparsers(dest='command')

        self.wallet_parser = self.subparsers.add_parser('wallet', help='Wallet commands')
        self.wallet_subparsers = self.wallet_parser.add_subparsers(dest='wallet_command')

        self.create_wallet_parser = self.wallet_subparsers.add_parser('create', help='Create a new wallet')
        self.create_wallet_parser.add_argument('--password', help='Password for the wallet')

        self.import_wallet_parser = self.wallet_subparsers.add_parser('import', help='Import an existing wallet')
        self.import_wallet_parser.add_argument('private_key', help='Private key to import')

        self.export_wallet_parser = self.wallet_subparsers.add_parser('export', help='Export the wallet')
        self.export_wallet_parser.add_argument('--password', help='Password for the wallet')

        self.get_address_parser = self.wallet_subparsers.add_parser('get_address', help='Get the wallet address')
        self.get_balance_parser = self.wallet_subparsers.add_parser('get_balance', help='Get the wallet balance')

        self.send_parser = self.subparsers.add_parser('send', help='Send tokens')
        self.send_parser.add_argument('recipient', help='Recipient address')
        self.send_parser.add_argument('amount', help='Amount to send')

        self.explorer_parser = self.subparsers.add_parser('explorer', help='Blockchain explorer commands')
        self.explorer_subparsers = self.explorer_parser.add_subparsers(dest='explorer_command')

        self.get_block_parser = self.explorer_subparsers.add_parser('get_block', help='Get a block by height')
        self.get_block_parser.add_argument('block_height', help='Block height')

        self.get_transaction_parser = self.explorer_subparsers.add_parser('get_transaction', help='Get a transaction by hash')
        self.get_transaction_parser.add_argument('transaction_hash', help='Transaction hash')

        self.get_address_info_parser = self.explorer_subparsers.add_parser('get_address_info', help='Get address information')
        self.get_address_info_parser.add_argument('address', help='Address')

    def create_wallet(self, args):
        password = args.password
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
            backend=default_backend()
        )
        private_key_pem = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        )
        with open('wallet.pem', 'wb') as f:
            f.write(private_key_pem)
        print(f'Wallet created with password {password}')

    def import_wallet(self, args):
        private_key = args.private_key
        with open('wallet.pem', 'wb') as f:
            f.write(private_key.encode())
        print('Wallet imported')

    def export_wallet(self, args):
        password = args.password
        with open('wallet.pem', 'rb') as f:
            private_key_pem = f.read()
        private_key = serialization.load_pem_private_key(private_key_pem, password=password, backend=default_backend())
        print(f'Wallet exported with password {password}')

    def get_address(self, args):
        wallet = Wallet()
        address = wallet.generate_address()
        print(f'Wallet address: {address}')

    def get_balance(self, args):
        wallet = Wallet()
        balance = wallet.get_balance()
        print(f'Wallet balance: {balance}')

    def send(self, args):
        wallet = Wallet()
        recipient = args.recipient
        amount = int(args.amount)
        transaction = wallet.create_transaction(recipient, amount)
        wallet.send_transaction(transaction)
        print(f'Transaction sent to {recipient} with amount {amount}')

    def get_block(self, args):
        explorer = BlockchainExplorer()
        block_height = int(args.block_height)
        block = explorer.get_block(block_height)
        print(json.dumps(block, indent=4))

    def get_transaction(self, args):
        explorer = BlockchainExplorer()
        transaction_hash = args.transaction_hash
        transaction = explorer.get_transaction(transaction_hash)
        print(json.dumps(transaction, indent=4))

    def get_address_info(self, args):
        explorer = BlockchainExplorer()
        address = args.address
        address_info = explorer.get_address(address)
        print(json.dumps(address_info, indent=4))

    def run(self):
        if len(sys.argv) == 1:
            self.parser.print_help()
            sys.exit(1)

        args = self.parser.parse_args()

        if args.command == 'wallet':
            if args.wallet_command == 'create':
                self.create_wallet(args)
            elif args.wallet_command == 'import':
                self.import_wallet(args)
            elif args.wallet_command == 'export':
                self.export_wallet(args)
            elif args.wallet_command == 'get_address':
                self.get_address(args)
            elif args.wallet_command == 'get_balance':
                self.get_balance(args)
        elif args.command == 'send':
            self.send(args)
        elif args.command == 'explorer':
            if args.explorer_command == 'get_block':
                self.get_block(args)
            elif args.explorer_command == 'get_transaction':
                self.get_transaction(args)
            elif args.explorer_command == 'get_address_info':
                self.get_address_info(args)

if __name__ == '__main__':
    cli = CLI()
    cli.run()
