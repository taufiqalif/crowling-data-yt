import os
import pandas as pd
from googleapiclient.discovery import build

# Masukkan kunci API YouTube Anda di sini
API_KEY = ' '

# Buat koneksi ke API YouTube
youtube = build('youtube', 'v3', developerKey=API_KEY)

# Definisikan parameter pencarian
search_query = 'hantu'  # Kata kunci pencarian
max_results = 1000  # Jumlah maksimum hasil yang ingin diambil

# Kirim permintaan API
search_response = youtube.search().list(
    q=search_query,
    part='snippet',
    type='video',
    maxResults=max_results
).execute()

# Olah respons
videos = []
for search_result in search_response.get('items', []):
    video_id = search_result['id']['videoId']
    video_response = youtube.videos().list(
        part='statistics',
        id=video_id
    ).execute()

    video = {
        'Judul': search_result['snippet']['title'],
        'Saluran': search_result['snippet']['channelTitle'],
        'ID Video': video_id,
        'Deskripsi': search_result['snippet']['description'],
        'Jumlah Pencarian': video_response['items'][0]['statistics']['viewCount']
    }
    videos.append(video)

# Konversi data ke dalam dataframe pandas
df = pd.DataFrame(videos)

# Buat folder "hasil" jika belum ada
output_folder = 'berdasarkan-pencarian/hasil'
os.makedirs(output_folder, exist_ok=True)

# Simpan dataframe ke dalam file CSV
output_file = os.path.join(output_folder, 'hasil_pencarian.csv')
df.to_csv(output_file, index=False, encoding='utf-8')

print(f"Hasil pencarian telah disimpan dalam file {output_file}")
