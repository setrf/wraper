import unittest
import requests
from unittest.mock import patch, MagicMock
from wraper.sources.hackernews import fetch_top_stories

class TestHackerNews(unittest.TestCase):
    @patch('wraper.sources.hackernews.requests.get')
    def test_fetch_top_stories_success(self, mock_get):
        # Mock response for top stories ID list
        mock_ids_response = MagicMock()
        mock_ids_response.status_code = 200
        mock_ids_response.json.return_value = [1, 2, 3]
        
        # Mock response for individual item
        mock_item_response = MagicMock()
        mock_item_response.status_code = 200
        mock_item_response.json.return_value = {
            "id": 1,
            "title": "Test Story",
            "url": "http://example.com",
            "score": 100,
            "descendants": 50
        }

        # Side_effect to return different responses for different calls
        # First call is for the list of IDs, subsequent calls are for items
        mock_get.side_effect = [mock_ids_response, mock_item_response, mock_item_response, mock_item_response]

        stories = fetch_top_stories(limit=3)

        self.assertEqual(len(stories), 3)
        self.assertEqual(stories[0]['title'], "Test Story")
        self.assertEqual(stories[0]['score'], 100)
        
    @patch('wraper.sources.hackernews.requests.get')
    def test_fetch_top_stories_failure(self, mock_get):
        # Mock failure for top stories ID list
        mock_get.side_effect = requests.exceptions.RequestException("Network error")
        
        stories = fetch_top_stories(limit=5)
        self.assertEqual(stories, [])
