from smart_contracts import SmartContract

class ERC721(SmartContract):
    def __init__(self, name, symbol, total_supply):
        self.name = name
        self.symbol = symbol
        self.total_supply = total_supply
        self.token_owners = {}

    def deploy(self):
        print(f'Deploying ERC721 contract {self.name} with symbol {self.symbol} and total supply {self.total_supply}')

    def execute(self, function, *args, **kwargs):
        if function == 'mint':
            self.mint(*args, **kwargs)
        elif function == 'transfer':
            self.transfer(*args, **kwargs)
        elif function == 'approve':
            self.approve(*args, **kwargs)
        elif function == 'get_owner':
            self.get_owner(*args, **kwargs)

    def mint(self, to_address, token_id):
        if token_id not in self.token_owners:
            self.token_owners[token_id] = to_address
            print(f'Minted token {token_id} to {to_address}')
        else:
            print(f'Token {token_id} already exists')

    def transfer(self, from_address, to_address, token_id):
        if token_id in self.token_owners:
            if self.token_owners[token_id] == from_address:
                self.token_owners[token_id] = to_address
                print(f'Transferred token {token_id} from {from_address} to {to_address}')
            else:
               print(f'Only the owner {self.token_owners[token_id]} can transfer token {token_id}')
        else:
            print(f'Token {token_id} does not exist')

    def approve(self, owner, approved_address, token_id):
        if token_id in self.token_owners:
            if self.token_owners[token_id] == owner:
                self.token_owners[token_id] = approved_address
                print(f'Approved token {token_id} for {approved_address} by {owner}')
            else:
                print(f'Only the owner {self.token_owners[token_id]} can approve token {token_id}')
        else:
            print(f'Token {token_id} does not exist')

    def get_owner(self, token_id):
        if token_id in self.token_owners:
            return self.token_owners[token_id]
        else:
            return None

    def get_balance(self, address):
        return len([token_id for token_id, owner in self.token_owners.items() if owner == address])

    def get_owner(self):
        return 'ERC721 Contract Owner'
