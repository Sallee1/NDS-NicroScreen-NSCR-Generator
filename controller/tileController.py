from __imports__ import *
from DsType.DsGraph import DsGraph
from Utils.imgTool import tiles2Img

class tileController:
  @staticmethod
  def setTileViewerCfg(dsGraph:DsGraph):
    Config.TileViewConfig.GraphDataBpp4 = dsGraph.getTileData(PalFormat.bpp4)
    Config.TileViewConfig.GraphDataBpp8 = dsGraph.getTileData(PalFormat.bpp8)

    Config.TileViewConfig.bpp4Img = tiles2Img(Config.TileViewConfig.GraphDataBpp4)
    Config.TileViewConfig.bpp8Img = tiles2Img(Config.TileViewConfig.GraphDataBpp8)

  @staticmethod
  def appendTileViewerCfg(dsGraph:DsGraph):
    GraphDataBpp4 = dsGraph.getTileData(PalFormat.bpp4)
    GraphDataBpp8 = dsGraph.getTileData(PalFormat.bpp8)
    
    Config.TileViewConfig.GraphDataBpp4 = np.concatenate((GraphDataBpp4,Config.TileViewConfig.GraphDataBpp4),axis = 0)

    Config.TileViewConfig.GraphDataBpp8 = np.concatenate((GraphDataBpp8,Config.TileViewConfig.GraphDataBpp8),axis = 0)

    Config.TileViewConfig.bpp4Img = tiles2Img(Config.TileViewConfig.GraphDataBpp4)
    Config.TileViewConfig.bpp8Img = tiles2Img(Config.TileViewConfig.GraphDataBpp8)

