"""Defines the MainWindow class."""

__author__ = "COMP-2327 Faculty"
__version__ = "1.0.0"

from PySide6.QtCore import Qt
from PySide6.QtGui import QAction
from PySide6.QtWidgets import (QMainWindow,
                               QWidget,
                               QGroupBox,
                               QLayout,
                               QHBoxLayout,
                               QVBoxLayout,
                               QFormLayout,
                               QLabel,
                               QLineEdit,
                               QPushButton,
                               QTableWidget,
                               QHeaderView,
                               QAbstractItemView,
                               QSizePolicy)

class MainWindow(QMainWindow):
    """Represents a main window for looking up BankAccounts."""

    def __init__(self):
        """Initializes a new instance of the LookupWindow class."""

        super().__init__()

        self.setFixedWidth(600)
        self.setMinimumHeight(400)
        self.setWindowFlag(Qt.WindowType.WindowTitleHint.WindowMaximizeButtonHint, False)
        self.setWindowFlag(Qt.WindowType.WindowTitleHint.CustomizeWindowHint, True)

        container = QWidget()
        self.setCentralWidget(container)

        root_layout = QVBoxLayout(container)

        self.__initialize_menu_bar()

        root_layout.addWidget(self.__initialize_client_search())

        self._search_error_label = QLabel("ERROR")
        self._search_error_label.setStyleSheet("color: #FF2C2C")

        root_layout.addWidget(self._search_error_label)

        root_layout.addWidget(self.__initialize_client_groupbox())
        root_layout.addWidget(self.__initialize_accounts_table_groupbox())

    def __initialize_menu_bar(self) -> None:
        """Initializes the menu bar."""

        menubar = self.menuBar()

        file_menu = menubar.addMenu("&File")
        file_menu.setMinimumWidth(180)
        exit_action = QAction("E&xit", self)
        exit_action.setShortcut("Alt+F4")
        file_menu.addAction(exit_action)

        edit_menu = menubar.addMenu("&Edit")
        edit_menu.setMinimumWidth(180)
        clear_action = QAction("&Clear")
        clear_action.setShortcut("Ctrl+Shift+R")
        edit_menu.addAction(clear_action)

        help_menu = menubar.addMenu("&Help")
        help_menu.setMinimumWidth(180)
        about_action = QAction("&About", self)
        help_menu.addAction(about_action)

        self._exit_action = exit_action
        self._clear_action = clear_action
        self._about_action = about_action

    def __initialize_client_search(self) -> QWidget:
        """Initializes the client search widget.

        Returns:
            QWidget: The client search widget.
        """

        container = QWidget()
        layout = QHBoxLayout(container)
        layout.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)

        label = QLabel("Client #:")

        self._client_number_line_edit = QLineEdit()

        layout.addWidget(label)
        layout.addWidget(self._client_number_line_edit)

        search_button = QPushButton("&Search")
        search_button.setAutoDefault(True)

        layout.addWidget(search_button)

        container.setSizePolicy(QSizePolicy.Policy.Fixed,
                                QSizePolicy.Policy.Fixed)

        self._search_button = search_button

        return container

    def __initialize_client_groupbox(self) -> QGroupBox:
        """Returns a GroupBox containing the client details widgets.

        Returns:
            QGroupBox: A GroupBox containing the client details widgets.
        """

        groupbox = QGroupBox("Client")
        groupbox.setSizePolicy(QSizePolicy.Policy.Expanding,
                               QSizePolicy.Policy.Fixed)

        layout = QFormLayout(groupbox)
        layout.setLabelAlignment(Qt.AlignmentFlag.AlignRight)
        layout.setVerticalSpacing(15)

        name_label = QLabel("XXXXXX XXXXXX")
        layout.addRow(QLabel("Name:"), name_label)

        email_label = QLabel("XXXXXX@XXXXXX")
        layout.addRow(QLabel("Email:"), email_label)

        self._name_label = name_label
        self._email_label = email_label

        return groupbox

    def __initialize_accounts_table_groupbox(self) -> QGroupBox:
        """Returns a GroupBox containing the accounts table.

        Returns:
            QGroupBox: A GroupBox containing the accounts table.
        """

        COLUMN_HEADERS = ["Account #",
                          "Balance",
                          "Status"]

        groupbox = QGroupBox("Accounts")
        layout = QHBoxLayout(groupbox)

        self._account_table = QTableWidget()

        self._account_table.setColumnCount(len(COLUMN_HEADERS))
        self._account_table.setHorizontalHeaderLabels(COLUMN_HEADERS)
        self._account_table.resizeColumnsToContents()
        self._account_table.resizeRowsToContents()
        self._account_table.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self._account_table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self._account_table.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)

        header = self._account_table.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        layout.addWidget(self._account_table)

        return groupbox

    def keyPressEvent(self, event) -> None:
        """Handles the key press event of the window.

        Args:
            event (QKeyEvent): Contains data about the event.
        """

        # Determine if the key that was pressed is the return/enter key
        if event.key() == Qt.Key.Key_Return or event.key() == Qt.Key.Key_Enter:
            self._search_button.click()
