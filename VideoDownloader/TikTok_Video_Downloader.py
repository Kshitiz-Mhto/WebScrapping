import requests

#Read the GuideMe First before using it...
Video_Link = input("Enter the Video Link ") 
Link_response = requests.get(Video_Link,stream=True)
Video_name = input('Enter the name you want to save downloading tiktok as ')
try:
	with open(Video_name+'.mp4','wb') as file:
		file.write(Link_response.content)
except Exception as e:
	print(e)
