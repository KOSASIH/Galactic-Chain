from smart_contracts.erc20 import ERC20

class GalacticToken(ERC20):
    def __init__(self, name, symbol, total_supply):
        super().__init__(name, symbol, total_supply)

    def deploy(self):
        print(f'Deploying GalacticToken contract {self.name} with symbol {self.symbol} and total supply {self.total_supply}')

    def execute(self, function, *args, **kwargs):
        if function == 'launch_spaceship':
            self.launch_spaceship(*args, **kwargs)
        else:
            super().execute(function, *args, **kwargs)

    def launch_spaceship(self, address, amount):
        if address in self.balances:
            if self.balances[address] >= amount:
                self.balances[address] -= amount
                print(f'Launched spaceship for {address} with {amount} {self.symbol}')
            else:
                print(f'Insufficient balance for {address}')
        else:
            print(f'Address {address} does not exist')

    def get_balance(self, address):
        return super().get_balance(address)

    def get_owner(self):
        return super().get_owner()
