import numpy as np
import Utils.regex as regex
import Utils.colorDepthConverter as colorDepthConv
import Exception.Exceptions as ex

from FileType.DsPal import DsPal,PalFormat
from FileInterface.palReader import InterfacePalReader
from Utils.Decorator.checkType import checkFileType

class ExtPalReader(InterfacePalReader):
  """读取.pal格式的调色板"""
  @checkFileType(".pal")
  def readFromFile(self,filePath: str) -> DsPal:
    with open(filePath,mode="rb") as palFile:
      #读取调色板的颜色个数
      palFile.seek(0x16)
      length = int.from_bytes(palFile.read(2),"little")           
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
      #读取bmp的颜色格式
      bmpFile.seek(0x1c)
      biBitCount = int.from_bytes(bmpFile.read(2), 'little')  
      if(biBitCount > 8): 
        raise ex.FileTypeError("BMP索引颜色图像","BMP全彩图像") 
      #使用了多少种颜色
      biClrUsed = int.from_bytes(bmpFile.read(4), 'little')  
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
      #读取颜色格式
      nclrFile.seek(0x18)
      palFormatFlag = int.from_bytes(nclrFile.read(2),'little')
      palFormat = PalFormat.bpp4 if(palFormatFlag == 3) else PalFormat.bpp8
      #读取调色版数据
      nclrFile.seek(0x28)
      dsPalBuffer = nclrFile.read()
      #去除PMCP数据
      findPmcpRes = dsPalBuffer.find(b"PMCP")
      if(findPmcpRes != -1):
        dsPalBuffer = dsPalBuffer[:findPmcpRes]
      #计算调色板颜色个数
      length = (len(dsPalBuffer)) // 2
      #如果是4bpp，读取颜色计数
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