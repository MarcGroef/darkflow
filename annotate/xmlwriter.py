
class XMLWriter():


   #detection should be list: [[classname, x,y,w,h]]
   def __init__(self, detections, datafolder, imagefilename, imheight, imwidth, imchannels, exportfile):
      try:
        #print "init....."
        #print "making annotation file: " + self.exportfile
        self.detections = detections
        self.exportfile = exportfile
        self.imfile = imagefilename  #without relative path
        self.exportfile = exportfile  #with relative path
        self.datafolder = datafolder
      
        self.annotation = open(self.exportfile, 'w')
        self.imheight = imheight
        self.imwidth = imwidth
        self.imchannels = imchannels
      except:
        print "except in init.."


   def writeHead(self):
      head = "\
<annotation>\n\
\t<folder>" + self.datafolder + "</folder>\n\
\t<filename>" + str(self.imfile) + "</filename>\n\
\t<size>\n\
\t\t<width>" + str(self.imwidth) + "</width>\n\
\t\t<height>" + str(self.imheight) + "</height>\n\
\t</size>\n"

      self.annotation.write(head)

   def writeObjects(self):
      objects = ""
      for obj in self.detections:
         stringObj = "\
\t<object>\n\
\t\t<name>"+ obj[0] + "</name>\n\
\t\t<bndbox>\n\
\t\t\t<xmin>" + str(obj[1]) + "</xmin>\n\
\t\t\t<xmax>" + str(obj[1] + obj[3]) + "</xmax>\n\
\t\t\t<ymin>" + str(obj[2]) + "</ymin>\n\
\t\t\t<ymax>" + str(obj[2] + obj[4]) + "</ymax>\n\
\t\t</bndbox>\n\
\t</object>\n"
         objects += stringObj
      self.annotation.write(stringObj)
      
      
   def writeTail(self):
      tail = "</annotation>"
      self.annotation.write(tail)
      
   def write(self):
      self.writeHead()
      self.writeObjects()
      self.writeTail()
      self.annotation.close()
      print "Done exporting!"

