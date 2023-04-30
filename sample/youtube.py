####
# 下載 db_list.txt 中所有的 youtube 連結  
####

from pytube import YouTube

with open('db_list.txt', 'r') as f:
	urls = f.readlines()

for url in urls:
	print("Download..."+url.strip())
	yt = YouTube(url.strip(), use_oauth=True)
	yt.streams.filter().get_highest_resolution().download(output_path='./list/')

# 下載最高畫質影片，如果沒有設定 filename，則以原本影片的 title 作為檔名
yt.streams.filter().get_highest_resolution().download(output_path='./list/')

print('ok!')