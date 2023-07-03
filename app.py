from flask import Flask, render_template
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

app = Flask(__name__)

API_KEY = 'your-api'


def crawl_popular_videos(max_results):
    try:
        youtube = build('youtube', 'v3', developerKey=API_KEY)
        response = youtube.videos().list(
            part='snippet,statistics',
            chart='mostPopular',
            maxResults=max_results
        ).execute()
        video_data = []
        for video in response['items']:
            video_id = video['id']
            title = video['snippet']['title']
            views = video['statistics']['viewCount']
            likes = video['statistics']['likeCount']

            video_data.append({
                'video_id': video_id,
                'title': title,
                'views': views,
                'likes': likes
            })

        video_data.sort(key=lambda x: int(x['views']), reverse=True)
        return video_data

    except HttpError as e:
        print('Terjadi kesalahan saat mengakses API:', e)
        return None


@app.route('/')
def home():
    max_results = 1000
    video_data = crawl_popular_videos(max_results)
    return render_template('index.html', video_data=video_data)


if __name__ == '__main__':
    app.run(debug=True)
