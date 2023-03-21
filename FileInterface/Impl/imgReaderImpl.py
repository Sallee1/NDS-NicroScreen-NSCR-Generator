from __imports__ import *

from customException.ex import FileTypeError

import Utils.imgTool as imgTool
from FileInterface.imgReader import InterfaceImgReader


class TrueColorImgReader(InterfaceImgReader):
  """读取真彩色图片"""
  def readFromFile(self, filePath: str) -> Image.Image:
    imgFile = Image.open(filePath)
    # 尝试将索引颜色图像转换为真彩色
    realColorImg = imgTool.indexedImg2TrueColor(imgFile)
    return realColorImg

class IndexColorImgReader(InterfaceImgReader):
  """读取索引颜色图片"""
  def readFromFile(self, filePath: str) -> Image.Image:
    imgFile = Image.open(filePath)
    if(imgFile.getpalette is None):
      raise FileTypeError(f"文件格式错误，需要的格式为索引颜色图像，但实际打开真彩色图像")
    return imgFile