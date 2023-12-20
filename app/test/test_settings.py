import unittest
from unittest.mock import patch, mock_open

from settings_handler import Settings


class SettingsTestCase(unittest.TestCase):
    @patch("os.path.isfile", return_value=True)
    @patch("builtins.open", new_callable=mock_open, read_data='{"bundesland": "Bremen", "only_my_bundesland": true, "always_running": true}')
    def test_read_existing_settings(self, mock_file, mock_isfile):
        settings = Settings()
        self.assertEqual(settings.bundesland, "Bremen")
        self.assertEqual(settings.only_my_bundesland, True)
        self.assertEqual(settings.always_running, True)

    @patch("os.path.isfile", return_value=False)
    def test_new_settings(self, mock_isfile):
        settings = Settings()
        self.assertIsNone(settings.bundesland)
        self.assertEqual(settings.only_my_bundesland, False)
        self.assertEqual(settings.always_running, False)

    @patch("os.remove")
    @patch("os.path.isfile", return_value=True)
    @patch("builtins.open", new_callable=mock_open)
    def test_save_empty_settings(self, mock_file, mock_isfile, mock_remove):
        settings = Settings()
        settings.save()
        mock_remove.assert_called_once_with('settings.json')

    @patch("os.remove")
    @patch("os.path.isfile", return_value=True)
    @patch("builtins.open", new_callable=mock_open)
    def test_save_with_bundesland(self, mock_file, mock_isfile, mock_remove):
        settings = Settings()
        settings.set_bundesland("Bremen")
        settings.save()
        mock_file.assert_called_once_with('settings.json', 'w')


if __name__ == "__main__":
    unittest.main()
