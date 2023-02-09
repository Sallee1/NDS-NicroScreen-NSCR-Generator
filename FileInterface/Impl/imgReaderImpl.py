import cv2
import numpy as np

from FileInterface.imgReader import InterfaceImgReader
from Utils.Decorator.checkNoneReturn import checkNoneReturn


class RealColorImgReader(InterfaceImgReader):
  @checkNoneReturn
  def readFromFile(self, filePath: str) -> np.ndarray:
    """目前只考虑读取常规图片"""
    return cv2.imread(filePath,flags=cv2.IMREAD_COLOR)