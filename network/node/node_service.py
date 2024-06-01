from.transaction_validator import TransactionValidator
from.block_validator import BlockValidator

class NodeService:
    def __init__(self, transaction_validator, block_validator):
        self.transaction_validator = transaction_validator
        self.block_validator = block_validator

    def validate_transaction(self, transaction):
        return self.transaction_validator.validate(transaction)

    def validate_block(self, block):
        return self.block_validator.validate(block)
