from abc import ABC, abstractmethod

from PIL import Image


class InterfaceImgSaver(ABC):
  @abstractmethod
  def saveAsFile(self,filePath:str,img:Image.Image):
    """
    根据文件名，保存图像文件
    
    params:
    * fileName:需要保存的文件路径
    * img:图像的数组表示
    
    return:
    无
    """