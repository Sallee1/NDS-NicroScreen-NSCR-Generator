from __imports__ import *
from DsType.DsScreen import DsScreen
from FileInterface.screenReader import InterfaceScreenReader
from Utils.Decorator.checkType import checkFileType
from Utils.struct import NscrStruct


class ScreenReaderWithBOM(InterfaceScreenReader):
  @checkFileType(".nscr"):
  def readFromFile(self, filePath: str) -> DsScreen:
    with open(filePath,"rb") as nscrFile:
      #解包
      nscrStruct = NscrStruct()
      nscrStruct.unpack_from(nscrFile)
      nscrStructDic = nscrStruct.getStructDic()
      #读取文件头
      width = nscrStructDic[NscrStruct.Keys.width]
      height = nscrStructDic[NscrStruct.Keys.height]
      
      #读取数据
      nscrFile.seek(36)
      rawData = nscrFile.read()
      dataNp = np.frombuffer(rawData,dtype=np.uint16).reshape(height,width)
      #处理数据
      return DsScreen(dataNp,width,height)
    
class ScreenReaderWithoutBOM(InterfaceScreenReader):
  def readFromFile(self, filePath: str) -> DsScreen:
    with open(filePath,"rb") as nscrFile:
      rawData = nscrFile.read()
      dataNp = np.frombuffer(rawData,dtype=np.uint16)
      #处理数据
      return DsScreen(dataNp)