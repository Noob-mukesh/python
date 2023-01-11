import os
os.system("pip install pytube")
from pytube import YouTube
# # link of the video to be downloaded
link = input("enter the link of youtube \t")
download = YouTube(link)

z = download.streams.first()

try:
    x = z.download("")
    print("downloaded sucessfully")
except:
    print("something error while processing")
