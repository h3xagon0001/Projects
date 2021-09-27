from pytube import YouTube

print("+++++++++++++++++++++++++++++++++++++++++++++++")
print("+       Python YouTube Video Downloader       +")
print("+++++++++++++++++++++++++++++++++++++++++++++++")
print()

while True:
	
	#ask for the link from user
	link = input("Enter the link of YouTube video you want to download:  ")
	yt = YouTube(link)
        
	#Showing details
	print("Title: ",yt.title)
	print("Views: ",yt.views)
	print("Duration: ",round(yt.length/60, 1))
	print("Rating: ",yt.rating)
	#Getting the highest resolution possible
	ys = yt.streams.get_highest_resolution()

	#Starting download
	print("Downloading...")
	ys.download()
	print("Downloaded")
	print()
