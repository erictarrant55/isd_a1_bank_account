from account.account_status import AccountStatus

import unittest

class TestInit(unittest.TestCase):
    """Defines test for __init__"""
    def test_inactive(self) -> None:
            expected = 0
            actual = AccountStatus.INACTIVE

            self.assertEqual(expected, actual)

    def test_active(self) -> None:
        expected = 1
        actual = AccountStatus.ACTIVE

        self.assertEqual(expected, actual)

    def test_suspended(self) -> None:
        expected = 2
        actual = AccountStatus.SUSPENDED

        self.assertEqual(expected, actual)

    def test_closed(self) -> None:
        expected = 3
        actual = AccountStatus.CLOSED

        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()    