import requests
import json

# From google console get your youtube v3 api key and paste it here
API_KEY = "YOUR_YOUTUBE_V3_API KEY"
# Paste Your all playlist IDs
playlist_ids = [
  
  "PLwLSw1_eDZl33XF-NyOM6dJZ6hNDi54lg",
  "PLwLSw1_eDZl1lv3DwQr43Dbdnjsxfa_cB",
  "PLwLSw1_eDZl3lKZF-kZV6oca85WPnTHod",
  "PLwLSw1_eDZl3qq9KSn9zKK_DpaXxSxiKA",
  "PLwLSw1_eDZl2VQRIahDF73hnkdPjNRYnu",
  "PLwLSw1_eDZl1pvIv1fBd3oKkP3XEQpT_G",
  "PLwLSw1_eDZl0sgiAAegEz0YBnExhICwtl",
  "PLwLSw1_eDZl2T7bZTyLNt-PC8tuSa0jL0",
  "PLwLSw1_eDZl1nrqwrDFPpNWO2GkwuYmf1",
  "PLwLSw1_eDZl1Q4OIgY3DIF31SO_9cOo8M",
  "PLwLSw1_eDZl0AqkVnkd9eTh2OI1mRRpRs",
  "PLwLSw1_eDZl1ZHXQDzK5Qit6jqLTNzjZ3",
  "PLwLSw1_eDZl2mjV_pl9Dr_QTcn1nmNvB1",
  "PLwLSw1_eDZl2WCY-naAlexgVnI7CHlNNR",
  "PLwLSw1_eDZl3QnyIvBCFdHoCNqH7L44IX",
  "PLwLSw1_eDZl0aRsSiTx2Kq6Mc5zc0jrL1",
  "PLwLSw1_eDZl0-bp4bZ7ER-VQ-973riDyN",
  "PLwLSw1_eDZl3myw51ePNETmCVl587h_Y3",
  "PLwLSw1_eDZl3bhy_uFd1zFXKG7KIYXqCq",
  "PLwLSw1_eDZl3PjJbm6RKXGHPll7ZJjSkT",
  "PLwLSw1_eDZl2P4Wwj2piYnwauRoyEeqlZ",
  "PLwLSw1_eDZl1_y0Egv3OLQDJfK2hIx3Vc",
  "PLwLSw1_eDZl2cJtt6H_rYQoBf9rpMXphM",
  "PLwLSw1_eDZl1wGMYg5oB3uEns0CZNl6sI",
  "PLwLSw1_eDZl2v3GdglUbai_QNMJHZMOHP",
  "PLwLSw1_eDZl0oqORR5jlJJvR2Qa2a77Qu",
  "PLwLSw1_eDZl20EjWfUYYc1YyqdU8ilHEe",

]

BATCH_SIZE = 50
all_playlists = [
]

for i in range(0, len(playlist_ids), BATCH_SIZE):
    batch_ids = playlist_ids[i:i+BATCH_SIZE]
    ids_param = ",".join(batch_ids)
    
    url = f"https://www.googleapis.com/youtube/v3/playlists?part=snippet,contentDetails&id={ids_param}&key={API_KEY}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        all_playlists.extend(data.get("items", []))
    else:
        print(f"Error fetching batch starting at index {i}: {response.text}")

# Save to JSON
with open("youtube_playlists.json", "w", encoding="utf-8") as f:
    json.dump({"items": all_playlists}, f, ensure_ascii=False, indent=4)

print("✅ Fetched all playlists and saved to youtube_playlists.json")
