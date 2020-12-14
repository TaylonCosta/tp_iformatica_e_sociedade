from django.shortcuts import render
from django.conf import settings
import requests

from .forms import CanalForm
from .models import Canais
from urllib.parse import urlencode


def index (request):
    data = Canais.objects.all()
    q = []
    form = CanalForm(request.POST or None)
    videos = []

    if request.method == 'POST':
        if request.method != '':
            if form.is_valid():
                search = form.cleaned_data['nome_video']
                canal = form.cleaned_data['select']
                search_url = 'https://www.googleapis.com/youtube/v3/search'
                video_url = 'https://www.googleapis.com/youtube/v3/videos'

                parametros_serch = {
                    'part': 'snippet',
                    'q': search,
                    'key': settings.YOUTUBE_DATA_API_KEY,
                    'max_results': 50,
                    'type': 'video'
                }

                videos_ids = []
                r = requests.get(search_url, params=parametros_serch)
                results = (r.json()['items'])

                for i in results:
                    videos_ids.append(i['id']['videoId'])

                parametros_videos = {
                    'part': 'snippet',
                    'key': settings.YOUTUBE_DATA_API_KEY,
                    'id': ','.join(videos_ids),
                    'max_results': 50
                }

                r = requests.get(video_url, params=parametros_videos)
                results = r.json()['items']

                for i in results:
                    video_data = {
                        'title': i['snippet']['title'],
                        'id': i['id'],
                        'url': f'https://www.youtube.com/watch?v={i["id"]}',
                        'thumbnail': i['snippet']['thumbnails']['high']['url'],
                        'channel': i['snippet']['channelTitle'],
                    }
                    if video_data['channel'] == canal.nome_canal:
                        videos.append(video_data)

    context = {
        'form' : form,
        'videos': videos,
        'data': data
    }

    return render(request, "yt/index.html", context)