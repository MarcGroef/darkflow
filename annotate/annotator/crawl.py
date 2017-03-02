from cropper import Cropper

import os
import sys
import cv2

def exportHSV(hsv, name):
  im = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
  cv2.imwrite(name, im, [cv2.IMWRITE_JPEG_QUALITY, 100] )

def augment_image(imfile, targetdir):
  image = cv2.imread(imfile);
  hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
  #h, s, v = cv2.split(hsv)
  hsv[:,:,2] = 175
  exportHSV(hsv, targetdir)#+ '\+ "-175")
  #cv2.imshow('window', hsv)
  #cv2.waitKey(0)

  #out = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
  #cv2.imshow('example', out)
  #cv2.waitKey(0)
  for v in range(0,5):
     #print v
     pass



def main():

  cropper = Cropper()
  pathToImages = "/home/student/objects/dataset/"
  pathBack = "/home/student/objects/"
  cv2.namedWindow('window', cv2.WINDOW_AUTOSIZE)
  for root, dirs, files in os.walk(pathToImages):
    path = root.split('/')
    #print(path)
    if not os.path.exists(pathBack + "datasetenlarged"): 
      os.makedirs(pathBack + "datasetenlarged")
    #print(os.path.basename(root))
    for f in files:
      #print(pathBack + "datasetenlarged/" + f)
#      #print path[5]
      tardir = path[0] + "/" + path[1] + "/" + path[2] + "/" + path[3] + "/augment/" + path[5] + "/" + f
      sourcedir = path[0] + "/" + path[1] + "/" + path[2] + "/" + path[3] + "/" + path[4] + "/" + path[5] + "/" + f
      #print tardir
      #print f
      #augment_image(sourcedir, tardir)
      #print(root)
      #pass
 
if __name__ == '__main__':
  main()
