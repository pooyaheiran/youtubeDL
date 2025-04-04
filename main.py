import yt_dlp


url = input("enter video url: ")
isBan = input("Is YouTube restricted in your country? (y/n)")
if isBan == "y":
    proxy = input("enter your ip and port(example: socks5://your-ip:port): ")

    ydl_opts = {
        'proxy': proxy 
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

if isBan == "n":
      ydl_opts = {
            
      }
      with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])