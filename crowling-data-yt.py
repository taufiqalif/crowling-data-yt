from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager
from tabulate import tabulate
from textblob import TextBlob
import pandas as pd

# Masukkan kunci API YouTube Anda di sini
API_KEY = 'AIzaSyApnTptNWusgS4-BWf4cy98GW9wqqfBZkc'


def crawl_popular_videos(max_results):
    try:
        # Inisialisasi klien YouTube Data API
        youtube = build('youtube', 'v3', developerKey=API_KEY)

        # Mengirim permintaan API untuk mendapatkan video populer
        response = youtube.videos().list(
            part='snippet,statistics',
            chart='mostPopular',
            maxResults=max_results
        ).execute()

        # Menyiapkan data video populer
        video_data = []
        for video in response['items']:
            video_id = video['id']
            title = video['snippet']['title']
            views = video['statistics']['viewCount']
            likes = video['statistics']['likeCount']

            video_data.append([video_id, title, views, likes])

        # Mengurutkan data video berdasarkan jumlah views secara descending
        video_data.sort(key=lambda x: int(x[2]), reverse=True)

        # Menampilkan data video populer dalam bentuk tabel
        headers = ['Video ID', 'Judul', 'Jumlah Views', 'Jumlah Likes']
        print(tabulate(video_data, headers=headers))

    except HttpError as e:
        print('Terjadi kesalahan saat mengakses API:', e)


# Memanggil fungsi untuk melakukan crawling data video populer
max_results = 1000  # Jumlah video populer yang ingin diambil
crawl_popular_videos(max_results)
