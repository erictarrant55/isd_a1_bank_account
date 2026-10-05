import unittest
from decimal import Decimal

from account.account_status import AccountStatus
from account.bank_account import BankAccount
from account.client import Client


class TestBankAccount(unittest.TestCase):

    def setUp(self):
        self.client = Client(
            1001,
            "Eric Tarrant",
            "etarrant@rrc.ca"
        )

        self.account = BankAccount(
            20019,
            Decimal("400.00"),
            self.client,
            AccountStatus.ACTIVE
        )

    def test_init_account_id_less_than_zero(self):
        try:
            BankAccount(
                -1,
                Decimal("400.00"),
                self.client,
                AccountStatus.ACTIVE
            )
        except ValueError as exception:
            self.assertEqual(type(exception), ValueError)
            self.assertEqual(
                str(exception),
                "account_id must be a value greater than zero"
            )

    def test_init_account_id_is_zero(self):
        try:
            BankAccount(
                0,
                Decimal("400.00"),
                self.client,
                AccountStatus.ACTIVE
            )
        except ValueError as exception:
            self.assertEqual(type(exception), ValueError)
            self.assertEqual(
                str(exception),
                "account_id must be a value greater than zero"
            )

    def test_init_account_id(self):
        self.assertEqual(
            self.account._BankAccount__account_id,
            20019
        )

    def test_init_balance(self):
        self.assertEqual(
            self.account._BankAccount__balance,
            Decimal("400.00")
        )

    def test_init_owner(self):
        self.assertEqual(
            self.account._BankAccount__owner,
            self.client
        )

    def test_init_status(self):
        self.assertEqual(
            self.account._BankAccount__status,
            AccountStatus.ACTIVE
        )

    def test_update_balance_increase(self):
        self.account.update_balance(Decimal("100.00"))

        self.assertEqual(
            self.account.balance,
            Decimal("500.00")
        )

    def test_update_balance_decrease(self):
        self.account.update_balance(Decimal("-100.00"))

        self.assertEqual(
            self.account.balance,
            Decimal("300.00")
        )

    def test_deposit_increases_balance(self):
        self.account.deposit(Decimal("100.00"))

        self.assertEqual(
            self.account.balance,
            Decimal("500.00")
        )

    def test_deposit_amount_zero(self):
        self.account.deposit(Decimal("0.00"))

        self.assertEqual(
            self.account.balance,
            Decimal("400.00")
        )

    def test_deposit_negative_amount(self):
        try:
            self.account.deposit(Decimal("-100.00"))
        except ValueError as exception:
            self.assertEqual(type(exception), ValueError)
            self.assertEqual(
                str(exception),
                "amount must be a value greater than or equal to zero"
            )

    def test_withdraw_decreases_balance(self):
        self.account.withdraw(Decimal("100.00"))

        self.assertEqual(
            self.account.balance,
            Decimal("300.00")
        )

    def test_withdraw_amount_zero(self):
        self.account.withdraw(Decimal("0.00"))

        self.assertEqual(
            self.account.balance,
            Decimal("400.00")
        )

    def test_withdraw_negative_amount(self):
        try:
            self.account.withdraw(Decimal("-100.00"))
        except ValueError as exception:
            self.assertEqual(type(exception), ValueError)
            self.assertEqual(
                str(exception),
                "amount must be a value greater than or equal to zero"
            )

    def test_withdraw_amount_exceeds_balance(self):
        try:
            self.account.withdraw(Decimal("500.00"))
        except ValueError as exception:
            self.assertEqual(type(exception), ValueError)
            self.assertEqual(
                str(exception),
                "amount cannot exceed the account balance"
            )

    def test_str(self):
        self.account.deposit(Decimal("6364.67"))

        self.assertEqual(
            str(self.account),
            "Account Number: 20019 Balance: $6,764.67"
        )


if __name__ == '__main__':
    unittest.main()