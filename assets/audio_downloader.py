import youtube_dl
ydl_opts = {}
ydl_opts = {
    'writethumbnail': True,
    'postprocessors': [
        {
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
        },
        {'key': 'EmbedThumbnail'},
        {'key': 'FFmpegMetadata'},
    ],
}
d = input("Paste here : ")
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([d])
