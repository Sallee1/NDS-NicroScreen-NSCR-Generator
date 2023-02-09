from abc import ABC, abstractmethod

from DsType.DsPal import DsPal


class InterfacePalReader(ABC):
  @abstractmethod
  def readFromFile(self,filePath:str) -> DsPal:
    """
    根据文件名，读取调色板文件
    
    params:
    * fileName:需要读取的文件路径
    
    return:
    PalFile对象
    """
