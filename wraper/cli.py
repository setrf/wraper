import click
from rich.console import Console
from .sources.hackernews import fetch_top_stories
from .storage import save_items

console = Console()

@click.group()
def cli():
    """wraper: A tool to aggregate news from multiple sources."""
    pass

@cli.group()
def fetch():
    """Fetch content from various sources."""
    pass

@fetch.command()
@click.option('--limit', default=10, help='Number of items to fetch.')
def hn(limit):
    """Fetch top stories from Hacker News."""
    console.print(f"[bold green]Fetching top {limit} stories from Hacker News...[/bold green]")
    
    stories = fetch_top_stories(limit=limit)
    
    if stories:
        file_path = save_items("hackernews", stories)
        console.print(f"[bold blue]Successfully saved {len(stories)} items to:[/bold blue] {file_path}")
    else:
        console.print("[bold red]Failed to fetch stories or no stories found.[/bold red]")

if __name__ == '__main__':
    cli()
