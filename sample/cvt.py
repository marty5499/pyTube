# 程式功能：用 whisper 將指定的影片轉字幕
# 下載影片 https://www.freemake.com/tw/free_video_downloader/
import argparse
import ffmpeg
import whisper
import datetime,time
from whisper.utils import get_writer

parser = argparse.ArgumentParser(description='Convert video to subtitle')
parser.add_argument('src_video', metavar='src_video', type=str, help='the source video file path')

args = parser.parse_args()

srcVideo = args.src_video

desVideo = srcVideo.split('.')
desVideo = desVideo[0] + ".srt." + desVideo[1]

###
### 記錄開始時間
###
now = datetime.datetime.now()
start_time = time.time()
print("現在的時間是：")
print(now)

###
### Step1. 分析影片，存字幕
###
model = whisper.load_model("medium")
result = model.transcribe(srcVideo)
# save SRT
srt_writer = get_writer("srt", './')
txt_writer = get_writer("txt", './')
srt_writer(result, srcVideo+'.srt')
txt_writer(result, srcVideo+'.txt')
print("完成語音辨識與字幕擷取,花費時間: %s 秒" % int((time.time() - start_time)))


###
### Step2. 將字幕和原來影片合併,輸出新的影片
###
video = ffmpeg.input(srcVideo)
audio = video.audio
ffmpeg.concat(video.filter("subtitles", srcVideo+'.srt'), audio, v=1, a=1).output(desVideo).run()
print("完成影片轉換,總花費時間: %s 秒" % int((time.time() - start_time)))
