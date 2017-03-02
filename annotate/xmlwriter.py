
class XMLWriter():


   #detection should be list: [[classname, x,y,h,w]]
   def __init__(self, detections, datafolder, imagefilename, exportfile):
      self.detections = detections
      self.exportfile = exportfile
      self.imfile = imagefilename  #without relative path
      self.exportfile = exportfile  #with relative path
      self.datafolder = datafolder
      self.annotation = open(exportfile, 'r+')
      
   def writeHead(self):
      head = "\
<annotation>\n\
\t<folder>" + self.datafolder + "</folder>\n\
\t<filename>" + self.imfile "</filename>\n"
      self.annotation.write(head)

   def writeObject(self, classname, xmin, ymin, xmax, ymax):
      for obj in self.detections:
         stringObj = "\
\t<object>\n\
\t\t<name>"+ obj[1] +"
\t\t<xmin>" +  + "</xmin>\n\
"

   def writeTail(self):
      pass
