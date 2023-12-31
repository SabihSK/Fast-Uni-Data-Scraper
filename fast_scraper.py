# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1CErG3jVZX4VwGn_owkCI_Vg-cdZlj7Hy
"""

from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np

url = 'https://khi.nu.edu.pk/faculty-php/'

nuwebpage = requests.get(url)
print(nuwebpage.status_code)

soup = BeautifulSoup(nuwebpage.content,  'html.parser')

datas = soup.find_all('div', class_='gdlr-core-personnel-list-column')



lname= []
position=[]
email=[]
ext=[]
image=[]

for data in datas:
  lname.append(data.find('h3', class_='gdlr-core-personnel-list-title').text)
  position.append(data.find('div', class_='gdlr-core-personnel-list-position').text)
  email.append(data.find('div', class_='kingster-type-email').text.replace('Email:', '').strip())
  ext.append(data.find('div', class_='kingster-type-phone').text.replace('Phone:', '').strip())
  image.append(data.find('img')['src'] if data.find('img') else None)

image

data = {
    'Name' : lname,
    'Position': position,
    'Email': email,
    'Ext': ext,
    'Image': image
}

data

df = pd.DataFrame(data, columns = ['Name', 'Position', 'Email', 'Ext', 'Image'])

df

df.to_csv('out.csv')

