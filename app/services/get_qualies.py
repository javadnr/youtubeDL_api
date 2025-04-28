from pytubefix import YouTube
import sys

def get_qualities(link):
    try:
        audio_qualities = []
        audio_size = []
        video_size = []
        video_qualities = []
        youtube = YouTube(link, use_oauth=True, allow_oauth_cache=True) 
        video_streams = youtube.streams.filter(subtype='mp4').order_by('resolution').desc()
        audio_streams = youtube.streams.filter(only_audio=True)

        for stream in audio_streams:
            audio_qualities.append(stream.abr)
            audio_size.append(stream.filesize_mb)
        for stream in video_streams:
            if stream.is_progressive:
                video_size.append(round(stream.filesize_mb, 2))
            else:
                video_size.append(round(stream.filesize_mb + audio_size[-1], 2))
            video_qualities.append(f'{stream.resolution}({stream.mime_type.split("/")[-1]})')

        if youtube.streams:
            title = str(youtube.streams.first().title)

        return {"video_qualities": video_qualities,
                        "video_size": video_size,
                        "audio_qualities": audio_qualities,
                        "audio_size": audio_size,
                        'youtube_link': link,
                        'thumbnail' : youtube.thumbnail_url,
                        'title': title}
    except Exception as e:
        print('Error on line {}'.format(sys.exc_info()[-1].tb_lineno), type(e).__name__, e)
        return 'ERROR'