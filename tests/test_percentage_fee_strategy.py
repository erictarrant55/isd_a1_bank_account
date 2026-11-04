import unittest
from decimal import Decimal
 
from fee.base_percentage_fee_strategy import BasePercentageFeeStrategy
__author__ = "Eric Tarrant"
__version__ = "1.0.0"
 
 
class TestInit(unittest.TestCase):
    """Defines tests for the __init__ method."""
 
    def test_base_fee_is_less_than_zero(self) -> None:
        # Arrange
        base_fee = Decimal("-1.00")
        percentage = Decimal("0.02")
 
        # Act
        with self.assertRaises(ValueError) as context:
            BasePercentageFeeStrategy(base_fee, percentage)
 
        # Assert
        expected = "base_fee must be greater than or equal to zero"
        actual = str(context.exception)
        self.assertEqual(expected, actual)
 
    def test_percentage_is_less_than_zero(self) -> None:
        # Arrange
        base_fee = Decimal("5.00")
        percentage = Decimal("-0.01")
 
        # Act
        with self.assertRaises(ValueError) as context:
            BasePercentageFeeStrategy(base_fee, percentage)
 
        # Assert
        expected = "percentage must be a value between 0 and 1 (inclusive)"
        actual = str(context.exception)
        self.assertEqual(expected, actual)
 
    def test_percentage_is_greater_than_one(self) -> None:
        # Arrange
        base_fee = Decimal("5.00")
        percentage = Decimal("1.01")
 
        # Act
        with self.assertRaises(ValueError) as context:
            BasePercentageFeeStrategy(base_fee, percentage)
 
        # Assert
        expected = "percentage must be a value between 0 and 1 (inclusive)"
        actual = str(context.exception)
        self.assertEqual(expected, actual)
 
    def test_base_fee_is_zero(self) -> None:
        # Arrange
        base_fee = Decimal("0.00")
        percentage = Decimal("0.02")
 
        # Act
        strategy = BasePercentageFeeStrategy(base_fee, percentage)
 
        # Assert
        self.assertEqual(
            base_fee,
            strategy._BasePercentageFeeStrategy__base_fee
        )
 
    def test_initialize_new_instance(self) -> None:
        # Arrange
        base_fee = Decimal("5.00")
        percentage = Decimal("0.02")
 
        # Act
        strategy = BasePercentageFeeStrategy(base_fee, percentage)
 
        # Assert
        self.assertEqual(
            base_fee,
            strategy._BasePercentageFeeStrategy__base_fee
        )
        self.assertEqual(
            percentage,
            strategy._BasePercentageFeeStrategy__percentage
        )
 
 
class TestGetFee(unittest.TestCase):
    """Defines tests for the get_fee method."""
 
    def setUp(self) -> None:
        self.strategy = BasePercentageFeeStrategy(
            Decimal("5.00"),
            Decimal("0.02")
        )
 
    def test_percentage_is_greater_than_base_fee(self) -> None:
        # Arrange
        amount = Decimal("1000.00")
 
        # Act
        actual = self.strategy.get_fee(amount)
 
        # Assert
        expected = Decimal("20.00")
        self.assertEqual(expected, actual)
 
    def test_percentage_is_less_than_base_fee(self) -> None:
        # Arrange
        amount = Decimal("100.00")
 
        # Act
        actual = self.strategy.get_fee(amount)
 
        # Assert
        expected = Decimal("5.00")
        self.assertEqual(expected, actual)
 
 
if __name__ == "__main__":
    unittest.main()