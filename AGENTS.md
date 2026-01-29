# AGENTS.md - wraper

## Purpose
`wraper` is a lightweight CLI for aggregating news/info from multiple sources (HN, etc.) into structured Markdown files (`data/YYYY/MM/YYYY-MM-DD-source.md`).

## Core Components
- `wraper/cli.py`: Entry point (Click). Commands: `fetch [source]`.
- `wraper/sources/`: Modular fetchers. `hackernews.py` implements top stories fetch.
- `wraper/storage.py`: Logic for directory nesting and MD generation.
- `wraper/config.py`: Path configurations.

## Development Context
- **Language**: Python 3.10+
- **Testing**: `pytest` in `tests/`. Mocks used for network/IO.
- **Dependencies**: `click`, `requests`, `rich`.
- **Style**: Direct CLI output with `rich`. Markdown storage for easy agent/human consumption.

## Integration Guide
Agents can use `wraper fetch [source]` to gather context.
To add a source:
1. Create `wraper/sources/[name].py` with a fetch function.
2. Add command to `wraper/cli.py`.
3. Use `wraper.storage.save_items(source_name, items)` to persist.
4. Add tests in `tests/test_[name].py`.
