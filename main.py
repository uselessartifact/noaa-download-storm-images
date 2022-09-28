from bs4 import *
import os, re, requests, urllib

url = "https://cdn.star.nesdis.noaa.gov/FLOATER/data/AL092022/GEOCOLOR/"

r = requests.get(url).content

soup = BeautifulSoup(r, 'html.parser')

folder = "C:/Users/rbaldwin/OneDrive - Paytech, Inc/Pictures/HURIAN/"

dirlist = os.listdir(folder)

for img in soup.findAll('a', href=True):
	filename = re.search('.*-1000x1000.jpg', img['href'])
	if filename != None and filename.string not in dirlist:
		image = urllib.request.urlopen(url + filename.string)
		fullfile = str(folder + filename.string)
		print(url + filename.string)
		with open(fullfile,'wb') as f:
			f.write(image.read())
			f.close()
