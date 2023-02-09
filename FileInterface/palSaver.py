from abc import ABC, abstractmethod

from DsType.DsPal import DsPal


class InterfacePalSaver(ABC):
  @abstractmethod
  def saveAsFile(self,filePath:str,dsPal:DsPal):
    """
    根据文件名，写入调色板文件
    
    params:
    * fileName:需要写入的文件路径
    
    return:
    无
    """
