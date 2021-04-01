import youtube_dl
ydl_opts = {}
ydl_opts = {
    'writethumbnail': True,
    'postprocessors': [
        {
            # cannot keep this code public please read the documentation of youtube_dl
            # for futher assitance please feel free to reach me
    ],
}
d = input("Paste here : ")
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([d])
