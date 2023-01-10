import os
from sensor.constant.s3_bucket import TRAILING_BUCKET_NAME

TARGET_COLUMN = "class"
PIPELINE_NAME: str = "sensor"
ARTIFACT_DIR: str = "artifact"
FILE_NAME: str = "sensor.csv"

TRAIN_FILE_NAME: str = "train.csv"
TEST_FILE_NAME: str = "test.csv"

PREPROCESSING_OBJECT_FILE_NAME = "preprocessing.csv"
MODEL_FILE_NAME = "model.pkl"
SCHEMA_FILE_PATH = os.path.join("cofig", "schema.yaml")
