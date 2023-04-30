import os
import datetime
import time
from pytube import YouTube
import ffmpeg
import whisper
from whisper.utils import get_writer

class YoutubeLoader:

    def __init__(self, url,model='base'):
        self.url = url
        self.video_filename = ''
        self.video_spend_time = 0
        self.subTitles_spend_time = 0
        self.model = model

    def setStartTime(self):
        now = datetime.datetime.now()
        self.start_time = time.time()

    def calSpendTime(self, totalSec):
        # 計算小時、分鐘和秒數
        hours = totalSec // 3600
        minutes = (totalSec % 3600) // 60
        seconds = (totalSec % 3600) % 60
        return f"{hours}小時{minutes}分鐘{seconds}秒"

    def info(self):
        video_filename = os.path.basename(self.video_filename)
        res = "『" + video_filename+"』"
        res += "\n  抓影片耗時:"+self.calSpendTime(self.video_spend_time)
        res += "\n  轉字幕耗時:"+self.calSpendTime(self.subtitles_spend_time)
        res += "\n  影片+字幕耗時:"+self.calSpendTime(self.merge_spend_time)
        return res

    def saveVideo(self, output_dir):
        # 檢查輸出目錄是否存在，不存在就建立目錄
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        # 下載 YouTube 影片
        self.setStartTime()
        yt = YouTube(self.url, use_oauth=True)
        video = yt.streams.filter(progressive=True, file_extension='mp4').order_by(
            'resolution').desc().first()
        video_path = video.download(output_path=output_dir)
        self.video_filename = video_path
        self.video_spend_time = int((time.time() - self.start_time))
        return self

    def saveSubtitles(self, output_dir, video_filename=None):
        if video_filename is None:
            video_filename = self.video_filename
        else:
            self.video_filename = video_filename
        # 檢查輸出目錄是否存在，不存在就建立目錄
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        self.setStartTime()
        # 讀取影片路徑 , 預設中文語音
        # tiny , base , small , medium , large
        model = whisper.load_model(self.model)
        result = model.transcribe(video_filename, language='zh')
        # save SRT
        srt_writer = get_writer("srt", output_dir)
        txt_writer = get_writer("txt", output_dir)
        srt_writer(result, video_filename+'.srt')
        txt_writer(result, video_filename+'.txt')
        self.subtitles_spend_time = int((time.time() - self.start_time))
        return self

    def merge(self, output_dir, video_filename=None):
        if video_filename is None:
            video_filename = self.video_filename
        else:
            self.video_filename = video_filename
        # 檢查輸出目錄是否存在，不存在就建立目錄
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)        
        video = ffmpeg.input(self.video_filename)
        audio = video.audio

        filename, ext = self.video_filename.rsplit('.', 1)
        desVideo = f"{filename}.str.{ext}"
        print("DesVideo:"+desVideo)
        self.setStartTime()
        ffmpeg.concat(video.filter("subtitles", self.video_filename+'.srt'), audio, v=1, a=1).output(desVideo).run()
        self.merge_spend_time = int((time.time() - self.start_time))
        return self
