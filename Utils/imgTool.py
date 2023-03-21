import numpy as np
import cv2
from PIL import Image
from typing import List

#DS颜色格式转真彩色
def dsColor2TrueColor(dsColorVal:int)->np.ndarray:
  r = (dsColorVal & 0b0000000000011111) << 3
  g = (dsColorVal & 0b0000001111100000) >> 2
  b = (dsColorVal & 0b0111110000000000) >> 7
  return np.asarray([r,g,b],dtype=np.uint8)

# np数组版本
def v_dsColor2TrueColor(dsColorVal:np.ndarray)->np.ndarray:
  r = (dsColorVal & 0b0000000000011111) << 3
  g = (dsColorVal & 0b0000001111100000) >> 2
  b = (dsColorVal & 0b0111110000000000) >> 7
  ret = np.ndarray((dsColorVal.shape[0],3),dtype=np.uint8)
  ret[:,0] = r
  ret[:,1] = g
  ret[:,2] = b
  return ret


# 真彩色转DS颜色格式
def trueColor2DsColor(colorArr:np.ndarray)->int:
  colorArr16bpp = colorArr.astype(np.uint16)
  r = (colorArr[0] >> 3) & 0b0000000000011111
  g = (colorArr[1] << 2) & 0b0000001111100000
  b = (colorArr[2] << 7) & 0b0111110000000000
  return r+g+b

# np数组版本
def v_trueColor2DsColor(colorArr:np.ndarray)->np.ndarray:
  colorArr16bpp = colorArr.astype(np.uint16)
  r = (colorArr16bpp[:,0] >> 3) & 0b0000000000011111
  g = (colorArr16bpp[:,1] << 2) & 0b0000001111100000
  b = (colorArr16bpp[:,2] << 7) & 0b0111110000000000
  return r+g+b


# 索引颜色图像转真彩色
def indexedImg2TrueColor(img:Image.Image) -> Image.Image:
  #img = Image.open("path")
  palette = np.asarray(img.getpalette(),dtype=np.uint8).reshape((-1,3))
  if(palette is None): return img
  imgNp = np.asarray(img)
  imgRealColorNp = palette[imgNp]
  return Image.fromarray(imgRealColorNp)

# 填充图像至整倍数长宽
def paddingImg(img:Image.Image) -> Image.Image:
  imgNp = np.asarray(img)
  ht,wd = imgNp.shape[0:2]
  paddingD,paddingR = 0,0
  if(wd & 0b111 != 0):
    paddingR = (8-wd&0b111)
  if(ht & 0b111 != 0):
    paddingD = (8-ht&0b111)
  imgNp = cv2.copyMakeBorder(imgNp,0,paddingD,0,paddingR,cv2.
  BORDER_CONSTANT,value=0)
  
  palData = img.getpalette()
  retImg = Image.new("P",(wd+paddingR,ht+paddingD))
  retImg.putpalette(palData)
  retImg.putdata(imgNp.flatten())
  return retImg

# 图像切分tiles
def img2Tiles(imgNp:np.ndarray)->np.ndarray:
  HTileCount = imgNp.shape[1] // 8
  VTileCount = imgNp.shape[0] // 8
  retImg = np.asarray(np.split(imgNp,HTileCount,axis=1))
  retImg = np.asarray(np.split(retImg,VTileCount,axis=1))
  return retImg

# tiles合并img
def tiles2Img(tiles:np.ndarray,tileShape = (32,32))->np.ndarray:  
  #填充
  flatTiles = tiles.flatten()
  emptyImg = np.zeros(tileShape[0]*tileShape[1]*64,dtype=np.uint8)
  emptyImg[0:flatTiles.shape[0]] = flatTiles[0:tileShape[0]*tileShape[1]*64]
  paddedImg = emptyImg.reshape((tileShape[1],tileShape[0],8,8))
  #拼接
  tileRows = tuple(paddedImg[r] for r in range(tileShape[1]))
  retImg = np.concatenate(tileRows,1)
  tileCols = tuple(retImg[c] for c in range(tileShape[0]))
  retImg = np.concatenate(tileCols,1)
  return retImg
