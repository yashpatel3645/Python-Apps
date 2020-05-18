from pytube import YouTube

Save_Path = "D:/Youtube Downloaded Video"

link = input("Enter the Link : ")

try:
    yt = YouTube(link)
except:
    print("Connection Problem....!!!")

# print(yt.streams.all())
mp4file = yt.streams.get_highest_resolution()

print("Please Wait Your video is being downloading.......")
try:
    mp4file.download(Save_Path)
except:
    print('There will be some error.')

print('Task Completed!')

