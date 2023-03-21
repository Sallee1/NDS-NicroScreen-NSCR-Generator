from __imports__ import *

from FileInterface.graphReader import InterfaceGraphReader, DsGraph

from DsType.DsPal import PalFormat
from Utils.struct import NcgrStruct
from FileInterface.factory.imgReaderFactory import ImgReaderFactory
from Utils.Decorator.checkType import checkFileType
import Utils.imgTool as imgTool


class GraphReaderWithBOM(InterfaceGraphReader):
  #NCGR文件直接解析原始数据，不转换颜色格式
  @checkFileType(".ncgr")
  def readFromFile(self,filePath:str,colorFormat:PalFormat = PalFormat.bpp8) -> DsGraph:
    with open(filePath,"rb") as ncgrFile:
      #解包
      ncgrStruct = NcgrStruct()
      ncgrStruct.unpack_from(ncgrFile,0)
      ncgrStructDic = ncgrStruct.getStructDic()
      #读取文件头
      dataSize = ncgrStructDic[NcgrStruct.Keys.dataSize]
      length4bpp = dataSize // 32
      #读取数据
      ncgrFile.seek(48)
      rawData = ncgrFile.read(dataSize)
      #处理数据
      return DsGraph(rawData,length4bpp)

class GraphReaderWithoutBOM(InterfaceGraphReader):
  #无文件头的NCGR
  def readFromFile(self, filePath: str, colorFormat: PalFormat = PalFormat.bpp8) -> DsGraph:
    with open(filePath,"rb") as ncgrFile:
      ncgrFile.seek(0,2)
      dataSize = ncgrFile.tell() % 32
      length4bpp = dataSize // 32
      #读取数据
      ncgrFile.seek(0)
      rawData = ncgrFile.read(dataSize)
      #处理数据
      return DsGraph(rawData,length4bpp)

class GraphReaderFromImg(InterfaceGraphReader):
  #从图像中读取
  def readFromFile(self, filePath: str, colorFormat: PalFormat = PalFormat.bpp8) -> DsGraph:
    imgReader = ImgReaderFactory().getInstance(ImgReaderFactory.Keys.indexedColor)
    imgFile = imgReader.readFromFile(filePath)
    rawData = self.__image2RawData(imgFile,colorFormat)
    dataSize = len(rawData)
    length4bpp = dataSize // 32
    return DsGraph(rawData,length4bpp)


  def __image2RawData(self,img:Image.Image,colorFormat:PalFormat)->bytes:
    img = imgTool.paddingImg(img)
    imgNp = np.asarray(img)
    if(colorFormat == PalFormat.bpp4):
      imgNp %= 16
    imgSplitNp = imgTool.img2Tiles(imgNp)
    imgFlat = imgSplitNp.flatten()
    if(colorFormat == PalFormat.bpp4):
      newImg = imgFlat[0::2]+imgFlat[1::2] * 16
      imgFlat = newImg
    return imgFlat.tobytes()