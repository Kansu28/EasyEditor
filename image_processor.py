import os
from PIL import Image, ImageOps
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap


class ImageProcessor:
    def __init__(self):
        self.image = None
        self.dir = None
        self.filename = None
        self.save_dir = "Modified/"
        self.lb_image = None

    def loadImage(self,dir,filename):
        self.dir = dir
        self.filename = filename
        image_path = os.path.join(dir,filename)
        self.image = Image.open(image_path)

    def showImage(self,path,lb_image):
        self.lb_image = lb_image
        lb_image.hide()
        qpixmapimage = QPixmap(path)
        qpixmapimage = qpixmapimage.scaled(lb_image.width(),lb_image.height(),Qt.KeepAspectRatio)
        lb_image.setPixmap(qpixmapimage)
        lb_image.show()

    def saveImage(self):
        path = os.path.join(self.dir,self.save_dir)
        if not (os.path.exists(path) or os.path.isdir(path)):
            os.mkdir(path)
        image_path = os.path.join(path,self.filename)
        self.image.save(image_path)

    def do_bw(self):
        self.image = self.image.convert("L")
        self.saveImage()
        image_path = os.path.join(self.dir,self.save_dir,self.filename)
        self.showImage(image_path,self.lb_image)

    def do_left(self):
        self.image = self.image.rotate(-90)
        self.saveImage()
        image_path = os.path.join(self.dir, self.save_dir, self.filename)
        self.showImage(image_path, self.lb_image)

    def do_right(self):
        self.image = self.image.rotate(90)
        self.saveImage()
        image_path = os.path.join(self.dir, self.save_dir, self.filename)
        self.showImage(image_path, self.lb_image)


    def do_flip(self):
        self.image = ImageOps.mirror(self.image)
        self.saveImage()
        image_path = os.path.join(self.dir, self.save_dir, self.filename)
        self.showImage(image_path, self.lb_image)
