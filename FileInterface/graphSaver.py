from abc import ABC, abstractmethod

from DsType.DsGraph import DsGraph,PalFormat

class InterfaceGraphSaver(ABC):
  @abstractmethod
  def saveAsFile(self,filePath:str,dsGraph:DsGraph,palFormat:PalFormat):
    """
    根据文件名，读取Ds图形文件
    
    params:
    * fileName:需要读取的文件路径
    * dsGraph:需要保存的图形
    """