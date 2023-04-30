此程式的目的是將 Youtube 視為資料源，可抓取影片下來存成 .mp4 檔案，
然後透過 Whisper API 將語音進行分析，輸出 .srt (字幕檔)和 .txt(文字檔)
文字檔可以當作 LangChain 數據源，就可以透過 llm 提供問答機器人

使用方式
======
## Youtube Loader
dl = YoutubeLoader(url='https://www.youtube.com/watch?v=LRMBvXnl0H0',model='base')
# 如果 OUTPUT_DIR 不存在就建立該目錄
dl.saveVideo('db/mp4')
# 透過 Whisper API 進行語音辨識，存放 .srt , .txt 檔案
dl.saveSubtitles('db/txt')

or

dl.saveVideo('db/mp4').saveSubtitles('db/txt').merge('db/mp4')

dl.loadVideo('test/ok.mp4').saveSubtitles('db/txt').merge('db/mp4')
