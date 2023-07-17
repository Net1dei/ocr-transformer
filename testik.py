import sys
import torch
import random
import pathlib
import os
sys.path.append(str(pathlib.Path(__file__).parent.resolve())+'/src')

from const import DIR, PATH_TEST_DIR, PATH_TEST_LABELS, WEIGHTS_PATH, PREDICT_PATH

def aboba():
  print(DIR)
