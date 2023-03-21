from __imports__ import *

from FileInterface.graphReader import InterfaceGraphReader
from FileInterface.Impl.graphReaderImpl import *

class GraphReaderFactory():
  """Ds图形文件读取器的工厂类"""

  class Keys(Enum):
    NCGR = 1
    NCGRWithoutBOM = 2
    Image = 3
  
  @staticmethod
  def getInstance(graphType)->InterfaceGraphReader:
    """
    给定文件格式，返回对应的DS图形读取模块
    Params:
    * graphType: 文件格式，从keys获取
    """

    graphTypeDic = {
      GraphReaderFactory.Keys.NCGR: GraphReaderWithBOM(),
      GraphReaderFactory.Keys.NCGRWithoutBOM:GraphReaderWithoutBOM(),
      GraphReaderFactory.Keys.Image:GraphReaderFromImg()
    }
    return graphTypeDic[graphType]