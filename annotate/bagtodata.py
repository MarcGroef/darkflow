import rospy
import cv2

import numpy as np
from sensor_msgs.msg import Image
from cv_bridge import CvBridge


DATASET_FOLDER = "/home/marc/datasets/borgball/"
IMAGES = "JPEGImages/"
ANNOTATIONS = "Annotations/"
IMEXT = ".jpg"
ANEXT = ".xml"


class Extractor:
   def __init__(self): 
      self.counter = 0
      rospy.init_node("bagdump")
      rospy.Subscriber("/NAO/image_bottom", Image, self.imageCB)
      self.bridge = CvBridge()

   def imageCB(self,data):
      temp = self.bridge.imgmsg_to_cv2(data)
      image = np.asarray(temp[:,:]) 
      cv2.imwrite(DATASET_FOLDER + IMAGES + str(self.counter) + IMEXT, image, [cv2.IMWRITE_JPEG_QUALITY, 100] )
      print "exported " + str(self.counter) + IMEXT
      self.counter += 1

def main():
   extr = Extractor()
   rospy.spin()



if __name__ == '__main__':
   main()
