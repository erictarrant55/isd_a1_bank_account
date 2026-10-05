import unittest

from account.account_status import AccountStatus
from account.bank_account import BankAccount
from account.client import Client
from account.bank_transfer_transaction import BankTransferTransaction
from account.transaction_status import TransactionStatus
from decimal import Decimal

class TestInit(unittest.TestCase):
    def setUp(self) -> None:
        self.client = Client(
            1,
            "Eric Tarrant",
            "etarrant@rrc.ca"
        )

        self.account = BankAccount(
            123456,
            Decimal("5000.00"),
            self.client,
            AccountStatus.ACTIVE
        )

        self.target_account = BankAccount(
            676767,
            Decimal("1000.00"),
            self.client,
            AccountStatus.ACTIVE
        )
    
    def test_init_transaction_id_is_blank(self) -> None:
        # Arrange
        transaction_id = ""
        amount = Decimal("100.00")
        account = self.account
        target_account = self.target_account
        # Act
        with self.assertRaises(ValueError) as context:
            BankTransferTransaction(
                transaction_id,
                amount,
                account,
                target_account
            )
        # Assert
        expected = "transaction_id cannot be blank"
        actual = str(context.exception)
        self.assertEqual(expected, actual)

    def test_account_is_less_than_zero(self) -> None:
        # Arrange
        transaction_id = "123"
        amount = Decimal("100.00")
        account = ("-1.00")
        target_account = self.target_account
        # Act
        with self.assertRaises(ValueError) as context:
            BankTransferTransaction(
                transaction_id,
                amount,
                account,
                target_account
            )
        # Assert
        expected = "account must be a value greater than zero"
        actual = str(context.exception)
        self.assertEqual(expected, actual)

    def test_account_is_zero(self) -> None:
        # Arrange
        transaction_id = "123"
        amount = Decimal("100.00")
        account = ("0.00")
        target_account = self.target_account
        # Act
        with self.assertRaises(ValueError) as context:
            BankTransferTransaction(
                transaction_id,
                amount,
                account,
                target_account
            )
        # Assert
        expected = "account must be a value greater than zero"
        actual = str(context.exception)
        self.assertEqual(expected, actual)

    def test_initialize_new_instance(self) -> None:
        # Arrange
        transaction_id = "123"
        amount = Decimal("100.00")
        account = self.account
        target_account = self.target_account
        # Act
        transaction = BankTransferTransaction(
            transaction_id,
            amount,
            account,
            target_account
        )
        # Assert
        self.assertEqual(transaction_id, transaction.transaction_id)
        self.assertEqual(amount, transaction.amount)
        self.assertEqual(
            TransactionStatus.PENDING,
            transaction.status
        )
        self.assertEqual(account, transaction.account)
        self.assertEqual(
            target_account,
            transaction.target_account
        )

class TestFees(unittest.TestCase):
    """Defines tests for the fees property."""

    def setUp(self) -> None:
        self.client = Client(
            1,
            "Eric Tarrant",
            "etarrant@rrc.ca"
        )

        self.account = BankAccount(
            123456,
            Decimal("5000.00"),
            self.client,
            AccountStatus.ACTIVE
        )

        self.target_account = BankAccount(
            676767,
            Decimal("1000.00"),
            self.client,
            AccountStatus.ACTIVE
        )

    def test_returns_base_fee(self) -> None:
        # Arrange
        transaction = BankTransferTransaction(
            "123",
            Decimal("100.00"),
            self.account,
            self.target_account
        )

        # Act
        actual = transaction.fees

        # Assert
        expected = Decimal("1.00")
        self.assertEqual(expected, actual)

    def test_returns_percentage_of_transaction_amount(self) -> None:
        # Arrange
        transaction = BankTransferTransaction(
            "123",
            Decimal("1000.00"),
            self.account,
            self.target_account
        )

        # Act
        actual = transaction.fees

        # Assert
        expected = Decimal("7.000")
        self.assertEqual(expected, actual)


class TestProcess(unittest.TestCase):
    """Defines tests for the process method."""

    def setUp(self) -> None:
        self.client = Client(
            1,
            "Eric Tarrant",
            "etarrant@rrc.ca"
        )

        self.account = BankAccount(
            123456,
            Decimal("5000.00"),
            self.client,
            AccountStatus.ACTIVE
        )

        self.target_account = BankAccount(
            676767,
            Decimal("1000.00"),
            self.client,
            AccountStatus.ACTIVE
        )

    def test_account_status_is_not_active(self) -> None:
        # Arrange
        self.account._BankAccount__status = AccountStatus.SUSPENDED

        transaction = BankTransferTransaction(
            "123",
            Decimal("100.00"),
            self.account,
            self.target_account
        )

        # Act
        transaction.process()

        # Assert
        expected = TransactionStatus.FAILED
        actual = transaction.status
        self.assertEqual(expected, actual)

    def test_target_account_status_is_not_active(self) -> None:
        # Arrange
        self.target_account._BankAccount__status = AccountStatus.SUSPENDED

        transaction = BankTransferTransaction(
            "123",
            Decimal("100.00"),
            self.account,
            self.target_account
        )

        # Act
        transaction.process()

        # Assert
        expected = TransactionStatus.FAILED
        actual = transaction.status
        self.assertEqual(expected, actual)

    def test_amount_and_fees_are_greater_than_balance(self) -> None:
        # Arrange
        transaction = BankTransferTransaction(
            "123",
            Decimal("5000.00"),
            self.account,
            self.target_account
        )

        # Act
        transaction.process()

        # Assert
        expected = TransactionStatus.FAILED
        actual = transaction.status
        self.assertEqual(expected, actual)

    def test_transaction_is_processed(self) -> None:
        # Arrange
        transaction = BankTransferTransaction(
            "123",
            Decimal("100.00"),
            self.account,
            self.target_account
        )

        # Act
        transaction.process()

        # Assert
        self.assertEqual(
            TransactionStatus.PROCESSED,
            transaction.status
        )

        self.assertEqual(
            Decimal("4899.00"),
            self.account.balance
        )

        self.assertEqual(
            Decimal("1100.00"),
            self.target_account.balance
        )


class TestStr(unittest.TestCase):
    """Defines tests for the __str__ method."""

    def setUp(self) -> None:
        self.client = Client(
            1,
            "Eric Tarrant",
            "etarrant@rrc.ca"
        )

        self.account = BankAccount(
            123456,
            Decimal("5000.00"),
            self.client,
            AccountStatus.ACTIVE
        )

        self.target_account = BankAccount(
            676767,
            Decimal("1000.00"),
            self.client,
            AccountStatus.ACTIVE
        )

    def test_returns_string_representation(self) -> None:
        # Arrange
        transaction = BankTransferTransaction(
            "98765",
            Decimal("2983.35"),
            self.account,
            self.target_account
        )

        # Act
        actual = str(transaction)

        # Assert
        expected = (
            "ID: 98765\n"
            "STATUS: PENDING\n"
            "AMOUNT: $2,983.35\n"
            "SOURCE ACCT: 123456 --> TARGET ACCT: 676767"
        )

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()