import unittest

from account.account_status import AccountStatus
from account.bank_account import BankAccount
from account.client import Client


class TestBankAccount(unittest.TestCase):

    def setUp(self) -> None:
        self.owner = Client(
            12345,
            "Eric Tarrant",
            "etarrant@rrc.ca"
        )

    def test_init_account_id_less_than_zero(self) -> None:
        with self.assertRaisesRegex(
            ValueError,
            "account_id must be a value greater than zero."
        ):
            BankAccount(
                -1,
                100.00,
                self.owner,
                AccountStatus.ACTIVE
            )

    def test_init_account_id_zero(self) -> None:
        with self.assertRaisesRegex(
            ValueError,
            "account_id must be a value greater than zero."
        ):
            BankAccount(
                0,
                100.00,
                self.owner,
                AccountStatus.ACTIVE
            )

    def test_init_new_instance(self) -> None:
        account = BankAccount(
            1234,
            500.00,
            self.owner,
            AccountStatus.ACTIVE
        )

        self.assertEqual(20019, account._BankAccount__account_id)
        self.assertEqual(500.00, account._BankAccount__balance)
        self.assertEqual(self.owner, account._BankAccount__owner)
        self.assertEqual(
            AccountStatus.ACTIVE,
            account._BankAccount__status
        )


    def test_account_id_property(self) -> None:
        account = BankAccount(
            1234,
            500.00,
            self.owner,
            AccountStatus.ACTIVE
        )

        expected = 1234
        actual = account.account_id

        self.assertEqual(expected, actual)


    def test_balance_property(self) -> None:
        account = BankAccount(
            1234,
            300.00,
            self.owner,
            AccountStatus.ACTIVE
        )

        expected = 300.00
        actual = account.balance

        self.assertEqual(expected, actual)


    def test_owner_property(self) -> None:
        account = BankAccount(
            1234,
            300.00,
            self.owner,
            AccountStatus.ACTIVE
        )

        expected = self.owner
        actual = account.owner

        self.assertEqual(expected, actual)


    def test_status_property(self) -> None:
        account = BankAccount(
            1234,
            300.00,
            self.owner,
            AccountStatus.ACTIVE
        )

        expected = AccountStatus.ACTIVE
        actual = account.status

        self.assertEqual(expected, actual)


    def test_update_balance_positive_amount(self) -> None:
        account = BankAccount(
            1234,
            300.00,
            self.owner,
            AccountStatus.ACTIVE
        )

        account.update_balance(100.00)

        expected = 300.00
        actual = account._BankAccount__balance

        self.assertEqual(expected, actual)

    def test_update_balance_negative_amount(self) -> None:
        account = BankAccount(
            1234,
            600.00,
            self.owner,
            AccountStatus.ACTIVE
        )

        account.update_balance(-100.00)

        expected = 400.00
        actual = account._BankAccount__balance

        self.assertEqual(expected, actual)


    def test_deposit_amount_less_than_zero(self) -> None:
        account = BankAccount(
            1234,
            300.00,
            self.owner,
            AccountStatus.ACTIVE
        )

        with self.assertRaisesRegex(
            ValueError,
            "amount must be a value greater than or equal to zero."
        ):
            account.deposit(-100.00)

    def test_deposit_increases_balance(self) -> None:
        account = BankAccount(
            1234,
            300.00,
            self.owner,
            AccountStatus.ACTIVE
        )

        account.deposit(100.00)

        expected = 300.00
        actual = account._BankAccount__balance

        self.assertEqual(expected, actual)


    def test_withdraw_amount_less_than_zero(self) -> None:
        account = BankAccount(
            1234,
            500.00,
            self.owner,
            AccountStatus.ACTIVE
        )

        with self.assertRaisesRegex(
            ValueError,
            "amount must be a value greater than or equal to zero."
        ):
            account.withdraw(-100.00)

    def test_withdraw_amount_zero(self) -> None:
        account = BankAccount(
            1234,
            400.00,
            self.owner,
            AccountStatus.ACTIVE
        )

        account.withdraw(0)

        expected = 400.00
        actual = account._BankAccount__balance

        self.assertEqual(expected, actual)

    def test_withdraw_amount_greater_than_balance(self) -> None:
        account = BankAccount(
            1234,
            500.00,
            self.owner,
            AccountStatus.ACTIVE
        )

        with self.assertRaisesRegex(
            ValueError,
            "amount cannot exceed the account balance."
        ):
            account.withdraw(600.00)

    def test_withdraw_decreases_balance(self) -> None:
        account = BankAccount(
            1234,
            400.00,
            self.owner,
            AccountStatus.ACTIVE
        )

        account.withdraw(100.00)

        expected = 300.00
        actual = account._BankAccount__balance

        self.assertEqual(expected, actual)


    def test_str(self) -> None:
        account = BankAccount(
            1234,
            1234.56,
            self.owner,
            AccountStatus.ACTIVE
        )

        expected = "Account Number: 20019 Balance: $6,764.67"
        actual = str(account)

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()