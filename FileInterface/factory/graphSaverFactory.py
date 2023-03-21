from __imports__ import *
from FileInterface.Impl.graphSaverImpl import *

from FileInterface.graphSaver import InterfaceGraphSaver


class GraphSaverFactory():
  """Ds图形文件保存器的工厂类"""

  class Keys(Enum):
    NCGR = 1
    NCGRWithoutBOM = 2

  @staticmethod
  def getInstance(graphType)->InterfaceGraphSaver:
    """
    给定文件格式，返回对应的DS图形保存模块
    Params:
    * graphType: 文件格式，从keys获取
    """
    graphTypeDic = {
      GraphSaverFactory.Keys.NCGR:GraphSaverWithBOM(),
      GraphSaverFactory.Keys.NCGRWithoutBOM:GraphSaverWithoutBOM()
    }
    return graphTypeDic[graphType]