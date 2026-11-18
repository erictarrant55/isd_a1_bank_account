"""Defines the TransactionDialog class."""

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QDialog,
                               QLayout,
                               QVBoxLayout,
                               QHBoxLayout,
                               QFormLayout,
                               QWidget,
                               QGroupBox,
                               QLabel,
                               QComboBox,
                               QLineEdit,
                               QPushButton,
                               QSizePolicy)

__author__ = "COMP-2327 Faculty"
__version__ = "1.0.0"

class TransactionDialog(QDialog):
    """Represents a dialog window contain details about a BankAccount.
    """

    def __init__(self):
        """Initializes a new instance of the LookupWindow class."""

        super().__init__()

        self.setFixedWidth(400)
        self.setFixedHeight(260)
        self.setModal(True)

        main_layout = QVBoxLayout(self)

        self.__initialize_widgets(main_layout)

    def __initialize_widgets(self, main_layout: QLayout) -> None:
        """Initializes the widgets on this dialog window."""

        main_layout.addWidget(self.__initialize_account_details())
        main_layout.addWidget(self.__initialize_transaction_details())

        container = QWidget()
        layout = QHBoxLayout(container)
        layout.setContentsMargins(0, 0, 0, 0)

        process_button = QPushButton("Process")
        process_button.setFixedWidth(100)
        process_button.setDefault(True)

        layout.addStretch()
        layout.addWidget(process_button)

        self._process_transaction_button = process_button

        main_layout.addWidget(container)

    def __initialize_account_details(self) -> QGroupBox:
        """Initializes the account details group box.

        Returns:
            QGroupBox: The account details group box.
        """

        groupbox = QGroupBox("Account Details")
        layout = QFormLayout(groupbox)
        layout.setLabelAlignment(Qt.AlignmentFlag.AlignRight)

        label = QLabel("Account #:")
        account_number_label = QLabel("999999")

        layout.addRow(label, account_number_label)

        label = QLabel("Current Balance:")
        current_balance_label = QLabel("$9,990.00")

        layout.addRow(label, current_balance_label)

        self._account_number_label = account_number_label
        self._current_balance_label = current_balance_label

        groupbox.setMinimumHeight(80)

        return groupbox

    def __initialize_transaction_details(self) -> QGroupBox:
        """Initializes the transaction details group box.

        Returns:
            QGroupBox: The transaction details group box.
        """

        groupbox = QGroupBox("Transaction")
        layout = QFormLayout(groupbox)
        layout.setLabelAlignment(Qt.AlignmentFlag.AlignRight)

        label = QLabel("Type:")
        type_combobox = QComboBox(editable=False)
        type_combobox.addItem("Deposit")
        type_combobox.addItem("Withdraw")
        self.__set_width(type_combobox)

        layout.addRow(label, type_combobox)

        label = QLabel("Amount:")
        amount_line_edit = QLineEdit()
        amount_line_edit.setAlignment(Qt.AlignmentFlag.AlignRight)
        amount_line_edit.setFixedWidth(100)
        layout.addRow(label, amount_line_edit)

        error_label = QLabel("ERROR")
        error_label.setStyleSheet("color: #FF2C2C")

        layout.addRow(error_label)

        self._transaction_type_combobox = type_combobox
        self._amount_line_edit = amount_line_edit
        self._transaction_error_label = error_label

        groupbox.setMinimumHeight(80)

        return groupbox

    def __set_width(self, combobox: QComboBox) -> None:
        """Sets the minimum width of the QComboBox to fit the widest
        item.

        Args:
            combobox (QComboBox): The QComboBox to update the width of.
        """

        font_metrics = combobox.fontMetrics()
        maximum_width = 0

        # Iterate through all items
        for index in range(combobox.count()):
            # Get the text representation
            text = combobox.itemText(index)

            # Calculate the width of the text
            text_width = font_metrics.horizontalAdvance(text)

            # Add space for the dropdown arrow
            total_width = text_width + 50

            if total_width > maximum_width:
                maximum_width = total_width

        # Apply the calculated width.
        combobox.setFixedWidth(maximum_width)
