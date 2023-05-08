from youtube import YoutubeLoader

OUTPUT_DIR = './video/生物01/'
URL = 'https://youtu.be/LHY3oyhlTsw'
URL = 'https://www.youtube.com/watch?v=LHY3oyhlTsw'

#dl = YoutubeLoader(URL, model='large')
#dl.saveVideo(OUTPUT_DIR)

dl = YoutubeLoader("./video/生物01/111AB402_01_03.mp4", model='large')
dl.loadVideo()
dl.saveSubtitles(OUTPUT_DIR)
dl.merge(OUTPUT_DIR)

print(dl.info())
