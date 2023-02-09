import numpy as np

import Exception.Exceptions as ex
import Utils.colorDepthConverter as colorDepthConv
from DsType.DsPal import DsPal, PalFormat
from FileInterface.palSaver import InterfacePalSaver
from Utils.Decorator.checkType import checkFileType
from Utils.struct import *


class ExtPalSaver(InterfacePalSaver):
  """保存.pal格式的色板"""
  @checkFileType(".pal")
  def saveAsFile(self, filePath: str, dsPal: DsPal):
    with open(filePath,mode="wb") as palFile:
      palStruct = PalStruct()
      palStructDic = palStruct.getStructDic()
      # 准备信息
      palLength = dsPal.getLength()
      fileSize = palLength * 4 + 16
      # 写入结构
      palStructDic[PalStruct.Keys.colorCount] = palLength
      palStructDic[PalStruct.Keys.fileSize] = fileSize
      palStruct.setStructDic(palStructDic)
      palStruct.pack_into(palFile,0)
      # 写入数据
      data:np.ndarray = dsPal.getData()[:palLength]
      data = np.concatenate((data,np.zeros((palLength,1),dtype=np.uint8)),axis=1)
      palFile.write(data.tobytes())

class ExtActSaver(InterfacePalSaver):
  """保存.act格式的色板"""
  @checkFileType(".act")
  def saveAsFile(self, filePath: str, dsPal: DsPal):
    with open(filePath,mode="wb") as actFile:
      # 准备信息
      palLength = dsPal.getLength()
      data = dsPal.getData()[:palLength]
      # 写入数据
      actFile.write(data)

class ExtNclrSaver(InterfacePalSaver):
  """保存Nitro调色板"""
  @checkFileType(".nclr")
  def saveAsFile(self, filePath: str, dsPal: DsPal):
    with open(filePath,mode="wb") as nclrFile:
      nclrStruct = NclrStruct()
      nclrStructDic = nclrStruct.getStructDic()
      # 准备信息
      palLength = dsPal.getLength()
      palFormat = 3 if dsPal.getFormat() == PalFormat.bpp4 else 4
      fileSize = palLength * 2 + 40
      sectionSize = fileSize - 16
      memorySize = palLength * 2
      # 写入结构
      nclrStructDic[NclrStruct.Keys.fileSize] = fileSize
      nclrStructDic[NclrStruct.Keys.bitDepth] = palFormat
      nclrStructDic[NclrStruct.Keys.sectionSize] = sectionSize
      nclrStructDic[NclrStruct.Keys.memorySize] = memorySize
      nclrStruct.setStructDic(nclrStructDic)
      nclrStruct.pack_into(nclrFile,0)
      # 写入数据
      dsPalData = dsPal.getData()[:palLength]
      data = colorDepthConv.v_trueColor2DsColor(dsPalData)
      nclrFile.write(data.tobytes())

