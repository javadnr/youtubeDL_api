from pytubefix import YouTube
import sys


def download_video(link, quality):
    try:
        print(link)
        youtube = YouTube(link, use_oauth=True, allow_oauth_cache=True)
        stream = youtube.streams.filter(res=f'{quality}', file_extension='mp4').first()
        if stream:
            download_link = stream.url
            return download_link
        else:
            return 'invalid quality'
    except Exception as e:
        print('Error on line {}'.format(sys.exc_info()[-1].tb_lineno), type(e).__name__, e)
        return 'ERROR'
    
def download_audio(link, quality):
    try:
        print(link)
        youtube = YouTube(link, use_oauth=True, allow_oauth_cache=True)
        stream = youtube.streams.filter(only_audio=True,abr=f'{quality}kbps').first()
        if stream:
            download_link = stream.url
            return download_link
        else:
            return 'invalid quality'
    except Exception as e:
        print('Error on line {}'.format(sys.exc_info()[-1].tb_lineno), type(e).__name__, e)
        return 'ERROR'