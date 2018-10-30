###################### 
# Installation
conda create --name youDownload python=3.6
conda activate youDownload
pip install --upgrade pip
pip install pytube moviepy

###################### 
# Usage
1. cd to folder NN-youtubeDownload
	cd /media/nhnguyen/DATA/NN-youtubeDownload-0.1
2. activate anaconda 
	conda activate youDownload
3. call bash file with syntax
	Notice: time syntax does not need colon. For example minute1:second20 can be written as 120
	
	bash run.sh <youtube Url> <startTime> <endTime> 
	bash run.sh https://youtu.be/NxxvylzZ1Hs?t=31 031 105

	get video from above url, trim from 0:31 to 1:05

4. The output is in the same folder as download.py file


###################### 
Version 0.1
Youtube download and trimming
Date: 10/30/2018

Update:
- handle special characters in title. For example slash / 
- output videos are created in folder final

Issues:
- due to tokenized in bash, cannot get in long url, like https://www.youtube.com/watch?v=x1iBjqn1lJQ&feature=youtu.be&t=13
	Solution 1: cut the url to just the watch part https://www.youtube.com/watch?v=x1iBjqn1lJQ
	Solution 2: use the short url from Youtube Share button https://youtu.be/x1iBjqn1lJQ