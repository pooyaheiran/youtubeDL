

from __future__ import unicode_literals
import yt_dlp


url = input("enter video url: ")
isBan = input("Is YouTube restricted in your country? (y/n)")
if isBan == "y":
    proxy = input("enter your ip and port(example: socks5://your-ip:port): ")

ydl_opts = {
    'proxy': proxy 
}



with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['https://www.youtube.com/watch?v=aCWTzT23UTI&ab_channel=EnjoyChess%D9%84%D8%B0%D8%AA%D8%B4%D8%B7%D8%B1%D9%86%D8%AC'])
