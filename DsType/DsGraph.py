from __imports__ import *

from DsType.DsPal import PalFormat
from Utils.Decorator.returnCopy import returnCopy

class DsGraph:
  """
  描述NDS使用的瓦图文件\n
  瓦图文件中没有对颜色格式的描述信息，需要借助调色板的格式\n
  为了方便管理，实际上使用的是原始字节流，通过DsGraph提供的访问接口获取4bpp或8bpp图像
  attribute:\n
  * bytes rawData:tile的原始字节数据.
  * int length{get,set}: tile的数量,范围1~1024
  methods:\n
  * DsGraph [data] [length] [PalFormat]\n
      参数详见attribute，默认构造长度为0的4bpp瓦图\n
  * getTileData [palFormat] -> np.ndarray[-1,8,8]\n
      将原始数据转换为tile
  """
  __rawData:bytes
  __length4bpp:int

  def __init__(self,
    rawData:bytes,
    length4bpp:int = 0):
    self.__rawData = rawData
    self.__length4bpp = length4bpp

  @returnCopy
  def getRawData(self): return self.__rawData
  def setRawData(self,tiles:bytes):self.__rawData = tiles
  
  @returnCopy
  def getLength8bpp(self): return self.__length4bpp // 2
  def setLength8bpp(self,length:int): self.__length4bpp = length * 2

  @returnCopy
  def getLength4bpp(self): return self.__length4bpp
  def setLength4bpp(self,length:int): self.__length4bpp = length

  @returnCopy
  def getTileData(self,palFormat:PalFormat) -> np.ndarray:
    if(palFormat == PalFormat.bpp4):
      return self.__bytesTobpp4Tile()
    return self.__bytesTobpp8Tile()
  
  def setTileData(self,data:np.ndarray,palFormat:PalFormat) -> None:
    if(palFormat == PalFormat.bpp4):
      self.__rawData = self.__bpp4TileToBytes(data)
    self.__rawData = self.__bpp8TileToBytes(data)
      
  def __bytesTobpp4Tile(self) -> np.ndarray:
    npRawData = np.frombuffer(self.__rawData,dtype=np.uint8).reshape((-1,8,4))
    np4bbpData = np.zeros((npRawData.shape[0],8,8))
    np4bbpData[:,:,0::2] = npRawData & 0b11110000
    np4bbpData[:,:,1::2] = npRawData & 0b00001111
    return np4bbpData
  
  def __bytesTobpp8Tile(self) -> np.ndarray:
    npRawData = np.frombuffer(self.__rawData,dtype=np.uint8).reshape((-1,8,8))
    np8bppData = npRawData
    return np8bppData
  
  def __bpp8TileToBytes(self,tiles:np.ndarray) -> bytes:
    return tiles.tobytes()
  
  def __bpp4TileToBytes(self,tiles:np.ndarray) -> bytes:
    npRawData = (tiles[:,:,0::2] >> 4)+tiles[:,:,1::2]
    return npRawData.tobytes()