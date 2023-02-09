import Exception.Exceptions as ex
from FileInterface.Impl.palReaderImpl import *
from FileInterface.palReader import InterfacePalReader


class PalReaderFactory():
  """PalReader的工厂类"""
  @staticmethod
  def getInstance(fileType:str)->InterfacePalReader:
    """
    给定文件格式，输出对应的调色板读取模块\n
    Params:
    * fileType:扩展名，需要带上"."
    """
    typeDic = {
      ".pal":ExtPalReader(),
      ".act":ExtActReader(),
      ".bmp":ExtBmpReader(),
      ".nclr":ExtNclrReader()
    }
    fileType = fileType.lower()
    if(fileType not in typeDic.keys()):
      raise ex.FileTypeError(".pal/.act/.bmp/.nclr",fileType)
    return typeDic[fileType]