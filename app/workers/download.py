# from redis import Redis
# from rq import Worker
# from app.dal import update_status
# from app.core import downloader

# these are the imports when I uncomment it starts failing

async def start_download_work(download_data):
    print("Packet got from queue {}".format(download_data))
    # uid = download_data.get("id", None)
    # url = download_data.get("url", None)
    # file_id = download_data.get("file_id", None);
    # update_status.update_workflow_status(uid, "DOWNLOAD_INPROGRESS")
    # wav_file_path = await downloader.download_youtube_podcast(url, file_id)
    # print("Path of the wav file {}".format(wav_file_path))