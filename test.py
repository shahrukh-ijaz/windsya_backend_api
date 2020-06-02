from bs4 import BeautifulSoup as soup
import requests
import time
import os

req = requests.get("http://windsya.com/download/ok.mp4")
import pdb;pdb.set_trace();

url = 'https://www.dailymotion.com/video/x4b8ojh'
if 'playlist' in url:
    code=(re.findall(r'video/.+\?',url)[0][:-1])
print('Loading... takes up to 15 seconds')
sr=soup(requests.get(f'https://dmvideo.download/?url={url}').text,'html.parser',time.sleep(5))
res=sr.findAll('tbody')[0].findAll('tr')
links=[]

path = "download/"
if not os.path.exists(path):
    os.makedirs(path)

for x in res:
    req = requests.get("http://windsya.com/download/ok.mp4")
    import pdb;pdb.set_trace();
    filename = req.headers['Content-Disposition'].split('="')[1].split('"')[0]
    if filename:
        with open(os.path.join(path, filename),'wb') as f:
            f.write(req.content)
        break
filename = filename.replace(' ', '_')
print("{}{}".format(path, filename))
