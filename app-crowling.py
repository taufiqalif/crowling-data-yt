import requests
from bs4 import BeautifulSoup

# URL video YouTube yang akan diambil datanya
video_url = "https://www.youtube.com/watch?v=5UaAZGteBPg"

# Mengakses halaman video menggunakan requests
response = requests.get(video_url)

# Menganalisis HTML halaman video menggunakan BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# Menemukan elemen HTML yang berisi informasi yang diinginkan
title_element = soup.find("h1", class_="title")
title = title_element.text.strip() if title_element else ""

author_element = soup.find("yt-formatted-string", class_="ytd-channel-name")
author = author_element.text.strip() if author_element else ""

description_element = soup.find("yt-formatted-string", class_="content")
description = description_element.text.strip() if description_element else ""

# Menampilkan informasi yang telah diekstrak
print("Judul Video:", title)
print("Penulis:", author)
print("Deskripsi:", description)
