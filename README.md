# ReelNight

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![PyQt6](https://img.shields.io/badge/UI-PyQt6-41CD52?logo=qt&logoColor=white)
![Type](https://img.shields.io/badge/Type-Desktop%20App-111827)

ReelNight is a lightweight desktop movie browser built with PyQt6. It packages a curated 100-title movie dataset into a clean watchlist experience with poster browsing, title search, genre shortcuts, and one-click IMDb redirection.

## Overview

ReelNight solves a simple but practical problem: choosing something to watch without opening multiple websites and tabs. The application ships with a local JSON dataset and uses remote poster URLs to present films in a visual desktop UI.

The current implementation focuses on discovery:

- browse a rotating selection of titles from a local Top 100 dataset
- search by exact movie title
- filter recommendations by genre
- open a detailed modal with rating, year, description, and IMDb link

## Features

- Desktop-first PyQt6 interface
- Curated local dataset with 100 movie records
- Randomized poster cards on launch
- Title search against the local catalog
- Genre shortcut buttons for quick filtering
- Detail modal with title, ranking, genres, rating, year, and description
- Direct "Watch" action that opens the IMDb page in the system browser

## Tech Stack

- Python
- PyQt6
- Pillow
- Requests
- Local JSON data store

## Architecture / Project Structure

```text
ReelNight/
├── main.py
├── config.py
├── images/
├── modules/
│   ├── app.py
│   ├── cards.py
│   ├── frames.py
│   ├── load_image.py
│   ├── widgets.py
│   └── window.py
├── static/
│   └── json/json_watch.json
└── utils/
    └── api_requests.py
```

## Getting Started

### Prerequisites

- Python 3.10 or newer
- `pip`
- Internet access for loading poster images and opening IMDb links

### Installation

```bash
python -m venv .venv
source .venv/bin/activate
pip install PyQt6 Pillow requests
```


### Running Locally

```bash
python main.py
```

## Main Functionality

- **Browse movies**: the home screen renders five poster cards from the local dataset.
- **Search**: entering a title in the search box attempts an exact lowercase match against the stored movie names.
- **Filter by genre**: the UI generates genre shortcut buttons and loads matching movies when a button is clicked.
- **View details**: clicking a poster opens a modal with metadata and description.
- **Open IMDb**: the modal includes a `Watch` button that opens the title's IMDb page.

## Future Improvements

- Replace the static dataset with a real movie API integration
- Move secrets and API configuration out of source files
- Improve search matching with partial text and suggestions
- Clear previous cards before rendering new search/filter results
- Package the app with PyInstaller or a native installer

