import sys
from Fore.mainWindow import mainWindows
from PySide6.QtWidgets import QApplication

if __name__ == "__main__":
  app = QApplication(sys.argv)
  mainWin = mainWindows()
  mainWin.show()
  sys.exit(app.exec())