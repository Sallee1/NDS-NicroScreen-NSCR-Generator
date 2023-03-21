from __imports__ import *


from FileInterface.imgSaver import InterfaceImgSaver
from FileInterface.Impl.imgSaverImpl import *


class ImgSaverFactory():
  """图像保存器工厂类"""

  class Keys(Enum):
    indexedColor = 2
    trueColor = 3
  
  @staticmethod
  def getInstance(colorType)->InterfaceImgSaver:
    """
    给定颜色格式，返回对应的图像写入模块
    Params:
    * ColorType: 颜色格式，从keys获取
    """

    colorDic = {
      ImgSaverFactory.Keys.indexedColor:IndexedColorImgSaver(),
      ImgSaverFactory.Keys.trueColor:TrueColorImgSaver()
    }
    return colorDic[colorType]