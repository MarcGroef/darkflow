from cropper import Cropper
from SplitImage import SplitImage
import os
import sys
import cv2

def exportHSV(hsv, name):
  im = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
  cv2.imwrite(name, im, [cv2.IMWRITE_JPEG_QUALITY, 100] )

def augment_image(imfile, targetdir, tarfile):
  image = cv2.imread(imfile);
  hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
  #h, s, v = cv2.split(hsv)
  hsv[:,:,2] = 175
  h[:,:,0]
  
  #cv2.imshow('window', hsv)
  #cv2.waitKey(0)

  #out = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
  #cv2.imshow('example', out)
  #cv2.waitKey(0)
  for v in range(0,5):
     deltaV = 0
     exportHSV(hsv, targetdir + deltaV + "-" + tarfile)
     



def main():
#  crop = Cropper()
  split = SplitImage()
  pathToImages = "/home/marc/objects/dataset/"
  pathBack = "/home/marc/objects/"
  #cv2.namedWindow('window', cv2.WINDOW_AUTOSIZE)
  for root, dirs, files in os.walk(pathToImages):
    path = root.split('/')
    #print(path)
    if not os.path.exists(pathBack + "datasetenlarged"): 
      os.makedirs(pathBack + "datasetenlarged")
    print(os.path.basename(root))
    print(len(files))
    
    for idx in range(0, len(files)):
      f = str(idx) + ".jpg"
      #for f in sorted(files):
      tardir = path[0] + "/" + path[1] + "/" + path[2] + "/" + path[3] + "/slicesofcroppedimages/" + path[5] + "/"
      cropdir = path[0] + "/" + path[1] + "/" + path[2] + "/" + path[3] + "/crop/" + path[5] + "/" + f
      sourcedir = path[0] + "/" + path[1] + "/" + path[2] + "/" + path[3] + "/" + path[4] + "/" + path[5] + "/" + f
      #augment_image(sourcedir, tardir, f)
      #crop.crop(sourcedir, cropdir)
      #split.split(cropdir, tardir, f)
 
if __name__ == '__main__':
  main()
