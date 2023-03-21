from __imports__ import *

#存放前端的数据配置
class PalConfig:
  palette = np.zeros((16,16,3),dtype = np.uint8)
  isBpp4 = False
  isTransport = True
  enabledPalList = [True] * 16

class TileEditorConfig:
  tileCanvas = np.zeros((8,8),dtype = np.uint8)
  activeColorNo = 0


class ScreenViewConfig:
  ScreenData:np.ndarray
  img:np.ndarray

class TileViewConfig:
  GraphDataBpp4:np.ndarray
  GraphDataBpp8:np.ndarray
  bpp4Img:np.ndarray
  bpp8Img:np.ndarray