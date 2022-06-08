import requests
from bs4 import BeautifulSoup

link = input('url ')
response = requests.get(link)
obj = BeautifulSoup(response.text, 'html.parser')
list_imgs = obj.find_all('img')

c=1

try:
	for imgTag in list_imgs:
		# print(imgTag)
		imgLink = imgTag.get('src')
		#print(imgLink)
		extension = imgLink[imgLink.rindex('.'):]
		fileN = str(c) + extension
		if(imgLink.startswith('https')):
			imgRep = requests.get(imgLink, stream=True)
			with open(fileN, 'wb') as img:
				img.write(imgRep.content)
			c += 1
		elif(imgLink.startswith('http:')):
			print('Not Secure Site')
			inpu = (input('Do U insist, y or n ')).lower()
			if(inpu == 'y'):
				imgLink_c = imgLink 
				imgRep = requests.get(imgLink_c, stream=True)
				with open(fileN, 'wb') as img:
					img.write(imgRep.content)
				c+=1
			else:
				break

		elif(imgLink.startswith('/')):
			imgLink_c = link + imgLink 
			imgRep = requests.get(imgLink_c, stream=True)
			with open(fileN, 'wb') as img:
				img.write(imgRep.content)
			c+=1
		else:
			imgRep = requests.get(imgLink, stream=True)
			with open(fileN, 'wb') as img:
				img.write(imgRep.content)
			c+=1

except Exception as e:
	print(e)
