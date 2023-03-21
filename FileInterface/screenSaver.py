from abc import ABC,abstractmethod

from DsType.DsScreen import DsScreen


class InterfaceScreenSaver(ABC):
  @abstractmethod
  def saveAsFile(self,filePath:str,dsScreen:DsScreen):
    """
    根据文件名，保存命名表文件
    
    params:
    * fileName:需要保存的文件路径
    * dsScreen:需要保存的数据
    """