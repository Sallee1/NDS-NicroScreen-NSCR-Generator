from typing import List,Tuple,Set
from enum import Enum
import numpy as np
import cv2
from PIL import Image

import controller.config as Config
import Fore.ForeConfig as ForeConfig


class PalFormat(Enum):
  bpp4 = 3
  bpp8 = 4

class FlipMode(Enum):
  none = 0
  H = 1
  V = 2
  HV = 3