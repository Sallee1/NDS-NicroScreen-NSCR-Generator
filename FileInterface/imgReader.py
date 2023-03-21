from abc import ABC, abstractmethod

import numpy as np
from PIL import Image

from DsType.DsPal import DsPal


class InterfaceImgReader(ABC):
  @abstractmethod
  def readFromFile(self,filePath:str) -> Image.Image:
    """
    根据文件名，读取图像文件
    
    params:
    * fileName:需要读取的文件路径
    
    return:
    PIL格式的图像
    """

  