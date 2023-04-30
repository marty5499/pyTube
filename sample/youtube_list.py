####
# 下載 db_list.txt 中所有的 youtube 連結  
####
import os
from pytube import YouTube

output_path = './list/'
youtube_list_file = 'db_list.txt'

with open(youtube_list_file, 'r') as f:
    urls = f.readlines()

for url in urls:
    url = url.strip()
    print("get Info by URL: " + url)
    try:
        yt = YouTube(url, use_oauth=True)
        filename = yt.streams.filter().get_highest_resolution().default_filename
        print("Video filename:"+filename);
        filepath = os.path.join(output_path, filename)
        if os.path.exists(filepath):
            print("File already exists, skipping...")
            continue
        else:
            print("Downloading...")
            #yt.streams.filter().get_highest_resolution().download(output_path=output_path)
            print("Download completed!")
    except Exception as e:
        print("Error processing url: " + url)
        print(e)

print('All urls processed.')