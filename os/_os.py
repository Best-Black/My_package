'''
Author: PHH
Data: 2021.11.04
Update: 2021.11.04

Describe: this package is building for os, such as read txt or an image
'''

import os
import numpy as np



def get_filename(dir):
    '''
    You can input a folder-name and this function will output the filenames
    in this folder
    :param dir:  a path
    :return: the filename in the path
    '''
    files = os.listdir(dir)
    r = [os.path.join(dir,f)
         for f in files]
    return r

def get_image_filename(dir):
    '''
    Only return images name
    :param dir:
    :return:
    '''
    image_types = ('jpg','jpeg','tiff','tif','png','bmp','gif','BMP')
    files = os.listdir(dir)
    exts = (os.path.splitext(f)[1] for f in files)
    images = [os.path.join(dir,f)
              for e,f in zip(exts,files)
              if e[1:] in image_types]
    return images

def get_doc_filename(dir):
    '''
    Only return docs name
    :param dir:
    :return:
    '''
    docs_types = ('txt','pdf','word')
    files = os.listdir(dir)
    exts = (os.path.splitext(f)[1] for f in files)
    docs = [os.path.join(dir,f)
              for e,f in zip(exts,files)
              if e[1:] in docs_types]
    return docs


















if __name__ == '__main__':
    print(get_filename(r'E:\Project_git\My_package\os'))




