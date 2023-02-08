from enum import Enum

import numpy as np

from Utils.Decorator.returnCopy import returnCopy

class PalFormat(Enum):
  bpp4 = 16
  bpp8 = 256

class DsPal:
  """
  描述NDS中使用的调色板文件

  attributes:
  * ndarray[256,3] data{get,set}: 调色板保存的实际颜色数据(15bpp)，默认为全[0,0,0]
  * PalFormat format{get,set}: 调色板的格式，可选4bpp和8bpp，默认为8bpp
  * int length{get,set}: 调色版的长度，范围为1~256，默认为256
  * int bpp4Count{get,set}: 4bpp模式下，调色板的数量，默认为16
  * bool isAlpha{get,set}: 调色板是否将第一个颜色作为透明色处理，默认为是

  methods:
  * DsPal [data] [palFormat] [length] [bpp4Count] [isAlpha] -> None\n
      params:\n
        参见attributes
  """
  def __init__(self,
    data=np.zeros((256,3),dtype=np.uint8),
    palFormat=PalFormat.bpp8,
    length = 256,
    bpp4Count = 16,
    isAlpha = True) -> None:

    self.__data:np.ndarray[256:3] = data    #调色板数据
    self.__format:PalFormat = palFormat      #调色板格式
    self.__length:int = length   #调色板颜色数
    self.__bpp4Count:int = bpp4Count #4bpp格式下，调色板个数
    self.__isAlpha:bool = isAlpha  #是否是透明格式。透明格式第一个颜色用做透明色
  
  @returnCopy
  def getData(self)->np.ndarray:return self.__data
  def setData(self,data:np.ndarray):self.__data = data

  @returnCopy
  def getFormat(self)->PalFormat:return self.__format
  def setFormat(self,format:PalFormat):self.__format = format

  @returnCopy
  def getLength(self)->int:return self.__length
  def setLength(self,length:int): self.__length = length

  @returnCopy
  def getBpp4Count(self)->int:return self.__bpp4Count
  def setBpp4Count(self,bpp4Count):self.__bpp4Count = bpp4Count

  @returnCopy
  def getIsAlpha(self)->int: return self.__isAlpha
  def setIsAlpha(self,isAlpha:bool): self.__isAlpha = isAlpha