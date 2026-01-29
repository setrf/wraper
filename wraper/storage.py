import os
from datetime import datetime
from pathlib import Path
from .config import get_storage_dir

def ensure_directory(path: Path):
    """Ensures the directory exists."""
    path.mkdir(parents=True, exist_ok=True)

def save_items(source_name: str, items: list):
    """
    Saves a list of items to a markdown file in the format:
    storage_dir/YYYY/MM/YYYY-MM-DD-{source_name}.md
    """
    now = datetime.now()
    year = now.strftime("%Y")
    month = now.strftime("%m")
    date_str = now.strftime("%Y-%m-%d")
    
    storage_dir = get_storage_dir()
    target_dir = storage_dir / year / month
    ensure_directory(target_dir)
    
    filename = f"{date_str}-{source_name}.md"
    file_path = target_dir / filename
    
    content = f"# {source_name.title()} - {date_str}\n\n"
    content += f"Fetched at: {now.strftime('%H:%M:%S')}\n\n"
    
    for item in items:
        title = item.get('title', 'No Title')
        url = item.get('url', '#')
        # specific for HN but generic enough
        points = item.get('score', 0)
        comments = item.get('descendants', 0)
        text = item.get('text', '')
        
        content += f"### [{title}]({url})\n"
        if 'score' in item:
            content += f"- **Points**: {points}\n"
        if 'descendants' in item:
            content += f"- **Comments**: {comments}\n"
        if text:
            content += f"\n{text}\n"
        content += "\n---\n\n"
        
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return file_path
