#Testing BeautifulSoup
from __future__ import print_function
from bs4 import BeautifulSoup

import time
import re
import requests
import subprocess				
							# regex = '<title>(.+?)</title>

MAX = 100
url = "";

def sendmessage(message):
	subprocess.Popen(['notify-send',message])
	return
	
def pingurl(url):
	r = requests.get(url)
	data = r.text
	soup = BeautifulSoup(data)
	return soup
	
def matchscoreupdate():
	url = raw_input("Enter a url : ")
	count = 1
	while(count < MAX):
		soup = pingurl(str(url))
		sendmessage(soup.title.string)
		count += 1
		time.sleep(10)

if __name__ == "__main__":
	matchscoreupdate()
	
	