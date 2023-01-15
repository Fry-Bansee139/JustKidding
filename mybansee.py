from pytube import YouTube
import os
import os,sys,time,requests
from time import sleep
import sys
import time
import json
import random
import socket
import shutil
import webbrowser
import concurrent.futures
import time, os, requests, json, random, bs4
os.system("mkdir /sdcard/WelsyYTDownloader")
DownloadFile = "/sdcard/WelsyYTDownloader"
os.system("clear")
os.system("cowsay -f ghostbusters Youtube Downloader Created By WelsyDun| lolcat")
print("\033[1;33;40mhow to press the ':' button and press share and press copy link\033[0m \033[1;32;40m")
link=input("\033[1;33;40mPlease paste youtube Link in here,Youtube Link :\033[0m \033[1;32;40m")
print("\033[1;33;40mchoose in here\033[0m \033[1;32;40m")
Inp=int(input("\033[1;33;40m [1] Video \n [2] Audio \n Choose :\033[0m \033[1;32;40m"))
print("\033[1;33;40mis downloading...\033[0m \033[1;32;40m")
ys=YouTube(link)
if (Inp == 1):
      vedios=ys.streams.filter(file_extension='mp4',progressive=True)
elif (Inp == 2):
      vedios=ys.streams.filter(only_audio=True)
else:
      pass
i=1
for vedio in vedios:
	print(f"\033[1;32;40m{i}.\033[0m \033[1;33;40m {vedio}\033[0m")
	i+=1
	print("\033[1;33;40mchoose the resolution\033[0m \033[1;32;40m")
res=input("\033[1;33;40mEnter the resolution :\033[0m \033[1;32;40m")
print("\033[1;30m<════════════[\033[1;33;41m • \033[1;37mStatus\033[1;33m• \033[0m\033[1;30m]══════════════>")
print(f"\033[1;33;40mTitle of Video  :\033[0m \033[1;32;40m{ys.title}\033[0m")
print(f"\033[1;33;40mViews of Video  :\033[0m \033[1;32;40m{ys.views}\033[0m")
print(f"\033[1;33;40mLength of Video  :\033[0m \033[1;32;40m{ys.length}\033[0m")
print(f"\033[1;33;40mRating  :\033[0m \033[1;32;40m{ys.rating}\033[0m")
print(f"\033[1;33;40mDescription of Video  :\033[0m \033[1;32;40m{ys.description}\033[0m")
vedios=vedios[int(res)-1]
vedios.download(DownloadFile)
