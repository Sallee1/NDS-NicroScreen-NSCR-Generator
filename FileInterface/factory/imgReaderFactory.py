from __imports__ import *

from FileInterface.imgReader import InterfaceImgReader
from FileInterface.Impl.imgReaderImpl import *


class ImgReaderFactory():
  """图像读取器的工厂类"""
  class Keys(Enum):
    trueColor = 1
    indexedColor = 2
  
  @staticmethod
  def getInstance(colorType)->InterfaceImgReader:
    """
    给定颜色格式，返回对应的图像读取模块
    Params:
    * ColorType: 颜色格式，从keys获取
    """

    colorDic = {
      ImgReaderFactory.Keys.indexedColor:IndexColorImgReader(),
      ImgReaderFactory.Keys.trueColor:TrueColorImgReader()
    }
    return colorDic[colorType]

