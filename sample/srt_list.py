import os
import argparse
import ffmpeg
import whisper
import datetime,time
from whisper.utils import get_writer

src_dir = './list/'
model = whisper.load_model("medium")

for filename in os.listdir(src_dir):
    if filename.endswith('.mp4'):
        src_video = os.path.join(src_dir, filename)
        print(f"開始處理 {src_video}")
        result = model.transcribe(src_video,language='zh')
        srt_writer = get_writer("srt", src_dir)
        txt_writer = get_writer("txt", src_dir)
        srt_writer(result, os.path.splitext(src_video)[0] + '.srt')
        txt_writer(result, os.path.splitext(src_video)[0] + '.txt')
        print(f"完成 {src_video} 的字幕擷取")

print("所有影片的字幕擷取已完成!")