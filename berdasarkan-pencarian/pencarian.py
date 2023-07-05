from googleapiclient.discovery import build
from tabulate import tabulate

# Masukkan kunci API YouTube Anda di sini
API_KEY = ' '

# Buat koneksi ke API YouTube
youtube = build('youtube', 'v3', developerKey=API_KEY)

# Definisikan parameter pencarian
search_query = 'hantu'  # Kata kunci pencarian
max_results = 10  # Jumlah maksimum hasil yang ingin diambil

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

# Konversi data menjadi tabel
table = tabulate(videos, headers="keys", tablefmt="grid")

# Tampilkan tabel
print(table)
