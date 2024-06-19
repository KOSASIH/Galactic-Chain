import random
import time

class Validator:
    def __init__(self, address, stake):
        self.address = address
        self.stake = stake
        self.last_validated = 0

    def is_eligible_to_validate(self):
        now = int(time.time())
        if now - self.last_validated > 60:  # validate every minute
            return True
        return False

class PoSConsensus:
    def __init__(self, validators):
        self.validators = validators

    def select_validator(self):
        total_stake = sum([v.stake for v in self.validators])
        stake_sum = 0
        selected_validator = None
        for v in self.validators:
            stake_sum += v.stake / total_stake
            if random.random() < stake_sum:
                selected_validator = v
                break
        return selected_validator

    def validate_transaction(self, transaction):
        validator = self.select_validator()
        if validator.is_eligible_to_validate():
            # validate the transaction
            # reward the validator
            validator.last_validated = int(time.time())
