from abc import ABC, abstractmethod

import numpy as np


class InterfaceImgReader(ABC):
  @abstractmethod
  def readFromFile(self,filePath:str) -> np.ndarray:
    """
    根据文件名，读取图像文件
    
    params:
    * fileName:需要读取的文件路径
    
    return:
    numpy格式的图像对象
    """