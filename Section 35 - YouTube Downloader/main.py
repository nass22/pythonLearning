from pytube import YouTube

# ? FUNCTIONS ?

def get_url_user_input():
    BASE_YOUTUBE_URL = "https://www.youtube.com"

    while True:
        url = input("Enter the url: ")
        
        # if url[:len(BASE_YOUTUBE_URL)] == BASE_YOUTUBE_URL:
        if url.lower().startswith(BASE_YOUTUBE_URL):
            return url
        print("Invalid url")

def choiceQuality(stream):
    for i in range(len(stream)):
        print(f"{i+1} - {stream[i].abr}")

    while True:
        choice = input("Choice your audio quality:")
        if choice == "":
            print("Invalid choice")
        else:
            try:
                choice_int = int(choice)
            except:
                print("Your choice is not a number")
            else:
                if not 1 <= choice_int <= len(stream):
                    print("ERROR: Your choice is out of range")
                else:
                    break

    print("Téléchargement de la vidéo...")
    stream[int(choice)-1].download("audio") #audio permet de créer un dossier audio
    print("Téléchargement de la vidéo terminée.")


def on_download_progress(stream, chunk, bytes_remaining):
    bytes_downloaded = stream.filesize - bytes_remaining
    percent = bytes_downloaded * 100 / stream.filesize
    print(f"Progress: {int(percent)}%")

# ********************************

video = YouTube(get_url_user_input())

video.register_on_progress_callback(on_download_progress)

# print("Title: ", video.title)
# print("Views: ", video.views)
# print("Author: ", video.author)
# print("url: ", video.channel_url)
# print("Streams: ", video.streams)

# ! dans les balises stream, il y a un progressive ="True" ou "False", si True alors le stream comporte et le flux vidéo et le flux audio. Si False alors le flux audio et vidéo sont séparés.

# for stream in video.streams:
#     print("Stream: ", stream)

# *** permet de filtrer
# stream_filter = video.streams.filter(only_audio=True, abr="128kbps")
# print(stream_filter)

# *** permet d'avoir la vidéo avec la meilleur résolution
# stream = video.streams.get_highest_resolution()

# *** DL la video
# stream = video.streams.filter(only_audio=True, abr="128kbps").first()

# print("Téléchargement de la vidéo...")
# stream.download()
# print("Téléchargement de la vidéo terminée.")

stream = video.streams.filter(only_audio=True).order_by('abr').desc()
choiceQuality(stream)






