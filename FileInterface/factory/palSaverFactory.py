from FileInterface.Impl.palSaverImpl import *
from FileInterface.palSaver import InterfacePalSaver


class PalSaverFactory():
  """PalSaver的工厂类"""
  class Keys(Enum):
    pal = 1
    act = 2
    nclr = 4

  @staticmethod
  def getInstance(fileType)->InterfacePalSaver:
    """
    给定文件格式，输出对应的调色板保存模块\n
    Params:
    * fileType:扩展名，从keys获取
    """
    typeDic = {
      PalSaverFactory.Keys.pal: ExtPalSaver(),
      PalSaverFactory.Keys.act:ExtActSaver(),
      PalSaverFactory.Keys.nclr:ExtNclrSaver()
    }

    return typeDic[fileType]