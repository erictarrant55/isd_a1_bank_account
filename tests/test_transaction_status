import unittest

from transaction.transaction_status import TransactionStatus

__author__ = "Eric Tarrant"
__version__ = "1.0.0"


class TestInit(unittest.TestCase):
    """Defines tests to verify the enumeration values are initialized."""

    def test_pending(self) -> None:
        # Arrange
        expected = 1
        actual = TransactionStatus.PENDING
        # Act
        self.assertEqual(expected, actual)

    def test_processed(self) -> None:
        # Arrange
        expected = 2
        actual = TransactionStatus.PROCESSED
        
        # Act   
        self.assertEqual(expected, actual)

    def test_failed(self) -> None:
        # Arrange
        expected = 3
        actual = TransactionStatus.FAILED

        # Act
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()