#!/usr/bin/env python3
import requests
import os
user = os.environ.get('USER')
url = "http://localhost/upload/"
directory_images = '/home/'+user+'/supplier-data/images/'
for file in os.listdir(directory_images):
  if file.endswith('.jpeg'):
    with open(directory_images + file, 'rb') as opened:
      r = requests.post(url, files={'file':opened})