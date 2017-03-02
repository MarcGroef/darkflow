from cropper import Cropper
import os
import sys
import cv2

DATASET_FOLDER = "/home/marc/datasets/borg/"
IMAGES = "JPEGImages"
ANNOTATIONS = "Annotations"
IMEXT = ".jpg"
ANEXT = ".xml"

ANNOTATIONS_FOLDER = DATASET_FOLDER + ANNOTATIONS
IMAGE_FOLDER = DATASET_FOLDER + IMAGES

def main():
   cropper = Cropper()
   for root, dirs, files in os.walk(IMAGE_FOLDER):  ##assumption imname = [number].jpg, 1.jpg, 2.jpg, ...
      for idx in range(0,len(files)):
         ann_name = str(idx) + ANEXT
         im_name = str(idx) + IMEXT
         


if __name__ == '__main__':
   main()
