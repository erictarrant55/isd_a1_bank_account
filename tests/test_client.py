import unittest

from email_validator import EmailNotValidError

from account.client import Client

__author__ = "Eric Tarrant"
__verison__ = "1.0.0"

class TestClient(unittest.TestCase):

    def setUp(self) -> None:
        self.client = Client(
            1234,
            "Eric Tarrant",
            "etarrant@rrc.ca"
        )

    def test_init_client_id_less_than_zero(self) -> None:
        with self.assertRaisesRegex(
            ValueError,
            "client_id must be a value greater than zero."
        ):
            Client(
                -1,
                "Eric Tarrant",
                "etarrant@rrc.ca"
            )

    def test_init_client_id_zero(self) -> None:
        with self.assertRaisesRegex(
            ValueError,
            "client_id must be a value greater than zero."
        ):
            Client(
                0,
                "Eric Tarrant",
                "etarrant@rrc.ca"
            )

    def test_init_name_empty_string(self) -> None:
        with self.assertRaisesRegex(
            ValueError,
            "name cannot be an empty string."
        ):
            Client(
                1234,
                "",
                "etarrant@rrc.ca"
            )

    def test_init_email_invalid(self) -> None:
        with self.assertRaises(EmailNotValidError):
            Client(
                1234,
                "Eric Tarrant",
                "invalid-email"
            )

    def test_init_new_instance(self) -> None:
        client = Client(
            1234,
            "Eric Tarrant",
            "etarrant@rrc.ca"
        )

        self.assertEqual(1234, client._Client__client_id)
        self.assertEqual(
            "Eric Tarrant",
            client._Client__name
        )
        self.assertEqual(
            "etarrant@rrc.ca",
            client._Client__email_address
        )

    def test_client_id_property(self) -> None:
        expected = 1234
        actual = self.client.client_id

        self.assertEqual(expected, actual)

    def test_name_property(self) -> None:
        expected = "Eric Tarrant"
        actual = self.client.name

        self.assertEqual(expected, actual)

    def test_email_address_property(self) -> None:
        expected = "etarrant@rrc.ca"
        actual = self.client.email_address

        self.assertEqual(expected, actual)

    def test_email_address_invalid(self) -> None:
        with self.assertRaises(EmailNotValidError):
            self.client.email_address = "invalid-email"

    def test_email_address_valid(self) -> None:
        self.client.email_address = " NEW@EXAMPLE.COM "

        expected = "NEW@example.com"
        actual = self.client._Client__email_address

        self.assertEqual(expected, actual)

    def test_str(self) -> None:
        expected = "Eric Tarrant [1234] - etarrant@rrc.ca"
        actual = str(self.client)

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()