from xmlwriter import XMLWriter
import cv2
import os
import time
import numpy as np

class Cropper():
   
  def __init__(self, labels, exportfolder):

     self.space = 1048608
     self.delete = 1114111   
     self.w = 1048695
     self.a = 1048673
     self.s = 1048691
     self.d = 1048676
     self.r = 1048690
     self.up = 1113938
     self.down = 1113940
     self.left = 1113937
     self.right = 1113939
     self.enter = 1048586
     
     self.objects = [] 
     self.height = 100
     self.width = 100
     self.x = 100
     self.y = 100

     self.currentImage = None
     self.labels = labels
     self.exportfolder = exportfolder
     self.currentImagePath = ""
     self.counter = 0

     cv2.namedWindow('imageWindow', cv2.WINDOW_AUTOSIZE)

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
     
  def updateX(self, val):
     self.x = self.x + val
     
  
  def updateY(self, val):
     self.y = self.y + val
  
  def updateWidth(self, val):
     self.width = self.width + val
  
  def updateHeight(self, val):
     self.height = self.height + val
     
  def addBBox(self, label):
     self.objects = self.objects + [[self.getLabelFromUser(), self.x, self.y, self.width, self.height]]
  
  def reset(self):
     self.objects = [] 
     
  
  def resetBBox(self):
     self.height = 100
     self.width = 100
     self.x = 100
     self.y = 100

  def getLabelFromUser(self):
     print "Label options:"
     labelIdx = 0
     for label in self.labels:
        print "(" + str(labelIdx) + "): " + label + ", "
        labelIdx += 1
     
     inp = cv2.waitKey(0) - 1048625 + 1
     print "It's a " + self.labels[int(inp)] + "!"
     return self.labels[int(inp)]

  def writeXML(self):
     try:
       print "trying to write..."
       xml = XMLWriter(self.objects, "borgball", (str(self.imIdx) + ".jpg"), 240, 320, 3, (self.exportfolder + str(self.imIdx) + ".xml"))
       xml.write()
     except Exception as ex:
       print ex
       print "something went wrong during writeXML()"



  def listen(self):
     while True:
        self.render()
        key = cv2.waitKey(200)
        if key != -1:
           #print key
           if key == self.enter:
              self.writeXML()
              self.reset()
              return
           if key == self.space:
              self.addBBox("")
           if key == self.r:
              self.resetBBox()
           if key == self.a:
              self.updateX(-2)
           if key == self.d:
              self.updateX(2)
           if key == self.w:
              self.updateY(-2)
           if key == self.s:
              self.updateY(2)
           if key == self.up:
              self.updateHeight(-2)
           if key == self.down:
              self.updateHeight(2)
           if key == self.left:
              self.updateWidth(-2)
           if key == self.right:
              self.updateWidth(2)
              
              
  def render(self):
     
     if(len(self.currentImage) > 0):
        renderImage = np.ndarray.copy(self.currentImage)
        for obj in self.objects:
           cv2.putText(renderImage,obj[0],(obj[1],obj[2] - 2), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (115,115,115),2)
           cv2.rectangle(renderImage,(obj[1],obj[2]),(obj[1]+obj[3],obj[2]+obj[4]),(50,50,50),2)

        
        cv2.rectangle(renderImage,(self.x,self.y),(self.x+self.width,self.y+self.height),(0,0,255),2)
        cv2.imshow( 'imageWindow', renderImage)
        cv2.waitKey(1)




  def crop(self, imagepath, exportPath, imIdx):
     self.imIdx = imIdx
     self.currentImagePath = imagepath
     self.currentImage = cv2.imread(imagepath)
     self.render()
     self.listen()

     
     
     

