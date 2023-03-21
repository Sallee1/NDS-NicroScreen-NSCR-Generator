from __imports__ import *
from controller.config import *

#存放前端的视图配置
class ForePalConfig(PalConfig):
  pass

class ForeTileEditorConfig(TileEditorConfig):
  tileNo = 0
  
  paletteNo = 0
  flip = FlipMode.none
  activeColor = "000000"
  isDrawScreen = False

class ForeScreenViewConfig(ScreenViewConfig):
  foreScreenViewImg = None
  zoomSize = 1.0
  width,height = 32,32
  hasGrid = False
  isTransport = False

class ForeTileViewConfig(ScreenViewConfig):
  foreTileViewImg = None
  zoomSize = 1.0
  hasGrid = False
  paletteNo = 0
  autoPalNo = False
  maskNotUse = False
  isTransport = False