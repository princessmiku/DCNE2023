import unittest
from unittest.mock import MagicMock, patch

from runner import Runner


class TestRunner(unittest.TestCase):

    @patch('runner.get_feiertage_as_list')
    @patch('runner.datetime')
    @patch('runner.get_default_notification')
    def test_loop_feiertage(self, mock_get_default_notification, mock_datetime, mock_get_feiertage_as_list):
        # Mock data
        mock_feiertag = MagicMock()
        mock_feiertag.current_year_date.date.return_value = "2023-12-25"
        mock_get_feiertage_as_list.return_value = [mock_feiertag]
        mock_datetime.now.return_value.date.return_value = "2023-12-25"
        mock_notification = MagicMock()
        mock_get_default_notification.return_value = mock_notification
        mock_settings = MagicMock()
        mock_settings.only_my_bundesland = False

        # Instantiate Runner class with mock settings
        runner = Runner(mock_settings)

        # Call loop_feiertage()
        runner.loop_feiertage()

        # Check if methods were called
        mock_notification.send.assert_called_once()
        mock_feiertag.current_year_date.date.assert_called()
        mock_get_default_notification.assert_called_once()

    @patch('runner.Runner.loop_feiertage')
    def test_run(self, mock_loop_feiertage):
        mock_settings = MagicMock()
        mock_settings.always_running = False

        runner = Runner(mock_settings)
        runner.run()

        mock_loop_feiertage.assert_called_once()


if __name__ == '__main__':
    unittest.main()
