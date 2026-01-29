import unittest
from unittest.mock import patch, mock_open, MagicMock
from datetime import datetime
from wraper.storage import save_items

class TestStorage(unittest.TestCase):
    @patch('wraper.storage.get_storage_dir')
    @patch('wraper.storage.datetime')
    @patch('builtins.open', new_callable=mock_open)
    @patch('pathlib.Path.mkdir')
    def test_save_items(self, mock_mkdir, mock_file, mock_datetime, mock_get_storage_dir):
        # Setup mocks
        mock_now = datetime(2026, 1, 29, 12, 0, 0)
        mock_datetime.now.return_value = mock_now
        
        mock_storage_dir = MagicMock()
        mock_get_storage_dir.return_value = mock_storage_dir
        # Mocking / operator for Path
        mock_year_dir = MagicMock()
        mock_storage_dir.__truediv__.return_value = mock_year_dir
        mock_month_dir = MagicMock()
        mock_year_dir.__truediv__.return_value = mock_month_dir
        
        mock_final_path = MagicMock()
        mock_month_dir.__truediv__.return_value = mock_final_path
        
        items = [
            {"title": "Story 1", "url": "http://one.com", "score": 10, "descendants": 5},
            {"title": "Story 2", "url": "http://two.com", "text": "This is a description."}
        ]
        
        save_items("testsource", items)
        
        # Check if directory creation was attempted
        mock_month_dir.mkdir.assert_called_once_with(parents=True, exist_ok=True)
        
        # Check if file was opened
        mock_file.assert_called_once()
        
        # Verify content written
        handle = mock_file()
        written_content = "".join(call.args[0] for call in handle.write.call_args_list)
        
        self.assertIn("# Testsource - 2026-01-29", written_content)
        self.assertIn("[Story 1](http://one.com)", written_content)
        self.assertIn("**Points**: 10", written_content)
        self.assertIn("[Story 2](http://two.com)", written_content)
        self.assertIn("This is a description.", written_content)
