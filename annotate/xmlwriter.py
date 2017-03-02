
class XMLWriter():


   #detection should be list: [[classname, x,y,w,h]]
   def __init__(self, detections, datafolder, imagefilename, imheight, imwidth, imchannels, exportfile):
      self.detections = detections
      self.exportfile = exportfile
      self.imfile = imagefilename  #without relative path
      self.exportfile = exportfile  #with relative path
      self.datafolder = datafolder
      self.annotation = open(exportfile, 'r+')
      self.imheight = imheight
      self.imwidth = imwidth
      self.imchannels = imchannels
      
   def writeHead(self, imheight, imwidth):
      head = "\
<annotation>\n\
\t<folder>" + self.datafolder + "</folder>\n\
\t<filename>" + self.imfile "</filename>\n\
\t<size>
\t\t<width>" + self.imwidth + "</width>\n\
\t\t<height>" + self.imheight + "</height>\n\
\t<\size>
"

      self.annotation.write(head)

   def writeObjects(self):
      objects = ""
      for obj in self.detections:
         stringObj = "\
\t<object>\n\
\t\t<name>"+ obj[0] +"
\t\t<bndbox>\n\
\t\t\t<xmin>" + str(obj[1]) + "</xmin>\n\
\t\t\t<xmax>" + str(obj[1] + obj[3]) + "</xmax>\n\
\t\t\t<ymin>" + str(obj[2]) + "</ymin>\n\
\t\t\t<ymax>" + str(obj[2] + obj[4]) + "</ymax>\n\
\t\t</bndbox>\n\
\t<object>\n"
         objects += stringObj
      self.annnotation.write(stringObj)
      
      
   def writeTail(self):
      tail = "<\annotation>"
      self.annnotation.write(tail)
      
   def write(self):
      self.writeHead()
      self.writeObjects()
      self.writeTail()
      

