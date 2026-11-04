import unittest
from decimal import Decimal
 
from fee.percentage_fee_strategy import PercentageFeeStrategy
__author__ = "Eric Tarrant"
__version__ = "1.0.0"
 
 
class TestInit(unittest.TestCase):
    """Defines tests for the __init__ method."""
 
    def test_percentage_is_less_than_zero(self) -> None:
        # Arrange
        percentage = Decimal("-0.01")
 
        # Act
        with self.assertRaises(ValueError) as context:
            PercentageFeeStrategy(percentage)
 
        # Assert
        expected = "percentage must be a value between 0 and 1 (inclusive)"
        actual = str(context.exception)
        self.assertEqual(expected, actual)
 
    def test_percentage_is_greater_than_one(self) -> None:
        # Arrange
        percentage = Decimal("1.01")
 
        # Act
        with self.assertRaises(ValueError) as context:
            PercentageFeeStrategy(percentage)
 
        # Assert
        expected = "percentage must be a value between 0 and 1 (inclusive)"
        actual = str(context.exception)
        self.assertEqual(expected, actual)
 
    def test_percentage_is_zero(self) -> None:
        # Arrange
        percentage = Decimal("0")
 
        # Act
        strategy = PercentageFeeStrategy(percentage)
 
        # Assert
        self.assertEqual(percentage, strategy._PercentageFeeStrategy__percentage)
 
    def test_percentage_is_one(self) -> None:
        # Arrange
        percentage = Decimal("1")
 
        # Act
        strategy = PercentageFeeStrategy(percentage)
 
        # Assert
        self.assertEqual(percentage, strategy._PercentageFeeStrategy__percentage)
 
    def test_initialize_new_instance(self) -> None:
        # Arrange
        percentage = Decimal("0.02")
 
        # Act
        strategy = PercentageFeeStrategy(percentage)
 
        # Assert
        self.assertEqual(percentage, strategy._PercentageFeeStrategy__percentage)
 
 
class TestGetFee(unittest.TestCase):
    """Defines tests for the get_fee method."""
 
    def test_returns_percentage_of_transaction_amount(self) -> None:
        # Arrange
        strategy = PercentageFeeStrategy(Decimal("0.02"))
 
        # Act
        actual = strategy.get_fee(Decimal("1000.00"))
 
        # Assert
        expected = Decimal("20.00")
        self.assertEqual(expected, actual)
 
    def test_fee_is_rounded_to_two_decimal_places(self) -> None:
        # Arrange
        strategy = PercentageFeeStrategy(Decimal("0.015"))
 
        # Act
        actual = strategy.get_fee(Decimal("100.01"))
 
        # Assert
        expected = Decimal("1.50")
        self.assertEqual(expected, actual)
 
 
if __name__ == "__main__":
    unittest.main()