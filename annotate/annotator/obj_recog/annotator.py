from cropper import Cropper
import os
import sys
import cv2

DATASET_FOLDER = "~/datasets/borg/"
IMAGES = "JPEGImages"
ANNOTATIONS = "Annotations"

ANNOTATIONS_FOLDER = DATASET_FOLDER + ANNOTATIONS
IMAGE_FOLDER = DATASET_FOLDER + IMAGES

def main():
   Cropper cropper();
   for root, dirs, files in os.walk(IMAGE_FOLDER):
      print files


if __name__ == '__main__':
   main()
