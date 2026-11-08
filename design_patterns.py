"""This module includes a program to demonstrate your understanding of
the Design Patterns used in this project.
"""
from decimal import Decimal

from transaction.credit_card_transaction import CreditCardTransaction
from fee.percentage_fee_strategy import PercentageFeeStrategy
from fee.base_percentage_fee_strategy import BasePercentageFeeStrategy
from events.logging_listener import LoggingListener
from account.bank_account import BankAccount
from account.account_status import AccountStatus
from account.client import Client

__author__ = "Eric Tarrant"
__version__ = "1.0.0"


def main() -> None:
    """The program's main entry point."""

    # 1. Create a transaction instance.

    client = Client(
        12345,
        "Eric Tarrant",
        "eric@example.com"
    )

    account = BankAccount(
        777777777,
        Decimal("5000.00"),
        client,
        AccountStatus.ACTIVE
    )

    transaction = CreditCardTransaction(
        "12345",
        Decimal("1000.00"),
        account,
        authorization_code="AUTH123"
    )

    # 2. Print the transaction fee.
    print(transaction.fees)

    # 3. Create a new instance of a fee strategy.
    # The fee is determined by whichever is higher:
    # the base fee ($1.26) or 0.07% of the transaction amount.

    fee_strategy = BasePercentageFeeStrategy(
        Decimal("1.26"),
        Decimal("0.0007")
    )

    # 4. Update the transaction to use the fee strategy.
    transaction.set_fee_strategy(fee_strategy)

    # 5. Print the transaction fees.
    print(transaction.fees)

    # 6. Update the transaction to use percentage-only fees.
    # The fee is 0.35% of the transaction amount.

    fee_strategy = PercentageFeeStrategy(
        Decimal("0.0035")
    )

    transaction.set_fee_strategy(fee_strategy)

    # 7. Print the transaction fees.
    print(transaction.fees)

    # 8. Create a logging listener instance.
    listener = LoggingListener()

    # 9. Subscribe the listener to the processed event.
    transaction.on_processed.add_listener(listener)

    # 10. Invoke the method to raise the event.
    transaction.process()


if __name__ == "__main__":
    main()