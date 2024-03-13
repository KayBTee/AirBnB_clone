import unittest
from unittest.mock import patch, mock_open
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.storage = FileStorage()

    def test_all_returns_dict(self):
        self.assertIsInstance(self.storage.all(), dict)

    @patch('builtins.open', new_callable=mock_open)
    def test_save(self, mock_open):
        self.storage.new(BaseModel())
        self.storage.save()
        mock_open.assert_called_with('file.json', 'w')
        mock_open().write.assert_called()

    @patch('builtins.open',
            new_callable=mock_open,
            read_data='{"BaseModel.1234":{"id": "1234", "__class__": "BaseModel"}}')
    def test_reload(self, mock_open):
        self.storage.reload()
        self.assertIn('BaseModel.1234', self.storage.all())
