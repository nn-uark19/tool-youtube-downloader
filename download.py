"""
Version 0.1
Youtube download and trimming
Date: 10/30/2018

Update:
- handle special characters in title. For example slash / 
- output videos are created in folder final
"""


from pytube import YouTube
import os
import sys
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

###==========================
def downloadYouTube(videourl, path):    

    # rule to strip special character. Unused for now
    keep=set(' ')
    
    # initialize download + strip special character
    yt = YouTube(videourl)
    titleOri = yt.title
    title = ''.join(e for e in titleOri if e.isalnum() or e in keep)

    # check path exists
    if not os.path.exists(path):
        os.makedirs(path)

    # download video with new name    
    download = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    download.download(path, filename=title)

    # rename new name
    return title
    
###==========================
def convertTime(timeIn):
	if (len(str(timeIn)) == 3):
		return int(str(timeIn)[0])*60 + int(str(timeIn)[1:3])
	else:
		return timeIn

###==========================
def trimVideo(title, pathIn, pathOut):
	# check path exists
    if not os.path.exists(pathIn):
        os.makedirs(pathIn)
    if not os.path.exists(pathOut):
        os.makedirs(pathOut)

    title += '.mp4'
    video = pathIn + '/' + title
    dest = pathOut + '/' + title
    ffmpeg_extract_subclip(video, timeStart, timeEnd, targetname=dest)

###==========================
if __name__ == "__main__":
	print(f'Number of arguments: {len(sys.argv)} arguments.')
	print(f'Argument List: {str(sys.argv)}')

	# parameters
	url = sys.argv[1]
	timeStart = convertTime(int(sys.argv[2]))
	timeEnd = convertTime(int(sys.argv[3]))


	# download, get the title
	title = downloadYouTube(url, './raw')
	print(f'Downloaded... {title}')

	# trimming
	print('Trimming video...')
	trimVideo(title, './raw', './final')
	


