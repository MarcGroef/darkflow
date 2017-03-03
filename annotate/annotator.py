from cropper import Cropper
import os
import sys
import cv2

DATASET_FOLDER = "/home/marc/datasets/borgball/"
IMAGES = "JPEGImages/"
ANNOTATIONS = "Annotations/"
IMEXT = ".jpg"
ANEXT = ".xml"

ANNOTATIONS_FOLDER = DATASET_FOLDER + ANNOTATIONS
IMAGE_FOLDER = DATASET_FOLDER + IMAGES

def main():
   print "Usage:\n[w/a/s/d]: move current bbox\n[arrow keys]: adjust bbox size\n[space] add current bbox to image bbox stack\n[enter]: next image"
   labels = ["ball", "nao"]
   cropper = Cropper(labels, ANNOTATIONS_FOLDER)
   for root, dirs, files in os.walk(IMAGE_FOLDER):  ##assumption imname = [number].jpg, 1.jpg, 2.jpg, ...
      try:
         for idx in range(0,len(files)):
            ann_name = str(idx) + ANEXT
            im_name = IMAGE_FOLDER + str(idx) + IMEXT
            image = cv2.imread(im_name)
            #print ann_name
            cropper.crop(im_name, ANNOTATIONS_FOLDER, idx)
      except:
	print "something went wrong loading image.."

if __name__ == '__main__':
   main()
