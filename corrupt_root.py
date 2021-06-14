from os import listdir
from PIL import Image
import shutil 
import random
import os
import numpy as np

city = 'nyc'
for filename in listdir('./' + city + '_photos/'):
    with open(os.path.join('./' + city + '_photos', filename), 'rb') as f:
        check_chars = f.read()[-2:]
        img = np.array(Image.open('./' + city + '_photos/' + filename))
        if len(img.shape) !=3 or check_chars != b'\xff\xd9':
            print('Not complete image')
            shutil.move('./'  +city + '_photos/' + filename, './incomplete_image')
            metadata = filename[:-3] + 'txt'
            shutil.move('./' + city + '_metadata/' + metadata, './incomplete_image')
