from DsType.DsPal import PalFormat
from FileInterface.graphSaver import InterfaceGraphSaver,DsGraph
from Utils.Decorator.checkType import checkFileType
from Utils.struct import NcgrStruct

class GraphSaverWithBOM(InterfaceGraphSaver):
  @checkFileType(".ncgr")
  def saveAsFile(self, filePath: str, dsGraph: DsGraph,palFormat:PalFormat):
    #准备数据
    dataSize = 32*dsGraph.getLength4bpp()
    fileSize = dataSize+48
    sectionSize = dataSize+32
    bitDepth = 3 if palFormat == PalFormat.bpp4 else 4
    #打包
    ncgrStruct = NcgrStruct()
    ncgrStructDic = ncgrStruct.getStructDic()
    ncgrStructDic[NcgrStruct.Keys.dataSize] = dataSize
    ncgrStructDic[NcgrStruct.Keys.fileSize] = fileSize
    ncgrStructDic[NcgrStruct.Keys.sectionSize] = sectionSize
    ncgrStructDic[ncgrStruct.Keys.BitDepth] = bitDepth
    ncgrStruct.setStructDic(ncgrStructDic)
    with open(filePath, "wb") as ncgrFile:
      ncgrStruct.pack_into(ncgrFile)
      ncgrFile.seek(48)
      ncgrFile.write(dsGraph.getRawData())

class GraphSaverWithoutBOM(InterfaceGraphSaver):
  def saveAsFile(self, filePath: str, dsGraph: DsGraph, palFormat: PalFormat):
    with open(filePath, "wb") as ncgrFile:
      ncgrFile.write(dsGraph.getRawData())