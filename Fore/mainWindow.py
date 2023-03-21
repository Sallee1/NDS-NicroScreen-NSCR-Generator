
from Fore.Ui_mainWindow import Ui_mainWidget
from PySide6.QtWidgets import QWidget


class mainWindows(QWidget,Ui_mainWidget):
  def __init__(self, parent = None) -> None:
    super().__init__(parent)
    self.setupUi(self)

  def onPaletteClick(self):pass
  def onPaletteDoubleClick(self):pass
  def onLoadPaletteButtom(self):pass
  def onSavePaletteButtom(self):pass
  def onTileCanvasClick(self):pass
  def onApplyTileCanvasButtom(self):pass
  def onResetTileCanvasButtom(self):pass
  def onSwitchScreenDrawButtom(self):pass
  def onChangeTileNoSpinBox(self):pass
  def onChangePaletteSpinBox(self):pass
  def onChangeFlipGroupBox(self):pass
  def onClickLoadImgButtom(self):pass
  def onClickSaveImgButtom(self):pass
  def onChangePaletteFilter(self):pass
  def onSwitch4bbpChackBox(self):pass
  def onChangeScreenZoomSpinBox(self):pass
  def onClickLoadScreenButtom(self):pass
  def onClickSaveScreenButtom(self):pass
  def onChangeScreenSizeSpinBox(self):pass
  def onSwitchUseAlphaChackBox(self):pass
  def onSwitchScreenGridChackBox(self):pass
  def onSwitchTilesGridCheckBox(self):pass
  def onChangeTileSpinBox(self):pass
  def onClickLoadTilesButtom(self):pass
  def onClickSaveTilesButtom(self):pass
  def onSwitchAutoPaletteCheckBox(self):pass
  def onSwitchMaskNoUseTileCheckBox(self):pass
  def onSwitchShowScreenAlpha(self):pass
  def onSwitchShowTilesAlpha(self):pass
  def onChangePalShowSpinBox(self):pass
  def onSwitchNoClearTilesCheckBox(self):pass
  def onSwitchGeneratorPaletteCheckBox(self):pass
  def onSwitchCompressTilesCheckBox(self):pass

