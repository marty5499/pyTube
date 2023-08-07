from youtube import YoutubeLoader

OUTPUT_DIR = './video/new/'
URL = 'https://youtu.be/LHY3oyhlTsw'
URL = 'https://www.youtube.com/watch?v=LHY3oyhlTsw'
URL = 'https://www.youtube.com/watch?v=72bQ2CbED-Y' #新聞面對面

"""
dl = YoutubeLoader(URL, model='large')
dl.saveVideo(OUTPUT_DIR)
"""

dl = YoutubeLoader("./video/new/news.mp4", model='large')
dl.loadVideo()
dl.saveSubtitles(OUTPUT_DIR)
dl.merge(OUTPUT_DIR)
print(dl.info())
