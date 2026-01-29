# wraper

A lightweight CLI tool to aggregate news and information from multiple sources.

## Overview

`wraper` is designed to be a unified interface for fetching updates from various platforms like Hacker News, Reddit, RSS feeds, etc. It stores the fetched data in a structured, local file system (Markdown files organized by Year/Month).

## Installation

### Prerequisites

- Python 3.7+
- pip

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/setrf/wraper.git
   cd wraper
   ```

2. Install dependencies and the package in editable mode:
   ```bash
   pip install -r requirements.txt
   pip install -e .
   ```

## Usage

The CLI is invoked using the `wraper` command.

### Fetch Hacker News Top Stories

To fetch the top 10 stories from Hacker News:

```bash
wraper fetch hn
```

You can specify a limit using the `--limit` option:

```bash
wraper fetch hn --limit 20
```

### Output

Fetched items are saved to the `data/` directory in the current working directory, organized by date:

```
data/
└── YYYY/
    └── MM/
        └── YYYY-MM-DD-hackernews.md
```

## Project Structure

- `wraper/`
    - `cli.py`: The main entry point for the CLI (Click).
    - `config.py`: Configuration settings (storage paths).
    - `storage.py`: Logic for file system operations and saving data.
    - `sources/`: Modules for different data sources.
        - `hackernews.py`: Fetcher for Hacker News.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.