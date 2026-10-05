import unittest
from decimal import Decimal

from account.account_status import AccountStatus
from account.bank_account import BankAccount
from account.client import Client
from transaction.credit_card_transaction import CreditCardTransaction
from transaction.transaction_status import TransactionStatus
__author__ = "Eric Tarrant"
__version__ = "1.0.0"


class TestInit(unittest.TestCase):
    """Defines tests for the __init__ method."""

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

    def test_transaction_id_is_blank_string(self) -> None:
        # Arrange
        transaction_id = ""
        amount = Decimal("100.00")
        account = self.account
        authorization_code = "AUTH123"

        # Act
        with self.assertRaises(ValueError) as context:
            CreditCardTransaction(
                transaction_id,
                amount,
                account,
                authorization_code
            )

        # Assert
        expected = "transaction_id cannot be blank"
        actual = str(context.exception)
        self.assertEqual(expected, actual)

    def test_amount_is_less_than_zero(self) -> None:
        # Arrange
        transaction_id = "123"
        amount = Decimal("-1.00")
        account = self.account
        authorization_code = "AUTH123"

        # Act
        with self.assertRaises(ValueError) as context:
            CreditCardTransaction(
                transaction_id,
                amount,
                account,
                authorization_code
            )

        # Assert
        expected = "amount must be greater than zero"
        actual = str(context.exception)
        self.assertEqual(expected, actual)

    def test_amount_is_zero(self) -> None:
        # Arrange
        transaction_id = "123"
        amount = Decimal("0.00")
        account = self.account
        authorization_code = "AUTH123"

        # Act
        with self.assertRaises(ValueError) as context:
            CreditCardTransaction(
                transaction_id,
                amount,
                account,
                authorization_code
            )

        # Assert
        expected = "amount must be greater than zero"
        actual = str(context.exception)
        self.assertEqual(expected, actual)

    def test_initialize_new_instance(self) -> None:
        # Arrange
        transaction_id = "123"
        amount = Decimal("100.00")
        account = self.account
        authorization_code = "AUTH123"

        # Act
        transaction = CreditCardTransaction(
            transaction_id,
            amount,
            account,
            authorization_code
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
            authorization_code,
            transaction.authorization_code
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

    def test_returns_two_percent_of_transaction_amount(self) -> None:
        # Arrange
        transaction = CreditCardTransaction(
            "123",
            Decimal("100.00"),
            self.account,
            "AUTH123"
        )

        # Act
        actual = transaction.fees

        # Assert
        expected = Decimal("2.00")
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

    def test_account_status_is_not_active(self) -> None:
        # Arrange
        self.account._BankAccount__status = AccountStatus.SUSPENDED

        transaction = CreditCardTransaction(
            "123",
            Decimal("100.00"),
            self.account,
            "AUTH123"
        )

        # Act
        transaction.process()

        # Assert
        expected = TransactionStatus.FAILED
        actual = transaction.status
        self.assertEqual(expected, actual)

    def test_amount_and_fees_are_greater_than_balance(self) -> None:
        # Arrange
        transaction = CreditCardTransaction(
            "123",
            Decimal("5000.00"),
            self.account,
            "AUTH123"
        )

        # Act
        transaction.process()

        # Assert
        expected = TransactionStatus.FAILED
        actual = transaction.status
        self.assertEqual(expected, actual)

    def test_authorization_code_is_blank(self) -> None:
        # Arrange
        transaction = CreditCardTransaction(
            "123",
            Decimal("100.00"),
            self.account,
            ""
        )

        # Act
        transaction.process()

        # Assert
        expected = TransactionStatus.FAILED
        actual = transaction.status
        self.assertEqual(expected, actual)

    def test_transaction_is_processed(self) -> None:
        # Arrange
        transaction = CreditCardTransaction(
            "123",
            Decimal("100.00"),
            self.account,
            "AUTH123"
        )

        # Act
        transaction.process()

        # Assert
        self.assertEqual(
            TransactionStatus.PROCESSED,
            transaction.status
        )

        self.assertEqual(
            Decimal("4898.00"),
            self.account.balance
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

    def test_returns_string_representation(self) -> None:
        # Arrange
        transaction = CreditCardTransaction(
            "98765",
            Decimal("2983.35"),
            self.account,
            "c13d9c63-d8c3-4876-a00c-81ab7c3ff1fc"
        )

        # Act
        actual = str(transaction)

        # Assert
        expected = (
            "ID: 98765\n"
            "STATUS: PENDING\n"
            "AMOUNT: $2,983.35\n"
            "SOURCE ACCT: 123456\n"
            "AUTH CODE: c13d9c63-d8c3-4876-a00c-81ab7c3ff1fc"
        )

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()