import requests
from typing import List, Dict

HN_TOP_STORIES_URL = "https://hacker-news.firebaseio.com/v0/topstories.json"
HN_ITEM_URL = "https://hacker-news.firebaseio.com/v0/item/{}.json"

def fetch_top_stories(limit: int = 10) -> List[Dict]:
    """
    Fetches the top N stories from Hacker News.
    """
    try:
        # Fetch top story IDs
        response = requests.get(HN_TOP_STORIES_URL)
        response.raise_for_status()
        story_ids = response.json()
        
        top_ids = story_ids[:limit]
        stories = []
        
        for story_id in top_ids:
            # Fetch story details
            item_resp = requests.get(HN_ITEM_URL.format(story_id))
            if item_resp.status_code == 200:
                stories.append(item_resp.json())
                
        return stories
    except requests.RequestException as e:
        print(f"Error fetching Hacker News stories: {e}")
        return []
