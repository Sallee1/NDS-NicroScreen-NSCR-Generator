from __imports__ import *

from Utils.Decorator.returnCopy import returnCopy

class DsPal:
  """
  描述NDS中使用的调色板文件

  attributes:
  * ndarray[256,3] data{get,set}: 调色板保存的实际颜色数据(15bpp)，默认为全[0,0,0]
  * PalFormat format{get,set}: 调色板的格式，可选4bpp和8bpp，默认为8bpp
  * int length{get,set}: 调色版的长度，范围为1~256，默认为256

  methods:
  * DsPal [data] [palFormat] [length] -> None\n
      params:\n
        参见attributes
  """
  def __init__(self,
    data=np.zeros((256,3),dtype=np.uint8),
    palFormat=PalFormat.bpp8,
    length = 256) -> None:

    self.__data:np.ndarray = data    #调色板数据
    self.__format:PalFormat = palFormat      #调色板格式
    self.__length:int = length   #调色板颜色数
  
  @returnCopy
  def getData(self)->np.ndarray:return self.__data
  def setData(self,data:np.ndarray):self.__data = data

  @returnCopy
  def getFormat(self)->PalFormat:return self.__format
  def setFormat(self,format:PalFormat):self.__format = format

  @returnCopy
  def getLength(self)->int:return self.__length
  def setLength(self,length:int): self.__length = length