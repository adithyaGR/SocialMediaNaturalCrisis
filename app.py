import os
from flask import Flask, render_template, jsonify, request
from urlparse import urljoin
from werkzeug.contrib.atom import AtomFeed
import urllib2
from twitter import *

app = Flask(__name__)



@app.route("/")
def home():
    
    entries = []
    
    return render_template('home.html')
    
@app.route('/twitter')
def twitter():
    hashtag = request.args.get('hashtag', 0, type=str)
    #api code here
    access_token = '720064526192758785-xBpJAVy8K17cy8cN1XRgqK9SVE1gBM7'
    access_token_secret = 'hHk5eApjGTylZZQTf3qUZSfynMQSM2k5q7UCUbcrHWVr4'
    consumer_key = 'p6F7uXZGzIH5EtjNZeeD2pVXO'
    consumer_secret = 'FPBpRhvEdjYYNXqRCT4z7cVfGTdt3MmWYLTkNfL0eCt8YWHjsI'
    # hashtag = '#' + hashtag
    twitter = Twitter(auth=OAuth(access_token, access_token_secret,consumer_key,consumer_secret))
    results = twitter.search.tweets(q=hashtag, count=30)
    return jsonify(result=results.get('statuses'))
  
@app.route('/facebook')
def facebook():
    #api code here
    page_id = request.args.get('link', 0, type=str)
    app_id = "1717188741826592"
    app_secret = "e3490a08c71ee8539b987fdb25ed0861"
    get_auth_token = 'https://graph.facebook.com/oauth/access_token?grant_type=client_credentials&client_id='+app_id+'&client_secret='+app_secret
    authToken = urllib2.urlopen(get_auth_token).read()
    feed_url = "https://graph.facebook.com/"+page_id+"/feed?"+authToken
    page_feed = urllib2.urlopen(feed_url).read()
    
    return jsonify(result=page_feed)
    

    

app.run(debug=True,host=os.getenv("IP", "0.0.0.0"),port=int(os.getenv("PORT", 8080)))

