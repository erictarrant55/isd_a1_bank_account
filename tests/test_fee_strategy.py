import unittest
from decimal import Decimal
 
from fee.fee_strategy import FeeStrategy
__author__ = "Eric Tarrant"
__version__ = "1.0.0"
 
 
class IncompleteStrategy(FeeStrategy):
    """Subclass that does not implement get_fee."""
    pass
 
 
class FlatFeeStrategy(FeeStrategy):
    """Subclass that implements get_fee."""
 
    def get_fee(self, transaction_amount: Decimal) -> Decimal:
        return Decimal("1.00")
 
 
class TestInit(unittest.TestCase):
    """Defines tests for the FeeStrategy interface."""
 
    def test_interface_cannot_be_instantiated(self) -> None:
        # Arrange
        # Act
        with self.assertRaises(TypeError):
            FeeStrategy()
 
        # Assert
 
    def test_subclass_without_get_fee_cannot_have_instance(self) -> None:
        # Arrange
        # Act
        with self.assertRaises(TypeError):
            IncompleteStrategy()
 
        # Assert
 
    def test_subclass_with_get_fee_can_have_instance(self) -> None:
        # Arrange
        # Act
        strategy = FlatFeeStrategy()
 
        # Assert
        self.assertIsInstance(strategy, FeeStrategy)
        self.assertEqual(
            Decimal("1.00"),
            strategy.get_fee(Decimal("100.00"))
        )