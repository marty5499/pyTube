# 程式功能：用 whisper 將影片轉字幕
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

def printSpendTime(total_seconds):
	# 計算小時、分鐘和秒數
	hours = total_seconds // 3600
	minutes = (total_seconds % 3600) // 60
	seconds = (total_seconds % 3600) % 60
	# 打印結果
	print(f"花費：{hours}小時{minutes}分鐘{seconds}秒")

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
model = whisper.load_model("medium") # base , small , medium , large
print("語音轉字幕：" + srcVideo)
result = model.transcribe(srcVideo,language='zh')

# save SRT
srt_writer = get_writer("srt", './')
txt_writer = get_writer("txt", './')
srt_writer(result, srcVideo+'.srt')
txt_writer(result, srcVideo+'.txt')
printSpendTime(int((time.time() - start_time)))
