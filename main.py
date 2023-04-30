from youtube import YoutubeLoader

OUTPUT_DIR = 'test/'
URL = 'https://youtu.be/gVMp_vKwslI'
dl = YoutubeLoader(URL, model='medium')
# 下載影片
dl.saveVideo(OUTPUT_DIR)
dl.saveSubtitles(OUTPUT_DIR)
dl.merge(OUTPUT_DIR)
print(dl.info())
