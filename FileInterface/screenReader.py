from abc import ABC, abstractmethod

from DsType.DsScreen import DsScreen


class InterfaceScreenReader(ABC):
  @abstractmethod
  def readFromFile(self,filePath:str) -> DsScreen:
    """
    根据文件名，读取命名表文件
    
    params:
    * fileName:需要读取的文件路径
    
    return:
    DsScreen对象
    """
