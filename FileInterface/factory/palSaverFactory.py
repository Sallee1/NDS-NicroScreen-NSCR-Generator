import Exception.Exceptions as ex
from FileInterface.Impl.palSaverImpl import *
from FileInterface.palSaver import InterfacePalSaver


class PalSaverFactory():
  """PalSaver的工厂类"""
  @staticmethod
  def getInstance(fileType:str)->InterfacePalSaver:
    """
    给定文件格式，输出对应的调色板保存模块\n
    Params:
    * fileType:扩展名，需要带上"."
    """
    typeDic = {
      ".pal":ExtPalSaver(),
      ".act":ExtActSaver(),
      ".nclr":ExtNclrSaver()
    }
    fileType = fileType.lower()
    if(fileType not in typeDic.keys()):
      raise ex.FileTypeError(".pal/.act/.nclr",fileType)
    return typeDic[fileType]