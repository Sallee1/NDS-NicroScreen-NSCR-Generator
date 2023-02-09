import numpy as np

import Exception.Exceptions as ex
import Utils.colorDepthConverter as colorDepthConv
from DsType.DsPal import DsPal, PalFormat
from FileInterface.palReader import InterfacePalReader
from Utils.Decorator.checkType import checkFileType
from Utils.struct import *


class ExtPalReader(InterfacePalReader):
  """读取.pal格式的调色板"""
  @checkFileType(".pal")
  def readFromFile(self,filePath: str) -> DsPal:
    with open(filePath,mode="rb") as palFile:
      #解包
      palStruct = PalStruct()
      palStruct.unpack_from(palFile,0)
      palStructDic = palStruct.getStructDic()
      #读取文件头
      length = palStructDic[PalStruct.Keys.colorCount]     
      #读取调色板数据
      palData = np.frombuffer(palFile.read(length*4),dtype=np.uint8) 
      palData = np.reshape(palData,(length,4))
      palData = palData[:,0:3]
      #处理pal数据
      data = handlePal(palData)    
      return DsPal(data=data,length=length)

class ExtActReader(InterfacePalReader):
  """读取.act格式的调色板"""
  @checkFileType(".act")
  def readFromFile(self, filePath: str) -> DsPal:
    with open(filePath,mode="rb") as actFile:
      #计算调色板的颜色个数
      actFile.seek(0,2)                
      length = actFile.tell() // 3      
      #读取调色板数据
      actFile.seek(0,0)
      palData = np.frombuffer(actFile.read(length*3),dtype=np.uint8)  
      palData = np.reshape(palData,(length,3))
      #处理pal数据
      data = handlePal(palData)         
      return DsPal(data=data,length=length)

class ExtBmpReader(InterfacePalReader):
  """读取bmp位图色板"""
  @checkFileType(".bmp")
  def readFromFile(self, filePath: str) -> DsPal:
    with open(filePath,mode="rb") as bmpFile:
      # 解包
      bmpStruct = BmpStruct()
      bmpStruct.unpack_from(bmpFile,0)
      bmpStructDic = bmpStruct.getStructDic()
      # 读取文件头
      biBitCount = bmpStructDic[BmpStruct.Keys.biBitCount]
      if(biBitCount > 8): 
        raise ex.FileTypeError("BMP索引颜色图像","BMP全彩图像") 
      biClrUsed = bmpStructDic[BmpStruct.Keys.biClrUsed]
      if(biClrUsed <= 0 or biClrUsed > 256):
        biClrUsed = 256
      #读取调色板数据
      bmpFile.seek(54)
      PalBuffer = bmpFile.read(biClrUsed*4)
      palData = np.frombuffer(PalBuffer,dtype=np.uint8).reshape(biClrUsed,4)
      palData = palData[:,2::-1]
      #处理数据
      data = handlePal(palData)
      return DsPal(data=data,length=biClrUsed) 

class ExtNclrReader(InterfacePalReader):
  """Nitro调色板"""
  @checkFileType(".nclr")
  def readFromFile(self, filePath: str) -> DsPal:
    with open(filePath,mode="rb") as nclrFile:
      #解包
      nclrStruct = NclrStruct()
      nclrStruct.unpack_from(nclrFile,0)
      nclrStructDic = nclrStruct.getStructDic()

      #读取颜色格式
      palFormatFlag = nclrStructDic[NclrStruct.Keys.bitDepth]
      palFormat = PalFormat.bpp4 if(palFormatFlag == 3) else PalFormat.bpp8
      #计算调色板大小
      nclrFile.seek(0x14)
      sectionSize = nclrStructDic[NclrStruct.Keys.sectionSize]
      length = (sectionSize - 24) // 2
      #读取调色版数据
      nclrFile.seek(0x28)
      dsPalBuffer = nclrFile.read(length*2)
      #如果是4bpp，计算颜色计数
      bpp4Count = 16
      if(palFormat == PalFormat.bpp4):
        bpp4Count = length // 16
      #读取颜色数据，并转换为真彩色
      dsPalData = np.frombuffer(dsPalBuffer,dtype=np.uint16)
      palData = colorDepthConv.v_dsColor2TrueColor(dsPalData)
      #处理数据
      data = handlePal(palData)
      return DsPal(data=data,palFormat=palFormat,length=length,bpp4Count=bpp4Count)

def handlePal(palData:np.ndarray):
  # 不足256填充0数据
  data = np.zeros((256,3),dtype=np.uint8)
  data[0:palData.shape[0]] = palData
  # 转换为5bpp
  data = data >> 3 << 3       
  return data