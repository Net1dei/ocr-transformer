from pathlib import Path
import os

DIR = Path.cwd() # work directory
PATH_TEST_DIR = os.fspath(Path(DIR, 'test'))
PATH_TEST_LABELS = os.fspath(Path( DIR, 'test.tsv'))
PATH_TRAIN_DIR = os.fspath(Path( DIR, 'train'))
PATH_TRAIN_LABELS = os.fspath(Path( DIR, 'train.tsv'))
PREDICT_PATH = os.fspath(Path(DIR, 'test'))
CHECKPOINTS_PATH = os.fspath(Path(DIR))
FROM_CHECKPOINT_PATH = '/content/drive/MyDrive/ocr_transformer_4h2l_simple_conv_64x256.pt' # if not None then training start with this checkpoint
WEIGHTS_PATH = '/content/drive/MyDrive/ocr_transformer_4h2l_simple_conv_64x256.pt'
PATH_TEST_RESULTS = os.fspath(Path(DIR, 'test_rn50_4h2l_result.tsv'))
TRAIN_LOG = os.fspath(Path(DIR, 'train_log.tsv'))
