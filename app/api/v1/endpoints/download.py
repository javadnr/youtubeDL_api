from fastapi import APIRouter, Query
from app.services.downloader import download_video, download_audio
router = APIRouter()

@router.get("/download-audio")
def download_audio_route(link: str = Query(..., description="URL to download audio"),quality: str =Query(..., description="quality to download audio")):
    return {"download_link": download_audio(link,quality)}



@router.get("/download-video")
def download_video_route(link: str = Query(..., description="URL to download video"),quality: str =Query(..., description="quality to download audio")):
    return {"download_link": download_video(link,quality)}
