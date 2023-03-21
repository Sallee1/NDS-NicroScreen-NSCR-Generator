from customException.ex import FileTypeError
import cv2
import numpy as np
from PIL import Image

from FileInterface.imgSaver import InterfaceImgSaver
from Utils.imgTool import indexedImg2TrueColor
from Utils.Decorator.checkNoneReturn import checkNoneReturn


class IndexedColorImgSaver(InterfaceImgSaver):
  """索引颜色图像"""
  def saveAsFile(self, filePath: str, img: Image.Image):
    if(img.getpalette() is None):
      raise FileTypeError(f"文件格式错误，需要的格式为索引颜色图像，但实际打开真彩色图像")
    img.save(filePath)

class TrueColorImgSaver(InterfaceImgSaver):
  """全彩色图像"""
  def saveAsFile(self, filePath: str, img: Image.Image):
    if(img.getpalette() is not None):
      img = indexedImg2TrueColor(img)
    img.save(filePath)