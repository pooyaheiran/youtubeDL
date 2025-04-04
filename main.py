import yt_dlp


url = input("enter video url: ")
isBan = input("Is YouTube restricted in your country? (y/n)").lower()


print("----------------------------------------------------")

if isBan == "y":
    proxy = input("Use the specified HTTP/HTTPS/SOCKS proxy. \
For example socks5://127.0.0.1:1080/ >>>: ")

    ydl_opts = {
        'proxy': proxy,
        'format': 'best[height<=720]'
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

if isBan == "n":
      ydl_opts = {
            'format': 'best[height<=720]'
      }
      with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])