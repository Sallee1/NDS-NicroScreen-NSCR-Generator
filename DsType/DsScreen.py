import numpy as np

from DsType.DsPal import PalFormat
from Utils.Decorator.returnCopy import returnCopy


class DsScreen:
  """
  描述NDS使用的命名表文件\n
  attributes:
  * ndarray[ht,wd] tileData{get,set}:tile编号位平面，范围在0~1023
  * ndarray[ht,wd] flipData{get,set}:翻转位平面，范围在0~4
  * ndarray[ht,wd] palData{get,set}: 颜色位平面，范围在0~16
  * int width{get,set}:宽度，以tile为计
  * int height{get,set}:高度，以tile为计
  
  methods:
  * DsScreen [data] [width] [height] -> None\n
      params:\n
        np.ndarray data:从NSCR直接读取的原始数据\n
        其他参见attributes\n
        默认构造长宽为32的空白DsScreen\n
  * getData() -> np.ndarray\n
      return:\n
        将位平面合并为原始数据返回\n
  * setData <data> -> None\n
      params:\n
        np.ndarray data: 将原始数据拆分为位平面
  """
  def __init__(self,
    data = np.zeros((256,256),dtype=np.int16),
    width = 32, height = 32):
    self.__tileData = data&0b0000001111111111
    self.__flipData = data&0b0000110000000000 >> 10
    self.__palData  = data&0b1111000000000000 >> 12
    self.__width = width
    self.__height = height

  @returnCopy
  def getTileData(self): return self.__tileData
  def setTileData(self,tileData:np.ndarray):self.__tileData=tileData

  @returnCopy
  def getFlipData(self): return self.__flipData
  def setFlipData(self,flipData:np.ndarray):self.__flipData=flipData

  @returnCopy
  def getPalData(self): return self.__palData
  def setPalData(self,palData:np.ndarray):self.__tileData=palData

  def getData(self):
    return self.__tileData + (self.__flipData << 10) + (self.__palData << 12)
  
  def setData(self,data:np.ndarray):
    self.__tileData = data&0b0000001111111111
    self.__flipData = data&0b0000110000000000 >> 10
    self.__palData  = data&0b1111000000000000 >> 12
  
  @returnCopy
  def getWidth(self):return self.__width
  def setWidth(self,width:int): self.__width = width

  @returnCopy
  def getHeight(self):return self.__height
  def setHeight(self,height:int): self.__height = height