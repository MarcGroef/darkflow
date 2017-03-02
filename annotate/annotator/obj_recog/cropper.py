import cv2
import os


class Cropper():
   
  def __init__(self):

     self.space = 1048608
     self.delete = 1114111   
 
     self.height = 100
     self.width = 100
     self.x = 100
     self.y = 100

     self.currentImage = None
     self.croppedImage = None

     cv2.namedWindow('trackbarWindow', cv2.WINDOW_AUTOSIZE)
     cv2.namedWindow('imageWindow', cv2.WINDOW_AUTOSIZE)
     cv2.namedWindow('croppedWindow', cv2.WINDOW_AUTOSIZE)
     cv2.createTrackbar("height", 'trackbarWindow', 100, 300, self.heightCB)
     cv2.createTrackbar("width", 'trackbarWindow', 100, 300, self.widthCB)
     cv2.createTrackbar("y", 'trackbarWindow', 100, 300, self.YCB)
     cv2.createTrackbar("x", 'trackbarWindow', 100, 300, self.XCB)
     cv2.waitKey(1)

  def heightCB(self, value):
     self.height = value
     self.render()


  def widthCB(self, value):
     self.width = value
     self.render()
     

  def XCB(self, value):
     self.x = value
     self.render()

  def YCB(self, value):
     self.y = value
     self.render()


  def render(self):
     self.modify()
     if(self.currentImage != None):
	     cv2.imshow( 'imageWindow', self.currentImage)
	     cv2.waitKey(1)

     if(self.croppedImage != None):
	     cv2.imshow( 'croppedWindow', self.croppedImage)
	     cv2.waitKey(1)

  def modify(self):
     self.croppedImage = self.currentImage[self.y:(self.height + self.y),self.x:(self.width + self.x)]

  def crop(self, imagepath, exportPath):
     self.currentImage = cv2.imread(imagepath)
     self.render()
     if(os.path.isfile(exportPath)):
        return
     key = None
     while True:
        key = cv2.waitKey(1)
        self.render()
        if key == self.space:
           cv2.imwrite(exportPath, self.croppedImage, [cv2.IMWRITE_JPEG_QUALITY, 100] )
           print("exported to " + exportPath)
           break
        if key == self.delete:
           break
        
     
     
     

