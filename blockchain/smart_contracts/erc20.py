from smart_contracts import SmartContract

class ERC20(SmartContract):
    def __init__(self, name, symbol, total_supply):
        self.name = name
        self.symbol = symbol
        self.total_supply = total_supply
        self.balances = {}

    def deploy(self):
        print(f'Deploying ERC20 contract {self.name} with symbol {self.symbol} and total supply {self.total_supply}')

    def execute(self, function, *args, **kwargs):
        if function == 'transfer':
            self.transfer(*args, **kwargs)
        elif function == 'approve':
            self.approve(*args, **kwargs)
        elif function == 'transfer_from':
            self.transfer_from(*args, **kwargs)

    def transfer(self, from_address, to_address, amount):
        if from_address not in self.balances:
            self.balances[from_address] = 0
        if to_address not in self.balances:
            self.balances[to_address] = 0
        if self.balances[from_address] >= amount:
            self.balances[from_address] -= amount
            self.balances[to_address] += amount
            print(f'Transferred {amount} {self.symbol} from {from_address} to {to_address}')
        else:
            print(f'Insufficient balance for {from_address}')

    def approve(self, owner, spender, amount):
        if owner not in self.balances:
            self.balances[owner] = 0
        if spender not in self.balances:
            self.balances[spender] = 0
        self.balances[owner] -= amount
        self.balances[spender] += amount
        print(f'Approved {amount} {self.symbol} for {spender} by {owner}')

    def transfer_from(self, from_address, to_address, amount):
        if from_address not in self.balances:
            self.balances[from_address] = 0
        if to_address not in self.balances:
            self.balances[to_address] = 0
        if self.balances[from_address] >= amount:
            self.balances[from_address] -= amount
            self.balances[to_address] += amount
            print(f'Transferred {amount} {self.symbol} from {from_address} to {to_address}')
        else:
            print(f'Insufficient balance for {from_address}')

    def get_balance(self, address):
        if address not in self.balances:
            self.balances[address] = 0
        return self.balances[address]

    def get_owner(self):
        return 'ERC20 Contract Owner'
