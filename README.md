# 🎬 YouTube Playlist Fetcher

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.7%2B-blue?logo=python&logoColor=white" alt="Python Version">
  <img src="https://img.shields.io/badge/YouTube%20Data%20API-v3-red?logo=youtube&logoColor=white" alt="YouTube API">
  <img src="https://img.shields.io/badge/Output-JSON-green?logo=json&logoColor=white" alt="JSON Output">
  <img src="https://img.shields.io/badge/Status-Stable-brightgreen?style=flat-square" alt="Status">
</p>

Fetch **YouTube playlist details** (title, channel name, thumbnails, and video count) in bulk using the **YouTube Data API v3** — all neatly exported into a single JSON file.

---

## ⚙️ Setup Instructions

### 1️⃣ Requirements
- Python **3.7+**
- A valid **YouTube Data API v3 Key**
- Install required library:
  ```bash
  pip install requests

### 2️⃣ Add Your API Key

Open the script and replace this line:

API_KEY = "YOUR_YOUTUBE_V3_API_KEY"

### 3️⃣ Add Playlist IDs

Replace the example IDs with your own:

playlist_ids = [
  "PLxxxxxxxxxxxxxxxxxxxxx",
  "PLyyyyyyyyyyyyyyyyyyyyy",
]

### 4️⃣ Run the Script

Run the script from your terminal:

python youtube_playlist_fetcher.py

### 📦 Output

The script creates a file named youtube_playlists.json in the same folder.

Example:
('''
{
  "items": [
    {
      "id": "PLxxxx",
      "snippet": {
        "title": "Sample Playlist",
        "channelTitle": "Example Channel",
        "thumbnails": { ... }
      },
      "contentDetails": {
        "itemCount": 25
      }
    }
  ]
}
''')
