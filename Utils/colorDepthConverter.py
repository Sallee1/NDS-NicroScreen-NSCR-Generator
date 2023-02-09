import numpy as np


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

def trueColor2DsColor(colorArr:np.ndarray[3])->int:
  colorArr16bpp = colorArr.astype(np.uint16)
  r = (colorArr[0] >> 3) & 0b0000000000011111
  g = (colorArr[1] << 2) & 0b0000001111100000
  b = (colorArr[2] << 7) & 0b0111110000000000
  return r+g+b

# np数组版本
def v_trueColor2DsColor(colorArr:np.ndarray[256,3])->np.ndarray:
  colorArr16bpp = colorArr.astype(np.uint16)
  r = (colorArr16bpp[:,0] >> 3) & 0b0000000000011111
  g = (colorArr16bpp[:,1] << 2) & 0b0000001111100000
  b = (colorArr16bpp[:,2] << 7) & 0b0111110000000000
  return r+g+b
