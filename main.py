from youtube import YoutubeLoader

OUTPUT_DIR = 'test_01/'

#dl = YoutubeLoader('https://www.youtube.com/watch?v=dZbqIXs9Z08', model='tiny')
#dl.saveVideo(OUTPUT_DIR).saveSubtitles(OUTPUT_DIR).merge(OUTPUT_DIR)

dl = YoutubeLoader('./test_01/用 ChatGPT 學運算思維 (開字幕).mp4', model='large')
dl.saveSubtitles(OUTPUT_DIR).merge(OUTPUT_DIR)
print(dl.info())
