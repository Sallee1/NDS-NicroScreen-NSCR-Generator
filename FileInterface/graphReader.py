from abc import ABC, abstractmethod

from DsType.DsGraph import DsGraph,PalFormat


class InterfaceGraphReader(ABC):
  @abstractmethod
  def readFromFile(self,filePath:str,colorFormat:PalFormat = PalFormat.bpp8) -> DsGraph:
    """
    根据文件名，读取Ds图形文件
    
    params:
    * fileName:需要读取的文件路径
    * colorFormat:颜色格式
    
    return:
    DsGraph对象
    """