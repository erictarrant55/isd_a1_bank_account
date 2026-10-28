__author__ = "Eric Tarrant"
__version__ = "1.0.0"

from events.event_listener import EventListener
from transaction.transaction import Transaction

class LoggingListener(EventListener):

    def update(self, sender: object) -> None:
        
        if not isinstance(sender, Transaction):
            raise TypeError("sender must be a Transaction type")

        print("TRANSACTION PROCESSED")
        print("-" * 80)
        print(f"ID: {sender.transaction_id}")
        print(f"STATUS: {sender.status.name}")
        print(f"AMOUNT: ${sender.amount:,.2f}")
        print(f"SOURCE ACCT: {sender.account.account_id}")
        print(f"AUTH CODE: {sender.authorization_code}")
        print("-" * 80)
        print()