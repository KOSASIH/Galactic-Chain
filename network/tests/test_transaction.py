import unittest
from transaction.transaction import Transaction
from transaction.transaction_validator import TransactionValidator

class TestTransaction(unittest.TestCase):
    def setUp(self):
        self.transaction_validator = TransactionValidator()
        self.transaction = Transaction(1, "sender", "recipient", 10.0)

    def test_transaction_init(self):
        self.assertEqual(self.transaction.transaction_id, 1)
        self.assertEqual(self.transaction.sender, "sender")
        self.assertEqual(self.transaction.recipient, "recipient")
        self.assertEqual(self.transaction.amount, 10.0)

    def test_transaction_validate(self):
        self.assertTrue(self.transaction_validator.validate(self.transaction))

    def test_transaction_invalid_sender(self):
        self.transaction.sender = ""
        self.assertFalse(self.transaction_validator.validate(self.transaction))

    def test_transaction_invalid_recipient(self):
        self.transaction.recipient = ""
        self.assertFalse(self.transaction_validator.validate(self.transaction))

    def test_transaction_invalid_amount(self):
        self.transaction.amount = -10.0
        self.assertFalse(self.transaction_validator.validate(self.transaction))

if __name__ == "__main__":
    unittest.main()
