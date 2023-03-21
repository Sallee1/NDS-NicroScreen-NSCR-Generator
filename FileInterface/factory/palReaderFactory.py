from FileInterface.Impl.palReaderImpl import *
from FileInterface.palReader import InterfacePalReader


class PalReaderFactory():
  """PalReader的工厂类"""
  class Keys(Enum):
    pal = 1
    act = 2
    bmp = 3
    nclr = 4

  @staticmethod
  def getInstance(fileType)->InterfacePalReader:
    """
    给定文件格式，输出对应的调色板读取模块\n
    Params:
    * fileType:从工厂类中的Keys获取
    """
    typeDic = {
      PalReaderFactory.Keys.pal:ExtPalReader(),
      PalReaderFactory.Keys.act:ExtActReader(),
      PalReaderFactory.Keys.bmp:ExtBmpReader(),
      PalReaderFactory.Keys.nclr:ExtNclrReader()
    }
    return typeDic[fileType]