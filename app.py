from __future__ import unicode_literals
from flask import Flask, render_template, request
from flask_cors import CORS, cross_origin
from bs4 import BeautifulSoup as soup
import pafy
import requests,re
import time
from flask import jsonify
import json


app = Flask(__name__)
CORS(app)


@app.route('/get_video', methods=['POST'])
@cross_origin()
def get_urls():
    URL=request.form['video_url']
    myvid = pafy.new(URL)
    format = "video"
    z=myvid.streams
    y=myvid.audiostreams 
    video_url = z[-1].url
    audio_url = y[-1].url
    
    urls = json.dumps(dict({
        "video_url": video_url,
        "audio_url": audio_url
    } ))
    return urls

@app.route('/get_dailymotion_video', methods=['POST'])
@cross_origin()
def dailymotion():
    url=request.form['video_url']  
    if 'playlist' in url:
        code=(re.findall(r'video/.+\?',url)[0][:-1])
    sr=soup(requests.get(f'https://dmvideo.download/?url={url}').text,'html.parser',time.sleep(5))
    res=sr.findAll('tbody')[0].findAll('tr')

    path = "download/"
    if not os.path.exists(path):
        os.makedirs(path)

    for x in res:
        req = requests.get(x.a['href'])
        filename = req.headers['Content-Disposition'].split('="')[1].split('"')[0]
        if filename:
            with open(os.path.join(path, filename),'wb') as f:
                f.write(req.content)
            break
    filename = filename.replace(' ', '_')
    return "{}{}".format(path, filename)

@app.route('/dailymotion')
def daily_video():
    return render_template("dailymotion.html")


@app.route('/api')
def api():
    return render_template("video.html")

if __name__ == '__main__':
    app.run()
