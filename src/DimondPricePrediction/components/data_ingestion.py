import pandas as pd
import numpy as np
from src.DimondPricePrediction.exception import logging
from src.DimondPricePrediction.exception import CustomException
import os
import sys
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from pathlib import Path

class DataIngestionConfig:
    raw_data_path:str = os.path.join("artifacts", "raw.csv")
    train_data_path:str = os.path.join("artifacts", "train.csv")
    test_data_path:str = os.path.join("artifacts", "test.csv")
    '''
    def __init__(self, training_data_path: Path, test_data_path: Path):
        self.training_data_path = training_data_path
        self.test_data_path = test_data_path
    '''
    


# Class for data ingestion
class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Data ingestion started")

        try:
            data = pd.read_csv(Path(os.path.join("notebooks/data", "gemstone.csv")))
            logging.info("Data reading completed")

            os.makedirs(os.path.dirname(os.path.join(self.ingestion_config.raw_data_path)), exist_ok=True)
            data.to_csv(self.ingestion_config.raw_data_path, index=False)
            logging.info("Saved the raw dataset in artifacts folder")

            logging.info("Train-test data splitting started")
            train_data, test_data = train_test_split(data, test_size=0.25)
            logging.info("Train-test data splitting completed")

            train_data.to_csv(self.ingestion_config.train_data_path,index=False)
            test_data.to_csv(self.ingestion_config.test_data_path,index=False)            
            logging.info("data ingestion part completed")


        except Exception as e:
            logging.info("exception during occured at data ingestion stage")
            raise customexception(e,sys)