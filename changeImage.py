#!/usr/bin/env python3

from PIL import Image
import os

directory = r'supplier-data/images'
fullpath = os.path.abspath(directory)

for filename in os.listdir(fullpath):
  if filename[-5:] == '.tiff':
    newsize = (600, 400)
    im = Image.open(os.path.join(fullpath,'/', filename))
    im.resize(newsize).convert('RGB').save(fullpath + '/' + filename.replace('.tiff', '.jpeg'))
