"""文件结构体，用于文件读写"""
import struct
from abc import ABC, abstractmethod
from enum import Enum
from typing import IO, Any, Dict

from Utils.Decorator.returnCopy import returnCopy


class AbstractStruct(ABC):
  """
  抽象结构体类，为了更方便访问，使用字典模拟c语言的命名结构体
  
  Attribute:
  * Dict structDic{get,set}:保存结构体用的字典
  * String structFormat:读写用的结构体格式串
  * structMaxSize:结构体可能的最大大小，用来读取数据

  mothods:
  * pack():打包结构体到字节串中
  * unpack():字节串解包到结构体中
  * pack_into():打包结构体到文件中
  * unpack_from():从文件解包结构体
  """
  structDic:Dict
  structFormat:str
  structSize:int
  def pack(self) -> bytes:
    v = tuple(self.structDic.values())
    return struct.pack(self.structFormat,*v)
  
  def unpack(self,bytes):
    v = struct.unpack(self.structFormat,bytes)
    vList = [(list(self.structDic.keys())[i],v[i]) for i in range(len(v))]
    self.structDic = dict(vList)
  
  def pack_into(self,file:IO,offset:int):
    file.seek(offset,0)
    file.write(self.pack())
  
  def unpack_from(self,file:IO,offset:int):
    file.seek(offset,0)
    self.unpack(file.read(self.structSize))

  @returnCopy
  def getStructDic(self): return self.structDic

  def setStructDic(self,dic:Dict): self.structDic = dic

class PalStruct(AbstractStruct):
  class Keys(Enum):
    riffHander = 0
    fileSize   = 1
    palHander  = 2
    blockSize  = 3
    colorCount = 4

  def __init__(self) -> None:
    self.structDic = {
      self.Keys.riffHander: b"RIFF",
      self.Keys.fileSize  : 0,
      self.Keys.palHander : b"PAL data",
      self.Keys.blockSize : 0,
      "Unknown0"          : 768,
      self.Keys.colorCount: 256,
    }
    self.structFormat = "<4sI8sIHH"
    self.structSize = 24

class NclrStruct(AbstractStruct):
  class Keys(Enum):
    nclrHander     = 0
    fileSize       = 1
    handerSize     = 2
    sectionVersion = 3
    sectionHander  = 4
    sectionSize    = 5
    bitDepth       = 6
    memorySize     = 7
    dataOffset     = 8

  def __init__(self) -> None:
    self.structDic = {
      self.Keys.nclrHander    :b"RLCN",
      "Unknown0"              :b"\xFF\xFE\x00\x01",
      self.Keys.fileSize      :0,
      self.Keys.handerSize    :16,
      self.Keys.sectionVersion:2,
      self.Keys.sectionHander :b"TTLP",
      self.Keys.sectionSize   :0,
      self.Keys.bitDepth      :3,
      "Unkonwn1"              :0,
      "Unknown2"              :0,
      self.Keys.memorySize    :0,
      self.Keys.dataOffset    :16
    }
  
    self.structFormat="<4s4sIHH4sIHHIII"
    self.structSize=40

class BmpStruct(AbstractStruct):
  class Keys(Enum):
    bfType          = 0
    bfSize          = 1
    bfReserved1     = 2
    bfReserved2     = 3
    bfOffBits       = 4
    biSize          = 5
    biWidth         = 6
    biHeight        = 7
    biPlanes        = 8
    biBitCount      = 9
    biCompression   = 10
    biSizeImage     = 11
    biXPelsPerMeter = 12
    biYPelsPerMeter = 13
    biClrUsed       = 14
    biClrImportant  = 15
  
  def __init__(self) -> None:
    self.structDic = {
      self.Keys.bfType         :b"BM",
      self.Keys.bfSize         :0,
      self.Keys.bfReserved1    :0,
      self.Keys.bfReserved2    :0,
      self.Keys.bfOffBits      :0,
      self.Keys.biSize         :0,
      self.Keys.biWidth        :0,
      self.Keys.biHeight       :0,
      self.Keys.biPlanes       :1,
      self.Keys.biBitCount     :24,
      self.Keys.biCompression  :0,
      self.Keys.biSizeImage    :0,
      self.Keys.biXPelsPerMeter:0,
      self.Keys.biYPelsPerMeter:0,
      self.Keys.biClrUsed      :0,
      self.Keys.biClrImportant :0
    }

    self.structFormat = "<2sIHHIIiiHHIIIIII"
    self.structSize = 54
