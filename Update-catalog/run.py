#! /usr/bin/env python3
import os
import requests
import json
user = os.environ.get('USER')
path = '/home/'+ user+'/supplier-data/descriptions/'
dirs=os.listdir(path)
url='http://localhost/fruits/'
fruit={}
for item in dirs:
 fruit.clear()
 filename=os.path.join(path,item)
 with open(filename) as f:
  line=f.readlines()
  description=""
  for i in range(2,len(line)):
    description=description+line[i].strip('\n')
  fruit["description"]=description
  fruit["weight"]=int(line[1].strip('\n').strip('lbs'))
  fruit["name"]=line[0].strip('\n')
  fruit["image_name"]=(item.strip('.txt'))+'.jpeg'
  print(fruit)
  response=requests.post("http://localhost/fruits/",json=fruit)
  print(response.request.url)
  print(response.status_code)



