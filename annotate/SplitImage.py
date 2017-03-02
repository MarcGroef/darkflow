import cv2
import os


class SplitImage():
   
  def __init__(self):
    self.currentImage = None
    self.croppedImage = None



  
  def split(self, imagepath, exportPath, filename):
     self.currentImage = cv2.imread(imagepath)
     if(self.currentImage == None):
        print("couldnt read " + exportPath + filename)
	return
     if(os.path.isfile(exportPath)):
        return

     height, width, channels = self.currentImage.shape
     height_slice = height / 10
     width_slice = width / 10
     sl_idx = 0
     for i in range(2, 8):
        self.croppedImage = self.currentImage[height_slice * i:height,0:width]
        cv2.imwrite(exportPath + "cropped_" + str(sl_idx) + "_" + filename, self.croppedImage, [cv2.IMWRITE_JPEG_QUALITY, 100] )
        sl_idx += 1

        self.croppedImage = self.currentImage[0 : height - height_slice * i,0:width]
	cv2.imwrite(exportPath + "cropped_" + str(sl_idx) + filename, self.croppedImage, [cv2.IMWRITE_JPEG_QUALITY, 100] )
        sl_idx += 1

        self.croppedImage = self.currentImage[0:height,width_slice * i:width]
	cv2.imwrite(exportPath + "cropped_" + str(sl_idx) + filename, self.croppedImage, [cv2.IMWRITE_JPEG_QUALITY, 100] )
        sl_idx += 1

        self.croppedImage = self.currentImage[0 : height,0:width - width_slice * i]
	cv2.imwrite(exportPath + "cropped_" + str(sl_idx) + filename, self.croppedImage, [cv2.IMWRITE_JPEG_QUALITY, 100] )
        sl_idx += 1
